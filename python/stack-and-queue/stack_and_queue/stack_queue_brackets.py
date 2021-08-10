def validatee_brackets(string):
    open_listt = ["[","{","("]
    close_listt = ["]","}",")"]
    stack = []
    for item in string:
        if item in open_listt:
            stack.append(item)
        elif item in close_listt:
            poss = close_listt.index(item)
            if ((len(stack) > 0) and
                (open_listt[poss] == stack[len(stack)-1])):
                print(open_listt[poss] )
                print(stack[len(stack)-1])
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

print(validatee_brackets('()[[Extra Characters]]'))
print(validatee_brackets('()}})'))
print(validatee_brackets('{)'))
print(validatee_brackets('{}'))
print(validatee_brackets('{}(){}'))
