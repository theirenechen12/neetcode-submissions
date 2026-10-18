# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        #input has the pair with a key which is an integer and value which is a string

        #write a for loop that iterates thru the element of list of pairs
        #have to put pairs because that is the name of the list that I am putting in as arguments 
        newlist = []
        temp = pairs.copy()
        tempElement = ()

        for i in range(0,len(pairs)):
            tempElement = temp[i] #declare pairs[i] as the temp element

            # Original code retained:
            # temp.append(tempElement)
            # for j in range(0,len(pairs)):
            #     if tempElement != pairs[j]:
            #         #append to left if key less than current, append to right if greater than
            #         if tempElement.key>=pairs[j].key:
            #             #want to insert to the left of tempElement instead of normal right
            #             temp.insert(pairs[j],tempElement.index - 1) #find the index for tempElement
            #         else:
            #             temp.insert(pairs[j],tempElement.index + 1) #insert to the right

            j = i
            while j > 0 and temp[j].key < temp[j - 1].key:
                temp[j], temp[j - 1] = temp[j - 1], temp[j]
                j -= 1

            newlist.append(temp.copy())

            # for j in range(0,len(pairs)-1):
            # if pairs[j].key<=pairs[j+1].key:
            #     temp.append(pairs[j])
            # else:
            #     temp.append(pairs[j+1])
            #remove all elements of array to clear for the next batch
            # Original code retained but disabled:
            # temp = []

        return newlist