use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;
use std::iter::Peekable;
use std::collections::HashMap;

struct DateTime {
    year: u64,
    month: u64,
    day: u64,
    hour: u64,
    minute: u64,
}

fn days(month : u64) -> u64 {
    return vec![31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        .iter().take(month as usize).sum();
}

impl DateTime {
    fn minutes(&self) -> u64 {
        // Leap years doesn't exist...
        self.minute + 60 * (
            self.hour + 24 * (
                self.day + days(self.month) + 365 * self.year))
    }
}

struct Sleep {
    start: DateTime,
    end: DateTime,
}

impl Sleep {
    fn duration(&self) -> u64 {
        self.end.minutes() - self.start.minutes()
    }
}

struct Shift {
    id: u64,
    sleeps: Vec<Sleep>,
}

fn parse_date_time(line : String) -> DateTime {
    return DateTime {
        year   : line.chars().skip(1).take(4).collect::<String>().parse().unwrap(),
        month  : line.chars().skip(6).take(2).collect::<String>().parse().unwrap(),
        day    : line.chars().skip(9).take(2).collect::<String>().parse().unwrap(),
        hour   : line.chars().skip(12).take(2).collect::<String>().parse().unwrap(),
        minute : line.chars().skip(15).take(2).collect::<String>().parse().unwrap(),
    }
}

fn parse_shift<'a, I>(lines : &mut Peekable<I>) -> Option<Shift>
               where I : Iterator<Item=String> {
    let mut shift = match lines.next() {
        None => return None,
        Some(line) => {
            Shift {
                id: line.split("Guard #").collect::<Vec<_>>()[1]
                        .split(" begins").collect::<Vec<_>>()[0]
                        .to_string().parse().unwrap(),
                sleeps: Vec::new()
            }
        }
    };

    loop {
        match lines.peek() {
            None => break,
            Some(line) => {
                if line.contains("Guard") {
                    break;
                }
            }
        }
        shift.sleeps.push(Sleep {
            start: parse_date_time(lines.next().unwrap()),
            end  : parse_date_time(lines.next().unwrap()),
        });
    }

    return Some(shift);
}

fn print_shift(shift : &Shift) {
    print!("Guard #{} => [ ", shift.id);
    for sleep in &shift.sleeps {
        print!("{}/{}/{} {}:{}=>",
               sleep.start.year,
               sleep.start.month,
               sleep.start.day,
               sleep.start.hour,
               sleep.start.minute);
        print!("{}/{}/{} {}:{} ({} min) ",
               sleep.end.year,
               sleep.end.month,
               sleep.end.day,
               sleep.end.hour,
               sleep.end.minute,
               sleep.duration());
    }
    println!("]");
}

fn sleeps_duration(sleeps : &Vec<Sleep>) -> u64 {
    return sleeps.iter().map(|s| s.duration()).sum::<u64>();
}

fn shifts_duration(shifts : &Vec<Shift>) -> u64 {
    return shifts.iter().map(|s| sleeps_duration(&s.sleeps)).sum::<u64>();
}

fn main() {
    let filename = "input/part1.txt";
    let file = File::open(filename).expect("File not found");
    let buffer = BufReader::new(&file);

    let mut lines : Vec<String> = buffer.lines().map(|l| l.unwrap()).collect();
    lines.sort();

    let mut iter_lines = lines.into_iter().peekable();
    let mut guards = HashMap::new();
    loop {
        match parse_shift(&mut iter_lines) {
            Some(shift) => {
                let id = shift.id.clone();
                guards.entry(id).or_insert(Vec::new()).push(shift);
            }
            None => break
        };
    }

    let (guard, shifts) = guards
        .into_iter()
        .max_by(|(_, lhs), (__, rhs)|
                shifts_duration(lhs).cmp(&shifts_duration(rhs)))
        .unwrap();

    let mut minutes = HashMap::new();
    for shift in &shifts {
        print_shift(&shift);

        for sleep in &shift.sleeps {
            for minute in sleep.start.minute..(sleep.start.minute + sleep.duration()) {
                *minutes.entry(minute % 60).or_insert(0) += 1;
            }
        }
    }

    let intermediate = minutes.into_iter().map(|(k, v)| v*100+k).max().unwrap();
    let num_sleeps = intermediate / 100;
    let minute = intermediate - num_sleeps * 100;
    println!("Sleepiest minute {} with number of sleeps {}", minute, num_sleeps);

    println!("Answer: {} * {} = {}", guard, minute, guard * minute);

}
