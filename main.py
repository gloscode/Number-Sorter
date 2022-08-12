arranging_input = input('''Enter "A" for Ascending order or "D" for Descending order: ''')

first_number = int(input("Enter First number: "))
second_number = int(input("Enter Second number: "))
third_number = int(input("Enter Third number: "))
fourth_number = int(input("Enter Fourth number: "))
fifth_number = int(input("Enter Fifth number: "))

if (arranging_input == "A") or (arranging_input == "a"):
    input_array = [first_number, second_number, third_number, fourth_number, fifth_number]
    input_array.sort()
    # print(input_array)
    for input_list in input_array:
        print(f"\t{input_list}\n\t↓")
    print("( ͡° ͜ʖ ͡°)")
elif (arranging_input == "D") or (arranging_input == "d"):
    input_array = [first_number, second_number, third_number, fourth_number, fifth_number]
    input_array.sort(reverse=True)
    # print(input_array)
    for input_list in input_array:
        print(f"\t{input_list}\n\t↓")
    print("( ͡° ͜ʖ ͡°)")
else:
    print("Wrong input")
    print("(;´༎ຶД༎ຶ`)")