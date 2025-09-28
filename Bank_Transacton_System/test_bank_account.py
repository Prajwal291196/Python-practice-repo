import os
import json
import pytest
from main import BankAccount

TEST_FILE = "test_bank_account.json"

@pytest.fixture(autouse=True)
def cleanup():
    """Fixture to remove test file before and after tests."""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

@pytest.fixture
def account():
    """Creates a new BankAccount for testing."""
    acc = BankAccount(initial_balance=100, account_number="123", account_name="Test User", data_file=TEST_FILE)
    return acc

# ------------------- TESTS -------------------

def test_initial_balance(account):
    assert account.balance == 100
    assert account.account_number == "123"
    assert account.account_name == "Test User"

def test_deposit_valid(account):
    result = account.deposit(50)
    assert result is True
    assert account.balance == 150
    assert any("Deposited" in t for t in account.transaction_history)

def test_deposit_invalid(account, capsys):
    result = account.deposit(-20)
    captured = capsys.readouterr().out
    assert result is False
    assert "❌ Amount must be greater than zero." in captured

def test_withdraw_valid(account):
    result = account.withdraw(30)
    assert result is True
    assert account.balance == 70
    assert any("Withdrew" in t for t in account.transaction_history)

def test_withdraw_insufficient_funds(account, capsys):
    result = account.withdraw(500)
    captured = capsys.readouterr().out
    assert result is False
    assert "❌ Insufficient funds" in captured

def test_check_balance(account, capsys):
    bal = account.check_balance()
    assert bal == 100
    out = capsys.readouterr().out
    assert "💰 Current balance" in out

def test_transaction_history(account, capsys):
    account.deposit(50)
    account.withdraw(30)
    account.print_transaction_history()
    out = capsys.readouterr().out
    assert "📜 Transaction History" in out
    assert "Deposited" in out
    assert "Withdrew" in out

def test_save_and_load_account(account):
    account.deposit(20)
    account.save_account()

    # Load from new instance to verify persistence
    new_acc = BankAccount()
    new_acc.data_file = TEST_FILE
    new_acc.load_account()

    assert new_acc.balance == account.balance
    assert new_acc.account_number == account.account_number
    assert len(new_acc.transaction_history) == len(account.transaction_history)
