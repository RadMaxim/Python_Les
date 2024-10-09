def checkName(name):
    state = False
    if len(name)<3:
        state = True
    if  not name.istitle():
        state = True
    return state

# print( checkName("Maxim"))
def checkSausages(term,temperature):
    state = True
    if a>12:
        state = False
    if b<4 or b>6:
        state = False
    return  state


print(checkSausages(10, 10))