from datetime import datetime
import random

seq = 0


def generate_order_no():
    global seq
    seq = seq + 1 if seq < 1000 else 1
    date_str = datetime.now().strftime("%y%m%d%H%M%S")
    rand = random.randint(1, 99)
    return int(date_str + seq + rand)
