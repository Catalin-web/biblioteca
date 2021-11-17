class Book:
    def __init__(self,id,titlu,descriere,autor):
        """
        Creaza o noua carte care are id, titlu, descriere si autor
        id->string, idul cartii
        titlu->string, titlul cartii
        descriere->string, descrierea cartii
        autor->string, autorul cartii
        """
        self.__id=id
        self.__titlu=titlu
        self.__descriere=descriere
        self.__autor=autor
    def get_id(self):
        return self.__id
    def get_titlu(self):
        return self.__titlu
    def get_descriere(self):
        return self.__descriere
    def get_autor(self):
        return self.__autor
    def set_id(self,new_id):
        self.__id=new_id
    def set_titlu(self,new_titlu):
        self.__titlu=new_titlu
    def set_descriere(self,new_descriere):
        self.__descriere=new_descriere
    def set_autor(self,new_autor):
        self.__autor=new_autor
    def __eq__(self,other):
        """
        Verifica egalitatea intre doua carti
        other->Book, cartea cu care facem comparatia
        return->bool
        """
        return self.get_autor()==other.get_autor() and self.get_titlu()==other.get_titlu() and self.get_descriere()==other.get_descriere()
    def __str__(self):
        return 'Id: '+self.get_id()+' | Titlu: '+self.get_titlu()+' | Autor: '+self.get_autor() +' | Descriere: '+self.get_descriere()

class Client:
    def __init__(self,id,nume,cnp):
        '''
        Creaza un nou client
        id->string, id unic client
        nume->string, numele clientului
        cnp->int, cnp-ul clientului
        '''
        self.__id=id
        self.__nume=nume
        self.__cnp=cnp
    def get_id(self):
        return self.__id
    def get_nume(self):
        return self.__nume
    def get_cnp(self):
        return self.__cnp
    def set_id(self,new_id):
        self.__id=new_id
    def set_nume(self,new_nume):
        self.__nume=new_nume
    def set_cnp(self,new_cnp):
        self.__cnp=new_cnp
    def __eq__(self,other):
        '''
        Determina daca doi clienti diferiti sunt de fapt aceeasi clienti
        other->celalalt client
        return->bool
        '''
        return self.get_nume()==other.get_nume() and self.get_cnp()==other.get_cnp()
    def __str__(self):
        return 'Id: ' + self.get_id()+' | Nume: '+self.get_nume()+' | Cnp: '+str(self.get_cnp())

#Teste

def test_create_book():
    #1
    book=Book('12AB','Wolf Hall','Fictiune istorica','Hilary Mantel')
    assert(book.get_id()=='12AB')
    assert(book.get_titlu()=='Wolf Hall')
    assert(book.get_descriere()=='Fictiune istorica')
    assert(book.get_autor()=='Hilary Mantel')
    #2
    book=Book('1102','Gilead','Fictiune crestina','Marilynne Robinson')
    assert(book.get_id()=='1102')
    assert(book.get_titlu()=='Gilead')
    assert(book.get_descriere()=='Fictiune crestina')
    assert(book.get_autor()=='Marilynne Robinson')
    #3
    book=Book('114C','Secondhand Time','Biografie','Svetlana Alexievich')
    assert(book.get_id()=='114C')
    assert(book.get_titlu()=='Secondhand Time')
    assert(book.get_descriere()=='Biografie')
    assert(book.get_autor()=='Svetlana Alexievich')
    #4
    book=Book('90OP','Never Let Me Go','Stiintifico-fantastic','Kazuo Ishiguro')
    assert(book.get_id()=='90OP')
    assert(book.get_titlu()=='Never Let Me Go')
    assert(book.get_descriere()=='Stiintifico-fantastic')
    assert(book.get_autor()=='Kazuo Ishiguro')

def test_equal_book():
    #1
    book1=Book('12AB','Wolf Hall','Fictiune istorica','Hilary Mantel')
    book2=Book('1454','Wolf Hall','Fictiune istorica','Hilary Mantel')
    assert(book1==book2)
    #2
    book1=Book('12AB','Wolf Hall','Fictiune istorica','Hilary Mantel')
    book2=Book('1102','Gilead','Fictiune crestina','Marilynne Robinson')
    assert(book1!=book2)
    #3
    book1=Book('12AB','Wolf Hall','Fictiune istorica','Hilary Mantel')
    book2=Book('1454','Wolf Hall','Fictiune istorica','Marilynne Robinson')
    assert(book1!=book2)
    #4
    book1=Book('12AB','Wolf Hall','Fictiune istorica','Hilary Mantel')
    book2=Book('1454','Wolf Hall','SCI-FI','Marilynne Robinson')
    assert(book1!=book2)
    #5
    book1=Book('12AB','Wolf Hall','Fictiune istorica','Hilary Mantel')
    book2=Book('12AB','Wolf Hall','SCI-FI','Marilynne Robinson')
    assert(book1!=book2)

def test_modify_book():
    #1
    book=Book('12AB','Wolf Hall','Fictiune istorica','Hilary Mantel')
    book.set_id('15AG')
    assert(book.get_id()=='15AG')
    #2
    book=Book('12AB','Gilead','Fictiune istorica','Hilary Mantel')
    book.set_titlu('Gilead')
    assert(book.get_titlu()=='Gilead')
    #3
    book=Book('12AB','Wolf Hall','SCI-FI','Hilary Mantel')
    book.set_descriere('SCI-FI')
    assert(book.get_descriere()=='SCI-FI')
    #4
    book=Book('12AB','Wolf Hall','Fictiune istorica','K. Robinson')
    book.set_autor('K. Robinson')
    assert(book.get_autor()=='K. Robinson')

def test_create_client():
    #1
    client=Client('ABCD','Bugnar Catalin',5021213322296)
    assert(client.get_id()=='ABCD')
    assert(client.get_nume()=='Bugnar Catalin')
    assert(client.get_cnp()==5021213322296)
    #2
    client=Client('BC27','Borodi Sara',2950411464768)
    assert(client.get_id()=='BC27')
    assert(client.get_nume()=='Borodi Sara')
    assert(client.get_cnp()==2950411464768)
    #3
    client=Client('90OP','Todoran Liana',2861122087866)
    assert(client.get_id()=='90OP')
    assert(client.get_nume()=='Todoran Liana')
    assert(client.get_cnp()==2861122087866)
    #4
    client=Client('6782','Nicula Cristian',1920224143530)
    assert(client.get_id()=='6782')
    assert(client.get_nume()=='Nicula Cristian')
    assert(client.get_cnp()==1920224143530)

def test_equal_client():
    #1
    client1=Client('ABCD','Bugnar Catalin',5021213322296)
    client2=Client('78H8','Bugnar Catalin',5021213322296)
    assert(client1==client2)
    #2
    client1=Client('ABCD','Bugnar Catalin',5021213322296)
    client2=Client('78H8','Bugnar Andreea',5021213322296)
    assert(client1!=client2)
    #3
    client1=Client('ABCD','Bugnar Catalin',5021213322296)
    client2=Client('78H8','Bugnar Andreea',2861122087866)
    assert(client1!=client2)
    #4
    client1=Client('ABCD','Bugnar Catalin',5021213322296)
    client2=Client('ABCD','Bugnar Andreea',2861122087866)
    assert(client1!=client2)

def test_modify_client():
    #1
    client=Client('ABCD','Bugnar Catalin',5021213322296)
    client.set_id('BS31')
    assert(client.get_id()=='BS31')
    #2
    client=Client('ABCD','Bugnar Catalin',5021213322296)
    client.set_nume('Maierean Mircea')
    assert(client.get_nume()=='Maierean Mircea')
    #3
    client=Client('ABCD','Bugnar Catalin',5021213322296)
    client.set_cnp(1880225099950)
    assert(client.get_cnp()==1880225099950)


test_create_book()
test_equal_book()
test_modify_book()
test_create_client()
test_equal_client()
test_modify_client()