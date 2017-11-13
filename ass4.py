def remove_adjacent(nums):
    ok=[nums[0]]


    for num in range(1,len(nums)):

        if nums[num] != nums[num-1]:
            ok.append(nums[num])
    return ok
print(remove_adjacent([1,2,2,3,3,6]))
#2
def linear_merge(list1, list2):
    list=[]


    while list1!=[] and list2!=[]:
        if list1[-1] > list2[-1]:
            list.append(list1.pop())
        else:
            list.append(list2.pop())
    if list1!=[]:
        list1.reverse()
        list=list+list1
    if list2!=[]:
        list2.reverse()
        list=list+list2

    list.reverse()
    return list

print(linear_merge([2,5,7,9],[1,3,6,8]))