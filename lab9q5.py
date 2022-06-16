def compareString(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False
    i: int = 0
    while i < len(string1):
        if string1[i] != string2[i]:
            return False
        i += 1
    return True
