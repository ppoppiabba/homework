
def get_valid_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input == 'done':
            return None
        try:
            num_list = [int(x) for x in user_input.split()]
            if len(num_list) < 2:
                print("must enter more than one integer")
            else:
                return num_list
        except ValueError:
            print("must enter integers separated by spaces")

def sum_list_recursive(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list_recursive(lst[1:])

if __name__ == '__main__':
    while True:
        input_numbers = get_valid_integer_input("Enter integers separated by spaces ==> ")

        if input_numbers is None:
            print("program terminated. good bye !!")
            break

        total_sum = sum_list_recursive(input_numbers)
        print("The sum of the input integers is ==> ", total_sum)