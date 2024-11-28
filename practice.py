"""# BLUEPRINT | DONT EDIT
playing = True

a = int(input("Choose a number:\n"))
b = int(input("Choose another one:\n"))
operation = input(
    "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
)
# /BLUEPRINT
"""
# 👇🏻 YOUR CODE 👇🏻:
playing=True
while playing:
        userfirstchoice = int(input("Chocse a number:"))
        usersecondchoice = int(input("Choose another one:"))
        operation = input(
            "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
        )
        if operation == "+":
                print("result:", userfirstchoice + usersecondchoice)
        elif operation == "-":
                print("result:", userfirstchoice - usersecondchoice)
        elif operation == "*":
                print("result:", usersecondchoice * userfirstchoice)
        elif operation == "exit":
                playing = False
# /YOUR CODE
