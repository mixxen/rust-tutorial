// Shared requirements: do not weaken these tests to make the exercise pass.
// Add your own cases in tests/your_cases.rs.
use threshold_rule::is_at_or_above_limit;

#[test]
fn excludes_reading_below_limit() {
    assert!(!is_at_or_above_limit(22, 25));
}

#[test]
fn includes_reading_equal_to_limit() {
    assert!(is_at_or_above_limit(25, 25));
}

#[test]
fn includes_reading_above_limit() {
    assert!(is_at_or_above_limit(29, 25));
}

#[test]
fn uses_the_supplied_limit() {
    assert!(!is_at_or_above_limit(39, 40));
    assert!(is_at_or_above_limit(40, 40));
    assert!(is_at_or_above_limit(41, 40));
}

#[test]
fn compares_negative_readings() {
    assert!(!is_at_or_above_limit(-7, -5));
    assert!(is_at_or_above_limit(-5, -5));
    assert!(is_at_or_above_limit(-3, -5));
}

#[test]
fn counts_two_qualifying_readings_in_the_sample() {
    let readings = [18, 22, 25, 29];
    let mut qualifying_count = 0;

    for reading in readings {
        if is_at_or_above_limit(reading, 25) {
            qualifying_count += 1;
        }
    }

    assert_eq!(qualifying_count, 2);
}
