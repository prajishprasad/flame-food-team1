from flask import Flask, render_template, request, redirect, url_for, session, flash

# Initialize the app
app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for sessions (to store cart data)

# Dummy data: cafes and menus
cafes = {
    "Cafe One": ["Coffee", "Sandwich", "Muffin"],
    "Cafe Two": ["Tea", "Burger", "Fries"],
    "Cafe Three": ["Pizza", "Pasta", "Salad"]
}


@app.context_processor
def inject_cart_count():
    """Make cart item count available in every template."""
    cart = session.get("cart", [])
    return {"cart_count": len(cart)}


@app.route("/")
def home():
    """Show list of cafes"""
    return render_template("index.html", cafes=cafes)

@app.route("/cafe/<name>")
def show_cafe(name):
    """Show menu of a cafe"""
    menu = cafes.get(name, [])
    return render_template("cafe.html", cafe=name, menu=menu)

@app.route("/add_to_cart/<cafe>/<item>")
def add_to_cart(cafe, item):
    """Add an item to the cart (stored in session)"""
    cart = session.get("cart", [])
    cart.append({"cafe": cafe, "item": item})
    session["cart"] = cart
    return redirect(url_for("view_cart"))

@app.route("/cart")
def view_cart():
    """View items in cart"""
    cart = session.get("cart", [])
    return render_template("cart.html", cart=cart)

@app.route("/orders")
def view_orders():
    """Show previous completed orders."""
    orders = session.get("orders", [])
    return render_template("orders.html", orders=orders)


@app.route("/checkout")
def checkout():
    """Save the cart as an order, then clear it."""
    cart = session.get("cart", [])
    if cart:
        orders = session.get("orders", [])
        orders.append({"items": list(cart)})
        session["orders"] = orders
        flash("Thanks for ordering! Your order has been placed.")
    session["cart"] = []
    return redirect(url_for("view_orders"))
    
if __name__ == "__main__":
    app.run(debug=True)
