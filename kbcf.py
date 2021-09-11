
def kbc(question_list,options_list):
    solution_list = [3, 4, 1]
    for i in range(len(question_list)):
        print(question_list[i])
        for j in options_list[i]:
            print((j))
        ainput=int(input("\nEnter the correct option number:\n"))
        if solution_list[i] == ainput:
            print("Congratulations!Correct answer.\n")
        else:
            print("Better luck next time:)")
            break
kbc(question_list = ["How many continents are there?",              
                 "What is the capital of India?",               
                 "NG mei kaun se course padhaya jaata hai?"],    
    options_list = [["1.Four", "2.Nine", "3.Seven", "4.Eight"],                              
                ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],                    
                ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]])