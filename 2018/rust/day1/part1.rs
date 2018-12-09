use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;

fn main() {
    let filename = "input/part1.txt";
    let mut frequency = 0;

    let file = File::open(filename)
        .expect("File not found in location");
    let buffer = BufReader::new(&file);

    for line in buffer.lines() {
        let freqency_diff: i32 = match line.unwrap().trim().parse() {
            Ok(num) => num,
            // Just skip invalid lines, there shouldn't be any.
            Err(_) => continue,
        };

        print!("Current frequency {}, change of {}; ",
               frequency, freqency_diff);
        frequency += freqency_diff;
        println!("resulting frequency {}", frequency);

    }

    println!("Resulting Frequency: {}", frequency);
}
