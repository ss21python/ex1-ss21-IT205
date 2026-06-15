import unittest
from ex1 import Wallet, InvalidAmountError, InsufficientBalanceError


class TestWallet(unittest.TestCase):

    def test1(self):
        w = Wallet()
        w.deposit(500000)
        self.assertEqual(w.balance, 500000)

    def test2(self):
        w = Wallet()
        w.deposit(100000)

        try:
            w.transfer("0987654321", 200000)
            self.fail("expected error")
        except InsufficientBalanceError:
            pass

    def test3(self):
        w = Wallet()

        try:
            w.deposit(-1000)
            self.fail("expected error")
        except InvalidAmountError:
            pass


if __name__ == "__main__":
    unittest.main()