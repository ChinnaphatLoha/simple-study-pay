def authenticate(username, password):
    print("Welcome! Please log in to continue.")
    while True:
        username_input = input("Enter your username: ")
        password_input = input("Enter your password: ")
        if username == username_input and password == password_input:
            print("Authentication successful!")
            break
        else:
            print("Invalid username or password. Please try again.")

def calculate_net_price(price_per_hour, num_of_hours, test_score):
    percent_of_discount = 0
    if num_of_hours > 15:
        percent_of_discount = 0.1
    if 10 <= test_score <= 20:
        percent_of_discount = 0.2

    list_price = price_per_hour * num_of_hours
    net_price = list_price - (list_price * percent_of_discount)
    return net_price

def process_payment(net_price):
    print(f"The total amount due is: {net_price:.2f}")
    amount_paid = float(input("Enter the amount you are paying: "))
    while amount_paid < net_price:
        remaining_amount = net_price - amount_paid
        print(f"Insufficient amount. You still owe: {remaining_amount:.2f}")
        additional_amount = float(input("Please enter the additional amount: "))
        amount_paid += additional_amount

    if amount_paid > net_price:
        change = amount_paid - net_price
        print(f"Payment accepted. Your change is: {change:.2f}")
    else:
        print("Payment accepted. Thank you!")

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Value must be positive.")
            return value
        except ValueError as e:
            print(e)

def get_test_score(prompt):
    while True:
        try:
            score = int(input(prompt))
            if not 0 <= score <= 20:
                raise ValueError("Test score must be between 0 and 20.")
            return score
        except ValueError as e:
            print(e)

def main():
    # Set initial username and password
    username = "st67"
    password = "67"

    # Authenticate user
    authenticate(username, password)

    # Set initial values
    price_per_hour = 150

    # Get number of hours of studying
    num_of_hours = get_positive_integer("Enter the number of hours you studied: ")

    # Get test score
    test_score = get_test_score("Enter your test score (0-20): ")

    # Calculate the net price
    net_price = calculate_net_price(price_per_hour, num_of_hours, test_score)
    print(f"The net price after discounts is: {net_price:.2f}")

    # Handle payment
    process_payment(net_price)

if __name__ == "__main__":
    main()