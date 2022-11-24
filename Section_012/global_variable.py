



"""/* Modifying Global Scope */ """

# enemies = 1

# def increase_enemies():
#     print(f'enemies inside function: {enemies}')
#     return (enemies + 1) 


# enemies = increase_enemies()
# print(f'enemies outside function: {enemies}')


"""/*  Using the return function to change variables soft */ """
enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f'enemies inside function: {enemies}')

print(f'enemies between function: {enemies}')

increase_enemies()
print(f'enemies outside function: {enemies}')