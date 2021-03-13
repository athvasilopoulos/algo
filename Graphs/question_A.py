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


def find_two_hops(data, node_A, node_B):
    """
    Uses the direct route function to find if you can go from node A to 
    node B in 2 hops. Returns the distance or 0 if it is not possible.
    """
    for k in range(num_of_samples):
        if data[k][0] == node_A:
            dist = find_direct_route(data, data[k][1], node_B)
            if dist != 0:
                return dist + data[k][2]
        if data[k][0] == node_B:
            dist = find_direct_route(data, data[k][1], node_A)
            if dist != 0:
                return dist + data[k][2]
        if data[k][1] == node_A:
            dist = find_direct_route(data, data[k][0], node_B)
            if dist != 0:
                return dist + data[k][2]
        if data[k][1] == node_B:
            dist = find_direct_route(data, data[k][0], node_A)
            if dist != 0:
                return dist + data[k][2]
    return 0


##########################  main  #######################################

start_t = time.time()
routes = createData()
print("Data creation took %.3f s" % (time.time() - start_t))
count = 0
for i in range(num_of_airports):
    for j in range(num_of_airports):
        if i == j:
            continue
        if find_direct_route(routes, i, j) != 0:
            continue
        elif find_two_hops(routes, i, j) != 0:
            continue
        else:
            count += 1
if count:
    print("{} routes between nodes need more than two hops".format(count // 2))
else:
    print("Every route can be done in one or two hops")

