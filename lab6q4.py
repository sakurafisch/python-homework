state_abb: dict = {
 "NSW": "New South Wales",
 "ACT": "Australian Capital Territory",
 "NT": "Northern Territory",
 "QLD": "Queensland",
 "SA": "South Australia",
 "TAS": "Tasmania",
 "VIC": "Victoria",
 "WA": "Western Australia"
}

def main() -> None:
    print(state_abb.get("QLD"))
    print(state_abb.get("VIC"))

if __name__ == '__main__':
    main()
