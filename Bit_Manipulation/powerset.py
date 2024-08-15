

def total_number_of_subsets(l:list)-> list[list]:
    
    total_subsets = 1<<len(l)
    
    final=[]
    
    for num in range(total_subsets):
        sub=[]
        
        for i in range(len(l)):
            if (num & (1<<i)):
                sub.append(l[i])

        final.append(sub)
    
    return final


print(total_number_of_subsets([1,2,3]))