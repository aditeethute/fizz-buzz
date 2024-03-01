#day5.4
#fizz buzz (job interview question)
# fizz buzz is actually a play game for small kids where the kids sits in circle and start counting 
#whenever the num is divisible by 3 the kid should say "fizz" and when the num is divisible by 5 they must"buzz" and if num is divisible by both then"fizz-buzz"
for number in range(1,101):
    if number%3==0 and number%5==0:
        print("FIZZ-BUZZ")
    elif number%3==0:
        print("FIZZ")
    elif number%5==0:
        print("BUZZ")
    else:
        print(number)
    