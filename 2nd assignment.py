Age=int(input('Enter Your Age : '))

Gender= input("Choose Your Gender (M/F) : ")


if Age>=65:

   if Gender=='M':

       Capital=int(input("Enter Capital Amount : "))

       Time= int(input("Enter Time In Years : "))

       SimInt= Capital*0.07*Time

       print("Simple interest of the give Capital : ", Capital, "and Time in Years : ", Time, "is", SimInt)

   else:

       Capital=int(input("Enter Capital Amount : "))

       Time= int(input("Enter Time In Years : "))

       SimInt= Capital*0.08*Time

       print("Simple interest of the give Capital : ", Capital, "and Time in Years : ", Time, "is", SimInt)

else:

   if Gender=='M':

       Capital=int(input("Enter Capital Amount : "))

       Time= int(input("Enter Time In Years : "))

       SimInt= Capital*0.05*Time

       print("Simple interest of the give Capital : ", Capital, "and Time in Years : ", Time, "is", SimInt)

       else:

       Capital=int(input("Enter Capital Amount : "))

       Time= int(input("Enter Time In Years : "))

       SimInt= Capital*0.06*Time

       print("Simple interest of the give Capital : ", Capital, "and Time in Years : ", Time, "is", SimInt)