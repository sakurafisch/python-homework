if __name__ == '__main__':
    cow: int = int(input("Enter number of cows to purchase: "));
    duck: int = int(input("Enter number of ducks to purchase: "));
    chicken: int = int(input("Enter number of chicken to purchase: "));
    print("cost:");
    print(f"{cow}  cow = {cow * 30} grassies");
    print(f"{duck}  duck = {duck * 5} grassies");
    print(f"{chicken} chick = {chicken * 3} grassies");
    print(f"Total = { cow * 30 + duck * 5 + chicken * 3} grassies");
