import os


def read_bible(base_path):
    chapters = {}
    verses = {}

    # book names
    for book_name in os.listdir(base_path):
        book_path = os.path.join(base_path, book_name)
        if os.path.isdir(book_path):
            for chapter_file in os.listdir(book_path):
                chapter_number = os.path.splitext(chapter_file)[0]  # Remove the .txt extension
                chapter_path = os.path.join(book_path, chapter_file)
                chapter_key = "bible" + "/" + book_name + "/" + chapter_number

                # chapter numbers
                with open(chapter_path, 'r', encoding='utf-8') as chaper_file:
                    # verse numbers
                    chapter_content = []
                    for line in chaper_file:
                        line = line.strip()
                        if line:
                            verse_number, verse_content = line.split('.', 1)
                            verse_number = verse_number.strip()
                            verse_content = verse_content.strip()
                            verse_path = "bible" + "/" + book_name + "/" + chapter_number + "/" + verse_number
                            
                            # get the content
                            verses[verse_path] = verse_content
                            
                            #print(verse_content)
                            chapter_content.append(verse_content)
                
                # print(chapter_content)
                chapters[chapter_key] = chapter_content
                        
    return chapters, verses




base_path = 'bible'
bible_verses = read_bible(base_path)[1]
bible_chapter = read_bible(base_path)[0]


# print(bible_chapter['ዘፍጥረት/1'])
# print(bible_verse['ዘፍጥረት/1/1']) 