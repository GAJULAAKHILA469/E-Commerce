from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(_name_)
app.secret_key = "secret123"

# Sample product data
products = [
    {"id": 1, "name": "Smartphone", "price": 20000},
    {"id": 2, "name": "Laptop", "price": 55000},
    {"id": 3, "name": "Headphones", "price": 2000},
    {"id": 4, "name": "Smart Watch", "price": 3000},
]

@app.route('/')
def home():
    return render_template('home.html', products=products)

@app.route('/add_to_cart/<int:id>')
def add_to_cart(id):
    product = next((p for p in products if p["id"] == id), None)
    if product:
        cart = session.get('cart', [])
        cart.append(product)
        session['cart'] = cart
    return redirect(url_for('home'))

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    total = sum(p['price'] for p in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/checkout')
def checkout():
    session.pop('cart', None)
    return render_template('checkout.html')

if _name_ == "_main_":
    app.run(debug=True)
