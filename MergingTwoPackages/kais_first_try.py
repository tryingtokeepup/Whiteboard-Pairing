def getIndicesOfItemWeights(arr, limit):
    # we need a hash table and we need to 
    weights_hash = {}
    # so, this is the trick -> do it dynamic programming style
    # is you need to iterate through the array, and add it to a hash table
    
    for i in range(len(arr)):
        weight = arr[i] # grab the stupid weight
        weights_hash[arr[i]] = i      # if weight was 4, key is 4, value is index 0    
                # take the weight, and Limit - weight == something in the hash table?
        remainder = limit - weight
        if remainder in weights_hash: 
            if i > weights_hash[remainder]:
                return [i, weights_hash[remainder]] # we have to wait until it goes through
            else:
                return [weights_hash[remainder], i]
    return []
            
# weights_hash[arr[i]] = i # arr[i] = weight

# return weights_hash[remainder]

# print(getIndicesOfItemWeights([4, 6, 10, 15, 16], 21))

arrs = [
    [4, 6, 10, 15, 16], 
    [4, 4], 
    [12, 6, 7, 14, 19, 3, 0, 25, 40], 
    [9]
]

limit_arrs = [
    21,8,7,9
]

# answers = [[3,1], [1,0], [6,2],[]]

print(getIndicesOfItemWeights(arrs[0], limit_arrs[0]))
print(getIndicesOfItemWeights(arrs[1], limit_arrs[1]))
print(getIndicesOfItemWeights(arrs[2], limit_arrs[2]))
print(getIndicesOfItemWeights(arrs[3], limit_arrs[3]))

# for i in range(len(arrs)):
#     output = getIndicesOfItemWeights(arrs[i], limit_arrs)
#     correct_answer = answers[i]
#     print("Your answer: %s\nCorrect answer: %s", output, correct_answer)
        
# space complexity is higher with the subtraction 