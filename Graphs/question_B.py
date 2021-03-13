import random
import time

# number of data nodes
num_of_samples = 500
# number of different airports
num_of_airports = 100


def createData():
    """
    The data are triads of (i, j, value) where i and j are the id
    of the airports and value is the time of the direct route between them.
    There is a duplication check, so we don't get the same route twice.  
    """
    possible_routes = [
        [True for j in range(num_of_airports)] for i in range(num_of_airports)
    ]
    for i in range(num_of_airports):
        possible_routes[i][i] = False
    data = []
    random.seed(1053578)
    for i in range(num_of_samples):
        route = [0 for j in range(3)]
        while True:
            route[0] = random.randint(0, num_of_airports - 1)
            route[1] = random.randint(0, num_of_airports - 1)
            if possible_routes[route[0]][route[1]]:
                possible_routes[route[0]][route[1]] = False
                possible_routes[route[1]][route[0]] = False
                break
        route[2] = random.uniform(1.0, 5.0)
        data.append(route)
    return data


def find_direct_route(data, node_A, node_B):
    """
    Finds if there is a direct route between node A and node B.
    Returns the distance or 0 if it is not possible.
    """
    for k in range(num_of_samples):
        if (data[k][0] == node_A and data[k][1] == node_B) or (
            data[k][1] == node_A and data[k][0] == node_B
        ):
            return data[k][2]
    return 0


def make_dnext(data):
    """
    Creates a dictionary where every key is the id of an airport and
    the value is a list with the airports directly accessible.
    """
    for airport in range(num_of_airports):
        dnext[airport] = []
        for sample in range(num_of_samples):
            if data[sample][0] == airport:
                dnext[airport].append(data[sample][1])
            elif data[sample][1] == airport:
                dnext[airport].append(data[sample][0])
        dnext[airport].sort()


def find_round_trips(destination, departure):
    """
    Recursive Depth First function for finding the round trips. The first
    call has the same destination and departure and the function finds and prints
    every possible round trip under the conditions described in check_time.
    The round trip is stored in a list named round_trip which is initialized
    in the main script for each node.
    """
    if len(round_trip) > 8:
        return
    for airport in dnext[departure]:
        if airport == destination:
            round_trip.append(destination)
            time = 0
            for i in range(len(round_trip) - 1):
                time += find_direct_route(routes, round_trip[i + 1], round_trip[i])
            if check_time(len(round_trip) - 1, time):
                print(round_trip)
            round_trip.pop()
        elif airport in round_trip:
            return
        else:
            round_trip.append(airport)
            find_round_trips(destination, airport)
            round_trip.pop()


def check_time(hops, time):
    """
    Conditions to consider a round trip successful.
    """
    if hops == 2 and time <= 4:
        return True
    elif hops == 3 and time <= 7.5:
        return True
    elif hops == 4 and time <= 10.5:
        return True
    elif hops == 5 and time <= 14:
        return True
    elif hops == 6 and time <= 17:
        return True
    elif hops == 7 and time <= 20.5:
        return True
    elif hops == 8 and time <= 24:
        return True
    else:
        return False


##########################  main  #######################################
start_t = time.time()
routes = createData()
print("Data creation took %.3f s" % (time.time() - start_t))

dnext = {}
make_dnext(routes)

# Find the round trips for all the airports.
for airport in range(num_of_airports):
    round_trip = [airport]
    find_round_trips(airport, airport)

