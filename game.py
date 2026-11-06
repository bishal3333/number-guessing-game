def main():

        print("Welcome to Number guessing game.\nGuess a number betn 1 and 100")
        count=0
        guess1=guess()
        while True:
            try:
                  user_guess=int(input("Enter number: "))
                  if user_guess>100 or user_guess<1:
                        raise ValueError
            except ValueError:
                  print("Enter a valid number")
            else:


                 if user_guess==guess1:
                      count+=1
                      print(f"Congratulation you guessed the number.\n You have guessed the number in {count} attempt ")
                      break
                 elif user_guess > guess1:
                      print("Too high")
                      count+=1
                 else:
                      print("Too low")
                      count+=1



def guess():
    import random
    guess=random.randint(1,100)

    return guess

main()




