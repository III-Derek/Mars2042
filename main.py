#import datetime

def main():
    while True:
        userInput = input() #capital letters only

        if userInput == 'NEW GAME':
            print("ENTER NAME OF NEW GAME:")
            newGameName=input()
            try:
                F=open(newGameName,"x")
            except:
                print("NAME ALREADY EXISTS")
            else:
                F=open(newGameName,"x")
            

        if userInput == 'END' :
            break
        else:
            print("NONSENSE");



if __name__ == "__main__":
    main()

        
