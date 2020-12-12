import requests
import time


#Helper class to contain all of Errsela's functionality
class errsela:
    
    def __init__(self):

        print("Initializing errsela client...\n")

        self.success_status = "SS_SUCCESS"

        #Right motor power
        self.right_motor = 180

        #Left motor power
        self.left_motor = 180

        #Speech command for Errsela to talk
        self.speech = ''

        #Eye 1 power
        self.servo1 = 180

        #Eye 2 power
        self.servo2 = 180

        #Duration of movement
        self.duration = 0

        #Base URL which will be concatenated for every request
        self.url= 'http://nyitetic.nyit.edu/errsela/botcommand.aspx?'

        print("Initialized.")

    #Prints the current success status
    def print_success_status(self):
        print("\nPrevious operation's success status: " + self.success_status + "\n")
        return self

    #Shows response information
    def showresponseinfo(self, command):
        print('\nResponse Info:\n')
        print(command.status_code)
        print(command.headers)

    #Function to handle commands and send to errsela
    def sendcommand(self):
        if(self.success_status == "SS_FAILURE"):
            self.print_success_status()
        print('Sending commands to ERRSELA...\n')
        try:
            command = requests.get(self.url + 'rm=' + str(self.right_motor) + '&lm=' + str(self.left_motor) + '&speech=' + str(self.speech) + '&servo1=' + str(self.servo1) + '&servo2=' + str(self.servo2) + '&duration=' + str(self.duration))
            print('Command successfuly sent.\n')
            
            #Handle an unsatisfactory response
            if(command.status_code != 200):
                print('\nCommand wasn\'t properly received by ERRSELA.')
                self.showresponseinfo(command)
                yesorno = input('Would you like to resend this commmand? Enter \'Yes\' to resend, otherwise enter \'No\' ').lower()
                if(yesorno == 'yes'):
                    print('You decided to resend the command.\nResending...')
                    command = requests.get(self.url + 'rm=' + str(self.right_motor) + '&lm=' + str(self.left_motor) + '&speech=' + str(self.speech) + '&servo1=' + str(self.servo1) + '&servo2=' + str(self.servo2) + '&duration=' + str(self.duration))
                    print('Command resent.')
                if(yesorno == 'no'):
                    print('Cancelled the command.')
            
            return self
        except Exception as e:
            self.success_status = "SS_FAILURE"
            print('Something went wrong...')
            choice = input("Would you like to see the error output?").lower()
            if(choice == 'yes'):
                print(e)
            else:
                print("Thoroughly review your code. This is a critical error in a builtin command.\n")
                print("It is highly encouraged to look at the command's success status\n")
                print("And look at the error output.\n")
            
            self.getdefaults()
            return 0

    #Resets all values to their defaults, helps prevent 
    #Accidentally reusing a value or command    
    def getdefaults(self):
        try:
            self.right_motor = 180
            self.left_motor = 180
            self.speech =''
            self.servo1 = 180
            self.servo2 = 180
            self.duration = 0
            
            return self
        except:
            print("Failed to reset values to their defaults. Returning...")
            return 0

    #Send a speech command to Errsela    
    def talk(self, message):
        try:
            self.speech = message
            return self.sendcommand()
        except:
            print("Command failed.")
            self.success_status = "SS_FAILURE"
            return self

    #Commands Errsela to move in one direction for an amount of time    
    def moveforward(self, time):
        try:
            self.duration = time
            self.right_motor = 0
            self.left_motor = 0
            return self.sendcommand()
        except:
            print("Command failed.")
            self.success_status = "SS_FAILURE"
            return self
        
    #Commands Errsela to turn right

    #Note: You can control the angle which Errsela turns by modifying the power
    #And duration arguments when calling this function    
    def turnright(self, power=180, duration=3):
        try:
            self.right_motor = 180
            self.left_motor = 180 - power
            self.duration = 3
            return self.sendcommand()
        except:
            print("Command failed.")
            self.success_status = "SS_FAILURE"
            return self

    #Commands Errsela to turn left
    
    #Note: You can control the angle which Errsela turns by modifying the power
    #And duration arguments when calling this function    
    def turnleft(self, power=180, duration=3):
        try:
            self.right_motor  = 180 - power
            self.left_motor = 180
            self.duration = 3
            return self.sendcommand()
        except:
            print("Command failed.")
            self.success_status = "SS_FAILURE"
            return self

    #Commands Errsela to make a U-turn towards the right    
    def turnaroundr(self):
        try:
            self.right_motor = 0
            self.left_motor = 180
            self.duration = 5
            return self.sendcommand()
        except:
            print("Command failed.")
            self.success_status = "SS_FAILURE"
            return self

    #Commands Errsela to make a U-turn towards the left    
    def turnaroundl(self):
        try:
            self.right_motor = 180
            self.left_motor = 0
            self.duration = 5
            return self.sendcommand()
        except:
            print("Command failed.")
            self.success_status = "SS_FAILURE"
            return self

    #Dims Errsela's lights    
    def blink(self, times):
        try:
            time.sleep(2.5)
            counter = 0
            if(counter < times):
                self.servo1 = 0
                self.servo2 = 0
                self.blink(times - 1)
                return self.sendcommand()
            else:
                return self
        except:
            print("Command failed.")
            self.success_status = "SS_FAILURE"
            return self
        

    #Dims one of Errsela's lights
    def winkl(self):
        try:
            self.servo1 = 0
            self.servo2 = 180
            return self.sendcommand()
        except:
            print("Command failed.")
            self.success_status = "SS_FAILURE"
            return self

     #Dims one of Errsela's lights   
    def winkr(self):
        try:
            self.servo1 = 180
            self.servo2 = 0
            return self.sendcommand()
        except:
            print("Command failed.")
            self.success_status = "SS_FAILURE"
            return self
