// Quantity adjustment logic
function adjustQty(btn, delta) {
  const control = btn.parentElement;
  const input = control.querySelector(".qty-input");
  if (!input) return;
  let val = parseInt(input.value) + delta;
  if (val < 1) val = 1;
  if (val > 99) val = 99;
  input.value = val;
  const form = control.closest("form");
  if (form) form.submit();
}

// Checkout Modal
function openCheckoutModal() {
  document.getElementById('checkout-modal').style.display = 'flex';
}
function closeCheckoutModal() {
  document.getElementById('checkout-modal').style.display = 'none';
}

// Removal Modal
function openCancelModal(url, itemName) {
  document.getElementById('remove-item-text').innerText = "Remove " + itemName + " from your cart?";
  document.getElementById('confirm-remove-link').href = url;
  document.getElementById('cancel-modal').style.display = 'flex';
}
function closeCancelModal() {
  document.getElementById('cancel-modal').style.display = 'none';
}

// Close on background click
window.onclick = function(event) {
  if (event.target.classList.contains('custom-modal-overlay')) {
    event.target.style.display = 'none';
  }
}