if __name__ == '__main__':
    product_code: str = "377B";
    product_name: str = "Beef Liquid Stock";
    product_size: str = "250mL";
    product_price: int = 2.15;
    print(product_code + ": " + product_name + ", " + product_size);
    print(product_name + ", " + product_size + ", $" + str(product_price));
    print("{0}: {1}, {2}".format(product_code, product_name, product_size));
    print("{0}, {1}, ${2}".format(product_name, product_size, product_price));
