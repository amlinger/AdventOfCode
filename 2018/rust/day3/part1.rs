use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;
use std::collections::HashMap;

fn main() {
    let filename = "input/part1.txt";
    let file = File::open(filename).expect("File not found");
    let buffer = BufReader::new(&file);

    let mut fabric = HashMap::new(); // HashMap<u32, HashMap<u32, u32>>;
    for line in buffer.lines() {
        let unwrapped = line.unwrap();
        let parts = unwrapped.split(|c| c == ':' || c == ' ').collect::<Vec<_>>();
        let position = parts[2].split(",").collect::<Vec<_>>();
        let x : u32 = position[0].parse().unwrap();
        let y : u32 = position[1].parse().unwrap();

        let dimension = parts[4].split("x").collect::<Vec<_>>();
        let w : u32 = dimension[0].parse().unwrap();
        let h : u32 = dimension[1].parse().unwrap();

        for i in x..(x+w) {
            for j in y..(y+h) {
                *fabric.entry(i)
                    .or_insert(HashMap::new())
                    .entry(j)
                    .or_insert(0) += 1;
            }
        }
    }

    let mut num_overlap = 0;
    for (_y, row) in fabric {
        for (_x, cell) in row {
            num_overlap += match cell > 1 {
                true => 1,
                false => 0,
            };
        }
    }

    println!("Number of overlapping square inches: {}", num_overlap);
}
