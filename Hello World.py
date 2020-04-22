#Like in the above statements, all we are doing here is getting some user input and storing 
#that input in the variable userName. In this case, the users log-in name is scored in the variable.

userName = input("Hello! Please enter your facebook username!")

#I'm doing the same thing here as in line 1, except
#the variable userPassword is storing the users password

userPassword = input("Hello! Please enter your facebook password!")

#Conditional if-statement checking the boolean expression if userName == wes resolves to true and
#userPassword == CSF534ROCKS! is also true, then we print out Welcome to facebook!

# If the username that the user provides does not match the string 'wes' and the userPassword the 
#user provides does not match the string CSF534ROCKS!, then the user is denied entry and 
#the message wrong credentials, try again! is reported.


if(userName.lower() == "wes" and userPassword == "CSF534ROCKS!"):
    print("Welcome to facebook!")
else:
    print("Wrong credentials, try again!")


#Notice the normalization of input with the .lower() method. This method will take whatever string is provided to it, and make it all lowercase. So, if I were to run the command HELLO.lower() the output would be `hello` in all lowercase characters

