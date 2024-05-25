import googlemaps
import networkx as nx
from collections import deque

# Google Maps API Key
gmaps = googlemaps.Client(key='YOUR_GOOGLE_MAPS_API_KEY')

def get_location(address):
    geocode_result = gmaps.geocode(address)
    return (geocode_result[0]['geometry']['location']['lat'], geocode_result[0]['geometry']['location']['lng'])

def get_nearest_nodes(graph, current_location, destination):
    current_node = None
    destination_node = None
    min_current_distance = float('inf')
    min_destination_distance = float('inf')
    
    for node in graph.nodes():
        node_location = (graph.nodes[node]['lat'], graph.nodes[node]['lon'])
        current_distance = calculate_distance(current_location, node_location)
        destination_distance = calculate_distance(destination, node_location)
        
        if current_distance < min_current_distance:
            min_current_distance = current_distance
            current_node = node
            
        if destination_distance < min_destination_distance:
            min_destination_distance = destination_distance
            destination_node = node
            
    return current_node, destination_node

def calculate_distance(location1, location2):
    # Haversine formula to calculate distance between two points on a sphere
    lat1, lon1 = location1
    lat2, lon2 = location2
    radius = 6371  # km
    
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c
    
    return distance

def bfs(graph, current_node, destination_node):
    queue = deque([[current_node]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == destination_node:
            return path
        for neighbor in graph.neighbors(node):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
            
    return None

def get_turn_by_turn_directions(path, graph):
    directions = ''
    for i in range(len(path) - 1):
        node1 = path[i]
        node2 = path[i + 1]
        node1_location = (graph.nodes[node1]['lat'], graph.nodes[node1]['lon'])
        node2_location = (graph.nodes[node2]['lat'], graph.nodes[node2]['lon'])
        directions += f'From {node1} to {node2}, go {calculate_bearing(node1_location, node2_location)}\n'
        
    return directions

def calculate_bearing(location1, location2):
    # Calculate the bearing between two points
    lat1, lon1 = location1
    lat2, lon2 = location2
    
    bearing = math.atan2(math.sin(math.radians(lon2) - math.radians(lon1)) * math.cos(math.radians(lat2)), 
                         math.cos(math.radians(lat1)) * math.sin(math.radians(lat2)) - 
                         math.sin(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(math.radians(lon2) - math.radians(lon1)))
    bearing = math.degrees(bearing)
    if bearing < 0:
        bearing += 360
        
    return bearing

# Create a graph of downtown Toronto
graph = nx.Graph()
# Add nodes and edges to the graph...

# Get the current location and destination from the user
current_location_address = input("Enter your current location: ")
destination_address = input("Enter your destination: ")

# Get the coordinates of the current location and destination
current_location = get_location(current_location_address)
destination = get_location(destination_address)

# Get the nearest nodes to the current location and destination
current_node, destination_node = get_nearest_nodes(graph, current_location, destination)

# Use BFS to find the most optimal path
path = bfs(graph, current_node, destination_node)

# Get the turn by turn directions
directions = get_turn_by_turn_directions(path, graph)

# Print the directions
print(directions)
