from src.drivers.password_handler import PasswordHandler
from src.models.interface.user_repository_interface import UserRepository

class UserRegister:
    def __init__(self, user_repository: UserRepository) -> None:
        self.__user_repository = user_repository
        self.__handler_password = PasswordHandler()
        
    def registry(self, user_name: str, password: str) -> dict:
        hashed_password = self.__create_hash_password(password)
        self.__registry_new_user(user_name, hashed_password) 
        return self.__format_response()
    
    def __create_hash_password(self, password: str) -> str:
        password_hashed = self.__handler_password.encrypt_password(password)
        return password_hashed
    
    def __registry_new_user(self, user_name: str, password: str) -> None:
        self.__user_repository.registry_user(user_name, password) 
        
    def __format_response(self) -> dict:
        return {
            "msg": "User registred with success"
        }