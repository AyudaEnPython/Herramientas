const shareButton = document.getElementById("shareButton");

if (navigator.share) {
  shareButton.addEventListener("click", () => {
    const iframeSrc = document.querySelector("#apps iframe").src;
    const appTitle =
      document.querySelector("#apps").dataset.appTitle || "AyudaEnPython App";
    navigator
      .share({
        title: appTitle,
        url: iframeSrc,
      })
      .then(() => console.log("Content shared successfully!"))
      .catch((error) => console.error("Error sharing:", error));
  });
} else {
  shareButton.style.display = "none";
}

document.querySelector(".nav-btn").addEventListener("click", function () {
  document.getElementById("header-menu").classList.toggle("active");
  this.classList.toggle("active");
});

document.addEventListener("keyup", function (e) {
  if (e.key === "Escape") {
    const modals = document.querySelectorAll(".modal-overlay");
    for (const modal of modals) {
      modal.click();
    }
  }
});

function loadApp(appName) {
  const iframe = document.createElement("iframe");
  iframe.src = `${appName}/index.html`;
  iframe.style.width = "100%";
  iframe.style.height = "500px";
  const appContainer = document.getElementById("apps");
  appContainer.innerHTML = "";
  appContainer.appendChild(iframe);
  appContainer.dataset.appTitle = appName;
}

document.querySelectorAll('a[href="#app-modal"]').forEach((link) => {
  link.addEventListener("click", function () {
    const appName = this.getAttribute("data-app");
    loadApp(appName);
  });
});
