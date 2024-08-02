lists=[1,2,3,4,5]
print(lists)

def reverse_list(somelists):
    if len(somelists)==0:
        return []
    return [somelists[-1]]+reverse_list(somelists[:-1])
 
print(reverse_list(lists))
