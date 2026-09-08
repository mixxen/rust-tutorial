fn is_above_limit(reading: i32, limit: i32) -> bool {
    reading > limit
}

fn main() {
    let readings = [18, 22, 25, 29];
    let limit = 25;
    let mut qualifying_count = 0;

    for reading in readings {
        if is_above_limit(reading, limit) {
            qualifying_count += 1;
        }
    }

    println!("Readings above {limit}: {qualifying_count}");
}
