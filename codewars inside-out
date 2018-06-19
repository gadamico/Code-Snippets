def inside_out(st):

    # We'll start by splitting our string on the spaces.
    
    st_list = st.split(' ')
    
    # Now we want to split each word into two halves.
    
    for i in range(len(st_list)):
        word_first = st_list[i][:int(len(st_list[i]) / 2)][::-1]
        if len(st_list[i]) % 2 == 0:
            word_second = st_list[i][int(len(st_list[i]) / 2):][::-1]
            st_list[i] = word_first + word_second
        
        # If our word has an odd length, then we need to keep the middle
        # letter in place.
        
        else:
            word_second = st_list[i][int(len(st_list[i]) / 2) + 1:][::-1]
            st_list[i] = word_first + st_list[i][int(len(st_list[i]) / 2)] + word_second
    return ' '.join(str(word) for word in st_list)
