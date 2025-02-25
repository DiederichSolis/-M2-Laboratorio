def validate_string(afd_dict, string):
   
    current_state = afd_dict['initial']

    for char in string:
        if char in afd_dict['transitions'].get(current_state, {}):
            current_state = afd_dict['transitions'][current_state][char]
        else:
            return False  # No hay transición para este carácter

    return current_state in afd_dict['accepted']