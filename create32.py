import time
import threading
from random import randint



class Bank:

    def __init__(self , lock , balance ):
        self.lock = lock
        self.balance = balance

    def deposit(self):
        for i in range(100):
            random_ = randint(50, 500)
            self.balance += random_
            print(f'Пополнение: {random_}. Баланс: {self.balance}')
            if random_ >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            random_ = randint(50, 500)
            print(f"Запрос на {random_}")
            if self.balance <= random_:
                self.balance -= random_
                print(f'Снятие: {random_}. Баланс: {self.balance}')
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)


th1 = threading.Thread(target=Bank.deposit, args=(Bank,))
th2 = threading.Thread(target=Bank.take, args=(Bank,))

th1.start()
th2.start()
th1.join()
th2.join()


