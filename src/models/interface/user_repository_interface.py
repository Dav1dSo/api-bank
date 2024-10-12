from abc import ABC, abstractmethod

class UserRepository(ABC):
    
    @abstractmethod
    def registry_user(self, username: str, password: str, balance: float) -> None:
        pass
    
    @abstractmethod
    def edit_balance(self, user_id: int, new_balance: float) -> None:
        pass
    
    @abstractmethod
    def find_user(self, user_id: str):
        pass
