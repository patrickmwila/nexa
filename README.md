# Nexa Solutions Limited Website

A professional and responsive website for Nexa Solutions Limited built with Python Flask and Bootstrap.

## Features

- Modern and responsive design
- Interactive user interface
- Contact form with validation
- Mobile-friendly layout
- Clean and professional appearance

## Pages

1. Homepage
   - Company introduction
   - Vision and Mission
   - Core Values
   - Call-to-action buttons

2. About Us
   - What We Stand For
   - Our Values
   - Leadership Team

3. Services
   - Software Development
   - Search Engine Optimization
   - System Support
   - Data Migration
   - Systems Installation
   - IT Consulting
   - System Maintenance
   - Social Media Management

4. Why Choose Us
   - Top-tier Expertise
   - Dependable Support
   - Competitive Pricing
   - Cutting-edge Technology
   - Client-centric Approach
   - Continuous Improvement

5. Contact Us
   - Contact Form
   - Company Information
   - Business Hours
   - Location Information

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd nexa
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables:
   Create a `.env` file in the root directory and add:
   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here
   ```

6. Run the application:
   ```bash
   flask run
   ```

7. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Technology Stack

- Python Flask
- Bootstrap 5
- HTML5
- CSS3
- JavaScript
- Font Awesome Icons

## Project Structure

```
nexa/
├── app.py
├── requirements.txt
├── README.md
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   └── images/
└── templates/
    ├── base.html
    ├── home.html
    ├── about.html
    ├── services.html
    ├── why_choose_us.html
    └── contact.html
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is proprietary and confidential. All rights reserved by Nexa Solutions Limited.

## Contact

Nexa Solutions Limited - info@nexasolutions.com

Project Link: [https://github.com/your-username/nexa](https://github.com/your-username/nexa)
