books = ['Rich Dad Poor Dad', 'How to heal yourself', 'Bhagwat Gita', 'Atomic Habits', 'RE WORK', 'Fear Not Be Strong']
name = input("Enter the book you want = ").upper()

if name in books:
    print(f"Book,{name} is available")
    remove = books.remove(name)
    books.sort()
    print(books)
    

else:
    print(f"Book,{name} not found.")