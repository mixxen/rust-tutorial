def is_above_limit(reading: int, limit: int) -> bool:
    return reading > limit


def main() -> None:
    readings = [18, 22, 25, 29]
    limit = 25
    qualifying_count = 0

    for reading in readings:
        if is_above_limit(reading, limit):
            qualifying_count += 1

    print(f"Readings above {limit}: {qualifying_count}")


if __name__ == "__main__":
    main()
