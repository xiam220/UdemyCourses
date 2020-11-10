numbers = '01234567'
  
  print(numbers[0])                           #return 0th index
  #Output: 0
  
  #numbers[0:i]                               #return 0th to ith index (not including ith position)
  print(numbers[0:2])                         
  #Output: 01
  
  #numbers[start:stop:stepover]               #return elements from start to stop, stepping over ever stepover
  print(numbers[0:8:2])                       #return elements from 0 to 8, stepping over every 2nd
  #Output: 0246
  
  print(numbers[1:])                          #start at 1 and print all the way to the end
  #Output: 1234567
  
  print(numbers[:5])                          #start at 0 and stops at 5
  #Output: 01234
  
  print(numbers[::1])                         #start at 0, stop at 8, step over by 1
  #Output: 01234567
  
  print(numbers[-1])                          #start at the end
  #Output: 7
  print(numbers[-2])
  #Output: 6
  print(numbers[::-1])
  #Output: 76543210
  
"""
String are immutable, meaning they cannot be changed 
For example, 
  numbers = '01234567'
You can modify the variable type:
  numbers = 100
  print(numbers)
  #Output: 100 
However, you can't change the String itself:
  numbers[0] = '8'
  print(numbers)
  #Output:
  Traceback (most recent call last):
    ...
  >
The only way to modify the String is to change the variable completely:
  numbers = '81234567'
  print(numbers[0])
  #Output: 8
"""
