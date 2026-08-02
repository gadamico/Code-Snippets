def tv_remote(words):
    
    # Let's represent the virtual keyboard:
    
    tv_dict = {'a': (1, 1), 'b': (1, 2), 'c': (1, 3), 'd': (1, 4),
            'e': (1, 5), '1': (1, 6), '2': (1, 7), '3': (1, 8),
            'f': (2, 1), 'g': (2, 2), 'h': (2, 3), 'i': (2, 4),
            'j': (2, 5), '4': (2, 6), '5': (2, 7), '6': (2, 8),
            'k': (3, 1), 'l': (3, 2), 'm': (3, 3), 'n': (3, 4),
            'o': (3, 5), '7': (3, 6), '8': (3, 7), '9': (3, 8),
            'p': (4, 1), 'q': (4, 2), 'r': (4, 3), 's': (4, 4),
            't': (4, 5), '.': (4, 6), '@': (4, 7), '0': (4, 8),
            'u': (5, 1), 'v': (5, 2), 'w': (5, 3), 'x': (5, 4),
            'y': (5, 5), 'z': (5, 6), '_': (5, 7), '/': (5, 8),
            ' ': (6, 2)}
            
    # Let's get a running total of 'shift' presses
    
    shifts = 0
    
    # degenerate case:
    
    if words == '':
        return 0
        
    # If the first character is not an uppercase letter, then we'll
    # just measure the distance from 'a' to that character.
    
    if not words[0].isupper():
        dist = tv_dict[words[0]][0] - 1 + tv_dict[words[0]][1] - 1
    
    # Otherwise we'll have to go to the 'shift' key and then back.
    
    else:
        shifts += 1
        dist = 5 + abs(tv_dict[words[0].lower()][0] - 6) + abs(tv_dict[words[0].lower()][1] - 1)
    
    # We'll store the location of the first character.
    
    pos = tv_dict[words[0].lower()]
    
    # Now we'll do the same thing for the rest of the characters.
    
    for i in range(1, len(words)):
        
        # We want to know if we need to press 'shift again'.
        
        if ((words[i].islower()) & (shifts % 2 == 1)) | ((words[i].isupper()) & (shifts % 2 == 0)):
                shifts += 1
                dist += abs(pos[0] - 6) + abs(pos[1] - 1) + abs(tv_dict[words[i].lower()][0] - 6) + abs(tv_dict[words[i].lower()][1] - 1)
        else:
            dist += abs(tv_dict[words[i].lower()][0] - pos[0]) + abs(tv_dict[words[i].lower()][1] - pos[1])
        pos = tv_dict[words[i].lower()]
        
        # We need now to count the distance traveled, together with
        # the shifts, together with one click for each letter in the
        # string.
        
    return dist + len(words) + shifts
