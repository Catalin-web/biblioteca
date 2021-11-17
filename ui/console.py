from termcolor import colored

class Console:
    def __init__(self,book_service,client_service):
        '''
        Initializeaza consola
        book_service->obiect de tip BookService, se ocupa cu service-ul pe partea cu cartiile bibliotecii
        client_service->obiect de tip ClientService, se ocupa cu service-ul pe partea cu clientii bibliotecii
        '''
        self.__book_service=book_service
        self.__client_service=client_service
    
    def __citire_comanda(self):
        '''
        Citeste comanda (2 optiuni: biblioteca/clienti)
        '''
        print(colored('Comenzi disponibile:','cyan'),colored('biblioteca clienti','green'))
        cmd=input(colored('Comanda dvs este: ','cyan'))
        cmd=cmd.lower().strip()
        return cmd
    def __aplicare_comanda(self,cmd,biblioteca,clienti):
        '''
        Aplica comanda citita de la tastatura
        cmd->string, comanda dorita
        biblioteca->functie, funcita ce vrem sa o aplicam daca comanda este biblioteca
        clienti->functie, functia pe care vrem sa o aplicam daca comanda este clienti
        '''
        if cmd=='biblioteca':
            biblioteca()
        elif cmd=='clienti':
            clienti()
        else: 
            print(colored('Comanda invalida!','red'))
    #Add
    def __add_book(self):
        '''
        Adauga o carte in biblioteca cu date citite de la tastatura
        '''
        id=input(colored('Id: ','cyan'))
        titlu=input(colored('Titlu: ','cyan'))
        descriere=input(colored('Descriere: ','cyan'))
        autor=input(colored('Autor: ','cyan'))
        try:
            added_book=self.__book_service.add_book(id,titlu,descriere,autor)
            print(colored('Cartea '+added_book.get_titlu()+' a fost adaugata cu succes!','green'))
        except ValueError as ve:
            print(colored(str(ve),'red'))
    def __add_client(self):
        '''
        Adauga un client in lista de clienti cu date citite de la tastatura
        '''
        id=input(colored('Id: ','cyan'))
        nume=input(colored('Nume: ','cyan'))
        try:
            cnp=int(input(colored('Cnp: ','cyan')))
            added_client=self.__client_service.add_client(id, nume, cnp)
            print(colored('Clientul '+added_client.get_nume()+' a fost adaugata cu succes!','green'))
        except ValueError as ve:
            print(colored(str(ve),'red'))
    def __add(self):
        '''
        O functie care citeste optiunile utilizator pentru adaugare obiect
        '''
        cmd=self.__citire_comanda()
        self.__aplicare_comanda(cmd,self.__add_book,self.__add_client)
    #Print
    def __print_books(self):
        '''
        Printeaza toate cartiile din biblioteca curenta
        '''
        books=self.__book_service.get_all_books()
        print(colored('Biblioteca:','green'))
        print(colored(books,'green'))
    def __print_clients(self):
        '''
        Printeaza toti clientii bibliotecii
        '''
        clients=self.__client_service.get_all_clients()
        print(colored('Clienti:','green'))
        print(colored(clients,'green'))
    def __print(self):
        '''
        O functie care citeste optiunile de printare de la utilizator (sa afiseze clientii sau cartiile)
        '''
        cmd=self.__citire_comanda()
        self.__aplicare_comanda(cmd,self.__print_books,self.__print_clients)
    #Import
    def __import_books(self):
        '''
        Importeaza o biblioteca
        '''
        self.__book_service.import_books()
    def __import_clients(self):
        '''
        Importeaza clienti
        '''
        self.__client_service.import_clients()
    def __import(self):
        '''
        O functie care citeste optiunile utilizatorului de a importa (biblioteca/clienti)
        '''
        cmd=self.__citire_comanda()
        self.__aplicare_comanda(cmd,self.__import_books,self.__import_clients)
        print(colored('Importare realizata cu succes!','green'))
    #Update
    def __update_book(self):
        '''
        O functie care citeste de la tastatura si updateaza o carte cu date citite de la tastatura
        '''
        print(colored('Da-ti criteriul de cautare al cartii:','cyan'),colored('id titlu autor','green'))
        cmd=input(colored('Criteriul este: ','cyan'))
        if cmd!='id' and cmd!='titlu' and cmd!='autor':
            print(colored('Comanda gresita!','red'))
            return
        value=input(colored(cmd+': ','cyan'))
        print(colored('Noile caracteristici ale cartii vor fi: (nu scrie nimic daca nu vrei sa updatezi un field)','cyan'))
        id=input(colored('Id: ','cyan'))
        titlu=input(colored('Titlu: ','cyan'))
        descriere=input(colored('Descriere: ','cyan'))
        autor=input(colored('Autor: ','cyan'))
        try:
            self.__book_service.update_book(cmd, value, id, titlu, descriere, autor)
            print(colored('Carte actualizata cu succes!','green'))
        except ValueError as ve:
            print(colored(str(ve),'red'))
    def __update_client(self):
        '''
        O functie care citeste de la tastatura numere si actualizeaza un client cu date citite de la tastatura
        '''
        print(colored('Da-ti criteriul de cautare al clientului:','cyan'),colored('id nume cnp','green'))
        cmd=input(colored('Criteriul este: ','cyan'))
        if cmd!='id' and cmd!='nume' and cmd!='cnp':
            print(colored('Comanda gresita!','red'))
            return
        value=input(colored(cmd+': ','cyan'))
        try:
            if cmd=='cnp':value=int(value)
        except ValueError:
            print(colored('Cnp-ul trebuie sa fie un numar!','red'))
            return
        print(colored('Noile caracteristici ale clientului vor fi: (nu scrie nimic daca nu vrei sa updatezi un field)','cyan'))
        id=input(colored('Id: ','cyan'))
        nume=input(colored('Nume: ','cyan'))
        try:
            cnp=input(colored('Cnp: ','cyan'))
            if cnp!='':cnp=int(cnp)
        except ValueError:
            print(colored('Cnp-ul trebuie sa fie un numar!','red'))
            return
        try:
            self.__client_service.update_client(cmd, value, id, nume,cnp)
            print(colored('Client actualizat cu succes!','green'))
        except ValueError as ve:
            print(colored(str(ve),'red'))
    def __update(self):
        '''
        O functie care citeste optiunile utilizatorului de a updata (biblioteca/clienti)
        '''
        cmd=self.__citire_comanda()
        self.__aplicare_comanda(cmd,self.__update_book,self.__update_client)
    #Delete
    def __delete_book(self):
        '''
        O functie care citeste date de la tastatura si sterge o carte cu datele primite de la utilizator
        '''
        print(colored('Da-ti criteriul de cautare al cartii:','cyan'),colored('id titlu autor','green'))
        cmd=input(colored('Criteriul este: ','cyan'))
        if cmd!='id' and cmd!='titlu' and cmd!='autor':
            print(colored('Comanda gresita!','red'))
            return
        value=input(colored(cmd+': ','cyan'))
        try:
            client=self.__book_service.delete_book(cmd,value)
            print(colored('Cartea a fost stearsa cu succes!','green'))
        except ValueError as ve:
            print(colored(str(ve),'red'))
    def __delete_client(self):
        '''
        O functie care citeste date de la tastatura si sterge un client cu datele primite de la utilizator
        '''
        print(colored('Da-ti criteriul de cautare al cartii:','cyan'),colored('id nume cnp','green'))
        cmd=input(colored('Criteriul este: ','cyan'))
        if cmd!='id' and cmd!='nume' and cmd!='cnp':
            print(colored('Comanda gresita!','red'))
            return
        value=input(colored(cmd+': ','cyan'))
        if cmd=='cnp':
            try:
                value=int(value)
            except ValueError:
                print(colored('Cnp-ul trebuie sa fie un numar!','red'))
        try:
            client=self.__client_service.delete_client(cmd,value)
            print(colored('Clientul a fost sters cu succes!','green'))
        except ValueError as ve:
            print(colored(str(ve),'red'))
    def __delete(self):
        '''
        O functie care citeste optiunile utilizatorului de a sterge o carte/ un client (biblioteca/clienti)
        '''
        cmd=self.__citire_comanda()
        self.__aplicare_comanda(cmd,self.__delete_book,self.__delete_client)
    
    def start(self):
        while True:
            print(colored('Comenzi disponibile:','cyan'),colored('add update delete print undo exit import','green'))
            cmd=input(colored('Comanda dvs este: ','cyan'))
            cmd=cmd.lower().strip()
            if cmd=='add':
                self.__add()
            elif cmd=='update':
                self.__update()
            elif cmd=='delete':
                self.__delete()
            elif cmd=='print':
                self.__print()
            elif cmd=='import':
                self.__import()
            elif cmd=='exit':
                return
            else:
                print(colored('Comanda invalida.','red'))