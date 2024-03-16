const textArea = document.getElementById("textArea");
const infoIcon = document.getElementById("infoIcon");
const submitButton = document.getElementById("submitButton");

// Show info icon when text area is focused
textArea.addEventListener("focus", () => {
  infoIcon.style.display = "inline";
});

// Hide info icon when text area loses focus
textArea.addEventListener("blur", () => {
  infoIcon.style.display = "none";
});

// Check input length and enable/disable submit button accordingly
function checkInput() {
  const inputLength = textArea.value.trim().length;
  if (inputLength > 50) {
    submitButton.disabled = false;
  } else {
    submitButton.disabled = true;
  }
}

// Show info message when clicking info icon
infoIcon.addEventListener("click", () => {
  alert("Minimum character limit is 50.");
});