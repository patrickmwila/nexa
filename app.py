from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap5
from datetime import datetime
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
app.config['ADMIN_EMAIL'] = os.getenv('ADMIN_EMAIL')

# Initialize extensions
bootstrap = Bootstrap5(app)
mail = Mail(app)

# Context processor for current year
@app.context_processor
def inject_year():
    return {'year': datetime.now().year}

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])

def send_contact_email(form_data):
    """Send contact form data via email."""
    try:
        # Email to admin
        admin_msg = Message(
            subject=f"New Contact Form Submission: {form_data.subject.data}",
            recipients=[app.config['ADMIN_EMAIL']],
            body=f"""
New contact form submission received:

Name: {form_data.name.data}
Email: {form_data.email.data}
Subject: {form_data.subject.data}
Message:
{form_data.message.data}
            """,
            reply_to=form_data.email.data
        )
        mail.send(admin_msg)

        # Confirmation email to user
        user_msg = Message(
            subject="Thank you for contacting Nexa Solutions",
            recipients=[form_data.email.data],
            body=f"""
Dear {form_data.name.data},

Thank you for contacting Nexa Solutions. We have received your message and will get back to you shortly.

Your message details:
Subject: {form_data.subject.data}
Message:
{form_data.message.data}

Best regards,
Nexa Solutions Team
            """
        )
        mail.send(user_msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/why-choose-us')
def why_choose_us():
    return render_template('why_choose_us.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        success = send_contact_email(form)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            if success:
                return jsonify({'success': True, 'message': 'Message sent successfully!'})
            return jsonify({'success': False, 'message': 'Error sending message. Please try again.'})
        
        if success:
            flash('Thank you for your message! We will get back to you soon.', 'success')
        else:
            flash('Error sending email. Please try again later.', 'error')
        return redirect(url_for('contact'))
    
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({
            'success': False,
            'message': 'Please fill out all required fields correctly.',
            'errors': form.errors
        })
    
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
