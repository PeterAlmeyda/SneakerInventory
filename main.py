#Inventory system for tracking shoes, sizes, qty.
#Peter Almeyda
#Dev began 10/01/22
#Build: v 1.2  (alpha build)


my_shoes = {                    #Shoe : Qty
    "Nike Pandas" : 1,
    "Jordan 1 " : 2,
    "Yeezy" : 4,
    "Vans" : 3,
    "Levis" : 1
}

all_shoes = {       #Dict with nested dict inside...
    'Nike' : {
        'Model' : 'Pandas',
        'Size' : [9, 9.5],
        'Qty' : 2,
    },

    'Yeezy' : {
        'Model' : '350 Red / Black',
        'Size' : [9],
        'Qty' : 4,
    }

}

#Official Protol Use


def main():
    print("Welcome to Shoe Inventory")
    while True:
        choice_1 = input("Type 'add' to add new shoe to inventory "
                         "Type 'view' to view current inventory").lower()

        if choice_1 == "add":
            #add2()
            add4()
        elif choice_1 == "view":
            #view()
            #view2()
            view3()
        else:
            print("Entry not found... ")
            main()
        continue


def add4(shoe_model = None, qty = 0, size = None, multi_qty = False):  #Backup func for testing
    print("Add new shoes to inventory: ")
    all_sizes = [] #empty list with int of sizes
    multi_qty = False
    shoe_model = input("Shoe Model:")
    qty = input(f" Enter qty of {shoe_model}: ")
    if qty.isdigit():
        qty = int(qty)
    else:
        print("You did not enter a valid character. Enter only-numbers. ")
        add4()
    print(f"You have entered {qty} quantities. ")  # Verified Works
    #try:
    #size = float(input(f"Enter size of  {shoe_model}: "))
    size = (input(f"Enter size of  {shoe_model}: "))
    if '.' in size:
        size = float(size)
    elif size.isdigit():
        size = int(size)
    else:
        print("Please enter a valid size number for shoe. ")
        add4()
    all_sizes.append(size)

    #except ValueError:
     #   print("Please enter a valid size number for shoe. ")
      #  add4()
    if qty > 1:
        try:
            size_input_counter = 1
            #multi_qty = True
            while size_input_counter != qty:
                print(f"You have entered {size_input_counter} | Total qty: {qty}")
                size_other = float(input("What is the size of other shoes?"))
                size_input_counter += 1
                all_sizes.append(size_other)
        except ValueError:
            print("Please enter a valid size number for shoe. ")
            all_sizes.pop()
        print("removed last index")
    print("All Sizes: ")
    print(all_sizes)


    new_shoe_dict = {f'Model': {shoe_model}, 'Size': tuple(all_sizes), 'Qty': {qty}}
    all_shoes[f'{shoe_model}'] = new_shoe_dict
    print("New shoe inventory recorded SUCCESSFULLY.")
    user_choice = input("Type 'view' to view most current / updated inventory. ").lower()
    if user_choice == 'view':
        view3()
    else:
        main()


def view3():        #Active funtion
    for shoe, shoe_info in all_shoes.items():
        print(f"\n Shoe Brand: {shoe}")
        model = f"{shoe_info['Model']}"
        size = f"{shoe_info['Size']}"
        quantity = f"{shoe_info['Qty']}"

        print(f"\t Model: {model}")
        print(f"\t Size: {size}")
        print(f"\t Qty: {quantity}")

main()

