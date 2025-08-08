const previewBtn   = document.getElementById("preview-btn");
const modal        = document.getElementById("order-modal");
const cancelBtn    = document.getElementById("cancel-preview");
const summaryBox   = document.getElementById("summary-items");
const totalDisplay = document.getElementById("order-total");

previewBtn.addEventListener("click", function () {
  summaryBox.innerHTML = "";
  let total = 0;
  let hasItem = false;

  document.querySelectorAll(".food-row").forEach(row => {
    const input = row.querySelector(".qty-input");
    const qty   = parseInt(input.value) || 0;
    if (qty <= 0) return;

    const name  = row.dataset.name;
    const price = Number(row.dataset.price);
    const line  = qty * price;

    summaryBox.insertAdjacentHTML("beforeend",
      `<p>${name} × ${qty} = $${line.toFixed(2)}</p>`);

    total += line;
    hasItem = true;
  });

  totalDisplay.textContent = total.toFixed(2);
  if (hasItem) modal.style.display = "flex";
  else alert("Please enter quantities before previewing.");
});

cancelBtn.addEventListener("click", function () {
  modal.style.display = "none";
});