from errpy import errsela

def main():

    try:
        client = errsela()
        client.winkl().winkr().turnleft().turnright().turnaroundl().turnaroundr().talk("I'm receiving commands from a Python API!").print_success_status()

        client.getdefaults()

    except AttributeError as e:
        print("\nAn attribute error likely means that sendcommand encountered an exception.")
        yesorno = input("\nWould you like to seen the error output?\n").lower()()
        if(yesorno == 'yes'):
            print(e)
        else:
            print("Try debugging your code.")

    except Exception as e:
        client.getdefaults()
        print("AN ERROR OCCURED. DEFAULTS SUCCESSFULLY RESET...")
        print(e)

if __name__ == "__main__":
    main()