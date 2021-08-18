#tut01
#To find whether number is meraki or not and print frequency of meraki and non-meraki numbers
#Ankit Anurag  Roll- 1901EE12
count_Meraki=0
count_nonMeraki=0
def meraki_helper(n):
    """This will detect meraki numner"""
    stringN=str(n)
    isMerakiNumber=True
    for char_index in range(len(stringN)-1):
        curr=int(stringN[char_index])
        next=int(stringN[char_index+1])
        if abs(curr-next)!=1:
            isMerakiNumber=False
            break
    
    if isMerakiNumber==True:
        global count_Meraki
        count_Meraki+=1
        print("Yes - "+stringN+" is a Meraki number")
    else:
        global count_nonMeraki
        count_nonMeraki+=1
        print("No - "+stringN+" is not a Meraki number")



input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]
for n in input:
    meraki_helper(n)

print("the input list contains " + str(count_Meraki) + " meraki and " + str(count_nonMeraki) + " non meraki numbers.")