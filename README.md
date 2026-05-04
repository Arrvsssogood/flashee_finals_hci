# Flashee.com

A redesign of Blinkee.com — a simplified e-commerce site for LED party products and party favors.  
Built with Flask (Python) as a **final project** for the course **Human Computer Interaction (CS 3215)**.

---

## What is Flashee?

Flashee aims to fix the problems found in Blinkee.com:

- Too many categories and poor navigation making product search slow  
- Information overload on the home page  
- Bulk ordering and shipping features are hard to find  

The redesign offers cleaner navigation, event-based browsing, working filters, and a smoother checkout experience.

---

## Tech Stack

- **Backend:** Flask (Python)  
- **Frontend:** HTML, CSS, Vanilla JavaScript, Jinja2 Templates  
- **Storage:** Flask Sessions (no database)  
- **Container:** Docker  

---

## Features

- Browse products by category (Balloons, LED Lights, Party Hats)  
- Browse by event (Birthday, Holiday, Graduation, etc.)  
- Filter products by price and rating  
- User signup and login (name displayed in navbar)  
- Profile dropdown with logout  
- Add to cart (login required)  
- Cart with quantity controls  
- Checkout with order summary  
- Order history page  

---

## Project Structure

```
flashee/
├── app.py                  # Flask routes and logic
├── products.py             # Product and category data
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── static/
│   ├── css/styles.css
│   └── js/
│       ├── app.js
│       └── cart.js
└── templates/
    ├── base.html
    ├── index.html
    ├── category.html
    ├── product.html
    ├── cart.html
    ├── checkout.html
    ├── orders.html
    ├── events.html
    ├── ultimate_fun.html
    ├── about.html
    ├── login.html
    └── signup.html
```

---

## How to Run

### Option A — Run with Python directly

Make sure Python is installed.

Open a terminal and go to the project folder:

```bash
cd flashee
```

Install Flask:

```bash
pip install flask
```

Run the app:

```bash
python app.py
```

Open your browser and go to:  
http://localhost:5000

---

### Option B — Run with Docker

Make sure Docker Desktop is open and running.

Open a terminal and go to the project folder:

```bash
cd flashee
```

Build and start the container:

```bash
docker-compose up
```

Open your browser and go to:  
http://localhost:5000

To stop:

```bash
Ctrl + C
docker-compose down
```

---

## Sample Products

| Product                | Price |
|------------------------|-------|
| Crown Headband         | ₱150  |
| Helium Balloon         | ₱50   |
| Happy Birthday Banner  | ₱37   |
| Balloons Chain Stripes | ₱18   |
| LED Strip Lights       | ₱550  |

---

## Notes

- Cart and order history reset when the server restarts (session-based, no database)  
- Login and signup are demo only — no real authentication  
- All data is stored in `products.py` as a Python list  