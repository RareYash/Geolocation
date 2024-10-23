// Initialize the map
var map = L.map('map').setView([51.505, -0.09], 13); // Default map view (London)

// Add tile layer from OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
}).addTo(map);

// Form submission
document.getElementById("accommodationForm").addEventListener("submit", function(e) {
    e.preventDefault();  // Prevent form from submitting

    var city = document.getElementById("city").value;
    var area = document.getElementById("area").value;
    var type = document.getElementById("type").value;
    var price = document.getElementById("price").value;

    alert(`Finding accommodation in ${city}, ${area} for ${type} within ${price} range.`);

    // You can integrate backend logic here to filter the results based on the user's input

    // For demo, update the map based on area (hardcoded values as example)
    if (city.toLowerCase() === "london") {
        map.setView([51.5074, -0.1278], 12);  // Center map on London
    } else if (city.toLowerCase() === "new york") {
        map.setView([40.7128, -74.0060], 12); // Center map on New York
    } else {
        alert("City not recognized. Showing default location.");
    }
});


