import jwt
import bcrypt
from datetime import datetime, timedelta

# Khóa bí mật để ký JWT
SECRET_KEY = "uit_admission_chatbot_super_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # Token có hạn 7 ngày

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Kiểm tra mật khẩu người dùng nhập có khớp với mã băm trong DB không"""
    # bcrypt yêu cầu chuỗi phải được chuyển sang định dạng bytes
    return bcrypt.checkpw(
        plain_password.encode('utf-8'), 
        hashed_password.encode('utf-8')
    )

def get_password_hash(password: str) -> str:
    """Băm mật khẩu trước khi lưu vào DB"""
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_bytes.decode('utf-8')

def create_access_token(data: dict):
    """Tạo JWT Token chứa thông tin user"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt