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

#[test]
fn includes_reading_above_limit() {
    assert!(is_above_limit(29, 25));
}

#[test]
fn excludes_reading_equal_to_limit() {
    assert!(!is_above_limit(25, 25));
}

#[test]
fn excludes_reading_below_limit() {
    assert!(!is_above_limit(22, 25));
}
