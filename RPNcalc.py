a=[]
operations ={'+': lambda x,y: y+x, '-': lambda x,y: y-x, '*': lambda x,y: y*x,'/': lambda x,y:y/x,'^': lambda x,y:y**x}

'''
for c in '3 4 2 * 1 5 - 2 3 ^ ^ / +'.split():
    if c in b: a.append(b[c](a.pop(),a.pop()))
    else: a.append(float(c))
    print c, a

# -------YOUR HOME FUNCTION
def calc(expression):
 tokens = expression.split()
 stack = []

 for token in tokens:
     if token in operations:
         step1 = stack.pop()
         step2 = stack.pop()
         result = operations[token](step1,step2)
         stack.append(result)
     else:
         stack.append(int(token))
 return stack.pop()

print(calc ("1 2 + "))
print(calc ("990 1 2 + *"))
print(calc ("1000 990 1 2 + * +"))

'''
#TESTING
banana_bag = "5 3 - 4 * "
palm_tree = {'+': lambda x,y: y+x, '-': lambda x,y: y-x, '*': lambda x,y: y*x,'/': lambda x,y:y/x,'^': lambda x,y:y**x}
stack = []
bananas = banana_bag.split()
for banana in bananas:
    if banana in palm_tree:
        step1 = stack.pop()
        print('step1',step1)
        step2 = stack.pop()
        print('step2',step2)
        result = operations[banana](step1, step2)
        print('result', result)
        stack.append(result)
        print('append',stack.append(result))
    else:
        stack.append(int(banana))
        #print('elseappend',stack.append(int(banana)))
# print(stack.append(int(banana)))
print(stack.pop())
