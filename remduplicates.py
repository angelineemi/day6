list1=[12,24,35,24,88,120,155,88,120,155]
final_list=[]
for num in list1:
    if num not in final_list:
        final_list.append(num)
print(final_list)        
