from flask import Flask, render_template, request
from dsa import LinkedList, Queue, Stack, Graph

app = Flask(__name__)

# =========================
# DATA STRUCTURES
# =========================
cities = LinkedList()
trip_queue = Queue()        # Trip planning system
recent_routes = Stack()     # Find route history (STACK)
graph = Graph()


# =========================
# HOME
# =========================
@app.route('/')
def home():
    return render_template('index.html')


# =========================
# ADD CITY (Linked List + Graph node)
# =========================
@app.route('/add_city', methods=['GET', 'POST'])
def add_city():
    if request.method == 'POST':
        city = request.form['city']
        cities.add_city(city)
        graph.add_city(city)

    return render_template('add_city.html')


# =========================
# CONNECT CITIES (GRAPH EDGES)
# =========================
@app.route('/connect_city', methods=['GET', 'POST'])
def connect_city():
    city_list = cities.get_cities()

    if request.method == 'POST':
        city1 = request.form['city1']
        city2 = request.form['city2']
        graph.connect_city(city1, city2)

    return render_template('connect_city.html', cities=city_list)


# =========================
# FIND ROUTE (BFS + STACK HISTORY)
# =========================
@app.route('/find_route', methods=['GET', 'POST'])
def find_route():
    city_list = cities.get_cities()
    route = []

    if request.method == 'POST':
        start = request.form['start']
        end = request.form['end']

        # BFS search on graph
        route = graph.bfs(start, end)

        # Store result in STACK (recent routes)
        if route:
            recent_routes.push(" → ".join(route))

    return render_template('find_route.html', cities=city_list, route=route)


# =========================
# HISTORY PAGE (STACK VIEW)
# =========================
@app.route('/history')
def history():
    return render_template(
        'history.html',
        routes=recent_routes.get_items()
    )


# =========================
# TRIP PLAN (QUEUE)
# =========================
@app.route('/trip_plan', methods=['GET', 'POST'])
def trip_plan():
    city_list = cities.get_cities()

    if request.method == 'POST':
        city = request.form['city']
        trip_queue.enqueue(city)

    return render_template(
        'trip_plan.html',
        cities=city_list,
        plan=trip_queue.get_items()
    )


# =========================
# COMPLETE TRIP (PROCESS QUEUE)
# =========================
@app.route('/complete_trip')
def complete_trip():

    completed = []

    # Dequeue all planned cities
    while trip_queue.get_items():
        city = trip_queue.dequeue()
        if city:
            completed.append(city)

    return render_template(
        'queue.html',
        requests=completed
    )


# =========================
# QUEUE VIEW (CURRENT TRIP PLAN)
# =========================
@app.route('/queue')
def queue_page():
    return render_template(
        'queue.html',
        requests=trip_queue.get_items()
    )


# =========================
# GRAPH VIEW
# =========================
@app.route('/graph_view')
def graph_view():
    return render_template(
        'graph.html',
        graph=graph.get_graph()
    )


# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True)