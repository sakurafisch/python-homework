def get_assessment_mark(assessment_name: str, mark_min: int, mark_max: int) -> int:
    inp = input(f"Enter {assessment_name} mark ({mark_min}-{mark_max}): ")
    try:
        num = int(inp)
    except ValueError:
        raise ValueError(f"{assessment_name} mark is invalid")
    if num < mark_min or num > mark_max:
        raise ValueError(f"{assessment_name} mark must be between {mark_min} and {mark_max}")
    return num

def main() -> None:
    sum: int = 0
    try:
        sum += get_assessment_mark("assignment", 0, 20)
        sum += get_assessment_mark("project", 0, 30)
        sum += get_assessment_mark("final exam", 0, 50)
        print(f"Total mark: {sum}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
