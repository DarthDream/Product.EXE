import json,csv

product = {}
next_id = 1

try:
    with open("product.json", "r") as file:
        data = json.load(file)

        if "products" in data:
            product = data["products"]
            next_id = data.get("next_id", 1)

        else:
            for name, price in data.items():
                product[name] = {
                    "id": next_id,
                    "price": price
                }
                next_id += 1

            next_id = max(
                [info["id"] for info in product.values()],
                default=0
            ) + 1

except (FileNotFoundError, KeyError, json.JSONDecodeError):
    product = {}
    next_id = 1


def save_product():
    with open("product.json", "w") as file:
        json.dump({
            "next_id": next_id,
            "products": product
        }, file, indent=4)


def save_json():
    save_product()
    print("JSON fayli yadda saxlanildi")


def get_price(name):
    return product[name]["price"]


def sort_by_pricepl():
    qiymet = sorted(product, key=get_price, reverse=False)

    for name in qiymet:
        print(f"ID: {product[name]['id']} | {name} | {product[name]['price']}")


def sort_by_pricemn():
    qiymet = sorted(product, key=get_price, reverse=True)

    for name in qiymet:
        print(f"ID: {product[name]['id']} | {name} | {product[name]['price']}")


def filter_product():
    print('''
    1.Azdan coxa
    2.Coxdan aza
    3.Back
    ''')

    try:
        choice = int(input("Secim et: "))

        if choice == 1:
            print("Azdan coxa siralandi")
            sort_by_pricepl()

        elif choice == 2:
            print("Coxdan aza siralandi")
            sort_by_pricemn()

        elif choice == 3:
            return

        else:
            print("Sehv choice!!!")

    except ValueError:
        print("ERROR 404 have problem")


def add_product():
    global next_id

    try:
        mehsul = input("Mehsul daxil et: ").strip()

        if not mehsul:
            print("Mehsul adi bos ola bilmez")
            return

        for name in product:
            if name.lower() == mehsul.lower():
                print("Mehsul artiq var")
                return

        qiymet = float(input("Qiymet daxil et: "))

        if qiymet < 0:
            print("Qiymet menfi ola bilmez")
            return

        product[mehsul] = {
            "id": next_id,
            "price": qiymet
        }

        print(f"Mehsul elave edildi! ID: {next_id}")

        next_id += 1
        save_product()

    except ValueError:
        print("ERROR 404 have problem")


def show_product():
    if not product:
        print("Mehsul yoxdur")
        return

    for name, info in product.items():
        print(f"ID: {info['id']} | Mehsul: {name} | Qiymet: {info['price']}")


def delete_product():
    try:
        mehsul_id = int(input("Mehsul ID daxil et: "))

        for name in list(product):
            if product[name]["id"] == mehsul_id:
                del product[name]
                save_product()
                print("Mehsul silindi")
                return

        print("Bu ID-de mehsul yoxdur")

    except ValueError:
        print("Duzgun ID daxil et!")


def save_csv():
    with open("product.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Mehsul", "Qiymet"])

        for name, info in product.items():
            writer.writerow([
                info["id"],
                name,
                info["price"]
            ])

    print("CSV fayli yaradildi")


def app():
    while True:
        print('''
        ============ PRODUCT MANAGEMENT ============
            1.Add Product
            2.Show Product
            3.Delete Product By ID
            4.Save CSV
            5.Save JSON
            6.Filter by price

            ***7.Exit***
        ''')

        try:
            choice = int(input("Secim et: "))

            if choice == 1:
                add_product()

            elif choice == 2:
                show_product()

            elif choice == 3:
                delete_product()

            elif choice == 4:
                save_csv()

            elif choice == 5:
                save_json()

            elif choice == 6:
                filter_product()

            elif choice == 7:
                break

            else:
                print("Yanlis secim")

        except ValueError:
            print("Duzgun secim daxil et!")


app()
