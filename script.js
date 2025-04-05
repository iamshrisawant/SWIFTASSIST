// script.js

document.addEventListener("DOMContentLoaded", function() {
    console.log("SwiftAssist website loaded");

    const requestServiceBtn = document.querySelector(".btn-warning");
    const emergencyCallBtn = document.querySelector(".btn-outline-light");

    requestServiceBtn.addEventListener("click", function() {
        alert("Service request feature coming soon!");
    });

    emergencyCallBtn.addEventListener("click", function() {
        window.location.href = "tel:+911234567890"; // Replace with actual emergency contact number
    });
});
