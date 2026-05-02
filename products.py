# products.py - All product data stored as a Python list (no database)

PRODUCTS = [
    {
        "id": 1,
        "name": "Crown Headband",
        "price": 150,
        "category": "party-hats",
        "category_label": "Party Hats",
        "description": "Shine like royalty at any party! This sparkly crown headband is perfect for birthdays, bachelorette parties, and celebrations. One size fits most.",
        "image": "https://images.unsplash.com/photo-1530103862676-de8c9debad1d?w=400&q=80",
        "sizes": ["Small", "Medium", "Large"],
        "badge": "Best Seller",
        "rating": 4.8,
        "reviews": 124,
    },
    {
        "id": 2,
        "name": "Helium Balloon",
        "price": 50,
        "category": "balloons",
        "category_label": "Balloons",
        "description": "Bright, colorful helium balloons to make any event pop! Available in a rainbow of colors. Each balloon floats for up to 24 hours.",
        "image": "https://images.unsplash.com/photo-1527529482837-4698179dc6ce?w=400&q=80",
        "sizes": ["Small", "Medium", "Large"],
        "badge": "New",
        "rating": 4.5,
        "reviews": 88,
    },
    {
        "id": 3,
        "name": "Happy Birthday Banner",
        "price": 37,
        "category": "balloons",
        "category_label": "Balloons",
        "description": "Hang this vibrant Happy Birthday banner to instantly transform any space into a celebration zone. Easy to hang, reusable, and eye-catching.",
        "image": "https://images.unsplash.com/photo-1464349153735-7db50ed83c84?w=400&q=80",
        "sizes": ["Small", "Medium", "Large"],
        "badge": "Sale",
        "rating": 4.6,
        "reviews": 57,
    },
    {
        "id": 4,
        "name": "Balloons Chain Stripes",
        "price": 18,
        "category": "balloons",
        "category_label": "Balloons",
        "description": "Create a stunning balloon arch or garland with these stripe-patterned balloons. Perfect for backdrops and photo booths.",
        "image": "https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=400&q=80",
        "sizes": ["Small", "Medium", "Large"],
        "badge": None,
        "rating": 4.3,
        "reviews": 42,
    },
    {
        "id": 5,
        "name": "LED Strip Lights",
        "price": 550,
        "category": "led-lights",
        "category_label": "LED Lights",
        "description": "Set the mood with these vibrant LED strip lights! RGB color changing with remote control. Waterproof and flexible — perfect for parties, bedrooms, and events.",
        "image": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&q=80",
        "sizes": ["Small", "Medium", "Large"],
        "badge": "Hot",
        "rating": 4.9,
        "reviews": 213,
    },
    {
        "id": 6,
        "name": "Flashing LED Pin",
        "price": 75,
        "category": "led-lights",
        "category_label": "LED Lights",
        "description": "Wear your fun! These flashing LED pins light up any outfit. Great for concerts, parties, and festivals. Battery-powered and long-lasting.",
        "image": "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=400&q=80",
        "sizes": ["Small", "Medium", "Large"],
        "badge": "New",
        "rating": 4.4,
        "reviews": 66,
    },
    {
        "id": 7,
        "name": "Party Cone Hat",
        "price": 25,
        "category": "party-hats",
        "category_label": "Party Hats",
        "description": "Classic party cone hats with elastic bands. Comes in a pack of 10. Perfect for kids and adults alike. Bright colors and glitter finish.",
        "image": "https://images.unsplash.com/photo-1513151233558-d860c5398176?w=400&q=80",
        "sizes": ["Small", "Medium", "Large"],
        "badge": None,
        "rating": 4.2,
        "reviews": 35,
    },
    {
        "id": 8,
        "name": "Confetti Popper",
        "price": 45,
        "category": "party-hats",
        "category_label": "Party Hats",
        "description": "Launch a burst of colorful confetti at the perfect moment! Easy to use, big impact. Great for New Year's, birthdays, and surprise parties.",
        "image": "https://images.unsplash.com/photo-1467810563316-b5476525c0f9?w=400&q=80",
        "sizes": ["Small", "Medium", "Large"],
        "badge": "Best Seller",
        "rating": 4.7,
        "reviews": 99,
    },
]

CATEGORIES = [
    {
        "id": "balloons",
        "label": "Balloons",
        "icon": "🎈",
        "image": "https://images.unsplash.com/photo-1527529482837-4698179dc6ce?w=300&q=80",
    },
    {
        "id": "led-lights",
        "label": "LED Lights",
        "icon": "💡",
        "image": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=300&q=80",
    },
    {
        "id": "party-hats",
        "label": "Party Hats",
        "icon": "🎉",
        "image": "https://images.unsplash.com/photo-1513151233558-d860c5398176?w=300&q=80",
    },
]


def get_product_by_id(product_id):
    """Return a product dict by its integer ID, or None if not found."""
    for p in PRODUCTS:
        if p["id"] == product_id:
            return p
    return None


def get_products_by_category(category_id):
    """Return all products belonging to a given category slug."""
    return [p for p in PRODUCTS if p["category"] == category_id]
