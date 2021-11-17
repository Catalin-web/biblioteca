import os
import sys
sys.path.append(os.getcwd() + "\\")
from domain.entities import *

#Generate

def generate_books():
    books=BookRepo()
    #0
    book=Book('12AB','Wolf Hall','Fictiune istorica','Hilary Mantel')
    books.store(book)
    #1
    book=Book('1102','Gilead','Fictiune crestina','Marilynne Robinson')
    books.store(book)
    #2
    book=Book('114C','Secondhand Time','Biografie','Svetlana Alexievich')
    books.store(book)
    #3
    book=Book('90KL','Austerlitz','Fictiune istorica','WG Sebald')
    books.store(book)
    #4
    book=Book('67HJ','Never Let Me Go','Stiintifico-fantastic','Kazuo Ishiguro')
    books.store(book)
    #5
    book=Book('ASDA','The Amber Spyglass','Fictiune Fantastica','Philip Pullman')
    books.store(book)
    #6
    book=Book('BVCX','Between the World and Me','Autobiografie','Ta-Nehisi Coates')
    books.store(book)
    #7
    book=Book('12WQ','Autumn','Fictiune Literara','Ali Smith')
    books.store(book)
    #8
    book=Book('TYUI','Cloud Atlas','Fantezie Stiintifica','David Mitchell')
    books.store(book)
    #9
    book=Book('1234','Half of a Yellow Sun','Fictiune Istorica','Chimamanda Ngozi Adichie')
    books.store(book)
    #10
    book=Book('5678','My Brilliant Friend','Fictiune','Elena Ferrante')
    books.store(book)
    return books.get_all_books()

#Class

class BookRepo:
    '''
    Clasa creata cu responsabilitatea de a gestiona
    multimea de carti
    '''
    def __init__(self,default=False):
        '''
        Initializarea multimii de carti din biblioteca
        '''
        if not default:
            self.__books=[]
        else:
            self.__books=generate_books()
    def store(self,book):
        '''
        Adaugarea unei carti in lista de carti
        book->Book, cartea pe care vrem sa o adaugam
        '''
        self.__books.append(book)
    def delete(self,value,poz=1):
        '''
        Determina stergerea tuturor cartiilor cu atributul value (id, titlu, sau autor)
        value->string, idul/titlul/autorul cartii pe care vrem sa o stergem
        poz->int, o valoare de la 0 la 2, care determina ce avem in value (id sau titlu sau autor)
        return->None
        '''
        if poz==0:
            self.__books=[el for el in self.__books if el.get_id()!=value]
        elif poz==1:
            self.__books=[el for el in self.__books if el.get_titlu()!=value]
        elif poz==2:
            self.__books=[el for el in self.__books if el.get_autor()!=value]
    def get_all_books(self):
        '''
        Returneaza o lista cu toate catiile din biblioteca
        return->list, lista cartiilor
        '''
        return [Book(book.get_id(),book.get_titlu(),book.get_descriere(),book.get_autor()) for book in self.__books]
    def add_dummy_data(self):
        '''
        Importeaza o biblioteca cu elemente
        '''
        self.__books=generate_books()
    def get_book(self,new_id,new_titlu,new_descriere,new_autor):
        '''
        Returneaza un obiect de tipul Book, cu acele caracteristici
        '''
        return Book(new_id,new_titlu,new_descriere,new_autor)
    #Find
    def find_book_by_id(self,id):
        '''
        Gaseste o carte dupa id-ul dat
        id->string, id-ul cartii date
        return->book, cartea data
        '''
        for el in self.__books:
            if el.get_id()==id:
                return el
    def find_book_by_titlu(self,titlu):
        '''
        Gaseste o carte dupa titlul ei
        titlu->string, titlul cartii date
        return->book, cartea ceruta
        '''
        for el in self.__books:
            if el.get_titlu()==titlu:
                return el
    def find_all_book_by_autor(self,autor):
        '''
        Gaseste cartiile cu autorul lor
        autor->string, autorul cartii date
        return->bookList, cartea ceruta
        '''
        bookList=[]
        for el in self.__books:
            if el.get_autor()==autor:
                bookList.append(el)
        return bookList
    def find_book(self,find_by,value):
        '''
        Gaseste o carte dupa toate criteriile
        find_by->string, id/titlu/autor
        value->string,valoare id/titlu/autor
        return->book, cartea cautata
        '''
        if find_by=='id':
            return self.find_book_by_id(value)
        elif find_by=='titlu':
            return self.find_book_by_titlu(value)
        elif find_by=='autor':
            if len(self.find_all_book_by_autor(value))>0:
                return self.find_all_book_by_autor(value)[0]
    
    def __str__(self):
        '''
        Suprascriem functia de printare
        return->string
        '''
        lst=[]
        for el in self.__books:
            lst.append(str(el))
        return '\n'.join(lst)
    #Update
    def update_book(self,find_by,value,new_id,new_titlu,new_descriere,new_autor):
        '''
        Updateaza o carte dupa orice criteriu de cautare
        find_by->string, id/titlu/autor
        value->string, id/titlu/autorul cartii cautate
        new_id->string, noul id al cartii
        new_titlu->string, noul titlu al cartii
        new_descriere->string, noua descriere a cartii
        new_autor->string, noul autor al cartii
        return->book, cartea actualizata
        '''
        book=self.find_book(find_by,value)
        if new_id!='':
            book.set_id(new_id)
        if new_titlu!='':
            book.set_titlu(new_titlu)
        if new_descriere!='':
            book.set_descriere(new_descriere)
        if new_autor!='':
            book.set_autor(new_autor)
        return book
    #delete
    def delete_book(self,find_by,value):
        '''
        Sterge o carte din lista de carti
        find_by->string, id/titlu/autor
        value->string, id/titlu/autorul cartii cautate
        return->book, cartea stearsa
        '''
        book=self.find_book(find_by,value)
        self.__books=[el for el in self.__books if el!=book]
        return book

#Teste

def test_store_books():
    books=BookRepo()
    #1
    book=Book('12AB','Wolf Hall','Fictiune istorica','Hilary Mantel')
    books.store(book)
    assert books.get_all_books()[0]==book
    #2
    book=Book('1102','Gilead','Fictiune crestina','Marilynne Robinson')
    books.store(book)
    assert books.get_all_books()[1]==book
    #3
    book=Book('114C','Secondhand Time','Biografie','Svetlana Alexievich')
    books.store(book)
    assert books.get_all_books()[2]==book
    #4
    book=Book('90OP','Never Let Me Go','Stiintifico-fantastic','Kazuo Ishiguro')
    books.store(book)
    assert books.get_all_books()[3]==book
    assert len(books.get_all_books())==4

def test_delete_books():
    books=BookRepo(True)
    #1
    titlu='Cloud Atlas'
    books.delete(titlu)
    assert len(books.get_all_books())==10
    for el in books.get_all_books():
        if el.get_titlu()==titlu:
            assert False
    #2
    titlu='Never Let Me Go'
    books.delete(titlu)
    assert len(books.get_all_books())==9
    for el in books.get_all_books():
        if el.get_titlu()==titlu:
            assert False
    #3
    titlu='Between the World and Me'
    books.delete(titlu)
    assert len(books.get_all_books())==8
    for el in books.get_all_books():
        if el.get_titlu()==titlu:
            assert False
    #4
    value='ASDA'
    poz=0
    books.delete(value,poz)
    assert len(books.get_all_books())==7
    for el in books.get_all_books():
        if el.get_id()==value:
            assert False
    #5
    value='Elena Ferrante'
    poz=2
    books.delete(value,poz)
    assert len(books.get_all_books())==6
    for el in books.get_all_books():
        if el.get_autor()==value:
            assert False
    #6
    value='nu_exista'
    poz=2
    books.delete(value,poz)
    assert len(books.get_all_books())==6
    for el in books.get_all_books():
        if el.get_autor()==value:
            assert False

#Find
def test_find_book_by_id():
    books=BookRepo(True)
    book_list=generate_books()
    #1
    id='12AB'
    book=books.find_book_by_id(id)
    assert book==book_list[0]
    #2
    id='1102'
    book=books.find_book_by_id(id)
    assert book==book_list[1]
    #3
    id='114C'
    book=books.find_book_by_id(id)
    assert book==book_list[2]
    #4
    id='90KL'
    book=books.find_book_by_id(id)
    assert book==book_list[3]
def test_find_book_by_titlu():
    books=BookRepo(True)
    book_list=generate_books()
    #1
    titlu='Wolf Hall'
    book=books.find_book_by_titlu(titlu)
    assert book==book_list[0]
    #2
    titlu='Gilead'
    book=books.find_book_by_titlu(titlu)
    assert book==book_list[1]
    #3
    titlu='Secondhand Time'
    book=books.find_book_by_titlu(titlu)
    assert book==book_list[2]
    #4
    titlu='Austerlitz'
    book=books.find_book_by_titlu(titlu)
    assert book==book_list[3]
def test_find_all_book_by_autor():
    books=BookRepo(True)
    book_list=generate_books()
    #1
    autor='Hilary Mantel'
    book=books.find_all_book_by_autor(autor)[0]
    assert book==book_list[0]
    #2
    autor='Marilynne Robinson'
    book=books.find_all_book_by_autor(autor)[0]
    assert book==book_list[1]
    #3
    autor='Svetlana Alexievich'
    book=books.find_all_book_by_autor(autor)[0]
    assert book==book_list[2]
    #4
    autor='WG Sebald'
    book=books.find_all_book_by_autor(autor)[0]
    assert book==book_list[3]
def test_find_book():
    books=BookRepo(True)
    book_list=generate_books()
    #1
    find_by='id'
    value='12AB'
    book=books.find_book(find_by,value)
    assert book==book_list[0]
    #2
    find_by='titlu'
    value='Wolf Hall'
    book=books.find_book(find_by,value)
    assert book==book_list[0]
    #3
    find_by='autor'
    value='Hilary Mantel'
    book=books.find_book(find_by,value)
    assert book==book_list[0]
#Update
def test_update_book():
    books=BookRepo(True)
    #1
    find_by='id'
    value='12AB'
    new_id='5121'
    new_titlu='Harry Potter'
    new_descriere=''
    new_autor=''
    book=books.update_book(find_by,value, new_id, new_titlu, new_descriere, new_autor)
    book_list=books.get_all_books()
    assert book==book_list[0]
    #2
    find_by='titlu'
    value='Gilead'
    new_id='new_id'
    new_titlu='new_titlu'
    new_descriere='new_descriere'
    new_autor=''
    book=books.update_book(find_by,value, new_id, new_titlu, new_descriere, new_autor)
    book_list=books.get_all_books()
    assert book==book_list[1]
    #3
    find_by='autor'
    value='Svetlana Alexievich'
    new_id='LOL'
    new_titlu=''
    new_descriere=''
    new_autor=''
    book=books.update_book(find_by,value, new_id, new_titlu, new_descriere, new_autor)
    book_list=books.get_all_books()
    assert book==book_list[2]
    #4
    find_by='id'
    value='90KL'
    new_id='new_id'
    new_titlu='new_titlu'
    new_descriere=''
    new_autor=''
    book=books.update_book(find_by,value, new_id, new_titlu, new_descriere, new_autor)
    book_list=books.get_all_books()
    assert book==book_list[3]
#Delete
def test_delete_book():
    books=BookRepo(True)
    #1
    find_by='id'
    value='12AB'
    book=books.delete_book(find_by, value)
    book_list=books.get_all_books()
    assert len(book_list)==10
    for el in book_list:
        assert el!=book
    #2
    find_by='titlu'
    value='Gilead'
    book=books.delete_book(find_by, value)
    book_list=books.get_all_books()
    assert len(book_list)==9
    for el in book_list:
        assert el!=book
    #3
    find_by='autor'
    value='Svetlana Alexievich'
    book=books.delete_book(find_by, value)
    book_list=books.get_all_books()
    assert len(book_list)==8
    for el in book_list:
        assert el!=book
    #4
    find_by='id'
    value='90KL'
    book=books.delete_book(find_by, value)
    book_list=books.get_all_books()
    assert len(book_list)==7
    for el in book_list:
        assert el!=book

#Apelare
test_store_books()
test_delete_books()
test_find_book_by_id()
test_find_book_by_titlu()
test_find_all_book_by_autor()
test_find_book()
test_update_book()
test_delete_book()