use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;
//use std::collections::HashMap;

fn get_same_characters(lhs : &str, rhs : &str) -> String {
    return lhs.chars()
        .enumerate()
        .filter(|&(i, ch)| ch == rhs.chars().nth(i).unwrap())
        .map(|(_i, ch)| ch)
        .collect();
}

fn lexical_difference(lhs : &str, rhs : &str) -> i32 {
    if lhs.len() != rhs.len() {
        return -1;
    }

    return (lhs.len() - get_same_characters(rhs, lhs).len()) as i32;
}

fn main() {
    let filename = "input/part1.txt";
    let file = File::open(filename).expect("File not found");
    let buffer = BufReader::new(&file);

    let mut lines = Vec::new();

    for line in buffer.lines() {
        lines.push(line.unwrap());
    }
    lines.sort();
    let mut prev = String::new();
    for line in lines {
        let lexical_diff = lexical_difference(&prev, &line);
        println!("Lexical difference: {}", lexical_diff);
        if lexical_diff == 1 {
            println!("Common characters from {} and {}: {}",
                prev, line, get_same_characters(&prev, &line));
            break
        }
        prev = line.clone();
    }
}
