'''
#1. Write a Python program which accepts a sequence of comma-separated numbers from the
   user and generate a list and a tuple with those numbers. 

i=input("enter the numbers separated by commas:").split(",")
print("list:",i)
print("tuple:",tuple(i))
'''



'''
#2. Write a Python program to print all even numbers from a given numbers list in the same 
   order and stop the printing if any numbers that come after 237 in the sequence. 
   
numbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
           399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
           815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
           958,743, 527 ]
for i in numbers:
    if i==237:
        break;
    elif(i%2==0):
        print(i)
        
'''





    
'''
#3. Write a python program for binary search to search a number in the list of given numbers.
   If the number isn't present, give the appropriate message. Both the list and the number 
   to be searched is given by the user. 

def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
	


n=int(input("enter the number of elements:"))
arr=[]

for i in range(0,n):
    ele=int(input())
    arr.append(ele)
    
n=int(input("enter the element to be searched:"))
if (binary_search(arr, n)):
     print("the element is present in the list")
else:
    print("the element is not present in the list")
    

'''

'''
#4. Write a Python program to calculate the sum of the digits in an integer.

n=int(input("enter a number:"))
s=0
while(n>0):
  dig=n%10
  s=s+dig
  n=n//10
print("the sum of the digits is :",s)
 '''


'''
#5. Write a Python program to check if a string is numeric.

string=input("enter a string:")
count = 0
for a in string: 
    if (a.isnumeric()) == True: 
        count=-1
        break
if (count!=0):
    print("the string is numeric")
else:
    print("the string is not numeric")
'''

