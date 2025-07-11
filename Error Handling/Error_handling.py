## Simple BankAccount class with proper industry-grade error handling:

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Custom exception
class InsufficientFunds(Exception):
    """Exception for withdrawing more than available balance"""
    pass

class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance
    
    def withdraw(self, amount: float):
        try:
            logger.info(f"Attempting to withdraw {amount}")
            if amount > self.balance:
                raise InsufficientFunds(f"Available: {self.balance}, Requested: {amount}")
            self.balance-=amount
            logger.info(f"Withdrawl successful, New Balance: {self.balance}")
        except InsufficientFunds as e:
            logger.warning(f"Withdraw failed: {e}")
        except Exception as e:
            logger.exception("Unexpectedn error during withdrawl.")
        finally:
            logger.debug("Withdraw operation completed.")

    def deposit(self, amount: float):
        if amount <=0:
            raise ValueError("Deposite must be positive.")
        self.balance += amount
        logger.info(f"Deposited: {amount}, New Balance: {self.balance}")

## Usage
account = BankAccount(1000)

account.withdraw(500)
account.withdraw(600)
account.deposit(-100)
