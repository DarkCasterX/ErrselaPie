from errpy import errsela
import sys

def interactive_mode():
    interface = errsela()
    while(True):
        try: 
            cmd = input("What command would you like to send ERRSELA? (Enter 'options' to see a list of commands) ")
            if(cmd.lower() == 'talk'):
                speech = input("What would you like ERRSELA to say? ")
                interface.talk(speech).getdefaults()
            elif(cmd.lower() == 'movef'):
                time = input("How long should ERRSELA move forward? ")
                interface.moveforward(int(time)).getdefaults()
            elif(cmd.lower() == 'turnr'):
                choice = input('Would you like to use the default settings for this function? ')
                if(choice.lower() == 'yes'):
                    interface.turnright().getdefaults()
                elif(choice.lower() == 'no'):
                    try:
                        power = int(input('How much power would you like to use? '))
                        duration = int(input('What time duration would you like to use? '))
                        interface.turnright(power, duration).getdefaults()
                    except Exception as e:
                        print(e)
                else:
                    print("\nInvalid input. The valid inputs for the \"turnr\" command are: \"left\", \"right\".\n")
            elif(cmd.lower() == 'turnl'):
                choice = input('Would you like to use the default settings for this function? ')
                if(choice.lower() == 'yes'):
                    interface.turnleft().getdefaults()
                elif(choice.lower() == 'no'):
                    try:
                        power = int(input('How much power would you like to use? '))
                        duration = int(input('What time duration would you like to use? '))
                        interface.turnleft(power, duration).getdefaults()
                    except Exception as e:
                        print(e)
                else:
                    print("\nInvalid input. The valid inputs for the \"turnl\" command are: \"yes\", \"no\".\n")
            elif(cmd.lower() == 'turnround'):
                choice = input('Which way should ERRSELA turn? ')
                if(choice.lower() == 'right'):
                    interface.turnaroundr().getdefaults()
                elif(choice.lower() == 'left'):
                    interface.turnaroundl().getdefaults()
                else:
                    print("\nInvalid input. The valid inputs for the \"turnround\" command are: \"left\", \"right\".\n")
            elif(cmd.lower() == 'blink'):
                times = int(input('How many times should ERRSELA blink? '))
                interface.blink(times).getdefaults()
            elif(cmd.lower() == 'wink'):
                choice = input('Which eye should ERRSELA wink? ')
                if(choice.lower() == 'left'):
                    interface.winkl().getdefaults()
                elif(choice.lower() == 'right'):
                    interface.winkr().getdefaults()
                else:
                    print("\nInvalid input. The valid inputs for the \"wink\" command are: \"left\", \"right\".\n")
            elif(cmd.lower() == 'end'):
                print("\nEnding interactive session...\n")
                break
            elif(cmd.lower() == 'options'):
                print("\nblink\nend\nmovef\ntalk\nturnl\nturnr\nturnround\nwink\n")
            else:
                print("ERRSELA didn't understand that.\n")
        except Exception as e:
            print("An error occured, ", e)

def main():
    try:
        interactive_mode()
    except KeyboardInterrupt:
        print("\nYou used Ctrl-C to exit. Next time, try using the \"end\" command.\n")

if __name__ == "__main__":
    main()
