def weight_on_planets():
   # write your code here
   weight = input("What is your weight on Earth in pounds? ")
   weight = float(weight)
   print("\n"+"Your weight on Mars:", 0.38*weight, "\n"+"Your weight on Jupiter:", 2.34*weight)

if __name__ == '__main__':
   weight_on_planets()