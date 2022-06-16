user_info: dict = {
    "first_name": "Amanda",
    "last_name": "Smith",
    "age": 20
}

def main() -> None:
    print(user_info.get("first_name"))
    user_info["last_name"] = "Harrison"
    user_info["email"] = "a.harrison@gmail.com"
    del user_info["age"]
    print(user_info)

if __name__ == '__main__':
    main()
