# Є готель з N номерами. Через випадковий час від 1 до t1 приходить
# новий клієнт та заселяється у один з номерів (якщо є вільний), у якому живе
# час від 1 до t2. Якщо вільних номерів немає, то клієнт очікує на звільнення
# будь-якого номера. При заданих параметрах N, t1, t2 розрахувати середню
# довжину черги клієнтів та середній час очікування.
# Вказівка: один клієнт – це 1 потік


from threading import Thread
from queue import Queue
from time import sleep
import random
import logging

logging.basicConfig(level=logging.DEBUG)

N = 3
t1 = 4
t2 = 15
index = 0

hotel = Queue(maxsize=N)
hotel_queue = Queue()


def create_customer():
    global index
    index += 1
    customer = [random.uniform(1, t1), random.uniform(1, t2), index]
    return customer


def add_customer_to_hotel_queue():
    while True:
        customer = create_customer()
        sleep(customer[0])
        hotel_queue.put(customer)
        logging.debug("Кліент {} приєднався до черги".format(customer[2]))


def customer_living_func(customer):
    sleep(customer[1])
    hotel.get()
    logging.debug("Кліент {} виселився з кімнати".format(customer[2]))


def add_customer_to_hotel():
    while True:
        customer = hotel_queue.get()
        hotel.put(customer)

        customer_th = Thread(target=customer_living_func, args=(customer,), daemon=True)
        customer_th.start()

        logging.debug("Кліент {} отримав кімнату".format(customer[2]))


all_in_queue = 0
count = 0


def count_queue():
    while True:
        global all_in_queue, count
        count += 1
        all_in_queue += hotel_queue.qsize()
        sleep(0.5)


if __name__ == '__main__':
    work_time = 60

    count_queue_th = Thread(target=count_queue, daemon=True)
    add_customer_to_hotel_queue_th = Thread(target=add_customer_to_hotel_queue, daemon=True)
    add_customer_to_hotel_th = Thread(target=add_customer_to_hotel, daemon=True)

    count_queue_th.start()
    add_customer_to_hotel_queue_th.start()
    add_customer_to_hotel_th.start()

    sleep(work_time)

    print(all_in_queue / count)
