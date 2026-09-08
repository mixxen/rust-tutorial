fn is_above_limit(reading: i32, limit: i32) -> bool {
    reading > limit
}

fn main() {
    println!("Above the limit: {}", is_above_limit(29, 25));
}
