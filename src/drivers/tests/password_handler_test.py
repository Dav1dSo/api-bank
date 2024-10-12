from src.drivers.password_handler import PasswordHandler

def test_password_hashed():
    password_test = "Teste123$"
    handler_password = PasswordHandler()
    
    password_encrypted = handler_password.encrypt_password(password_test)
    
    password_checked = handler_password.check_password(password_test, password_encrypted)
    
    assert password_checked