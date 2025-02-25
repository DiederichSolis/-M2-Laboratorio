
def minimize_afd(afd):
    accepted_states = set(afd['accepted'])
    non_accepted_states = set(afd['transitions'].keys()) - accepted_states

    grouped = {}
    
    for state, transitions in afd['transitions'].items():
        is_accepted = state in accepted_states
        key = (frozenset(transitions.items()), is_accepted)  
        grouped.setdefault(key, []).append(state)

    minimized_transitions = {}
    minimized_accepted = set()

   
    for group in grouped.values():
        representative = frozenset().union(*group)  
        minimized_transitions[representative] = {}

        for input_char, next_state in afd['transitions'][group[0]].items():
            for next_group in grouped.values():
                if next_state in next_group:
                    next_representative = frozenset().union(*next_group) 
                    minimized_transitions[representative][input_char] = next_representative
                    break

        if any(state in accepted_states for state in group):
            minimized_accepted.add(representative)

    return {
        'transitions': minimized_transitions,
        'accepted': list(minimized_accepted)
    }
