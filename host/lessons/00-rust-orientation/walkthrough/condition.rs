fn is_above_limit(reading: i32, limit: i32) -> bool {
    reading > limit
}

fn main() {
    let reading = 29;
    let limit = 25;

    if is_above_limit(reading, limit) {
        println!("Reading qualifies.");
    } else {
        println!("Reading does not qualify.");
    }
}
