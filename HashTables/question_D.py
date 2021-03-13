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
    4161557,
    8323109,
    16646237,
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


def make_new_table(old_table, table_id):
    """
    Makes a new and bigger table, migrating all the data from the
    previous table to the new table. Adds to the collision variable
    when it creates and fills the last table.
    """
    old_size = sizes.index(len(old_table))
    new_size = sizes[old_size + 1]
    new_table = create_table(new_size)
    for visit in old_table:
        if visit != 0:
            index = hashcode(visit[0], new_size)
            if new_size == final_table_sizes[table_id]:
                collisions[table_id] += check_collision(new_table, visit[0], index)
            while new_table[index] != 0:
                index = (index + 1) % len(tables[table_id])
            new_table[index] = visit
    return new_table


def check_collision(table, card, index):
    """
    Returns 1 if it detects a collision. A collision is found when
    the first time a card is registered, the hash position is not empty.
    """
    if table[index] == 0:
        return 0
    while table[index] != 0:
        if table[index][0] == card:
            return 0
        index = (index + 1) % len(table)
    return 1


##########################  main  #######################################

tables = []
for i in range(3):
    tables.append(create_table(sizes[0]))
collisions = [0] * 3
# The 3 different load factors
load_factors = [0.1, 0.3, 0.5]
# The corresponding final size for each load factor
final_table_sizes = [16646237, 4161557, 2080777]

for entry in range(1000000):
    (card, visit) = createVisit()
    for i in range(3):
        index = hashcode(card, len(tables[i]))
        if len(tables[i]) == final_table_sizes[i]:
            collisions[i] += check_collision(tables[i], card, index)
        while tables[i][index] != 0:
            index = (index + 1) % len(tables[i])
        tables[i][index] = visit
        if entry / len(tables[i]) > load_factors[i]:
            tables[i] = make_new_table(tables[i], i)

for i in range(3):
    print("Load factor =", load_factors[i], ", collisions =", collisions[i])
