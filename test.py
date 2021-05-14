#name = "Fred"
#age = 23
#occupation = "student"

input_name = input("What is your name: ")
input_age = int(input("What is your age: "))
input_occupation = input("What do you do in life: ")

#def hello_worldfunc():
#    print("Hello world")
#    if age == 1:
#        print("My name is", name, "I'm ", age, "year old and,", " I'm a", occupation)
#    elif age >= 2:
#        print("My name is", name, "I'm ", age, "years old and,", " I'm a", occupation)
#    else:
#        print("You can't be", name, "year old. Since you are using a computer right now. Please try again")    
#hello_worldfunc()

def inputFunc(input_name, input_age, input_occupation):
    

    if input_age == 1:
        print("So you said...Your name is", input_name, "you are", input_age, "year old and you're a", input_occupation)
    elif input_age >= 2:
        print("So you said...Your name is", input_name, "you are", input_age, "years old and you're a", input_occupation)
    else:
        print("Hey!",input_name ,"You can't be", input_age, "year old. Since you are using a computer right now. Please try again")
inputFunc(input_name, input_age, input_occupation)