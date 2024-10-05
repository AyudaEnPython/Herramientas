// uncomment when using Cirrus headers
//
// document.querySelector(".nav-btn").addEventListener("click", function () {
//   document.getElementById("header-menu").classList.toggle("active");
//   this.classList.toggle("active");
// });

function loadConfig() {
  fetch("setup.json")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("title").textContent = data.title;
      document.getElementById("subtitle").textContent = data.subtitle;
    })
    .catch((error) => console.error("Error: error loading json", error));
}

loadConfig();
