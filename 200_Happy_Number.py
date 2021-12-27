# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

def isHappy(n):
    # creating a set to append all numbers we visit
    seen = set()
    
    #If the number is not happy, at some point, the sum of squares will be repeated in a cycle, 
    # meaning the code will repeat the same calculations over and over in an infinite loop. 
    # So, we check if n has happened before in seen.
    # If a total ever repeated (was found in the visited array), it meant that the loop would g
    # o on endlessly and it is not a happy number.
   
    while n not in seen:
        # add the number to the seen set
        seen.add(n)

        n = sum([int(x)**2 for x in str(n)])

        if n==1:
            return True

    return False

print(isHappy(1298888999))