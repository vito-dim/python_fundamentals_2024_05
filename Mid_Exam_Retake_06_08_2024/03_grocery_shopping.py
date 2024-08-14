def important_func(cmd_attr: list, product_list: list):
    product = cmd_attr[1]
    if product in product_list:
        product_list.remove(product)
    product_list.insert(0, product)
    return product_list


def add_func(cmd_attr: list, product_list: list):
    product = cmd_attr[1]
    if product in product_list:
        print("The product is already in the list.")
        return product_list
    else:
        product_list += [product]
    return product_list


def swap_func(cmd_attr: list, product_list: list):
    product1 = cmd_attr[1]
    product2 = cmd_attr[2]
    missing_product = ""

    if product1 not in product_list:
        missing_product = product1
    elif product2 not in product_list:
        missing_product = product2

    if missing_product == "":
        index1 = product_list.index(product1)
        index2 = product_list.index(product2)
        product_list[index1], product_list[index2] = product_list[index2], product_list[index1]
        return product_list
    else:
        print(f"Product {missing_product} missing!")
        return product_list


def remove_func(cmd_attr: list, product_list: list):
    product = cmd_attr[1]
    if product in product_list:
        product_list.remove(product)
        return product_list
    else:
        print(f"Product {product} isn't in the list.")
    return product_list


def reverse_func(product_list: list):
    reversed_list = product_list[::-1]
    return reversed_list


products = input().split("|")

while True:
    command = input()
    if command == "Shop!":
        break

    command_attributes = command.split("%")
    if "Important" in command_attributes:
        products = important_func(command_attributes, products)
    elif "Add" in command_attributes:
        products = add_func(command_attributes, products)
    elif "Swap" in command_attributes:
        products = swap_func(command_attributes, products)
    elif "Remove" in command_attributes:
        products = remove_func(command_attributes, products)
    elif "Reversed" in command_attributes:
        products = reverse_func(products)

for index in range(len(products)):
    print(f"{index + 1}. {products[index]}")
