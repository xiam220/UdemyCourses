Lists and List Splicing
  """
  Lists are a form of arrays, a collection of items
  Lists are mutable, meaning they can be changed
  You are creating a new copy of a list
  """

  amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']

  print(amazon_cart)
  #Output: ['notebooks', 'sunglasses', 'toys', 'grapes']

  print(amazon_cart[0])
  #Output: notebooks

  amazon_cart[0] = 'laptop'
  print(amazon_cart)
  #Output: ['laptop', 'sunglasses', 'toys', 'grapes']

  """
  Changing the pointer of arr1 to arr2
  Modifications to arr1 or arr2 will modify the other array
  arr2 = arr1
  """
  new_cart = amazon_cart
  new_cart = 'gum'
  print(new_cart)
  #Output: ['gum', 'sunglasses', 'toys', 'grapes']

  print(amazon_cart)
  #Output: ['gum', 'sunglasses', 'toys', 'grapes']

  """
  Copying an array
  arr2 = arr1[:]
  """
  new_cart = amazon_cart[:]
  new_cart[0] = 'gum'
  print(new_cart)
  #Output: ['gum', 'sunglasses', 'toys', 'grapes']

  print(amazong_cart)
  #Output: ['laptop', 'sunglasses', 'toys', 'grapes']
  
Matrices
  matrix = [
            [1, 5, 1],
            [0, 1, 0],
            [1, 0, 1]
           ]
  print(matrix[0][1])
  #Output: 5
