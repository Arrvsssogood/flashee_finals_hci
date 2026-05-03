// app.js — General UI interactions for Flashee

// -------- Qty Selector on Product Page --------
function changeQty(delta) {
  const input = document.getElementById("qty-input");
  if (!input) return;
  let val = parseInt(input.value) + delta;
  if (val < 1) val = 1;
  if (val > 99) val = 99;
  input.value = val;
}

// -------- Sidebar Filter Clear --------
function clearFilters() {
  const checkboxes = document.querySelectorAll(".sidebar input[type='checkbox']");
  checkboxes.forEach((cb) => (cb.checked = false));
}

// -------- Sort Products (client-side) --------
function sortProducts(value) {
  const grid = document.getElementById("product-grid");
  if (!grid) return;
  const cards = Array.from(grid.querySelectorAll(".product-card"));

  cards.sort((a, b) => {
    const priceA = parseFloat(a.dataset.price || 0);
    const priceB = parseFloat(b.dataset.price || 0);
    const ratingA = parseFloat(a.dataset.rating || 0);
    const ratingB = parseFloat(b.dataset.rating || 0);

    if (value === "price-asc") return priceA - priceB;
    if (value === "price-desc") return priceB - priceA;
    if (value === "rating") return ratingB - ratingA;
    return 0; // default/featured — no change
  });

  // Re-append sorted cards
  cards.forEach((card) => grid.appendChild(card));
}

// -------- Auto-dismiss flash messages after 4 seconds --------
document.addEventListener("DOMContentLoaded", function () {
  const flashes = document.querySelectorAll(".flash");
  flashes.forEach((el) => {
    setTimeout(() => {
      el.style.opacity = "0";
      el.style.transition = "opacity 0.5s";
      setTimeout(() => el.remove(), 500);
    }, 4000);
  });
});

// -------- Profile Dropdown Toggle --------
function toggleDropdown() {
  const dropdown = document.getElementById("profileDropdown");
  if (dropdown) dropdown.classList.toggle("open");
}

// Close dropdown when clicking outside
document.addEventListener("click", function (e) {
  const dropdown = document.getElementById("profileDropdown");
  if (dropdown && !dropdown.contains(e.target)) {
    dropdown.classList.remove("open");
  }
});
