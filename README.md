# NAS Media Explorer

A lightweight, modern web-based file explorer and media player built with Flask. Designed for Raspberry Pi NAS setups to browse and play media files directly in the browser.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/flask-3.1-green)

## Features

-   **File Exploration**: Browse your media directories with a clean, grid-based interface.
-   **Media Playback**: Built-in player for video (`.mp4`, `.mkv`, `.mov`) and audio (`.mp3`, `.wav`, `.flac`) files.
-   **Modern UI**: Responsive dark theme with glassmorphism design effects.
-   **Scoped Access**: Securely restricted to a specific `media` directory.
-   **Lightweight**: Minimal dependencies, perfect for low-power devices like Raspberry Pi.

## Installation

### Prerequisites

-   Python 3.8 or higher installed.

### Setup

1.  **Clone or Download** the project to your Raspberry Pi or PC.

2.  **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    
    # Activate on Windows:
    venv\Scripts\activate
    
    # Activate on Linux/macOS:
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install Flask
    ```

4.  **Database Migration**:
    Initialize the internal database (SQLite):
    ```bash
    python manage.py migrate
    ```

5.  **Media Directory**:
    Create a folder named `media` in the project root directory. This is where you should put your files.
    ```bash
    mkdir media
    ```

## Usage

1.  **Start the Server**:
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```
    *Note: `0.0.0.0` allows access from other devices on your local network.*

2.  **Access the Interface**:
    -   On the device itself: Open `http://localhost:8000`
    -   From another device: Open `http://<PI_IP_ADDRESS>:8000` (e.g., `http://192.168.1.100:8000`)

3.  **Add Media**:
    Simply drag and drop your video and audio files into the `media` folder you created. They will instantly appear in the web interface.

## Project Structure

```text
NAS_on_Pi/
├── db.sqlite3          # Database file
├── manage.py           # Flask management script
├── media/              # YOUR MEDIA FILES GO HERE
├── nas_media/          # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── explorer/           # Main application
│   ├── templates/      # HTML templates
│   ├── views.py        # Logic for exploring and playing
│   └── urls.py
└── static/             # CSS and static assets
    └── css/
        └── style.css
```

## Security Note

This application is designed for **home network (LAN) use**. Do not expose this server directly to the public internet without proper authentication and security measures (like a reverse proxy with Basic Auth or VPN).

## Customization

-   **Theme**: Edit `static/css/style.css` to change colors and styles.
-   **Supported Formats**: Update `explorer/views.py` and `explorer/templates/explorer/explorer.html` to add more file extensions.
