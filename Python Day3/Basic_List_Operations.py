lst=list(map(int,input("Enter values: ").split()))
print("Original list: \n",lst)
print("Size of List:",len(lst))
print("Maximum element from the given list: \n",max(lst))
print("Minimum element from the given list: \n",min(lst))
print("Reversed printed List :\n",lst[::-1])
sort_lst=sorted(lst)
print("Sorted list : \n",sort_lst)
sort_lst=sorted(lst,reverse=True)
print("Reversed Sorted list : \n",sort_lst)
lst.append(118)
print("List after appending element at the end of list \n",lst)
lst.insert(2,79)
print("List after inserting element at the particular index of list \n",lst)
print("Sliced List: \n",lst[0:3])
lst.remove(79)
print("Delete particular elements from the list:\n",lst)
lst.pop()
print("Delete last element from the list: \n",lst)