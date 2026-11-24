fn is_above_limit(reading: i32, limit: i32) -> bool {
    return reading > limit;
}

fn main() {
    let reading_is_high = is_above_limit(29, 25);
    println!("Above limit: {reading_is_high}");
}
