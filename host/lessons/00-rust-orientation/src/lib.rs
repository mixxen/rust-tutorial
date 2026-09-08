/// Decide whether a reading is strictly above a limit.
///
/// Equality does not qualify in the worked example. The exercise introduces
/// a different requirement in a separate package.
pub fn is_above_limit(reading: i32, limit: i32) -> bool {
    reading > limit
}

#[cfg(test)]
mod tests {
    use super::is_above_limit;

    #[test]
    fn excludes_reading_below_limit() {
        assert!(!is_above_limit(22, 25));
    }

    #[test]
    fn excludes_reading_equal_to_limit() {
        assert!(!is_above_limit(25, 25));
    }

    #[test]
    fn includes_reading_above_limit() {
        assert!(is_above_limit(29, 25));
    }

    #[test]
    fn compares_negative_readings() {
        assert!(is_above_limit(-3, -5));
        assert!(!is_above_limit(-7, -5));
        assert!(!is_above_limit(-5, -5));
    }
}
