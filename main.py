# 📚 Step 1: Define an empty list to hold books
library = []
books = 3
# 🔁 Step 2: Use a for loop to get book entries from the user
# 💡 Use a tuple to represent an individual book in the list
print("Enter details for 3 books: ")
for x in range(3):
  print(f"Book {x+1}")
  title = input("Enter title: ").capitalize()
  author = input("Enter author: ").capitalize()
  year = int(input("Enter year: "))
  genre = input("Enter genre: ")
  ISBN = input("Enter ISBN: ")

  book = (title, author, year, genre, ISBN)
  library.append(book)
# 📄 Step 3: Print all books nicely
for book in library:
  print(f"Title of the book: {book[0]}")
  print(f"Author of the book: {book[1]}")
  print(f"Year of the book: {book[2]}")
  print(f"Genre of the book: {book[3]}")
  print(f"ISBN of the book: {book[-1]}")
# 🔍 Step 4: Search books by author
author_name = input("\nEnter the name of the author: ").capitalize()
print("Books by the author:", author_name)
found = False

for book in library:
  if book[1] == author_name:
    print(f"The title is:, {book[0]}, the year is: {book[2]}, the genre is {book[3]}, the ISBN is {book[4]}")
    found = True

if not found:
  print("No books were found by the author:", author_name)
# 🔎 Step 5: Filter books by year
found = False
year = input("\nSearch books before or after the books's year?: ").lower()

if year == "before":
  before = int(input("Enter the year before the book's year"))
  print(f"The books published before the year: {year}")
  for book in library:
    if book[2] > year:
      print(f"The title is:, {book[0]},the author is: {book[1]}, the year is: {book[2]}, the genre is {book[3]}, the ISBN is {book[4]}")
      found = True
  if not found:
    print("No book was found that was published before the given year:", year)

elif year == "after":
  after = int(input("Enter the year after the book's year"))
  print(f"The books published after the year: {year}")
  for book in library:
    if book[2] > year:
      print(f"The title is:, {book[0]},the author is: {book[1]}, the year is: {book[2]}, the genre is {book[3]}, the ISBN is {book[4]}")
      found = True

  if not found:
    print("No book was found that was published after the given year:", year)
    
else:
  print("Invalid Input", quit())

# Step 6: Search books by the ISBN
ISBN = input("\nEnter the ISBN: ")
print("Books with the ISBN", ISBN)
found = False

for book in library:
  if book[-1] == ISBN:
    print(f"The title is:, {book[0]},the author is: {book[1]}, the year is: {book[2]}, the genre is {book[3]}")
    found = True

if not found:
  print("No books were found with the ISBN", ISBN)
# 🧠 Step 7: Summary with stats
print("\nNumber of books in library:", books)
