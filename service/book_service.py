import os
import sys
sys.path.append(os.getcwd() + "\\")
from domain.entities import *
from domain.validators import *
from repository.book_repo import *
from repository.book_repo_validators import *

class BookService:
    '''
    GRASP Controller
    Responsabil de efectuarea operatiilor cerute de utilizator
    Coordoneaza operatiile necesare pentru a realiza actiunea declansata de utilizator
    '''
    def __init__(self,book_repo,book_validator,book_repo_validator):
        '''
        Initializeaza service
        book_repo: obiect de tip BookRepo, gestionam multimea de carti din biblioteca
        client_repo: obiect de tip ClientRepo, gestionam multimea de clienti ai bibliotecii
        validator: obiect de tip Validator, validarea datelor primite din consola
        '''
        self.__book_repo=book_repo
        self.__book_validator=book_validator
        self.__book_repo_validator=book_repo_validator
    #Add
    def add_book(self,id,titlu,descriere,autor):
        '''
        Adauga o carte noua in biblioteca
        id->string, id-ul cartii
        titlu->string, titlul cartii
        descriere->string, descrierea cartii
        autor->string, autorul cartii
        return->obiectul de tip Book creat
        raises: ValueEror daca cartea are date invalide
        '''
        book=Book(id,titlu,descriere,autor)
        self.__book_validator.validate_book(book)
        self.__book_repo.store(book)
        return book
    #Update
    def update_book(self,find_by,value,new_id,new_titlu,new_descriere,new_autor):
        '''
        Updateaza o carte din biblioteca dupa id, titlu sau autor
        find_by->string, id/titlu/autor
        value->string, id/titlu/autor in functie de find_by
        new_id->string, noul id al cartii (False => vechea valoare)
        new_titlu->string, noul titlu al cartii (False => vechea valoare)
        new_descriere->string, noua descriere a cartii (False => vechea valoare)
        new_autor->string, noul autor al cartii (False => vechea valoare)
        return->obiect de tipul Book, cartea modificata
        raise:ValueError daca sunt date gresite de intrare
        '''
        self.__book_repo_validator.validate_exist_book(find_by,value,self.__book_repo)
        book=self.__book_repo.update_book(find_by,value,new_id,new_titlu,new_descriere,new_autor)
        return book
    #Delete
    def delete_book(self,find_by,value):
        '''
        Sterge o carte a bibliotecii
        find_by->string, id/titlu/autor
        value->stirng, id/titlu/autorul cartii pe care vrem sa o stergem
        return->book, cartea stearsa
        raise:ValueError daca nu exista nici o carte cu specificatiile date
        '''
        self.__book_repo_validator.validate_exist_book(find_by,value,self.__book_repo)
        book=self.__book_repo.delete_book(find_by,value)
        return book
    #Import
    def import_books(self):
        '''
        Importeza date existente (pentru a lucra cu date mai multe)
        '''
        self.__book_repo.add_dummy_data()
    def get_all_books(self):
        '''
        O functie ce returneaza toate cartiile din biblioteca curenta
        return->obiect de tip-ul BookRepo, o lista cu toate cartiile din biblioteca
        '''
        return self.__book_repo
    def get_all_books_list(self):
        '''
        O functie ce returneaza toate cartiile din biblioteca sub forma de lista
        return->list, lista de obiecte de tipul Book
        '''
        return self.__book_repo.get_all_books()

#Teste

#Add
def test_add_book():
    repo=BookRepo()
    validator=BookValidator()
    repo_validator=BookRepoValidator()
    test_srv=BookService(repo,validator,repo_validator)
    #1
    id='13AD'
    titlu='Wolf Hall'
    descriere='Fictiune istorica'
    autor='Hilary Mantel'
    book=test_srv.add_book(id, titlu, descriere, autor)
    assert book.get_id()==id
    assert book.get_titlu()==titlu
    assert book.get_descriere()==descriere
    assert book.get_autor()==autor
    assert len(test_srv.get_all_books_list())==1
    #2
    id='1511'
    titlu='Gilead'
    descriere='Fictiune crestina'
    autor='Marilynne Robinson'
    book=test_srv.add_book(id, titlu, descriere, autor)
    assert book.get_id()==id
    assert book.get_titlu()==titlu
    assert book.get_descriere()==descriere
    assert book.get_autor()==autor
    assert len(test_srv.get_all_books_list())==2
    #3
    id='4124'
    titlu='Secondhand Time'
    descriere='Biografie'
    autor='Svetlana Alexievich'
    book=test_srv.add_book(id, titlu, descriere, autor)
    assert book.get_id()==id
    assert book.get_titlu()==titlu
    assert book.get_descriere()==descriere
    assert book.get_autor()==autor
    assert len(test_srv.get_all_books_list())==3
    #4
    id='3653'
    titlu='Austerlitz'
    descriere='Fictiune istorica'
    autor='WG Sebald'
    book=test_srv.add_book(id, titlu, descriere, autor)
    assert book.get_id()==id
    assert book.get_titlu()==titlu
    assert book.get_descriere()==descriere
    assert book.get_autor()==autor
    assert len(test_srv.get_all_books_list())==4
def test_add_book_errors():
    repo=BookRepo()
    validator=BookValidator()
    repo_validator=BookRepoValidator()
    test_srv=BookService(repo,validator,repo_validator)
    #1
    id='13AD'
    titlu='W'
    descriere='F'
    autor='H'
    try:
        book=test_srv.add_book(id, titlu, descriere, autor)
        assert False
    except ValueError as ve:
        assert str(ve)=='Titlul cartii trebuie sa aiba mai mult de 1 caracter!\nAutorul cartii trebuie sa aiba mai mult de 1 caracter!\nDescrierea cartii trebuie sa aiba mai mult de 1 caracter!'
        assert len(test_srv.get_all_books_list())==0
    #2
    id='13AD'
    titlu='Wolf Hall'
    descriere='F'
    autor='H'
    try:
        book=test_srv.add_book(id, titlu, descriere, autor)
        assert False
    except ValueError as ve:
        assert str(ve)=='Autorul cartii trebuie sa aiba mai mult de 1 caracter!\nDescrierea cartii trebuie sa aiba mai mult de 1 caracter!'
        assert len(test_srv.get_all_books_list())==0
    #3
    id='13AD'
    titlu='Wolf Hall'
    descriere='F'
    autor='Hilary Mantel'
    try:
        book=test_srv.add_book(id, titlu, descriere, autor)
        assert False
    except ValueError as ve:
        assert str(ve)=='Descrierea cartii trebuie sa aiba mai mult de 1 caracter!'
        assert len(test_srv.get_all_books_list())==0
    #4
    id='13AD'
    titlu='Wolf Hall'
    descriere='Fictiune Istorica'
    autor='H'
    try:
        book=test_srv.add_book(id, titlu, descriere, autor)
        assert False
    except ValueError as ve:
        assert str(ve)=='Autorul cartii trebuie sa aiba mai mult de 1 caracter!'
        assert len(test_srv.get_all_books_list())==0
    #5
    id='13AD'
    titlu='W'
    descriere='Fictiune Istorica'
    autor='Hilary Mantel'
    try:
        book=test_srv.add_book(id, titlu, descriere, autor)
        assert False
    except ValueError as ve:
        assert str(ve)=='Titlul cartii trebuie sa aiba mai mult de 1 caracter!'
        assert len(test_srv.get_all_books_list())==0
#Update
def test_update_book():
    repo=BookRepo(True)
    validator=BookValidator()
    repo_validator=BookRepoValidator()
    test_srv=BookService(repo,validator,repo_validator)
    #1
    find_by='id'
    value='12AB'
    new_id='12AB'
    new_titlu='Wolf Hall'
    new_descriere='new_descriere'
    new_autor='Hilary Mantel'
    book=test_srv.update_book(find_by,value,'','',new_descriere,'')
    assert book.get_id()==new_id
    assert book.get_titlu()==new_titlu
    assert book.get_descriere()==new_descriere
    assert book.get_autor()==new_autor
    #2
    find_by='titlu'
    value='Gilead'
    new_id='1102'
    new_titlu='new_titlu'
    new_descriere='Fictiune crestina'
    new_autor='Marilynne Robinson'
    book=test_srv.update_book(find_by,value,'',new_titlu,'','')
    assert book.get_id()==new_id
    assert book.get_titlu()==new_titlu
    assert book.get_descriere()==new_descriere
    assert book.get_autor()==new_autor
    #3
    find_by='autor'
    value='Svetlana Alexievich'
    new_id='new_id'
    new_titlu='new_titlu'
    new_descriere='new_descriere'
    new_autor='new_autor'
    book=test_srv.update_book(find_by,value,new_id,new_titlu,new_descriere,new_autor)
    assert book.get_id()==new_id
    assert book.get_titlu()==new_titlu
    assert book.get_descriere()==new_descriere
    assert book.get_autor()==new_autor
    #4
    find_by='id'
    value='90KL'
    new_id='90KL'
    new_titlu='Austerlitz'
    new_descriere='Fictiune istorica'
    new_autor='new_autor'
    book=test_srv.update_book(find_by,value,'','','',new_autor)
    assert book.get_id()==new_id
    assert book.get_titlu()==new_titlu
    assert book.get_descriere()==new_descriere
    assert book.get_autor()==new_autor
def test_update_book_errors():
    repo=BookRepo(True)
    validator=BookValidator()
    repo_validator=BookRepoValidator()
    test_srv=BookService(repo,validator,repo_validator)
    #1
    find_by='id'
    value='nu_exista'
    new_id='new_id'
    new_titlu='new_titlu'
    new_descriere='new_descriere'
    new_autor='new_autor'
    try:
        test_srv.update_book(find_by,value,new_id,new_titlu,new_descriere,new_autor)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici o carte cu acest id!'
    #2
    find_by='titlu'
    value='nu_exista'
    new_id='new_id'
    new_titlu='new_titlu'
    new_descriere='new_descriere'
    new_autor='new_autor'
    try:
        test_srv.update_book(find_by,value,new_id,new_titlu,new_descriere,new_autor)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici o carte cu acest titlu!'
    #3
    find_by='autor'
    value='nu_exista'
    new_id='new_id'
    new_titlu='new_titlu'
    new_descriere='new_descriere'
    new_autor='new_autor'
    try:
        test_srv.update_book(find_by,value,new_id,new_titlu,new_descriere,new_autor)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici o carte cu acest autor!'
#Delete
def test_delete_book():
    repo=BookRepo(True)
    validator=BookValidator()
    repo_validator=BookRepoValidator()
    test_srv=BookService(repo,validator,repo_validator)
    #1
    find_by='id'
    value='12AB'
    book=test_srv.delete_book(find_by,value)
    book_list=test_srv.get_all_books_list()
    assert len(book_list) == 10
    for el in book_list:
        assert el!=book
    #2
    find_by='titlu'
    value='Gilead'
    book=test_srv.delete_book(find_by,value)
    book_list=test_srv.get_all_books_list()
    assert len(book_list) == 9
    for el in book_list:
        assert el!=book
    #3
    find_by='autor'
    value='Svetlana Alexievich'
    book=test_srv.delete_book(find_by,value)
    book_list=test_srv.get_all_books_list()
    assert len(book_list) == 8
    for el in book_list:
        assert el!=book
    #4
    find_by='id'
    value='90KL'
    book=test_srv.delete_book(find_by,value)
    book_list=test_srv.get_all_books_list()
    assert len(book_list) == 7
    for el in book_list:
        assert el!=book
def test_delete_book_errors():
    repo=BookRepo(True)
    validator=BookValidator()
    repo_validator=BookRepoValidator()
    test_srv=BookService(repo,validator,repo_validator)
    #1
    find_by='id'
    value='nu exista'
    try:
        book=test_srv.delete_book(find_by,value)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici o carte cu acest id!'
        assert len(test_srv.get_all_books_list())==11
    #2
    find_by='titlu'
    value='nu exista'
    try:
        book=test_srv.delete_book(find_by,value)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici o carte cu acest titlu!'
        assert len(test_srv.get_all_books_list())==11
    #3
    find_by='autor'
    value='nu exista'
    try:
        book=test_srv.delete_book(find_by,value)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici o carte cu acest autor!'
        assert len(test_srv.get_all_books_list())==11

#Apelare
test_add_book()
test_add_book_errors()
test_update_book()
test_update_book_errors()
test_delete_book()
test_delete_book_errors()