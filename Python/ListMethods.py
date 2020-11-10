ListMethods1
  basket = [1, 2, 3, 4, 5]
  len(basket)
  #returns 5

  #Appending to list
  basket.append(100)
  #returns [1, 2, 3, 4, 5, 100]
  
  #Inserting to list
  basket.insert(4, 100)
  #returns [1, 2, 3, 4, 100, 5]
  
  #Extending list
  basket.extend([100, 101])                           #Takes an iterable [that you can loop over]
  #returns [1, 2, 3, 4, 5, 100, 101]                  #Modifies the list in place and extends our list
  
  #basket.pop(i)                                      #Removes element at position i
  basket.pop()                                        #Removes last element in list         
  #returns [1, 2, 3, 4, 5]
  
  basket.pop(0)                                       
  #returns [2, 3, 4, 5]
  
  #basket.remove()
  basket.remove(4)                                    #Pass value we want to remove
  #returns [2, 3, 5]
  
  """
  .pop() returns whatever you just removed
    basket = [1, 2, 3, 4, 5]
    new_list = basket.pop(4)
    print(new_list)
    #Output: 5
  """
  
  #Clear
  basket.clear()
  #returns []

ListMethods2
  basket = ['a', 'b', 'c', 'd', 'e']
  basket.index('d')
  #returns 3
  
  basket.index('d', 0, 3)
  """
  Console:
    Traceback (most recent call last):
      ...
    ValueError: 'd' is not in list
  """
  basket.index('d', 0, 4)
  #returns 3
  
  print('d' in basket)
  #Output: True
  
  print('i' in 'hi my name is Ian')
  #Output: True
  
  basket = ['a', 'b', 'c', 'd', 'e', 'd']
  
  #.count()                                       #Count how many times an item occurs
  basket.count('d')                                         
  #returns 2
