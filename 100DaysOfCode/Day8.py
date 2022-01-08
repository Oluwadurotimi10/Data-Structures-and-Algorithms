"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each 
person wears a sticker indicating their initial position in the queue from 1 to n.
 Any person can bribe the person directly in front of them to swap positions, but they
 still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. 
Print the number of bribes, or, if anyone has bribed more than two people, 
print Too chaotic.
"""
def minimumBribes(q):
    count = 0
    #looping through to check if anyone bribed more than 2 people
    for i, j in enumerate(q):
        #print(i,j)
        if (j - (i+1)) > 2:
            print("Too chaotic")
            return
        #checking for only bribes less than 2
        for k in range(max(0, q[i]-2), i):
            if q[i] < q[k]:
                #print(q[k])
                count += 1
   
    print(count)
    return 
q = [2,1,5,3,4,6,8,7]
#q = [2,1,3,4,8,5,6,7]
#q=[1,4,2,3]
minimumBribes(q)