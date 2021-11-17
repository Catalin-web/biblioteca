import os
import sys
sys.path.append(os.getcwd() + "\\")
from domain.entities import *

class BookValidator:
    def validate_book(self,book):
        errors=[]
        if book.get_titlu()!=False and len(book.get_titlu())<2:
            errors.append('Titlul cartii trebuie sa aiba mai mult de 1 caracter!')
        if book.get_autor()!=False and len(book.get_autor())<2:
            errors.append('Autorul cartii trebuie sa aiba mai mult de 1 caracter!')
        if book.get_descriere()!=False and len(book.get_descriere())<2:
            errors.append('Descrierea cartii trebuie sa aiba mai mult de 1 caracter!')
        if  len(errors)>0:
            errors_string='\n'.join(errors)
            raise ValueError(errors_string)

class ClientValidator:
    def validate_client(self,client):
        errors=[]
        if client.get_nume()!=False and len(client.get_nume())<2:
            errors.append('Numele clientului trebuie sa aiba mai mult de 1 caracter!')
        if client.get_cnp()!=False and str(type(client.get_cnp()))!="<class 'int'>":
            errors.append('Cnp-ul trebuie sa fie un numar!')
        if len(errors)>0:
            errors_string='\n'.join(errors)
            raise ValueError(errors_string)

#Teste

def test_validate_book():
    show_validator=BookValidator()
    #1
    book=Book('12AB','Wolf Hall','Fictiune istorica','Hilary Mantel')
    try:
        show_validator.validate_book(book)
        assert True
    except ValueError:
        assert False
    #2
    book=Book('12AB','W','Fictiune istorica','Hilary Mantel')
    try:
        show_validator.validate_book(book)
        assert False
    except ValueError as ve:
        assert (str(ve)=='Titlul cartii trebuie sa aiba mai mult de 1 caracter!')
    #3
    book=Book('12AB','W','F','Hilary Mantel')
    try:
        show_validator.validate_book(book)
        assert False
    except ValueError as ve:
        assert str(ve)=='Titlul cartii trebuie sa aiba mai mult de 1 caracter!\nDescrierea cartii trebuie sa aiba mai mult de 1 caracter!'
    #4
    book=Book('12AB','W','F','H')
    try:
        show_validator.validate_book(book)
        assert False
    except ValueError as ve:
        assert str(ve)=='Titlul cartii trebuie sa aiba mai mult de 1 caracter!\nAutorul cartii trebuie sa aiba mai mult de 1 caracter!\nDescrierea cartii trebuie sa aiba mai mult de 1 caracter!'

def test_validate_client():
    show_validator=ClientValidator()
    #1
    client=Client('ABCD','Bugnar Catalin',5021213322296)
    try:
        show_validator.validate_client(client)
        assert True
    except ValueError:
        assert False
    #2
    client=Client('ABCD','B',5021213322296)
    try:
        show_validator.validate_client(client)
        assert False
    except ValueError as ve:
        assert str(ve)=='Numele clientului trebuie sa aiba mai mult de 1 caracter!'
    #3
    client=Client('ABCD','B','5021213322296')
    try:
        show_validator.validate_client(client)
        assert False
    except ValueError as ve:
        assert str(ve)=='Numele clientului trebuie sa aiba mai mult de 1 caracter!\nCnp-ul trebuie sa fie un numar!'


test_validate_book()
test_validate_client()