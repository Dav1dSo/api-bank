import logging
from factory import db
from models.entities.users import User

class UserRepository:
    def __init__(self, connect) -> None:
        self.__connect = connect
        
    def registry_user(self, username: str, password: str, balance: float) -> None:
        self.__username = username
        self.__password = password
        self.__balance = balance
        
        try:
    
            new_user = User(
                username=self.__username,
                password=self.__password,
                balance=self.__balance
            )
            
            db.session.add(new_user)
            db.commit()
        
        except Exception as err:
            logging.error(f"ERROR AO CRIAR NOVO USUÁRIO: {type(err)} - {err}")
            return {'error': 'Erro ao criar novo usuário!'}, 500
        
    def edit_balance(self, user_id: int, new_balance: float) -> None:
        self.__user_id = user_id
        self.__new_balance = new_balance

        exist_user_balance = db.session.query(User).filter(User.id == self.__user_id)
        
        if exist_user_balance is None:
            return {'error': 'Conta não encontrada'}, 404
        
        exist_user_balance.balance = self.__new_balance
        
        db.session.commit()