// cart.js — Cart page quantity controls

// Adjust qty in cart and auto-submit the form
function adjustQty(btn, delta) {
  // btn is the +/- button; find the input sibling
  const control = btn.parentElement;
  const input = control.querySelector(".qty-input");
  if (!input) return;

  let val = parseInt(input.value) + delta;
  if (val < 1) val = 1;
  if (val > 99) val = 99;
  input.value = val;

  // Find the nearest form and submit
  const form = control.closest("form");
  if (form) form.submit();
}
