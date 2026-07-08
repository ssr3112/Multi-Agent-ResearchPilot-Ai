def calculate_confidence(
    source_count: int
):

    if source_count >= 4:
        return 95

    if source_count >= 3:
        return 90

    if source_count >= 2:
        return 80

    return 70