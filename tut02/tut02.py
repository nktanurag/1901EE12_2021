#Take a input_list and return a list containing all non-integers in input_list
def isNonInteger(input_nums):
    non_integer_value=[]
    for  integer in input_nums:
        if type(integer) != type(1):
            non_integer_value.append(integer)
    
    return non_integer_value


#Calculate the score according to given logic 
def get_memory_score(input_nums):
    memory=[]
    score=0
    for integer in input_nums:
        if (integer in memory):
            score+=1
        else:
            if len(memory)==5:
                memory.pop(0)
            memory.append(integer)
    
    return score
                

#Input List for calculating Score
input_nums = [3, 4, 5, 3, 2, 1]


#Getting a list of non integers value if present
non_integer_value=isNonInteger(input_nums)


if len(non_integer_value) != 0:
    print("Please enter a valid input list")
    print("Invalid inputs detected: ", end=" ")
    print(non_integer_value)

else:
    score=get_memory_score(input_nums)
    print("Score: " + str(score))

