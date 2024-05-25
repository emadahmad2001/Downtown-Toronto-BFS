# Downtown-Toronto-BFS

## Dependancies
``pip install -U googlemaps``

To solve this problem, we will use the Google Maps API to get the map data of downtown Toronto, and then we will use the Breadth-First Search (BFS) algorithm to find the most optimal path.

Please note that you will need to replace 'YOUR_GOOGLE_MAPS_API_KEY' with your actual Google Maps API key. Also, you will need to create a graph of downtown Toronto and add nodes and edges to the graph.

This program assumes that the graph is already created and the nodes are the intersections of the streets. The program uses the Google Maps API to get the coordinates of the current location and destination, and then uses the BFS algorithm to find the most optimal path. The program then calculates the turn by turn directions based on the bearing between each pair of nodes in the path.

This is a basic program and may need to be modified to suit your specific needs. For example, you may need to add more nodes and edges to the graph, or you may need to use a more advanced algorithm to find the most optimal path.
