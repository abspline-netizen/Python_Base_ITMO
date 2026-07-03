
import calculations as cl

def main():
    while True:
        try:
            user_typing = input(f"Command ('loc', 'zip', 'dist', 'end') =>")
            if not (user_typing=='loc' or user_typing=='zip' or user_typing=='dist' or user_typing=='end'):
                print('Invalid command, ignoring')
                continue
            if user_typing == 'loc':
                command = cl.loc_fn()
                return command
            elif user_typing == 'zip':
                command = cl.zip_fn()
                return command
            elif user_typing == 'dist':
                command = cl.dist_fn()
                return command

            elif user_typing == 'end':
                print('end')
                print('The end of program')
                return 0
        except:
            print('Please enter a valid input')
            print('use "end" for exit')


#a=1
#while a>0:
    #b=main()

while True:
    result = main()
    if result == 0:
        break