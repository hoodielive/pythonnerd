registry = []

# decorator -> append to pos arg -> decorated to registry variable -> return method unchanged -> any method that receives the 
# register decorator will have itself appened to registry.
def register(decorated):
    registry.append(decorated)
    return decorated

@register 
def examp1():
    return 3 

@register 
def examp2():
    return 5

answers = []
for func in registry:
    answers.append(func()) # answers list now will contain 3, 5
print(answers)
