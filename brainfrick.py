#Python Brainfuck Interpreter
#Coded by ReverseVelocity
print("Welcome to Brainfrick! The Python brainfuck interpreter!")
tape = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
tapenum = 0
stringcount = 0
loopcount = 0
code = input("Please enter your code: ")
code = list(code)
stringmax = len(code)
while stringcount < stringmax:
    if code[stringcount] == "+":
        tape[tapenum] += 1
    if code[stringcount] == "-":
        tape[tapenum] += -1
    if code[stringcount] == ">":
        tapenum += 1
    if code[stringcount] == "<":
        tapenum += -1
    if code[stringcount] == ".":
        print(chr(tape[tapenum]))
    if code[stringcount] == "[":
        loopcount = stringcount
    if code[stringcount] == "]":
        if tape[tapenum] != 0:
            stringcount = loopcount
    stringcount += 1
