def circuit(gas,cost):
    if sum(gas)<sum(cost):
        return -1
    start_index=0
    current_tank=0
    for i in range (len(gas)):
        current_tank+=gas[i]-cost[i]
        if current_tank<0:
            start_index=i+1
            current_tank=0
    return start_index
    
gas=[1,2,3,4,5]
cost=[3,4,5,1,2]
print(circuit(gas,cost))  
