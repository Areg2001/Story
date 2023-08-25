from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

UserModel = get_user_model()

def custom_validation(data):
    email = data['email'].strip()
    name = data['name'].strip()
    surname = data['surname'].strip()
    password = data['password'].strip()
    
    if not email or UserModel.objects.filter(email=email).exists():
        raise ValidationError('Choose another email')
    
    if not password or len(password) < 8:
        raise ValidationError('Choose another password, min 8 characters')
    
    if not name or len(name) < 4:
        raise ValidationError('Choose another name')
    
    if not surname or len(surname) < 4:
        raise ValidationError('Choose another surname')
 
    return data


def validate_email(data):
    email = data['email'].split()
    if not email:
        raise ValidationError('An email is needed')
    return True

def validate_name(data):
    name = data['name'].split()
    if not name:
        raise ValidationError('Choose another surname')
    return True

def validate_surname(data):
    surname = data['surname'].split()
    if not surname:
        raise ValidationError('Choose another surname')
    return True

def validate_changed_password(data):
    password = data.strip()
    if not password or len(password) < 8:
        raise ValidationError('A password is needed')
    return True

def validate_changed_name(data):
    name = data.strip()
    if not name or len(name) < 3:
        raise ValidationError('Invalid name')
    return True

def validate_password(data):
    password = data['password'].strip()
    print(password)
    if not password or len(password) < 8:
        raise ValidationError('A password is needed')
    return True