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


def find_minmax_round_trips(destination, departure):
    """
    Recursive Depth First function for finding the round trips. The first
    call has the same destination and departure and the function finds
    every possible round trip. If it's the longest or the shortest for 
    the specific number of hops, it is saved in the designated list.
    """
    if len(round_trip) > 8:
        return
    for airport in dnext[departure]:
        if airport == destination:
            round_trip.append(destination)
            time = 0
            for i in range(len(round_trip) - 1):
                time += find_direct_route(routes, round_trip[i + 1], round_trip[i])
            index = len(round_trip) - 3
            if time > max_times[index]:
                max_times[index] = time
                max_trip[index] = round_trip.copy()
            if time < min_times[index]:
                min_times[index] = time
                min_trip[index] = round_trip.copy()
            round_trip.pop()
        elif airport in round_trip:
            return
        else:
            round_trip.append(airport)
            find_minmax_round_trips(destination, airport)
            round_trip.pop()


##########################  main  #######################################
start_t = time.time()
routes = createData()
print("Data creation took %.3f s" % (time.time() - start_t))

dnext = {}
make_dnext(routes)

# Find the minmax round trips for all the airports.
for airport in range(num_of_airports):
    max_times = [0] * 7
    min_times = [10000] * 7
    max_trip = [[]] * 7
    min_trip = [[]] * 7
    round_trip = [airport]
    find_minmax_round_trips(airport, airport)
    # Print Results
    print("Airport ", airport, ":", sep="")
    print("\tLongest Roundtrips:")
    for i in range(len(max_trip)):
        print("\t\t", i + 2, " hops: distance = ", max_times[i], sep="")
        print("\t\t", max_trip[i])
    print("\tShortest Roundtrips:")
    for i in range(len(min_trip)):
        print("\t\t", i + 2, " hops: distance = ", min_times[i], sep="")
        print("\t\t", min_trip[i])

