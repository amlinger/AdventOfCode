use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;
use std::collections::HashMap;

struct Claim {
    i: u32,
    x: u32,
    y: u32,
    w: u32,
    h: u32,
}

fn main() {
    let filename = "input/part1.txt";
    let file = File::open(filename).expect("File not found");
    let buffer = BufReader::new(&file);

    let mut fabric = HashMap::new(); // HashMap<u32, HashMap<u32, u32>>;
    let mut claims = HashMap::new();
    let mut idx = 0;
    for line in buffer.lines() {
        let unwrapped = line.unwrap();

        let parts = unwrapped
            .split(|c| c == ':' || c == ' ' || c == '#')
            .collect::<Vec<_>>();
        let position = parts[3].split(",").collect::<Vec<_>>();
        let dimension = parts[5].split("x").collect::<Vec<_>>();

        let claim = Claim {
            i: parts[1].parse().unwrap(),
            x: position[0].parse().unwrap(),
            y: position[1].parse().unwrap(),
            w: dimension[0].parse().unwrap(),
            h: dimension[1].parse().unwrap(),
        };

        let mut inserted = false;

        for i in claim.x..(claim.x+claim.w) {
            for j in claim.y..(claim.y+claim.h) {
                let val = *fabric.entry(i)
                    .or_insert(HashMap::new())
                    .entry(j)
                    .or_insert(idx);
                if val != idx {
                    inserted = true;
                    claims.remove(&val);
                }
            }
        }

        if !inserted {
            claims.insert(idx, claim);
        }
        idx += 1;
    }

    for claim in claims.values() {
        println!("#{} @ {},{} {}x{}",
                 claim.i, claim.x, claim.y, claim.w, claim.h);
    }
}
