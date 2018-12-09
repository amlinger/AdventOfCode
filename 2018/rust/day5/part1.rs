use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;
use std::collections::LinkedList;

fn polarity(lhs : &Option<char>, rhs : &Option<char>) -> bool {
    if lhs.is_none() || rhs.is_none() {
        return false;
    }
    return lhs != rhs && (
        lhs.unwrap().to_ascii_uppercase() == rhs.unwrap() ||
        lhs.unwrap().to_ascii_lowercase() == rhs.unwrap());
}

fn main() {
    let filename = "input/part1.txt";
    let file = File::open(filename).expect("File not found");
    let buffer = BufReader::new(&file);

    let mut chain : LinkedList<char> = buffer
        .lines().next().unwrap().unwrap().chars().collect();

    let mut chain_len = 0;
    while chain_len != chain.len() {
        chain_len = chain.len();
        let mut reduced_chain = LinkedList::new();

        loop {
            let cur = chain.pop_front();
            let nex = chain.pop_front();
            if !polarity(&cur, &nex) {
                reduced_chain.push_back(match cur {
                    Some(ch) => ch,
                    None => break,
                });

                match nex {
                    Some(ch) => chain.push_front(ch),
                    None => {}
                };
            }
        }

        chain = reduced_chain;
    }

    println!("There are {} units left after annhilation", chain_len);
}

