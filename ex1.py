import logging

logging.basicConfig(filename="momo_transactions.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

balance = 0


class InvalidAmountError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


def menu():
    print("""
1. Nap tien
2. Chuyen tien
3. Xem so du
4. Thoat
""")


def deposit():
    global balance

    try:
        x = input("nhap tien nap: ")
        x = int(x)

        if x <= 0:
            raise InvalidAmountError("am")

        balance += x

        logging.info("Deposit successful: +%s VND. Current Balance: %s",
                     x, balance)

        print("nap thanh cong", balance)

    except ValueError:
        print("sai dinh dang")
        logging.error("ValueError - invalid input deposit")

    except InvalidAmountError:
        print("tien phai > 0")
        logging.error("InvalidAmountError deposit %s", x)


def transfer():
    global balance

    phone = input("phone: ")

    amt = input("money: ")

    try:
        amt = int(amt)

        if amt <= 0:
            raise InvalidAmountError("bad")

        if amt > balance:
            raise InsufficientBalanceError("no money")

        if amt >= 10000000:
            logging.warning("High value transaction detected: %s VND to %s",
                            amt, phone)

        balance -= amt

        logging.info("Transfer successful: -%s VND to %s. Current Balance: %s",
                     amt, phone, balance)

        print("done", balance)

    except ValueError:
        print("wrong format")
        logging.error("ValueError transfer")

    except InvalidAmountError:
        print("so tien sai")
        logging.error("InvalidAmountError transfer %s", amt)

    except InsufficientBalanceError:
        print("khong du tien")
        logging.error("InsufficientBalanceError %s %s", amt, balance)


def show():
    print("BALANCE =", balance)


def run():
    while True:
        menu()
        c = input("chon: ")

        if c == "1":
            deposit()

        elif c == "2":
            transfer()

        elif c == "3":
            show()

        elif c == "4":
            logging.info("System shutdown")
            print("bye")
            break

        else:
            print("invalid")


run()