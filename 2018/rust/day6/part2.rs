use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;

struct Point {
    x: i32,
    y: i32,
}

struct Bounds {
    min: Point,
    max: Point,
}

fn to_point(line : String) -> Point {
    let parts = line.split(", ").collect::<Vec<_>>();
    return Point {
        x: parts[0].parse().unwrap(),
        y: parts[1].parse().unwrap(),
    };
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

    let margin : i32 = (10000 / points.len()) as i32;
    let bounds = Bounds {
        min: Point {
            x: *x_s.iter().min().unwrap() - margin,
            y: *y_s.iter().min().unwrap() - margin,
        },
        max:  Point {
            x: *x_s.iter().max().unwrap() + margin,
            y: *y_s.iter().max().unwrap() + margin,
        }
    };

    println!("Dimensions {}x{} -> {}x{}",
             bounds.min.x, bounds.min.y, bounds.max.x, bounds.max.y);
    let mut area = 0;
    for x in bounds.min.x..bounds.max.x {
        for y in bounds.min.y..bounds.max.y {
            let sum_of_distances : i32 = points
                .iter()
                .map(|p| (p.x - x).abs() + (p.y - y).abs())
                .sum();
            if sum_of_distances < 10000 {
                area += 1;
            }
        }
    }

    println!("The safe area is {}", area);
}

