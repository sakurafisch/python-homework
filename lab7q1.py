def get_assessment_mark(assessment_name: str, mark_min: int, mark_max: int) -> int:
    inp: str = input(f"Enter {assessment_name} mark ({mark_min}-{mark_max})")
    try:
        num = int(inp)
    except ValueError:
        raise ValueError(f"{assessment_name} mark is invalid")
    if num < mark_min or num > mark_max:
        raise ValueError(f"{assessment_name} mark must be between {mark_min} and {mark_max}")
    return num

