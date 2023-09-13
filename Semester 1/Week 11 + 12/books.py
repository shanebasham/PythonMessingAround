
maxchapters = 0
maxbook = ''
maxchaptersbom = 0
maxbookbom = ''

choice = input('Which volume of scripture would you like to learn more about? ')
with open(r'C:\Users\shane\OneDrive\Desktop\PythonMessingAround\Week 11 + 12\books_and_chapters.txt', 'r') as file:
    for line in file:
        parts = line.split(':')

        book = parts[0].strip()
        chapters = int(parts[1])
        scripture = parts[2].strip()
        # while choice != scripture:
        #     choice = input('Please enter another volume of scripture: ')
        #     break
        #print(f'Scripture: {scripture}, Book: {book}, Chapters: {chapters}')
        # if chapters > maxchapters:
        #     maxchapters = chapters 
        #     maxbook= book
        if scripture.lower() == choice.lower():
            print(f'Scripture: {scripture}, Book: {book}, Chapters: {chapters}')
            if chapters > maxchaptersbom:
                maxchaptersbom = chapters 
                maxbookbom = book 
#print(f'The book with the most chapters overall is {maxbook} with {maxchapters} chapters.')
print(f'The book with the most chapters in the Book of Mormon is {maxbookbom} with {maxchaptersbom} chapters.\n')
