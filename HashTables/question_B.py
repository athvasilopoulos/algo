import random
import time

random.seed(1053578)
# Prime numbers for the hash table size
sizes = [
    1009,
    2027,
    4057,
    8117,
    16249,
    32503,
    65011,
    130027,
    260081,
    520193,
    1040387,
    2080777,
]


def create_table(size):
    """
    Creates a table of a given size filled with zeros
    """
    table = []
    for _ in range(size):
        table.append(0)
    return table


def createVisit():
    """
    Creates a credit card payment entry. The card string is 16 symbols consisted
    of 12 numbers and the 4 letters ABCD. The entry also contains the price and
    the day of the visit.
    """
    visit = []
    card = []
    chars = "ABCD"
    numbers = "0123456789"
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    for _ in range(16):
        card.append(numbers[random.randint(0, 9)])
    for letter in chars:
        while 1:
            index = random.randint(0, 15)
            if card[index].isdigit:
                card[index] = letter
                break
    random.shuffle(card)
    cardfin = "".join(card)
    visit.append(cardfin)
    visit.append(random.uniform(10, 100))
    visit.append(days[random.randint(0, 6)])
    return cardfin, visit


def hashcode(string, size):
    """
    String hash function
    """
    base = 128
    code = 0
    for i in range(len(string)):
        code = (base * code + ord(string[i])) % size
    return code


def make_new_table():
    """
    Makes a new and bigger table, migrating all the data from the
    previous table to the new table.
    """
    old_table = table
    old_size = sizes.index(len(old_table))
    new_size = sizes[old_size + 1]
    new_table = create_table(new_size)
    for visit in old_table:
        if visit != 0:
            index = hashcode(visit[0], new_size)
            while new_table[index] != 0:
                index = (index + 1) % len(table)
            new_table[index] = visit
    return new_table


def most_visits():
    """
    Finds the card with the most visits. Uses the fact that
    there is no empty space between 2 entries of the same card, due
    to the conflict resolution method chosen.
    """
    max_visits = 0
    max_card = ""
    for visit in table:
        if visit != 0:
            visits = 0
            card = visit[0]
            index = hashcode(card, len(table))
            while table[index] != 0:
                if table[index][0] == card:
                    visits += 1
                index = (index + 1) % len(table)
            if visits > max_visits:
                max_visits = visits
                max_card = card
    return max_card, max_visits


##########################  main  #######################################

table = create_table(sizes[0])
start_t = time.time()
for i in range(1000000):
    (card, visit) = createVisit()
    index = hashcode(card, len(table))
    # Conflict resolution
    while table[index] != 0:
        index = (index + 1) % len(table)
    table[index] = visit
    # Keep the load factor under 50%
    if i / len(table) > 0.5:
        table = make_new_table()

print("Data creation took {} seconds.".format(time.time() - start_t))
start_t = time.time()
(max_card, max_visits) = most_visits()
print("Finding max card took {} seconds.".format(time.time() - start_t))
print("The card with the most visits was", max_card, "with", max_visits, "visits.")
