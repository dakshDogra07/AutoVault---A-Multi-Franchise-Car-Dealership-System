from flask import Flask, render_template, request, redirect, url_for, session
from franchise import get_all_franchises
from db import get_connection

app = Flask(__name__)
app.secret_key = "autovault123"

@app.route("/")
def index():
    franchises = get_all_franchises()
    return render_template("index.html", franchises=franchises)

@app.route("/select/<int:franchise_id>")
def select_franchise(franchise_id):
    session["franchise_id"] = franchise_id
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    if "franchise_id" not in session:
        return redirect(url_for("index"))
    franchises = get_all_franchises()
    selected = next(f for f in franchises if f["id"] == session["franchise_id"])
    return render_template("dashboard.html", franchise=selected)

@app.route("/cars/<int:franchise_id>")
def cars(franchise_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cars WHERE franchise_id = %s AND sold = FALSE", (franchise_id,))
    cars = cursor.fetchall()
    conn.close()
    return render_template("cars.html", cars=cars, franchise_id=franchise_id)

@app.route("/add_car/<int:franchise_id>", methods=["POST"])
def add_car_route(franchise_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO cars (franchise_id, brand, model, price, color, year) VALUES (%s, %s, %s, %s, %s, %s)",
        (franchise_id, request.form["brand"], request.form["model"], request.form["price"], request.form["color"], request.form["year"])
    )
    conn.commit()
    conn.close()
    return redirect(url_for("cars", franchise_id=franchise_id))

@app.route("/customers/<int:franchise_id>")
def customers(franchise_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers WHERE franchise_id = %s", (franchise_id,))
    customers = cursor.fetchall()
    conn.close()
    return render_template("customers.html", customers=customers, franchise_id=franchise_id)

@app.route("/add_customer/<int:franchise_id>", methods=["POST"])
def add_customer_route(franchise_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO customers (franchise_id, name, phone, email) VALUES (%s, %s, %s, %s)",
        (franchise_id, request.form["name"], request.form["phone"], request.form["email"])
    )
    conn.commit()
    conn.close()
    return redirect(url_for("customers", franchise_id=franchise_id))

@app.route("/sales/<int:franchise_id>")
def sales(franchise_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT s.id, c.brand, c.model, cu.name, s.price, s.sale_date 
        FROM sales s
        JOIN cars c ON s.car_id = c.id
        JOIN customers cu ON s.customer_id = cu.id
        WHERE s.franchise_id = %s
    """, (franchise_id,))
    sales = cursor.fetchall()
    
    cursor.execute("SELECT * FROM cars WHERE franchise_id = %s AND sold = FALSE", (franchise_id,))
    available_cars = cursor.fetchall()
    
    cursor.execute("SELECT * FROM customers WHERE franchise_id = %s", (franchise_id,))
    customers = cursor.fetchall()
    
    conn.close()
    return render_template("sales.html", sales=sales, franchise_id=franchise_id, available_cars=available_cars, customers=customers)

@app.route("/sell_car/<int:franchise_id>", methods=["POST"])
def sell_car_route(franchise_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    car_id = request.form["car_id"]
    customer_id = request.form["customer_id"]
    cursor.execute("SELECT price FROM cars WHERE id = %s", (car_id,))
    car = cursor.fetchone()
    cursor.execute("UPDATE cars SET sold = TRUE WHERE id = %s", (car_id,))
    cursor.execute(
        "INSERT INTO sales (franchise_id, car_id, customer_id, price) VALUES (%s, %s, %s, %s)",
        (franchise_id, car_id, customer_id, car["price"])
    )
    conn.commit()
    conn.close()
    return redirect(url_for("sales", franchise_id=franchise_id))

if __name__ == "__main__":
    app.run(debug=True)