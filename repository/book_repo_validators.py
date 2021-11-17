import os
import sys
sys.path.append(os.getcwd() + "\\")
from repository.book_repo import *

class BookRepoValidator:
    def validate_exist_book(self,find_by,value,books_repo):
        '''
        find_by->string, id/titlu/autor
        value->stirng, id/titlu/autorul cartii
        book_repo->BookRepo
        raise:ValueError, daca nu exista nici o carte cu acele propietati/ daca exista mai multe
        '''
        book=books_repo.find_book(find_by,value)
        if not book:
            raise ValueError('Nu exista nici o carte cu acest '+find_by+'!')

#Teste

def test_validate_exist_book():
    validator=BookRepoValidator()
    books_repo=BookRepo(True)
    #1
    find_by='id'
    value='nu exista'
    try:
        validator.validate_exist_book(find_by, value, books_repo)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici o carte cu acest id!'
    #2
    find_by='titlu'
    value='nu exista'
    try:
        validator.validate_exist_book(find_by, value, books_repo)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici o carte cu acest titlu!'
    #3
    find_by='autor'
    value='nu exista'
    try:
        validator.validate_exist_book(find_by, value, books_repo)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici o carte cu acest autor!'
    #4
    find_by='id'
    value='12AB'
    try:
        validator.validate_exist_book(find_by, value, books_repo)
        assert True
    except ValueError as ve:
        assert False

test_validate_exist_book()