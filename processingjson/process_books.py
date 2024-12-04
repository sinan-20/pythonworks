from json import load

f=open("C:\\Users\\ACER\\Desktop\\pythonworks\\datasets\\books.json")

data=load(f)

# for book in data:

#     print(book)


# print all titles
all_titles=[book.get("title")for book in data]

# print(all_titles)

# books with pages<250

pages_filter=[book.get("title")for book in data if book.get("pages")<250]

# print(pages_filter)

# print all genres

all_generes=[book.get("genre") for book in data]
# print(set(all_generes))

gener_count={genre:all_generes.count(genre)for genre in all_generes}

# print(gener_count)

# costly book

costly_book=max(data,key=lambda d:d.get("price"))
# print(costly_book)

# author with more than one book

all_authors=[book.get("author")for book in data]
# print(all_authors)

auther_count={author:all_authors.count(author)for author in all_authors if all_authors.count(author)>1 }

# print([k for k,v in auther_count.items() if v>1])

print(auther_count)
