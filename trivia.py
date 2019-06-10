import tkinter
from time import sleep

global score 
score = []

questions = {
    1: {
        1: "What function would you use to ouput text?",
        "o1" : "Move",
        "o2" : "Go",
        "o3" : "Print",
        "ans": "Print"
        },
    2: {
        2: "What speed is a processor measured in?",
        "o1" : "Gigahertz",
        "o2" : "Megahertz!",
        "o3" : "Quadhertz",
        "ans": "Gigahertz"
        },
    3: {
        3: "What data type contains only positive and negitve whole number?",
        "o1": "variable",
        "o2": "Integer",
        "o3": "List",
        "ans": "Integer"
        },
    4: {
        4: "What data type does an input function return?",
        "o1": "String",
        "o2": "List",
        "o3": "Selection",
        "ans": "String"
        },
    5: {
        5: "What type of value returns true or false?",
        "o1": "If",
        "o2": "Boolean",
        "o3": "else",
        "ans": "Boolean"
        },
    6: {
        6 : "What type of loop is best used for runing code a set number of times? ",
        "o1": "If",
        "o2": "While",
        "o3": "For",
        "ans": "For"
        },
    7: {
        7: "What type of loop is best used for infinite loops?",
        "o1" : "Long",
        "o2" : "While",
        "o3" : "For",
        "ans": "While"
        },
    8: {
        8: "What is it called when you select a section of a string?",
        "o1" : "Slicing",
        "o2" : "Slection",
        "o3" : "Choosing",
        "ans": "Slicing"
        },
    9: {
        9: "What key word is used to exit a loop?",
        "o1" : "Break",
        "o2": "Exit",
        "o3": "End",
        "ans": "Break"
        },
    10: {
        10: "What is a stored value called?",
        "o1" : "Variable",
        "o2": "Stuck",
        "o3": "Stored",
        "ans": "Variable"
        },
    11: {
        11: "Who designed Python",
        "o1" : "James Gosling",
        "o2": "Guido van Rossum",
        "o3": "Yukihiro Matsumoto",
        "ans": "Guido van Rossum"
        },
    12: {
        12: "Ok. You are done. Press END",
        "o1" : "Dont press Submit",
        "o2": "Capisce?",
        "o3": "Press end",
        "ans": ""
        }
    }



def end():
    main.destroy()



global questions_passed
questions_passed = ["-"]



def check_answer():
    global questions_passed
    global score
    option = optionw.get()
    
    answer = questions[len(questions_passed)]["ans"]
    
    if option == answer:
        score.append("lsdf")
        questions_passed.append("seg")
        sleep(1)    
        question["text"] = questions[len(questions_passed)][len(questions_passed)]
        rb1["text"] = questions[len(questions_passed)]["o1"]
        rb1["value"] = questions[len(questions_passed)]["o1"]
        rb2["text"] = questions[len(questions_passed)]["o2"]
        rb2["value"] = questions[len(questions_passed)]["o2"]
        rb3["text"] = questions[len(questions_passed)]["o3"]
        rb3["value"] = questions[len(questions_passed)]["o3"]
        scorep["text"] = "Score: " + str(len(score)) + "/" + str(len(questions)-1)
    else:
        score = score
        questions_passed.append("1")
        sleep(1)
        question["text"] = questions[len(questions_passed)][len(questions_passed)]
        rb1["text"] = questions[len(questions_passed)]["o1"]
        rb1["value"] = questions[len(questions_passed)]["o1"]
        rb2["text"] = questions[len(questions_passed)]["o2"]
        rb2["value"] = questions[len(questions_passed)]["o2"]
        rb3["text"] = questions[len(questions_passed)]["o3"]
        rb3["value"] = questions[len(questions_passed)]["o3"]
        scorep["text"] = "Score: " + str(len(score)) + "/" + str(len(questions)-1)
        
#create widget
global main
main = tkinter.Tk()
question = tkinter.Message(main, text = questions[len(questions_passed)][len(questions_passed)], width = 150)
question.grid(row = 0, column = 1)
global optionw
optionw = tkinter.StringVar()
rb1 = tkinter.Radiobutton(main, text = questions[len(questions_passed)]["o1"], variable = optionw, value = questions[len(questions_passed)]["o1"])
rb1.grid(row = 1, column = 0)        
rb2 = tkinter.Radiobutton(main, text = questions[len(questions_passed)]["o2"], variable = optionw, value = questions[len(questions_passed)]["o2"])
rb2.grid(row = 1, column = 1)
rb3 = tkinter.Radiobutton(main, text = questions[len(questions_passed)]["o3"], variable = optionw, value = questions[len(questions_passed)]["o3"])
rb3.grid(row = 1, column = 3)
submit = tkinter.Button(main, text = "Submit", command = check_answer)
submit.grid(row = 2, column = 1)
scorep = tkinter.Label(main, text = "Score: " + str(len(score))  + "/" + str(len(questions)-1))
scorep.grid(row = 3, column = 1)
end = tkinter.Button(main, text = "End", command = end)
end.grid(row = 4, column = 2)
main.mainloop()
