class Library:
   def __init__(self, book_list, lib_name):
      self.book_list = book_list
      self.lent_list = {}
      self.lib_name = lib_name

   def show_list(self):
      print(self.book_list)

   def show_lent(self):
      print(self.lent_list)


   def lend(self):
      print(f"Available books :")
      self.show_list()
      lent_book = input("Which one do you want to borrow : ")

      if lent_book in self.book_list:
         self.book_list.remove(lent_book)

         name = input("Please enter your name : ")
         self.lent_list[lent_book] = name

         print("\n*************************************************************")
         print("Thank You for lending.. please return the book within a week.")
         print("*************************************************************")

      else :
         print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
         print("Sorry we don't have such book")
         print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


   def retn(self):
      ret_book = input("Which book are you returning : ")

      if ret_book in self.lent_list:
         del self.lent_list[ret_book]
         self.book_list.append(ret_book)

         print("\n*************************")
         print("Thank You for returning..")
         print("*************************")

      else:
         print("\n!!!!!!!!!!!!!!!!!!!!!!!!!")
         print("Please enter a valid book ")
         print("!!!!!!!!!!!!!!!!!!!!!!!!!")

   def donate(self):
      new_book = input("Which book you want to donate : ")
      self.book_list.append(new_book)

      print("\n**********************************")
      print("Thank You for your kind donation..")
      print("**********************************")


listofbooks = ["a", "b", "c", "d", "e", "f"]
library_name = "Harry"
HarryLibrary = Library(listofbooks, library_name)

while True:
   action = input("Enter : \n s to view list of available books \n l to view list of lent books and their lenders \n b "
                  "to borrow a book \n r to return a book \n d to donate a book \n --------------- \n Enter here :")
   if action == "s":
      HarryLibrary.show_list()
   elif action == "l":
      HarryLibrary.show_lent()
   elif action == "b":
      HarryLibrary.lend()

   elif action == "r":
      HarryLibrary.retn()

   elif action == "d":
      HarryLibrary.donate()

   else :
      print("Please enter a correct input.")

   print("\n------------------------------------------------------------------------------------------------------\n\n")

   input('Press enter to take further action ::::\n')