import os
import sys
sys.path.append(os.getcwd() + "\\")
from domain.entities import *
from domain.validators import *
from repository.client_repo import *
from repository.client_repo_validators import *

class ClientService:
    '''
    GRASP Controller
    Responsabil de efectuarea operatiilor cerute de utilizator
    Coordoneaza operatiile necesare pentru a realiza actiunea declansata de utilizator
    '''
    def __init__(self,client_repo,client_validator,client_repo_validator):
        '''
        Initializeaza service
        book_repo: obiect de tip BookRepo, gestionam multimea de carti din biblioteca
        client_repo: obiect de tip ClientRepo, gestionam multimea de clienti ai bibliotecii
        validator: obiect de tip Validator, validarea datelor primite din consola
        '''
        self.__client_repo=client_repo
        self.__client_validator=client_validator
        self.__client_repo_validator=client_repo_validator
    def import_clients(self):
        '''
        Importeza date existente (pentru a lucra cu date mai multe)
        '''
        self.__client_repo.add_dummy_data()
    #Add
    def add_client(self,id,nume,cnp):
        '''
        Adauga o un client in lista de clienti
        id->string, id-ul clientului
        nume->string, numele clientului
        cnp->int, cnp-ul clientului
        return->obiectul de tip Client creat
        raises: ValueEror daca clientul are date invalide
        '''
        client=Client(id,nume,cnp)
        self.__client_validator.validate_client(client)
        self.__client_repo.store(client)
        return client
    #Update
    def update_client(self,find_by,value,new_id,new_nume,new_cnp):
        '''
        Updateaza un client al bibliotecii
        find_by->string, id/nume/cnp
        value->string/cnp, id/nume/cnpul clientului
        new_id->string, noul id modificat
        new_nume->string, noul nume modificat
        new_cnp->string, noul cnp modificat
        return->obiect de tipul Client, noul client adaugat
        raise:ValueError daca datele de intrare sunt gresite
        '''
        self.__client_repo_validator.validate_exist_client(find_by,value,self.__client_repo)
        client=self.__client_repo.update_client(find_by,value,new_id,new_nume,new_cnp)
        return client
    #Delete
    def delete_client(self,find_by,value):
        '''
        Sterge un client al bibliotecii
        find_by->string, id/nume/cnp
        value->string/int, id/nume/cnp clientului in functie de find_by
        return->clientul sters
        raise:ValueError, daca nu gaseste nici un client cu datele respective
        '''
        self.__client_repo_validator.validate_exist_client(find_by,value,self.__client_repo)
        client=self.__client_repo.delete_client(find_by, value)
        return client
    def get_all_clients(self):
        '''
        O functie ce returneaza toti clientii bibliotecii
        return->obiect de tip-ul ClientRepo
        '''
        return self.__client_repo
    def get_all_clients_list(self):
        '''
        O functie ce returneaza toti clientii bibliotecii sub forma de lista
        return->list, lista de obiecte de tipul Client
        '''
        return self.__client_repo.get_all_clients()

#Teste

def test_add_client():
    repo=ClientRepo()
    validator=ClientValidator()
    repo_validator=ClientRepoValidator()
    test_srv=ClientService(repo,validator,repo_validator)
    #1
    id='3114'
    nume='Bugnar Catalin'
    cnp=5030727120535
    client=test_srv.add_client(id, nume, cnp)
    assert client.get_id()==id
    assert client.get_nume()==nume
    assert client.get_cnp()==cnp
    assert len(test_srv.get_all_clients_list())==1
    #2
    id='6134'
    nume='Bugnar Andreea'
    cnp=2870920253242
    client=test_srv.add_client(id, nume, cnp)
    assert client.get_id()==id
    assert client.get_nume()==nume
    assert client.get_cnp()==cnp
    assert len(test_srv.get_all_clients_list())==2
    #3
    id='5121'
    nume='Bugnar Diana'
    cnp=6020308238663
    client=test_srv.add_client(id, nume, cnp)
    assert client.get_id()==id
    assert client.get_nume()==nume
    assert client.get_cnp()==cnp
    assert len(test_srv.get_all_clients_list())==3
    #4
    id='2141'
    nume='Todoran Liana'
    cnp=2860830398046
    client=test_srv.add_client(id, nume, cnp)
    assert client.get_id()==id
    assert client.get_nume()==nume
    assert client.get_cnp()==cnp
    assert len(test_srv.get_all_clients_list())==4

def test_add_client_errors():
    repo=ClientRepo()
    validator=ClientValidator()
    repo_validator=ClientRepoValidator()
    test_srv=ClientService(repo,validator,repo_validator)
    #1
    id='3114'
    nume='B'
    cnp=5030727120535
    try:
        client=test_srv.add_client(id, nume, cnp)
        assert False
    except ValueError as ve:
        assert str(ve)=='Numele clientului trebuie sa aiba mai mult de 1 caracter!'
        assert len(test_srv.get_all_clients_list())==0
    #2
    id='3114'
    nume='B'
    cnp='5030727120535'
    try:
        client=test_srv.add_client(id, nume, cnp)
        assert False
    except ValueError as ve:
        assert str(ve)=='Numele clientului trebuie sa aiba mai mult de 1 caracter!\nCnp-ul trebuie sa fie un numar!'
        assert len(test_srv.get_all_clients_list())==0
    #3
    id='3114'
    nume='Bugnar Catalin'
    cnp='5030727120535'
    try:
        client=test_srv.add_client(id, nume, cnp)
        assert False
    except ValueError as ve:
        assert str(ve)=='Cnp-ul trebuie sa fie un numar!'
        assert len(test_srv.get_all_clients_list())==0

#Update
def test_update_client():
    repo=ClientRepo(True)
    validator=ClientValidator()
    repo_validator=ClientRepoValidator()
    test_srv=ClientService(repo,validator,repo_validator)
    #1
    find_by='id'
    value='13JK'
    new_id='13JK'
    new_nume='new_nume'
    new_cnp=5030727120535
    client=test_srv.update_client(find_by,value,'',new_nume,'')
    assert client.get_id()==new_id
    assert client.get_nume()==new_nume
    assert client.get_cnp()==new_cnp
    #2
    find_by='nume'
    value='Bugnar Andreea'
    new_id='new_id'
    new_nume='Bugnar Andreea'
    new_cnp=2870920253242
    client=test_srv.update_client(find_by,value,new_id,'','')
    assert client.get_id()==new_id
    assert client.get_nume()==new_nume
    assert client.get_cnp()==new_cnp
    #3
    find_by='cnp'
    value=6020308238663
    new_id='new_id'
    new_nume='new_nume'
    new_cnp=1111
    client=test_srv.update_client(find_by,value,new_id,new_nume,new_cnp)
    assert client.get_id()==new_id
    assert client.get_nume()==new_nume
    assert client.get_cnp()==new_cnp
    #4
    find_by='id'
    value='JKLS'
    new_id='JKLS'
    new_nume='Todoran Liana'
    new_cnp=2860830398046
    client=test_srv.update_client(find_by,value,new_id,new_nume,new_cnp)
    assert client.get_id()==new_id
    assert client.get_nume()==new_nume
    assert client.get_cnp()==new_cnp
def test_update_client_errors():
    repo=ClientRepo(True)
    validator=ClientValidator()
    repo_validator=ClientRepoValidator()
    test_srv=ClientService(repo,validator,repo_validator)
    #1
    find_by='id'
    value='nu exista'
    new_id='new_id'
    new_nume='new_nume'
    new_cnp=124312
    try:
        client=test_srv.update_client(find_by,value,new_id,new_nume,new_cnp)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici un client cu acest id!'
        assert len(test_srv.get_all_clients_list())==11
    #2
    find_by='nume'
    value='nu exista'
    new_id='new_id'
    new_nume='new_nume'
    new_cnp=124312
    try:
        client=test_srv.update_client(find_by,value,new_id,new_nume,new_cnp)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici un client cu acest nume!'
        assert len(test_srv.get_all_clients_list())==11
    #3
    find_by='cnp'
    value=51231
    new_id='new_id'
    new_nume='new_nume'
    new_cnp=124312
    try:
        client=test_srv.update_client(find_by,value,new_id,new_nume,new_cnp)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici un client cu acest cnp!'
        assert len(test_srv.get_all_clients_list())==11
#Delete
def test_delete_client():
    repo=ClientRepo(True)
    validator=ClientValidator()
    repo_validator=ClientRepoValidator()
    test_srv=ClientService(repo,validator,repo_validator)
    #1
    find_by='id'
    value='13JK'
    client=test_srv.delete_client(find_by,value)
    client_list=test_srv.get_all_clients_list()
    assert len(client_list)==10
    for el in client_list:
        assert el!=client
    #2
    find_by='nume'
    value='Bugnar Andreea'
    client=test_srv.delete_client(find_by,value)
    client_list=test_srv.get_all_clients_list()
    assert len(client_list)==9
    for el in client_list:
        assert el!=client
    #3
    find_by='cnp'
    value=6020308238663
    client=test_srv.delete_client(find_by,value)
    client_list=test_srv.get_all_clients_list()
    assert len(client_list)==8
    for el in client_list:
        assert el!=client
def test_delete_client_errors():
    repo=ClientRepo(True)
    validator=ClientValidator()
    repo_validator=ClientRepoValidator()
    test_srv=ClientService(repo,validator,repo_validator)
    #1
    find_by='id'
    value='nu exista'
    try:
        client=test_srv.delete_client(find_by,value)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici un client cu acest id!'
        assert len(test_srv.get_all_clients_list())==11
    #2
    find_by='nume'
    value='nu exista'
    try:
        client=test_srv.delete_client(find_by,value)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici un client cu acest nume!'
        assert len(test_srv.get_all_clients_list())==11
    #3
    find_by='cnp'
    value=31231
    try:
        client=test_srv.delete_client(find_by,value)
        assert False
    except ValueError as ve:
        assert str(ve)=='Nu exista nici un client cu acest cnp!'
        assert len(test_srv.get_all_clients_list())==11

#Apelare
test_add_client_errors()
test_add_client()
test_update_client()
test_update_client_errors()
test_delete_client()
test_delete_client_errors()