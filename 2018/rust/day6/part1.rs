use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;
use std::collections::HashMap;

struct Point {
    x: i16,
    y: i16,
}

struct Bounds {
    min: Point,
    max: Point,
}

fn nearest_point(x : i16, y : i16, points : &Vec<Point>) -> Option<(usize, i16)> {
    // return the index of, and nearest point, or None if there are multiple.
    let candidates = points
        .iter()
        .enumerate()
        .map(|(i, p)| (i, (p.x - x).abs() + (p.y - y).abs()));

    let mut min : Vec<(usize, i16)> = vec![(usize::max_value(), i16::max_value())];
    for candidate in candidates {
        let cur = min[0].1;

        if candidate.1 < cur {
            min = vec![candidate];
        } else if candidate.1 == cur {
            min.push(candidate);
        }
    }

    return if min.len() > 1 {None} else {Some(min[0])};
}

fn to_point(line : String) -> Point {
    let parts = line.split(", ").collect::<Vec<_>>();
    return Point {
        x: parts[0].parse().unwrap(),
        y: parts[1].parse().unwrap(),
    };
}

fn through_bounds(bounds : &Bounds,
                  points : &Vec<Point>,
                  func : &mut FnMut(usize, i16)) {
    for x in bounds.min.x..bounds.max.x {
        for y in bounds.min.y..bounds.max.y {
            match nearest_point(x, y, &points) {
                Some((idx, dist)) => { func(idx, dist); }
                None => {}
            }
        }
    }
}

fn main() {
    let filename = "input/part1.txt";
    let file = File::open(filename).expect("File not found");
    let buffer = BufReader::new(&file);

    let points = buffer.lines()
        .map(|line| to_point(line.unwrap()))
        .collect::<Vec<_>>();

    let x_s = points.iter().map(|p| p.x).collect::<Vec<_>>();
    let y_s = points.iter().map(|p| p.y).collect::<Vec<_>>();

    let bounds = Bounds {
        min: Point {
            x: *x_s.iter().min().unwrap(),
            y: *y_s.iter().min().unwrap(),
        },
        max:  Point {
            x: *x_s.iter().max().unwrap(),
            y: *y_s.iter().max().unwrap(),
        }
    };

    // Tallys is a map between index and size of area.
    let mut tallies : HashMap<usize, u32> = HashMap::new();

    through_bounds(&bounds, &points, &mut |idx, _| {
        *tallies
            .entry(idx)
            .or_insert(0) += 1;
    });

    // All the points that are closes to the boundary values for the
    // smallest encapsulating area are infinate, and shouldn't be considered.
    // Removing these by going through these areas, once again.
    //
    // Not a very elegant way but it does the trick.
    through_bounds(
        &Bounds{
            min: Point {x: bounds.min.x, y: bounds.min.y},
            max: Point {x: bounds.max.x, y: bounds.min.y+1}},
        &points,
        &mut |idx, _| { tallies.remove(&idx); });
    through_bounds(
        &Bounds{
            min: Point {x: bounds.max.x-1, y: bounds.min.y},
            max: Point {x: bounds.max.x, y: bounds.max.y}},
        &points,
        &mut |idx, _| { tallies.remove(&idx); });
    through_bounds(
        &Bounds{
            min: Point {x: bounds.min.x, y: bounds.max.y-1},
            max: Point {x: bounds.max.x, y: bounds.max.y}},
        &points,
        &mut |idx, _| { tallies.remove(&idx); });
    through_bounds(
        &Bounds{
            min: Point {x: bounds.min.x, y: bounds.min.y},
            max: Point {x: bounds.min.x+1, y: bounds.max.y}},
        &points,
        &mut |idx, _| { tallies.remove(&idx); });

    // Find the largest area of the remaining points.
    let (max_idx, max_area) = tallies
        .into_iter()
        .max_by(|(_, lhs_area), (__, rhs_area)| lhs_area.cmp(rhs_area))
        .unwrap();
    let max_p = points.get(max_idx).unwrap();
    println!("");
    println!("Maximum sized point {:2}: {:3}x{:<3} = {}",
             max_idx, max_p.x, max_p.y, max_area);
}

