terminals = {
    'X10.1': list(range(10, 16)) + list(range(20, 26))  # 12 pins: 10-15 and 20-25
}

# Display the initial state of terminals
for key, index in terminals.items():
    print(f'{key}: {"; ".join([str(x) for x in index])}')

# Loop to accept user input and remove the terminal
while True:
    user_input = input('Enter a terminal to remove (or type "exit" to stop): ')

    if user_input.lower() == 'exit':
        break

    try:
        user_input = int(user_input)
        if user_input in terminals['X10.1']:
            terminals['X10.1'].remove(user_input)
        else:
            print(f"Terminal {user_input} is not in the list.")
    except ValueError:
        print("Please enter a valid number.")

    # Display the updated state of terminals
    for key, index in terminals.items():
        print(f'{key}: {"; ".join(sorted([str(x) for x in index]))}')
