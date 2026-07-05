<div align="center">

# 🌤 WeatherSphere

### Modern Weather Application built with Django & OpenWeather API

<p>
<img src="https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Django-6.0-success?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/OpenWeather-API-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Responsive-Yes-green?style=for-the-badge">
<img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge">
</p>

A clean, responsive and modern weather application with **real-time weather updates**, **GPS location detection**, and **dynamic weather backgrounds**.

</div>

---

# ✨ Features

- 🌍 Search weather by city
- 📍 Detect current location using Geolocation API
- 🌡 Real-time temperature
- 🤗 Feels Like temperature
- 💧 Humidity
- 🌬 Wind Speed
- 🌤 Weather Description
- 🌅 Sunrise & Sunset
- 🌈 Dynamic weather backgrounds
- 📱 Fully Responsive UI
- 🔒 Secure API Keys using `.env`
- ⚠ Proper error handling

---

# 🛠 Tech Stack

### Backend

- Python
- Django

### Frontend

- HTML5
- CSS3
- JavaScript
- Font Awesome

### APIs

- OpenWeather API
- HTML5 Geolocation API

---

# 📸 Screenshots

> Add your screenshots inside a folder named **screenshots**

### Home Page

```
screenshots/home.png
```

### Weather Search

```
screenshots/search.png
```

### Current Location

```
screenshots/location.png
```

---

# 📂 Project Structure

```text
WeatherSphere/
│
├── config/
│
├── weather/
│   ├── static/
│   ├── templates/
│   ├── views.py
│   ├── urls.py
│
├── screenshots/
│
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/atharvabarbare-ctrl/WeatherSphere.git
```

Move into project

```bash
cd WeatherSphere
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```env
SECRET_KEY=your_secret_key

OPENWEATHER_API_KEY=your_openweather_api_key
```

Run the server

```bash
python manage.py runserver
```

Open your browser

```
http://127.0.0.1:8000
```

---

# 🔒 Security

- Environment Variables
- Secret Key Protection
- API Key Protection
- CSRF Protection
- Django Security Middleware

---

# 📈 Future Improvements

- 🌦 5-Day Forecast
- ⏰ Hourly Forecast
- 🌫 Air Quality Index
- ❤️ Favorite Cities
- 🌙 Dark Mode
- 📊 Weather Charts
- 🔔 Weather Alerts
- 📱 Progressive Web App (PWA)

---

# 👨‍💻 Author

## Atharva Barbare

**Python & Django Developer**

💼 LinkedIn

https://www.linkedin.com/in/atharva-barbare/

🐙 GitHub

https://github.com/atharvabarbare-ctrl

---

# 🤝 Contributing

Contributions are welcome.

Feel free to fork the repository and submit a pull request.

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

---

<div align="center">

Made with ❤️ using Django

</div>
