String Functions
  greet = 'hellloooo'

  print(len(greet)) 
  #Output: 9

  print(greet[0:len(greet)])
  #Output: hellloooo

Formatted Strings
  name = 'Johnny'
  age = 55
  
  print(f'Hi {name}. You are {age} years old.')
  #Output: Hi Johnny. You are 55 years old. 
  
  """
  Alternative:
  print('Hi ' + name + '. You are ' + str(age) + ' years old.')
  """
  
String Methods
  quote = 'to be or not to be'

  #str.upper()                                  #Modifies entire str to uppercase
  print(quote.upper())
  #Output: TO BE OR NOT TO BE

  #str.capitalize()                             #Capitalizes first character in str
  print(quote.capitalize())                 
  #Output: To be or not to be

  #str.find('x')                                #Returns position of x if it exists
  print(quote.find('be'))
  #Output: 3

  #str.replace(old, new)                        #Replace all occurrences of old with new
  print(quote.replace('be', 'me'))
  #Output: to me or not to me

  print(quote)
  #Output: to be or not to be
  
  """
   When we use methods, we are creating a new String
   We never modify the original String
   We are not assigning it to anything
  """
