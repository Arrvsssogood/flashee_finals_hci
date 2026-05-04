# app.py - Main Flask application for Flashee
# A simplified e-commerce site selling party favors

from flask import Flask, render_template, redirect, url_for, session, request, flash
from products import PRODUCTS, CATEGORIES, get_product_by_id, get_products_by_category
from datetime import datetime

app = Flask(__name__)
# Secret key needed for Flask sessions (cart storage)
app.secret_key = "flashee-secret-2024"


# ---------------------------------------------------------------------------
# Helper: get the cart from session, always returns a dict
# ---------------------------------------------------------------------------
def get_cart():
    if "cart" not in session:
        session["cart"] = {}
    return session["cart"]


def cart_total():
    """Calculate the total price of all items in the cart."""
    cart = get_cart()
    total = 0
    for product_id, item in cart.items():
        total += item["price"] * item["quantity"]
    return total


def cart_count():
    """Return total number of items (sum of quantities) in the cart."""
    cart = get_cart()
    return sum(item["quantity"] for item in cart.values())


# Make cart_count available in all templates automatically
@app.context_processor
def inject_cart_count():
    return dict(
        cart_count=cart_count(),
        user_name=session.get("user_name", None)
    )


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    """Home page — shows categories and all products."""
    return render_template("index.html", products=PRODUCTS, categories=CATEGORIES)


@app.route("/category/<category_id>")
def category(category_id):
    """Category page — filtered product grid with a sidebar."""
    products = get_products_by_category(category_id)
    # Find the matching category label for the heading
    current_cat = next((c for c in CATEGORIES if c["id"] == category_id), None)
    return render_template(
        "category.html",
        products=products,
        categories=CATEGORIES,
        current_cat=current_cat,
    )


@app.route("/product/<int:product_id>")
def product(product_id):
    """Product detail page."""
    p = get_product_by_id(product_id)
    if p is None:
        return redirect(url_for("index"))
    # Static reviews for the reviews section
    reviews = [
        {"author": "Maria S.", "rating": 5, "comment": "Amazing quality! Everyone at the party loved it."},
        {"author": "Juan D.", "rating": 4, "comment": "Fast delivery, looks exactly like the photo."},
        {"author": "Anna R.", "rating": 5, "comment": "Will definitely buy again for the next celebration!"},
    ]
    return render_template("product.html", product=p, reviews=reviews)


@app.route("/add_to_cart/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    """Add a product to the session cart — requires login."""
    # Block guests from adding to cart
    if not session.get("user"):
        flash("Please log in first to add items to your cart. 🔒", "error")
        return redirect(url_for("login"))

    p = get_product_by_id(product_id)
    if p is None:
        return redirect(url_for("index"))

    quantity = int(request.form.get("quantity", 1))
    size = request.form.get("size", "Medium")

    cart = get_cart()
    # Use a string key (session dict keys must be strings)
    key = str(product_id)
    if key in cart:
        cart[key]["quantity"] += quantity
    else:
        cart[key] = {
            "id": p["id"],
            "name": p["name"],
            "price": p["price"],
            "image": p["image"],
            "size": size,
            "quantity": quantity,
        }
    # Must reassign to mark session as modified
    session["cart"] = cart
    flash(f"{p['name']} added to cart!", "success")
    return redirect(url_for("cart"))


@app.route("/remove_from_cart/<int:product_id>")
def remove_from_cart(product_id):
    """Remove a product from the cart entirely."""
    cart = get_cart()
    key = str(product_id)
    if key in cart:
        del cart[key]
        session["cart"] = cart
    return redirect(url_for("cart"))


@app.route("/update_cart/<int:product_id>", methods=["POST"])
def update_cart(product_id):
    """Update quantity of an item in the cart."""
    cart = get_cart()
    key = str(product_id)
    quantity = int(request.form.get("quantity", 1))
    if key in cart:
        if quantity <= 0:
            del cart[key]
        else:
            cart[key]["quantity"] = quantity
    session["cart"] = cart
    return redirect(url_for("cart"))


@app.route("/cart")
def cart():
    """Cart page — shows all items, totals, and checkout button."""
    cart = get_cart()
    total = cart_total()
    return render_template("cart.html", cart=cart, total=total)


@app.route("/checkout", methods=["POST"])
def checkout():
    """Process checkout — save order to history, clear cart."""
    cart = get_cart()
    if not cart:
        return redirect(url_for("cart"))

    total = cart_total()
    shipping = 0 if total >= 999 else 99
    order = {
        "id": f"FLH-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "date": datetime.now().strftime("%B %d, %Y at %I:%M %p"),
        "items": [dict(item) for item in cart.values()],
        "subtotal": total,
        "shipping": shipping,
        "total": total + shipping,
        "status": "Order Placed"
    }

    if "order_history" not in session:
        session["order_history"] = []
    orders = session["order_history"]
    orders.append(order)
    session["order_history"] = orders

    session["cart"] = {}
    return render_template("checkout.html", order=order)


@app.route("/orders")
def orders():
    """My Orders page — shows all past orders from session."""
    if not session.get("user"):
        flash("Please log in to view your orders. 🔒", "error")
        return redirect(url_for("login"))
    order_history = list(reversed(session.get("order_history", [])))
    return render_template("orders.html", orders=order_history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Login page — stores name and email in session."""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "guest@flashee.com").strip()
        # Use the name if provided, otherwise use the part before @ in email
        display_name = name if name else email.split("@")[0].capitalize()
        session["user"] = email
        session["user_name"] = display_name
        flash(f"Welcome back, {display_name}! 🎉", "success")
        return redirect(url_for("index"))
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Signup page — stores name and email in session."""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "newuser@flashee.com").strip()
        display_name = name if name else email.split("@")[0].capitalize()
        session["user"] = email
        session["user_name"] = display_name
        flash(f"Welcome to Flashee, {display_name}! 🎉", "success")
        return redirect(url_for("index"))
    return render_template("signup.html")


@app.route("/logout")
def logout():
    name = session.get("user_name", "there")
    session.pop("user", None)
    session.pop("user_name", None)
    flash(f"See you next time, {name}! 👋", "success")
    return redirect(url_for("index"))


@app.route("/search")
def search():
    """Search by name, description, and category — partial match supported."""
    query = request.args.get("q", "").lower().strip()
    if query:
        results = [
            p for p in PRODUCTS
            if query in p["name"].lower()
            or query in p["description"].lower()
            or query in p["category_label"].lower()
        ]
    else:
        results = []
    return render_template("index.html", products=results, categories=CATEGORIES, search_query=query)



@app.route("/events")
def events():
    """Events page — themed bundles by occasion."""
    return render_template("events.html")


@app.route("/ultimate-fun")
def ultimate_fun():
    """Ultimate Fun page — best sellers and party tips."""
    # Sort by rating to get the top 4 best sellers
    top_products = sorted(PRODUCTS, key=lambda p: p["rating"], reverse=True)[:4]
    return render_template("ultimate_fun.html", top_products=top_products)


@app.route("/about")
def about():
    """About Us page — brand story and contact form."""
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
