use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;
use std::collections::LinkedList;
use std::collections::HashMap;

fn polarity(lhs : &Option<char>, rhs : &Option<char>) -> bool {
    if lhs.is_none() || rhs.is_none() {
        return false;
    }
    return lhs != rhs && (
        lhs.unwrap().to_ascii_uppercase() == rhs.unwrap() ||
        lhs.unwrap().to_ascii_lowercase() == rhs.unwrap());

}

fn annhilated_length(mut chain : LinkedList<char>) -> usize{
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

    return chain_len;
}

fn main() {
    let filename = "input/part1.txt";
    let file = File::open(filename).expect("File not found");
    let buffer = BufReader::new(&file);

    let chain : LinkedList<char> = buffer
        .lines().next().unwrap().unwrap().chars().collect();

    let mut polymer_lengths = HashMap::new();
    for letter in (b'a' .. b'z' + 1)       // Start as u8
            .map(|c| c as char)            // Convert all to chars
            .filter(|c| c.is_alphabetic()) // Filter only alphabetic chars
            .collect::<Vec<_>>() {

        polymer_lengths.insert(
            annhilated_length(chain
                .iter()
                .filter(|ch| ch != &&letter &&
                             ch != &&letter.to_ascii_uppercase())
                .map(|ch| *ch)
                .collect()),
            letter);
    }

    let len = polymer_lengths.into_iter().min().unwrap();

    println!("'{}' produces the shortest polymer of lenght {}",
             len.1, len.0);
}

