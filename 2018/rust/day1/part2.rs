use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;
use std::collections::HashSet;

fn main() {
    let mut frequency = 0;
    let mut visited_frequencies = HashSet::new();
    visited_frequencies.insert(0);

    let filename = "input/part1.txt";

    let mut found = false;
    while !found {

        // Terrible stuff. We shouldn't need to go to disk here for each time
        // we want to read the input, for every loop.
        let file = File::open(filename).expect("File not found in location");
        let buffer = BufReader::new(&file);

        for line in buffer.lines() {
            let freqency_diff: i32 = match line.unwrap().trim().parse() {
                Ok(num) => num,
                // Just skip invalid lines, there shouldn't be any.
                Err(_) => continue,
            };

            frequency += freqency_diff;
            let mapped_frequency = frequency.clone();
            // We've seen this frequency previously, so this is the second time.
            if visited_frequencies.contains(&mapped_frequency) {
                found = true;
                break;
            }

            visited_frequencies.insert(mapped_frequency);
        }
    }

    println!("Frequency found twice: {}", frequency);
}
