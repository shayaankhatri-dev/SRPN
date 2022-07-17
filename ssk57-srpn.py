#import relevant libraries
#module 're' to be used for re.split function
import re , sys

# Use of object oriented programming
# class SRPN which functions with the use of a stack
# PLEASE DO NOT ENTER EMPTY OPERATIONS IN THE TERMINAL FOR INPUT

class SRPN():
  
  # the following __init__ function ins the constructor for the class
  def __init__(self):
   # initially the stack will be empty   
   self.stack = []
   # setting the minimum and maximum value of an integer inside the stack
   self.pos_Saturation = 2147483647
   self.neg_Saturation = -2147483648
   # to caclulate the stack size
   self.stackSize = len(self.stack)
   # to set the maximum stack size
   self.maxstackSize = 22
   # initially the count variable is set to '0'
   self.count = 0
   # the following is list of random numbers that is relevant for the program
   self.randomNumbers = [1804289383, 846930886, 1681692777, 1714636915, 1957747793, 424238335, 719885386, 1649760492, 596516649, 1189641421, 1025202362, 1350490027, 783368690, 1102520059, 2044897763, 1967513926, 1365180540, 1540383426, 304089172, 1303455736, 35005211, 521595368]
   self.myInput = []

  #function to set the minimum and maximum saturation in a stack by comparing it with relevant input value
  def checkSaturation(self, value):
    # if the input value is less than negative saturation then the input value is turned to the value of negative saturation >
    if value < self.neg_Saturation:
      value = self.neg_Saturation

    
    elif value > self.pos_Saturation:
      value = self.pos_Saturation

    return value
  
  # function to push the value into the stack 
  def push(self, value):
    self.stack.append(value) 
   
  
  # function to set the tone of the logic behind the random number generation and generates the relevant value.
  def randomNumbGenerator(self, operator):
    # once self.count reaches 22, the self.count variable is again reset to 0. How the self.count increases is explained in 'try' below.
    if self.count == 22:
      # self.count set to zero
        self.count = 0

    try:
        # through the count variable we iterate through the list of random numbers from from 0 to 22 position
        value = self.randomNumbers[self.count]
        self.count += 1
        return value
        
        # in case the program is unable to execute the above code the value is set to 'Stack overflow' and returned
    except :
        value = 'Stack overflow.'
        return value  
   
 
 # function to make the program crash in the case where the input is '$', '£', '€' or '¢'
  def crash(self): 
    sys.exit()         
  
  # all results in the mathematical functions go through a saturation check by passing into the checkSaturation() function.
  # function to conduct the addition operation when called
  def addition(self):
        result = self.stack.pop() + self.stack.pop()
        value = self.checkSaturation(result)
        self.push(value)
  
  # function to conduct the substraction operation when called
  def substraction(self):
    # the last value is deducted from the second last value
    result = - self.stack.pop() + self.stack.pop()
    value = self.checkSaturation(result)
    self.push(value)   
  
  # function to conduct the multiplication operation when called
  def multiplication(self):
    result = self.stack.pop()*self.stack.pop()
    value = self.checkSaturation(result)
    self.push(value)
  
  # function to conduct the division operation when called
  def division(self):
    # Robustness adjustment to throw an error when a division by 0 is executed
    if self.stack[-1] == 0:
      print('Divide by 0.')
      return ZeroDivisionError

    else:
        # to handle division when one integer is a negative integer
        if self.stack[-1]*self.stack[-2] < 0:
            result = -(-self.stack.pop(-2)/self.stack.pop())

        else:   
        # to handle division of two positve integers or two negative integers   
            result = self.stack.pop(-2)/self.stack.pop()
        

        value = self.checkSaturation(result)
        self.push(value)

  # function to conduct the modulo operation when called
  def modulo(self):
    if self.stack[-2]*self.stack[-1] < 0:
      result = -(self.stack.pop(-2) % self.stack.pop())
    else:
      result = self.stack.pop(-2) % self.stack.pop()
    value = self.checkSaturation(result)
    self.push(value)

  # function to conduct the power operation when called
  def power(self):
     answer = self.stack.pop(-2)**self.stack.pop()
     answer = int(answer)
     answer = self.checkSaturation(answer)
     self.push(answer) 


  def myCalculator(self, operator):
    try:
      # in case of an '+' sign addition function is called.
      if operator == '+':
        self.addition()
      
      # in case of an '-' sign addition function is called.
      elif operator == '-':
          self.substraction()

      # in case of an '*' sign addition function is called.
      elif operator == '*':
          self.multiplication()

      # in case of an '/' sign addition function is called.           
      elif operator == '/':
          self.division()

      # in case of an 'extra %' sign addition function is called.       
      elif operator == '%':
          self.modulo()

      # in case of an '^' sign addition function is called.
      elif operator == '^':
          self.power()
    
    # if the stack does not have enough items then the operators cannot be applied
    except:
        # to print the stack overflow statement
        print('Stack underflow.')

        return False        

  #function to display the stack when 'd' is the input
  def display_stack(self):
    # Robustness adjustment: negative saturation value is printed when 'd' is the first input
    if len(self.stack) == 0:
      print (self.neg_Saturation)
    else:  
      # iteration to print all inputs inside the stack
      for data in self.stack:
        print (data)
     

  # the following function turns adds the integer value into the stack after goinh through robust operatiosn. This function is called in the handleOperators function and it is different than the push function.
  def appendStack(self, value):
      try:
        # on successful operation value if value is an integer it is pushed onto the stack
        return self.push(int(value))
      except:
        # if this function receives a value that is not an integer than it must be an unrecognised operator or operand and the following error statement is called:
        print("Unrecognised operator or operand \"" + str(value) + "\".")        
  
   # The following handleOperators function is used to handle all the regular operators ('+', '-', '*', '/', '*', '^') and the special operators ('r', 'd', '=', '$', '£', '€', '¢')     
  def handleOperators(self, input_list):

    # the following for loop loop iterates over a list called > input_list. This function is called in the parse() function after the program recognises that the input cannot be turned into an integer and therefor it must be an operator.
    for operator in input_list:
        # the following if statement checks for all the basis mathematical functions and calls the myCalculator function if the input in the list is a mathematical function.
        if (operator == '+') | (operator == '-') | (operator == '*') | (operator == '/') | (operator == '%') | (operator == '^'):
          self.myCalculator(operator)

        # the input 'd' is checked in the input_list and display_stack() function is called if 'd' is found.
        elif (operator == 'd'):
          self.display_stack()
        
        # the input '#' breaks the code to add the commenting function
        elif (operator == '#'):
          break
        
        # if any of these currencies is used > the program will crash
        elif (operator == '$') | (operator == '€') | (operator == '€') | (operator == '¢'):
          self.crash()   
        
        # the following operator checks are used to account for blank spaces and the code continues in such a case.
        elif (operator == '') | (operator == ' ') | (operator == ""):
          continue
        
        # if the operator is 'r' then a random number is generated by calling the randomNumbGenerator() function
        elif operator == 'r':
          if len(self.stack) < 23:
            # if stack size is less than 23 a random number is generated by calling the following function
            operator = self.randomNumbGenerator(operator)

            if operator == 'Stack overflow.':
              print('Stack overflow.')
            else:
              self.appendStack(operator)
          else:
            # if stack size is 23 of more > stack overflow is printed
            print("Stack overflow.")     
        
        # the last entry in the stack is printed as this is the result of an operation that has been appended into the stack
        elif operator == '=':
          print(self.stack[-1])

        else:
          # if the operator does not match any of the above operators, the operator is sent to the appendStack() function where it will be accepted or an error will be shown.
          self.appendStack(operator)
    
    # the execute function is called after the iteration so the program run continuously
    self.execute() 
            
  
  # The parse functions first turns the input expression into a list of strings using the split function in the 're' module in python. The function then seperates the number inputs and handles them. The operators in the input_list are passed on to the handleOperators function. 
  def startAndParse(self):
    # the following is used to ask user for an input and it is stored in the variable expression which is in the form of a string
    expression = input("")
    # the expression is then split using the re module and assigned to a variable self.myInput which is a variable within the class. Using split the expression is turned into a list of strings in the form [" ", " ", " "]... 
    # The numbers 0 to 9 are considered in this
    self.myInput = re.split('([^0-9])', expression)

    # Robustness 1: the following if statement is used for the special case when the first entry inside the stack is of a negative integer. 
    # The first element in the if statement makes sure that there is AN ENTRY at the third position and it is not empty, the second and third element.   which is then joined by the end statment to make sure that the first position is of a number and the second position is of a negative sign.

    # example: an input of -100 will be stored in the list as ['', '-', '100'] at this point
      
    
    if self.myInput [0] == '' and self.myInput[1] == '-' and self.myInput[2] != '':
    # the following split application on a list that has already been split would combine the relevant inputs into one string.
    # based on the previous example after the second split our list containing inputs would look like = ['-100']
        self.myInput = re.split(('( - )'), expression) 

    # Robustness 2:if the case is not of a first integer being a negative one then then the length of the stack is checked if it is greater than the allowed stack size of 22. 
    elif len(self.stack) > 22:
    # The following try statement makes sure that when the the stack size grows more than 22 the system returns an error of 'Stack overflow' as long as the entry into the stack is of an integer number. If the entry is an operator the input is passed to the except statement because when an operator is used > the stack size reduces so operators must be 'ACCEPTED' 
      try:
        # if this is successful the system will report 'Stack overflow'
        integer = int(expression)
        print('Stack overflow.')
        # to recontinue the loop after stack overflow
        self.parse()

      except ValueError:
        # if the int(expression) command is not successful the input is considered an operator and passed to the handleOperators function
        self.handleOperators(self.myInput)
  
  # function to set the execution priority of the program
  def execute(self):

    self.startAndParse()
    self.handleOperators(self.myInput)
  
  # the main function that runs the program
  def main(self):

    print("You can now start interacting with the SPRN calculator")  
    # while statement passed to maintain continuity of program
    while True:
      self.execute() 
 

# object SRPN assigned to calculator
calculator = SRPN()

# to start the program
calculator.main()
