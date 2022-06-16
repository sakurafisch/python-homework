state_map: dict = {
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
    inp = input("Enter state NSW/ACT/NT/QLD/SA/TAS/VIC/WA: ")
    if inp in state_map:
        print(f"The state you entered is {state_map.get(inp)}")
    else:
        print(f"Sorry I don't know the fulll name of {inp}")

if __name__ == '__main__':
    main()
