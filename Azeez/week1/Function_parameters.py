test_height=int(input("Height of wall: "))
test_width=int(input("Width of wall: "))
coverage=5

def paint_calc(test_height,test_width,coverage):
    area=test_height*test_width
    Number_of_cans=round(area/coverage)
    print(f"You will need {Number_of_cans} of cans")

print_calc()


n = int(input("Check this number: "))
if n / 1 == 1 or n / n == 1:
print(f"{n} is a prime number")
 
prime_checker(number=n)
