import os
import sys
sys.path.append(os.getcwd() + "\\")
from domain.entities import *

#Generate

def generate_clients():
    clients=ClientRepo()
    #0
    client=Client('13JK','Bugnar Catalin',5030727120535)
    clients.store(client)
    #1
    client=Client('89JS','Bugnar Andreea',2870920253242)
    clients.store(client)
    #2
    client=Client('Y123','Bugnar Diana',6020308238663)
    clients.store(client)
    #3
    client=Client('JKLS','Todoran Liana',2860830398046)
    clients.store(client)
    #4
    client=Client('1234','Nicula Cristian',1930803469296)
    clients.store(client)
    #5
    client=Client('5678','Maierean Mircea',1870601027651)
    clients.store(client)
    #6
    client=Client('9101','Borodi Sara',2930421275783)
    clients.store(client)
    #7
    client=Client('1121','Precup Alina',6001221180225)
    clients.store(client)
    #8
    client=Client('3141','Runcan Roxana',2870803403628)
    clients.store(client)
    #9
    client=Client('6171','Kerekes Karina',2991015093583)
    clients.store(client)
    #10
    client=Client('8192','Nicula Nelia',2900614015217)
    clients.store(client)
    return clients.get_all_clients()

#Class

class ClientRepo:
    '''
    Clasa creata cu responsabilitatea de a gestiona
    multimea de clienti
    '''
    def __init__(self,default=False):
        '''
        Initializarea multimii de clienti ai bibliotecii
        '''
        if not default:
            self.__clients=[]
        else:
            self.__clients=generate_clients()
    def store(self,client):
        '''
        Adaugarea unui nou client in lista de clienti
        client->Client, clientul pe care vrem sa il adaugam
        '''
        self.__clients.append(client)
    def delete(self,value,poz=1):
        '''
        Determina stergerea clientulor dupa id/nume/cnp
        value->string/int, idul sau numele sau cnp-ul clientului pe care vrem sa il stergem
        poz->int, o valoare intre 0 si 2 care determina dupa ce exact stergem clientul
        return->None
        '''
        if poz==0:
            self.__clients=[el for el in self.__clients if el.get_id()!=value]
        elif poz==1:
            self.__clients=[el for el in self.__clients if el.get_nume()!=value]
        elif poz==2:
            self.__clients=[el for el in self.__clients if el.get_cnp()!=value]
    def update(self,value,poz,new_id,new_nume,new_cnp):
        '''
        Determina updatarea unui client dupa id/nume/cnp
        value->string/int, valoarea dupa care modificam un client
        new_id->string/False, noul id al clientului
        new_nume->string/False, noul nume al clientului
        new_cnp->int/False, noul cnp al clientului
        return->clientul nou adaugat
        '''
        for el in self.__clients:
            if (poz==0 and el.get_id()==value) or (poz==1 and el.get_nume()==value) or (poz==2 and el.get_cnp()==value):
                if new_id:
                    el.set_id(new_id)
                else: new_id=el.get_id()
                if new_nume:
                    el.set_nume(new_nume)
                else: new_nume=el.get_nume()
                if new_cnp:
                    el.set_cnp(new_cnp)
                else: new_cnp=el.get_cnp()
        return Client(new_id,new_nume,new_cnp)
    def get_client(self,new_id,new_nume,new_cnp):
        '''
        Returneaza un obiect de tipul Client, cu acele caracteristici
        '''
        return Client(new_id,new_nume,new_cnp)
    def get_all_clients(self):
        '''
        Returneaza o lista cu toti clientii bibliotecii
        return->list, lista cartiilor
        '''
        return [Client(el.get_id(),el.get_nume(),el.get_cnp()) for el in self.__clients]
    def add_dummy_data(self):
        '''
        Importeaza clienti
        '''
        self.__clients=generate_clients()
    #Find
    def find_client_by_id(self,id):
        '''
        Gaseste un client cu un id anume
        id->string, id-ul clientului pe care vrem sa il cautam
        return->client, clientul cautat
        '''
        for el in self.__clients:
            if el.get_id()==id:
                return el
    def find_client_by_nume(self,nume):
        '''
        Gaseste un client dupa numele lui
        nume->string, numele clientului cautat
        return->client, clientul cautat
        '''
        for el in self.__clients:
            if el.get_nume()==nume:
                return el
    def find_client_by_cnp(self,cnp):
        '''
        Gaseste un client dupa cnpul lui
        cnp->string, cnpul clientului cautat
        return->client, clientul cautat
        '''
        for el in self.__clients:
            if el.get_cnp()==cnp:
                return el
    def find_client(self,find_by,value):
        '''
        Gaseste un client dupa orice termen de cautare
        find_by->string, id/nume/cnp
        value->string/int, id/nume/cnpul clientului cautat
        '''
        if find_by=='id':
            return self.find_client_by_id(value)
        elif find_by=='nume':
            return self.find_client_by_nume(value)
        elif find_by=='cnp':
            return self.find_client_by_cnp(value)
    #Update
    def update_client(self,find_by,value,new_id,new_nume,new_cnp):
        '''
        Actualizeaza un client dupa orice metoda de cautare
        find_by->string, id/nume/cnp
        value->string, id/nume/cnp-ul clientului cautat
        new_id->string, noul id
        new_nume->string, noul nume
        new_cnp->string, noul cnp
        return->client, clientul updatat
        '''
        client=self.find_client(find_by,value)
        if new_id!='':client.set_id(new_id)
        if new_nume!='':client.set_nume(new_nume)
        if new_cnp!='':client.set_cnp(new_cnp)
        return client
    #Delete
    def delete_client(self,find_by,value):
        '''
        Sterge un client al bibliotecii cu orice mijloc de gasire
        find_by->string, id/nume/cnp
        value->string/int, id/nume/cnpul clientului
        return->client, clientul sters din lista
        '''
        client=self.find_client(find_by,value)
        self.__clients=[el for el in self.__clients if el!=client]
        return client
    def __str__(self):
        '''
        Suprascriere functia pentru print
        return->string
        '''
        lst=[]
        for el in self.__clients:
            lst.append(str(el))
        return '\n'.join(lst)

#Teste

def test_store_clients():
    clients=ClientRepo()
    #1
    client=Client('ABCD','Bugnar Catalin',5021213322296)
    clients.store(client)
    assert clients.get_all_clients()[0]==client
    #2
    client=Client('BC27','Borodi Sara',2950411464768)
    clients.store(client)
    assert clients.get_all_clients()[1]==client
    #3
    client=Client('90OP','Todoran Liana',2861122087866)
    clients.store(client)
    assert clients.get_all_clients()[2]==client
    #4
    client=Client('6782','Nicula Cristian',1920224143530)
    clients.store(client)
    assert clients.get_all_clients()[3]==client
    assert len(clients.get_all_clients())==4

def test_delete_clients():
    clients=ClientRepo(True)
    #1
    value='13JK'
    poz=0
    clients.delete(value,poz)
    assert len(clients.get_all_clients())==10
    for el in clients.get_all_clients():
        if el.get_id()==value:
            assert False
    #2
    value='Bugnar Diana'
    poz=1
    clients.delete(value,poz)
    assert len(clients.get_all_clients())==9
    for el in clients.get_all_clients():
        if el.get_nume()==value:
            assert False
    #3
    value=2870803403628
    poz=2
    clients.delete(value,poz)
    assert len(clients.get_all_clients())==8
    for el in clients.get_all_clients():
        if el.get_cnp()==value:
            assert False
    #4
    value='Nicula Nelia'
    clients.delete(value)
    assert len(clients.get_all_clients())==7
    for el in clients.get_all_clients():
        if el.get_nume()==value:
            assert False
            #4
    value='nu_exista'
    poz=0
    clients.delete(value,poz)
    assert len(clients.get_all_clients())==7
    for el in clients.get_all_clients():
        if el.get_id()==value:
            assert False

def test_update_clients():
    clients=ClientRepo(True)
    #1
    value='13JK'
    poz=0
    new_id='13JK'
    new_nume='test_nume'
    new_cnp=5030727120535
    client=Client(new_id,new_nume,new_cnp)
    clients.update(value,poz,False,new_nume,False)
    assert client==clients.get_all_clients()[0]
    #2
    value='Bugnar Andreea'
    poz=1
    new_id='test_id'
    new_nume='test_nume'
    new_cnp=1111111111111
    client=Client(new_id,new_nume,new_cnp)
    clients.update(value,poz,new_id,new_nume,new_cnp)
    assert client==clients.get_all_clients()[1]
    #3
    value=6020308238663
    poz=3
    new_id='90JS'
    new_nume='Bugnar Diana'
    new_cnp=6020308238663
    client=Client(new_id,new_nume,new_cnp)
    clients.update(value,poz,new_id,False,False)
    assert client==clients.get_all_clients()[2]
    #4
    value='JKLS'
    poz=0
    new_id='JKLS'
    new_nume='test_nume'
    new_cnp=1111111111111
    client=Client(new_id,new_nume,new_cnp)
    clients.update(value,poz,False,new_nume,new_cnp)
    assert client==clients.get_all_clients()[3]
    #5
    value='Nicula Nelia'
    poz=1
    new_id='test_id'
    new_nume='Nicula Nelia'
    new_cnp=2900614015217
    client=Client(new_id,new_nume,new_cnp)
    clients.update(value,poz,new_id,False,False)
    assert client==clients.get_all_clients()[10]
#Find
def test_find_client_by_id():
    clients=ClientRepo(True)
    client_list=generate_clients()
    #1
    id='13JK'
    client=clients.find_client_by_id(id)
    assert client==client_list[0]
    #2
    id='89JS'
    client=clients.find_client_by_id(id)
    assert client==client_list[1]
    #3
    id='Y123'
    client=clients.find_client_by_id(id)
    assert client==client_list[2]
    #4
    id='JKLS'
    client=clients.find_client_by_id(id)
    assert client==client_list[3]
def test_find_client_by_nume():
    clients=ClientRepo(True)
    client_list=generate_clients()
    #1
    nume='Bugnar Catalin'
    client=clients.find_client_by_nume(nume)
    assert client==client_list[0]
    #2
    nume='Bugnar Andreea'
    client=clients.find_client_by_nume(nume)
    assert client==client_list[1]
    #3
    nume='Bugnar Diana'
    client=clients.find_client_by_nume(nume)
    assert client==client_list[2]
    #4
    nume='Todoran Liana'
    client=clients.find_client_by_nume(nume)
    assert client==client_list[3]
def test_find_client_by_cnp():
    clients=ClientRepo(True)
    client_list=generate_clients()
    #1
    cnp=5030727120535
    client=clients.find_client_by_cnp(cnp)
    assert client==client_list[0]
    #2
    cnp=2870920253242
    client=clients.find_client_by_cnp(cnp)
    assert client==client_list[1]
    #3
    cnp=6020308238663
    client=clients.find_client_by_cnp(cnp)
    assert client==client_list[2]
    #4
    cnp=2860830398046
    client=clients.find_client_by_cnp(cnp)
    assert client==client_list[3]
def test_find_client():
    clients=ClientRepo(True)
    client_list=generate_clients()
    #1
    find_by='id'
    value='13JK'
    client=clients.find_client(find_by, value)
    assert client==client_list[0]
    #2
    find_by='nume'
    value='Bugnar Andreea'
    client=clients.find_client(find_by, value)
    assert client==client_list[1]
    #3
    find_by='cnp'
    value=6020308238663
    client=clients.find_client(find_by, value)
    assert client==client_list[2]
    #4
    find_by='id'
    value='JKLS'
    client=clients.find_client(find_by, value)
    assert client==client_list[3]
#Update
def test_update_client():
    clients=ClientRepo(True)
    #1
    find_by='id'
    value='13JK'
    new_id='new_id'
    new_nume='new_nume'
    new_cnp=11111
    client=clients.update_client(find_by, value, new_id,new_nume,new_cnp)
    client_list=clients.get_all_clients()
    assert client==client_list[0]
    #2
    find_by='nume'
    value='Bugnar Andreea'
    new_id=''
    new_nume=''
    new_cnp=11111
    client=clients.update_client(find_by, value, new_id,new_nume,new_cnp)
    client_list=clients.get_all_clients()
    assert client==client_list[1]
    #3
    find_by='cnp'
    value=6020308238663
    new_id='new_id'
    new_nume='new_nume'
    new_cnp=11111
    client=clients.update_client(find_by, value, new_id,new_nume,new_cnp)
    client_list=clients.get_all_clients()
    assert client==client_list[2]
    #4
    find_by='id'
    value='JKLS'
    new_id=''
    new_nume='new_nume'
    new_cnp=''
    client=clients.update_client(find_by, value, new_id,new_nume,new_cnp)
    client_list=clients.get_all_clients()
    assert client==client_list[3]
#Delete
def test_delete_client():
    clients=ClientRepo(True)
    #1
    find_by='id'
    value='13JK'
    client=clients.delete_client(find_by, value)
    client_list=clients.get_all_clients()
    assert len(client_list)==10
    for el in client_list:
        assert el!=client
    #2
    find_by='nume'
    value='Bugnar Andreea'
    client=clients.delete_client(find_by, value)
    client_list=clients.get_all_clients()
    assert len(client_list)==9
    for el in client_list:
        assert el!=client
    #3
    find_by='cnp'
    value=6020308238663
    client=clients.delete_client(find_by, value)
    client_list=clients.get_all_clients()
    assert len(client_list)==8
    for el in client_list:
        assert el!=client
    #4
    find_by='id'
    value='JKLS'
    client=clients.delete_client(find_by, value)
    client_list=clients.get_all_clients()
    assert len(client_list)==7
    for el in client_list:
        assert el!=client

#Apelare
test_store_clients()
test_delete_clients()
test_update_clients()
test_find_client_by_id()
test_find_client_by_nume()
test_find_client_by_cnp()
test_find_client()
test_update_client()
test_delete_client()