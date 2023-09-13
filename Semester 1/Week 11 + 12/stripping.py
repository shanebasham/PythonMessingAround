
bookstxt = 'C:\\Users\\shane\\OneDrive\\Desktop\\PythonMessingAround\\Week 11 + 12\\books.txt'
with open(bookstxt) as books:
    for line in books:
        book = line.strip()
        print(book)