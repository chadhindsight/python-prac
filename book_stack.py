# Using a list to represent a stack of books
stack_of_books = ["The Catcher in the Rye", "1984", "To Kill a Mockingbird"]

# Push items onto the stack
stack_of_books.append("To Kill a Mockingbird")
stack_of_books.append("Of Mice and Men")

print("Here are the books listed in our stack:", stack_of_books)
# Pop items from the stack (LIFO order) 
# print(stack_of_books.pop())
print("The following book was removed from our stack:", stack_of_books.pop()) 
 
# "Of Mice and Men"
# "To Kill a Mockingbird"
# "1984"
# "The Catcher in the Rye"