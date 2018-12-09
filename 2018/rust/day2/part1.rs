use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;
use std::collections::HashMap;

fn count_char_occurances(word : &str) -> HashMap<char, u32> {
    let mut counts = HashMap::new();

    for ch in word.chars() {
        let count = 1 + counts.get(&ch).unwrap_or(&0);
        counts.insert(ch, count);
    }

    return counts;
}

fn find_num_occurrance(occurances : u32, counts : &HashMap<char, u32>) -> u32 {
    match counts.values().any(|&val| val == occurances) {
        true => 1,
        false => 0,
    }
}

fn main() {
    let filename = "input/part1.txt";
    let file = File::open(filename).expect("File not found");
    let buffer = BufReader::new(&file);

    let mut twice = 0;
    let mut thrice = 0;

    for line in buffer.lines() {
        let counts = count_char_occurances(&line.unwrap().trim());

        twice += find_num_occurrance(2, &counts);
        thrice += find_num_occurrance(3, &counts);
    }

    println!("Checksum: {} * {} = {}", twice, thrice, twice * thrice);
}
