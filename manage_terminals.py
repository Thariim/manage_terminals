def type_of_terminal():
    """Prompt user to choose a type of terminal and validate the input."""
    print('What type of terminal would you like to use:')
    print('20 pins (type "20")\n24 pins (type "24")\n32 pins (type "32")\n40 pins (type "40")\n64 pins (type "64")')
    terminal_type = user_info('Type of terminal: ')
    
    while terminal_type not in ['20', '24', '32', '40', '64']:
        print('Invalid response. Please choose a correct type of terminal.')
        terminal_type = user_info('Type of terminal: ')
    
    return int(terminal_type)

def handle_terminal_type(t_type):
    """Return terminal configurations based on the selected type."""
    if t_type == 20:
        terminals = {'X10.1': list(range(10, 30))}
    
    elif t_type == 24:
        terminals = {
            'X10.1': list(range(10, 16)) + list(range(20, 26)),  # 12 pins: 10-15 and 20-25
            'X10.2': list(range(10, 16)) + list(range(20, 26)),  # 12 pins: 10-15 and 20-25
        }
    
    elif t_type == 32:
        terminals = {
            'X10.1': list(range(10, 30)),  # 20 pins: 10-29
            'X10.2': list(range(10, 16)) + list(range(20, 26)),  # 12 pins: 10-15 and 20-25
        }
    
    elif t_type == 40:
        terminals = {
            'X10.1': list(range(10, 30)),  # 20 pins: 10-29
            'X10.2': list(range(10, 30)),  # 20 pins: 10-29
        }
    
    elif t_type == 64:
        terminals = {
            'X10.1': list(range(10, 30)),  # 20 pins: 10-29
            'X10.2': list(range(10, 16)) + list(range(20, 26)),  # 12 pins: 10-15 and 20-25
            'X10.3': list(range(10, 30)),  # 20 pins: 10-29 (same as X10.1)
            'X10.4': list(range(10, 16)) + list(range(20, 26)),  # 12 pins: 10-15 and 20-25 (same as X10.2)
        }
    
    else:
        terminals = {}
    
    return terminals

def one_or_more(terminals):
    """Prompt user to choose a terminal group from available options."""
    print('Choose which terminal group to use:')
    for key in terminals.keys():
        print(key)
    
    pick = input('Enter terminal group: ').upper().strip()
    while pick not in terminals:
        print('Invalid response. Choose from the following:')
        for key in terminals.keys():
            print(key)
        pick = input('Enter terminal group: ').upper().strip()
    
    return pick

def removing_base_terminals(terminals):
    """Allow user to remove terminals and manage terminal groups."""
    pick = one_or_more(terminals)
    
    while True:
        print(f'You are currently operating on {pick}.')
        print_base_terminal(terminals, pick)  
        user_input = input('Enter a terminal to remove (or type "exit" to stop, or type another terminal group to switch): ').strip()

        cancel_process(user_input)
        if user_input.upper() in terminals:
            pick = user_input.upper()
            print(f'Switched to {pick}.')
            continue
        
        try:
            user_input = int(user_input)
            if user_input in terminals[pick]:
                terminals[pick].remove(user_input)
            else:
                print(f"Terminal {user_input} is not in the list of {pick}. Would you like to add terminal {user_input} into the {pick}?")
                repair = user_info('Y/N: ')
                while repair not in ['y', 'n']:
                    print('Invalid response. Please enter Y or N.')
                    repair = user_info('Y/N: ')
                if repair == 'y':
                    terminals[pick].append(user_input)
                    print(f'Terminal {user_input} added.')
                
        except ValueError:
            print("Please enter a valid number.")

def print_base_terminal(terminals, pick):
    """Print the list of terminals for the selected terminal group."""
    print(f"{pick}: {'; '.join(sorted(map(str, terminals[pick])))}")

def cancel_process(cancel):
    """Exit the program if 'exit' is entered."""
    if cancel.lower() == 'exit':
        print('Exiting...')
        exit()

def manage_base_terminals():
    """Manage the base terminals based on the type of terminal chosen."""
    removing_base_terminals(handle_terminal_type(type_of_terminal()))

def manage_terminals():
    """Prompt user to choose between base and custom terminal management."""
    print('Would you like to use baseline terminal (type "Base") or custom terminal (type "Custom")?')
    terminal_type = user_info('Type of terminal: ')
    while terminal_type not in ['base', 'custom']:
        print('Invalid response. Please enter "Base" for baseline terminal or "Custom" for custom terminal')
        terminal_type = user_info('Type of terminal: ')
    if terminal_type == 'base':
        manage_base_terminals()
    else:
        manage_custom_terminals()

def user_info(prompt):
    """Get user input, converting to lowercase and stripping extra spaces."""
    return input(prompt).lower().strip()

def handle_typo(terminal, terminals):
    """Handle cases where the user may have made a typo in the terminal number."""
    typo = user_info('Typo? (Y/N): ')
    while typo not in ['y', 'n']:
        print('Invalid response. Please enter Y or N.')
        typo = user_info('Y/N: ')
    if typo == 'y':
        terminals.remove(terminal)
        print(f'Terminal {terminal} removed.')
    else:
        terminals.append(terminal)

def add_terminal(terminal, terminals):
    """Add a terminal to the list or handle typos if the terminal already exists."""
    if terminal in terminals:
        handle_typo(terminal, terminals)
    else:
        terminals.append(terminal)

def print_terminal(terminals):
    """Print the current list of terminals, sorted."""
    if terminals:
        print(sorted(terminals))
    else:
        print("All terminals have been removed.")

def manage_custom_terminals():
    """Manage custom terminals based on user input."""
    terminals = []
    
    while True:
        user_input = user_info('Enter terminal to be added or type "exit" to stop: ')
        cancel_process(user_input)

        try:
            terminal = int(user_input)
            add_terminal(terminal, terminals)
            print_terminal(terminals)
            print(len(terminals))
        except ValueError:
            print("Invalid input. Please enter a number or 'exit'.")
        
    print("Final list of terminals:", sorted(terminals))
    print("Final count of terminals:", len(terminals))

if __name__ == '__main__':
    manage_terminals()
