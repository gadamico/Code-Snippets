def lets_bowl():
    """
    This is a complex function that will return the scoresheet for a complete game
    of bowling. The user simply inputs the number of pins knocked down on each roll.
    """
    
    # Importing some useful tools. We'll display our final score
    # in a Pandas DataFrame.
    import numpy as np
    import pandas as pd
    
    # Our scoresheet will have scores for each ball as well as
    # a current frame score and a running cumulative score.
    score = np.zeros((4, 10), dtype=object)
    
    # We'll start, of course, in the first frame.
    frame = 1
    
    # Since the tenth frame can have extra balls, we'll treat that
    # frame separately.
    while frame < 10:
        
        # First ball score
        print(f"How many pins did you knock down on your first ball in frame {frame}?")
        first = int(input("Please enter a number from 0 to 10: "))
        
        # If we bowl a strike
        if first == 10:
            
            print("Strike!")
            
            # Record the strike as such and store the 10-pin score
            score[0, frame-1] = 'X'
            
            score[1, frame-1] = '-'
            
            score[2, frame-1] = 10
        
        # But in the general case:
        else:
            
            # Zeroes are generally marked specially as well
            if first == 0:
            
                score[0, frame-1] = '-'
            
            # Score the first ball
            else:
                
                score[0, frame-1] = first
            
            # If we don't get a strike, we have a second ball to score
            print("How many pins did you knock down on your second ball?")
            second = int(input(f"Please enter a number from 0 to {10-first}: "))

            # If we bowl a spare
            if second == 10 - first:
                
                print("Spare!")
                
                # Record the spare as such and store the 10-pin score
                score[1, frame-1] = '/'
                
                score[2, frame-1] = 10
            
            # But in the general case:
            else:
                
                # Again, mark the zeroes specially
                if second == 0:
            
                    score[1, frame-1] = '-'
                
                # Score the second ball
                else:
                    
                    score[1, frame-1] = second
                
                score[2, frame-1] = first + second
        
        # Update the cumulative score
        # If we're beyond the first frame, then take the previous
        # value of the cumulative score and add the current frame's
        # score.
        if frame > 1:
            
            score[3, frame-1] = score[2, frame-1] + score[3, frame-2]
        
        # Otherwise just set the cumulative score to the first frame's
        # score.
        else:
            
            score[3, frame-1] = score[2, frame-1]
        
        # A strike in frame F gets the next two rolls added into F's score.
        # A spare in frame F gets the next roll added into F's score.
        
        if frame > 1:
        
            if score[0, frame-2] == 'X' or score[1, frame-2] == '/':
        
                # Add ten for any strike in the current frame
                if score[0, frame-1] == 'X':

                    score[2, frame-2] += 10

                # Otherwise just add the value of the first ball.
                elif type(score[0, frame-1]) == int:

                    score[2, frame-2] += score[0, frame-1]
        
            # Then, if we got a strike in the last frame,
            # add the value of the second ball in the current frame (if
            # the first ball was not a strike).
            if score[0, frame-2] == 'X':

                if score[1, frame-1] == '/':

                    score[2, frame-2] += 10 - score[0, frame-1]

                elif type(score[1, frame-1]) == int:

                    score[2, frame-2] += score[1, frame-1]
            
        if frame > 2:
    
            # If we got a strike in each of the last two frames:
            if score[0, frame-3] == 'X' and score[0, frame-2] == 'X':

                if score[0, frame-1] == 'X':
                    
                    score[2, frame-3] += 10
                    
                    score[3, frame-3] += 10

                elif type(score[0, frame-1]) == int:
                    
                    score[2, frame-3] += score[0, frame-1]
                    
                    score[3, frame-3] += score[0, frame-1]
        
        # Update the cumulative scores
        score[3, frame-2] = score[2, frame-2] + score[3, frame-3]
        
        score[3, frame-1] = score[2, frame-1] + score[3, frame-2]
        
        frame += 1
        
    # Tenth frame
    print("How many pins did you knock down on your first ball in frame 10?")
    first = int(input("Please enter a number from 0 to 10: "))

    if first == 10:
        print("Strike!")

        # Record the strike as such and store the 10-pin score
        score[0, 9] = 'X'
        
        score[1, 9] = ['-', '-']
        
        score[2, 9] = 10

    else:

        if first == 0:

            score[0, 9] = '-'

        else:
            
            score[0, 9] = first

        print("How many pins did you knock down on your second ball?")
        second = int(input(f"Please enter a number from 0 to {10-first}: "))

        if second == 10 - first:

            print("Spare!")
            
            # Record the spare as such and store the 10-pin score
            score[1, 9] = ['/', '-']
            
            score[2, 9] = 10

        else:

            if second == 0:

                score[1, 9] = ['-', '-']

            else:
                
                score[1, 9] = second

            score[2, 9] = first + second
    
    score[3, 9] = score[2, 9] + score[3, 8]
    
    # If we bowl a strike in the tenth frame, then we get two bonus balls.
    if score[0, 9] == 'X':

        print("How many pins did you knock down on your first bonus ball?")
        bonus1 = int(input("Please enter a number from 0 to 10: "))

        if bonus1 == 10:
            
            score[1, 9] = ['X', '-']
            
        else:
        
            score[1, 9] = [bonus1, '-']
        
        score[2, 9] += bonus1

        if score[1, 9][0] == 'X':
        
            print("How many pins did you knock down on your second bonus ball?")
            bonus2 = int(input("Please enter a number from 0 to 10: "))
            
        else:
            
            print("How many pins did you knock down on your second bonus ball?")
            bonus2 = int(input(f"Please enter a number from 0 to {10-bonus1}: "))
   
        if bonus2 == 10:
            
            score[1, 9][1] = 'X'
            
        elif bonus2 == 0:
            
            score[1, 9][1] = '-'
        
        else:
            
            score[1, 9][1] = bonus2
        
        score[2, 9] += bonus2
    
    # If we bowl a spare in the tenth frame, then we get one bonus ball.
    if score[1, 9] == ['/', '-']:
        
        print("How many pins did you knock down on your bonus ball?")
        bonus1 = int(input("Please enter a number from 0 to 10: "))
        
        if bonus1 == 10:
            
            score[1, 9] = ['/', 'X']
            
        else:

            score[1, 9][1] = 10 - score[0, 9] + bonus1
        
        score[2, 9] += bonus1
        
    # Adjusting eighth- and ninth-frame scores if necessary
    
    # If we got a strike or a spare in the ninth frame:
    if score[0, 8] == 'X' or score[1, 8] == '/':
        
        # Add ten for any strike in the tenth
        if score[0, 9] == 'X':
            
            score[2, 8] += 10
            
        # Otherwise just add the value of the first ball in the tenth.
        elif type(score[0, 9]) == int:
            
            score[2, 8] += score[0, 9]
        
        # Then, if we got a strike in the ninth,
        # add the value of the second ball in the tenth.
        if score[0, 8] == 'X':
            
            if type(score[1, 9]) == int:

                score[2, 8] += score[1, 9]

            elif score[1, 9][0] == 'X':

                score[2, 8] += 10

            elif type(score[1, 9][0]) == int:

                score[2, 8] += score[1, 9][0]
            
        score[3, 8] = score[2, 8] + score[3, 7]
            
    # If we got a strike in the eighth and a strike in the ninth
    if score[0, 7] == 'X' and score[0, 8] == 'X':
        
        score[2, 7] += 10
        
        score[3, 7] += 10
        
    score[3, 8] = score[2, 8] + score[3, 7]
        
    score[3, 9] = score[2, 9] + score[3, 8]
        
    return pd.DataFrame(score, columns=range(1, 11),
                        index=['first_ball', 'second_ball', 'frame_score', 'cumulative_score'])