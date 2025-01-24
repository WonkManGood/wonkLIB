from os import path

states_path = str(path.dirname(path.abspath(__file__)) + '/states')
    ### Tony, where are you when i need you. . .

def states_modify(
        line: int,
        position: int,
        state: bool,
        ) -> None:
    '''
    Opens the state file for this library. It's formatting is as follows:\n\n
    
    | 0: ---
    | 1: 000
    | 2: 000
    | 3: 000
    | 4: ---
    | 5: 000
    | 6: 000
    | 7: 000
    
    The states file acts as a inter-file buffer to communicate communication
    between python files. Lines 1 -> 3 take zero-one operators and transforms them
    to booleans. Lines 5 -> 7 store single digit values for match statements
    presented by the using script.

    `states_modify()` opens the states and modifies the values with required
    positional arguments line, poistion, and state. If anything other than 1's
    or 0's is entered for lines 1-3, it returns a ValueError. It returns nothing
    and only modifies the file. No defaults.

    `states_read()` opens the states and reads the listed line and position. If line
    is equal-between 1-3 and positional is 1 or 0, it returns a boolean. All other
    lines besides 0 and 4 return the lines positional contents.

    `states_clear()` permanently resets states upon being called. Irreversable via package.
    '''
    
    positional = (((line-1)*3)+position)-1
    print(positional)
    
    with open(states_path, 'r') as states_read:
        
        if line == [1, 2, 3] and str(position).isalpha():
            raise ValueError('\n\nLines 1-3 take 1\'s and 0\'s\n')
        
        splitted = []
        read_lines: list = states_read.readlines()
        for row in read_lines:
            row = str(row).replace('\n', '')
            for letter in range(len(row)):
                if str(row[letter]) == str(positional):
                    if state: splitted.append('1')              #fix this later
                    if not state: splitted.append('0')
                else: splitted.append(row[letter])
        print(splitted)
        print(splitted[positional])
        
        # with open(states_path, 'w') as states_write:
            
        
    
states_modify(1, 1, False)

