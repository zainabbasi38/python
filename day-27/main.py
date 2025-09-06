question_list = ["Who is founder of pakistan ?", "When Pakistan get independence", "Who is the current PM of Pakistan?"]
score = 0
# print(question_list[0])
# user_input = input("Type Here: ")
# if user_input.lower() == "quaid-e-azam":
#     score = score + 1
#     print("Correct")
# else:
#     print("Wrong")

# print(question_list[1])
# user_input = input("Type Here: ")
# if user_input.lower() == "1947":
#     score = score + 1
#     # score = score + 1
#     print("Correct")
# else:
#     print("Wrong")

# print(question_list[2])
# user_input = input("Type Here: ")
# if user_input.lower() == "shahbaz":
#     score = score + 1
#     print("Correct")
# else:
#     print("Wrong")

for i,question in enumerate(question_list):
    print(f"Question {i+1}: {question}")
    user_input = input("Write your answer: ")
    if user_input.lower() == "quaid-e-azam" and (i == 0):

        score = score +1
        print("Correct")

    if user_input.lower() == "1947" and (i == 1):

        score = score +1
        print("Correct")
    if user_input.lower() == "shahbaz" and (i == 2):

        score = score +1
        print("Correct")

    
    

    # elif user_input== "1947":
    #     score = score +1
    #     print("Correct")

    # elif user_input.lower() == "shahbaz":
    #     score = score +1
    #     print("Correct")

    # else:
    #     print("Wrong")

result = (score/len(question_list))*100
print(f"Precentage: {result:.2f}")