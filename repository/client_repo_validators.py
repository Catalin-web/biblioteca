import os
import sys
sys.path.append(os.getcwd() + "\\")
from repository.client_repo import *
from domain.validators import *
from domain.entities import *

class ClientRepoValidator:
    def validate_exist_client(self,find_by,value,clients_repo):
        '''
        find_by->string, id/nume/cnp
        value->stirng/int, id/nume/cnp client
        book_repo->BookRepo
        raise:ValueError, daca nu exista nici un client cu acele propietati
        '''
        client=clients_repo.find_client(find_by,value)
        if not client:
            raise ValueError('Nu exista nici un client cu acest '+find_by+'!')

#Teste
def test_validate_exist_client():
    validator=ClientRepoValidator()
    clients_repo=ClientRepo(True)
    #1
    find_by='id'
    value='nu exista'
    try:
        validator.validate_exist_client(find_by, value, clients_repo)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici un client cu acest id!'
    #2
    find_by='nume'
    value='nu exista'
    try:
        validator.validate_exist_client(find_by, value, clients_repo)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici un client cu acest nume!'
    #3
    find_by='cnp'
    value=412341
    try:
        validator.validate_exist_client(find_by, value, clients_repo)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici un client cu acest cnp!'


test_validate_exist_client()