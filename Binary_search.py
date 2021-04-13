def BinarySearch(list,n):    
   l = 0    
   h = len(list)-1    
   found = 0    
   while i <= h:    
      mid = (l + h) // 2   
   
      if list[mid] == n:    
         print("Element {} found at position {}".format(n,mid+1))    
         found = 1    
      return True     
      if list[mid] > n:    
         h = mid - 1    
      if list[mid] < n:    
         l = mid + 1    
   if found !=1:    
      print("Searching element {} not found in the array list".format(n))    
       
   return    
       
list = []    
size = int(input("Enter the size of the array: "))    
       
for i in range(size):    
     x = int(input("Enter the element at {} position in the array: ".format(i+1)))    
     list.append(x)    
      
list.sort()    
print("Entered array elements are: ")    
for lists in list:    
    print(lists,end="\t")    
     
se = int(input("\nEnter the array element to be searched: "))    
BinarySearch(list, se)   
