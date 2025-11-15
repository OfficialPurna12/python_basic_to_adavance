// HTML: <input id="cityInput" type="text"> <button onclick="fetchWeather()">Get Weather</button>
// <div id="weatherDisplay"></div>

async function fetchWeather() {
   const city = document.getElementById('cityInput').value;
   const apiKey = 'f3e76db18779fe63f8cb48937d31360a';
   const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;

   try {
       const response = await fetch(url);
       if (!response.ok) {
           throw new Error('Invalid response from API');
       }
       const data = await response.json();
       
       // Extract data
       const temp = Math.round(data.main.temp - 273.15); // Convert to Celsius
       const humidity = data.main.humidity;
       const windSpeed = data.wind.speed;
       const conditions = data.weather[0].description;
       
       // Display
       document.getElementById('weatherDisplay').innerHTML = `
           Temperature: ${temp}°C<br>
           Humidity: ${humidity}%<br>
           Wind Speed: ${windSpeed} m/s<br>
           Conditions: ${conditions}
       `;
   } catch (error) {
       console.error('Error fetching weather:', error);
       alert('Failed to fetch weather data. Please check city name or network.');
   }
}