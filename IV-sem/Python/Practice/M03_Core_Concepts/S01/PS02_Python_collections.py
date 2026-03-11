accounts = [[1,2,3],
            [3,2,1],]
max_sum = sum(accounts[0])
for i in range( len(accounts)):
    if sum(accounts[i]) > max_sum:
        max_sum = sum(accounts[i])
print(max_sum)