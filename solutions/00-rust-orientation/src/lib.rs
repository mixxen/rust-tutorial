/// Decide whether a reading is at or above a limit.
///
/// Equality belongs to the qualifying side of the boundary.
pub fn is_at_or_above_limit(reading: i32, limit: i32) -> bool {
    reading >= limit
}
