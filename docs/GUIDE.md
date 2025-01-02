# Nexa Solutions Website Deployment Guide

This guide provides step-by-step instructions for deploying the Nexa Solutions website on Ubuntu 18.04 and Ubuntu 22.04 servers.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Ubuntu 18.04 Deployment](#ubuntu-1804-deployment)
- [Ubuntu 22.04 Deployment](#ubuntu-2204-deployment)
- [Common Configuration](#common-configuration)
- [SSL Configuration](#ssl-configuration)
- [Maintenance](#maintenance)

## Prerequisites
- Python 3.8+ (Ubuntu 18.04) or Python 3.10+ (Ubuntu 22.04)
- Nginx
- Git
- Virtual Environment
- Domain name (for production)

## Ubuntu 18.04 Deployment

### 1. System Updates
```bash
sudo apt update
sudo apt upgrade -y
```

### 2. Install Required System Packages
```bash
sudo apt install -y python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-venv nginx git
```

### 3. Install Python 3.8 (if not already installed)
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.8 python3.8-venv
```

### 4. Create Project Directory
```bash
sudo mkdir -p /var/www/nexa
sudo chown -R $USER:$USER /var/www/nexa
```

### 5. Clone Repository and Setup Virtual Environment
```bash
cd /var/www/nexa
git clone [your-repository-url] .
python3.8 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 6. Configure Gunicorn
Create a systemd service file:
```bash
sudo nano /etc/systemd/system/nexa.service
```

Add the following content:
```ini
[Unit]
Description=Gunicorn instance to serve Nexa website
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/nexa
Environment="PATH=/var/www/nexa/venv/bin"
ExecStart=/var/www/nexa/venv/bin/gunicorn --workers 3 --bind unix:nexa.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```

## Ubuntu 22.04 Deployment

### 1. System Updates
```bash
sudo apt update
sudo apt upgrade -y
```

### 2. Install Required System Packages
```bash
sudo apt install -y python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-venv nginx git
```

### 3. Create Project Directory
```bash
sudo mkdir -p /var/www/nexa
sudo chown -R $USER:$USER /var/www/nexa
```

### 4. Clone Repository and Setup Virtual Environment
```bash
cd /var/www/nexa
git clone [your-repository-url] .
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 5. Configure Gunicorn
Create a systemd service file:
```bash
sudo nano /etc/systemd/system/nexa.service
```

Add the following content (same as Ubuntu 18.04).

## Common Configuration

### 1. Configure Nginx
Create a new Nginx server block:
```bash
sudo nano /etc/nginx/sites-available/nexa
```

Add the following configuration:
```nginx
server {
    listen 80;
    server_name your_domain.com www.your_domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /var/www/nexa;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/nexa/nexa.sock;
    }
}
```

### 2. Enable the Site
```bash
sudo ln -s /etc/nginx/sites-available/nexa /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

### 3. Start and Enable Gunicorn Service
```bash
sudo systemctl start nexa
sudo systemctl enable nexa
sudo systemctl status nexa
```

## SSL Configuration

### 1. Install Certbot
For Ubuntu 18.04:
```bash
sudo apt install -y certbot python3-certbot-nginx
```

For Ubuntu 22.04:
```bash
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

### 2. Obtain SSL Certificate
```bash
sudo certbot --nginx -d your_domain.com -d www.your_domain.com
```

## Maintenance

### Updating the Website
```bash
cd /var/www/nexa
source venv/bin/activate
git pull
pip install -r requirements.txt
sudo systemctl restart nexa
```

### Backup Database (if applicable)
```bash
# Add backup commands based on your database
```

### Monitoring Logs
```bash
# Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log

# Application logs
sudo journalctl -u nexa
```

### Common Issues and Solutions
1. **502 Bad Gateway**
   - Check if Gunicorn is running
   - Verify permissions
   - Check error logs

2. **Static Files Not Loading**
   - Verify static file paths
   - Check Nginx configuration
   - Ensure proper permissions

3. **SSL Certificate Issues**
   - Renew certificate: `sudo certbot renew`
   - Check certificate status: `sudo certbot certificates`

## Security Recommendations
1. Enable UFW firewall
2. Regular system updates
3. Implement rate limiting
4. Use strong passwords
5. Regular security audits

For additional support or questions, please contact the development team.
