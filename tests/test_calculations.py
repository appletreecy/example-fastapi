from app.calculations import add, subtract, multiply, divide, BankAccount, InSufficientFunds
import pytest

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected",[
    (3,2,5),
    (7,1,8),
    (3,8,11)
])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) ==  expected
   
def test_subtract():
    assert subtract(9, 4) == 5

def test_multiply():
    assert multiply(3, 6) == 18

def test_divide():
    assert divide(9, 3) == 3

def test_bank_set_initial_amount(zero_bank_account):
 
    assert zero_bank_account.balance == 0

def test_bank_deposit(bank_account):
    bank_account.deposit(200)
    assert bank_account.balance == 250

def test_bank_withdraw():
    bank_account = BankAccount(500)
    bank_account.withdraw(500)
    assert bank_account.balance == 0

def test_bank_collect_interest():
    bank_account = BankAccount(500)
    bank_account.collect_interest()
    assert bank_account.balance == 550 

@pytest.mark.parametrize("deposited, withdrew, balanced",[
    (300,200,100),
    (7,1,6),
    (13,8,5)
])

def test_bank_transactions(zero_bank_account, deposited, withdrew, balanced):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == balanced

def test_insufficient_funds(bank_account):
    with pytest.raises(InSufficientFunds):
        bank_account.withdraw(200)
