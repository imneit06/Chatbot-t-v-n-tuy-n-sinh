from sqlalchemy import Column, Integer, String, Text
from app.db.session import Base

class Major(Base):
    __tablename__ = "majors"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True, nullable=False) # Mã ngành
    name = Column(String, nullable=False)                          # Tên ngành
    fee = Column(String)                                           # Học phí
    admission_blocks = Column(String)                              # Tổ hợp môn (VD: A00, A01)
    description = Column(Text)                                     # Mô tả ngắn