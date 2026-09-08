/// Decide whether a reading is at or above a limit.
///
/// Exercise: the implementation still follows the OLD strict comparison.
/// Update it to meet the new requirement described in EXERCISE.md.
pub fn is_at_or_above_limit(reading: i32, limit: i32) -> bool {
    reading > limit
}
