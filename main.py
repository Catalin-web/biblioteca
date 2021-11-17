from domain.validators import *
from repository.book_repo import *
from repository.client_repo import *
from service.book_service import *
from service.client_service import *
from ui.console import *
from repository.book_repo_validators import *
from repository.client_repo_validators import *

book_repo=BookRepo()
client_repo=ClientRepo()
book_validator=BookValidator()
book_repo_validators=BookRepoValidator()
client_validator=ClientValidator()
client_repo_validators=ClientRepoValidator()
book_service=BookService(book_repo,book_validator,book_repo_validators)
client_service=ClientService(client_repo,client_validator,client_repo_validators)
ui=Console(book_service,client_service)
ui.start()