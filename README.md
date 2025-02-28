# 🔐 Custom JWT Authentication System

## Overview
A custom implementation of JWT (JSON Web Token) authentication(login, register, logout) for Django Rest Framework, built from scratch without relying on third-party JWT libraries. This project demonstrates deep understanding of authentication mechanisms and token generation.

## 🌟 Key Features



### 🛠 Core Components


#### Token Structure
- **Header**: Algorithm & Token Type
- **Payload**: User Data & Claims
- **Signature**: Encrypted Verification

### Token Generation Process
```python
    
    # Encode header and payload
        header = base64.urlsafe_b64encode(json.dumps(header).encode('utf-8')).decode('utf-8').replace('=', '')
        payload = base64.urlsafe_b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8').replace('=', '')
        sign_input = f'{header}.{payload}'.encode('utf-8')
        hash_object = hmac.new(f'{self.secret_key}'.encode('utf-8'), sign_input, hashlib.sha256).digest()
        signature = base64.urlsafe_b64encode(hash_object).decode('utf-8').replace('=', '')
        token = f'{header}.{payload}.{signature}'
    
    return token
```

## 💻 Technical Implementation

### Security Features
- Custom token encoding/decoding
- Signature verification
- Token expiration handling
- Refresh token rotation
- CORS protection

### API Endpoints
```python
urlpatterns = [
    path('api/user/login', UserLogin.as_view()),
    path('api/api/register/', UserRegister.as_view()),
    path('api/api/logout/', UserLogout.as_view()),
]
```

## 🚀 Getting Started

### Prerequisites
```bash
# Required packages
Django>=3.2.0
djangorestframework>=3.12.0
python-dotenv>=0.19.0
```

### Installation
```bash
# Clone repository
git clone https://github.com/yamajid/authentication

# Install dependencies
pip install -r requirements.txt

# Run migrations]
python manage.py makemigrations
python manage.py migrate

# Start server
python manage.py runserver
```


### Environment Variables
```env
SECRET_KEY=your-secret-key
ACCESS_TOKEN_LIFETIME=3600
REFRESH_TOKEN_LIFETIME=604800
```

## 📝 Project Structure
```
custom_jwt_auth/
├── authentication/
│   ├── views.py
│   ├── serializers.py
│   ├── tokens.py
│   └── utils.py
├── core/
│   ├── settings.py
│   └── urls.py
└── requirements.txt
```

## 🛡️ Security Considerations

1. **Token Security**
   - Secure signature generation
   - Protected secret keys
   - Token expiration

2. **User Protection**
   - Password hashing by DRF using bcrypt
   - Rate limiting
   - Session management

## 🔍 Testing
```bash
# Run tests
python manage.py runserver

```

## 👤 Author
- Created by: @yamajid






*Built with ❤️ by @yamajid*
