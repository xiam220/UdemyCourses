Determine User Age
  birth_year = input('What year were you born?')
  age = 2019 - int(birth_year)
  print(f'Your age is: {age}')
  
  """
    Console:
    What year were you born?1999
    Your age is: 20
    >
  """

Password Checker
  username = input('Enter your username: ')
  password = input('Enter your password: ')
  
  password_length = len(password)
  hidden_password = '*' * password_length
  
  print(f'Username: {username} \n Password: {hidden_password}')
  
