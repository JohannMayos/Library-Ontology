from owlready2 import *

onto = get_ontology("http://www.example.org/library.owl")

class Person(Thing):
    namespace = onto

class Author(Thing):
    namespace = onto

class Work(Thing):
    namespace = onto

class Book(Thing):
    namespace = onto

class Category(Thing):
    namespace = onto

class WrittenBy(Property):
    namespace = onto
    domain = [Book]
    range = [Author]

class BookCategory(Property):
    namespace = onto
    domain = [Book]
    range = [Category]


author1 = Author("H.P Lovecraft")
author2 = Author("J.R.R Tolkien")

book1 = Book("The Lord of The Rings")
book2 = Book("The Call of Cthulhu")

category1 = Category("Fantasy")
category2 = Category("Eldritch Horror")

book1.WrittenBy.append(author1)
book2.WrittenBy.append(author2)

book1.BookCategory.append(category1)
book2.BookCategory.append(category2)

onto.save("Library_Hierarchy.owl")

for book in onto.Book.instances():
    print(f"Livro: {book.name}, Autor(es): {[autor.name for autor in book.WrittenBy]}")

# Exemplo de consulta: Listar todas as categorias
print("\nCategorias:")
for category in onto.Category.instances():
    print(category.name)
