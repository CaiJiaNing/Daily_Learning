def calc(scores: list[int]) -> float:
    return sum(scores) / len(scores) if scores else 0.0

def calc_data(scores: list[int]) -> tuple[int, int, float]:
    max_v = max(scores)
    min_v = min(scores)
    avg_v = calc(scores)
    return max_v, min_v, avg_v

