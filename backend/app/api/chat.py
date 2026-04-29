from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta
from pydantic import BaseModel
import time

from app.db.session import get_db
from app.models.chat_history import ChatHistory

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    user_id: str

class ChatResponse(BaseModel):
    reply: str
    status: str

@router.post("/", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest, db: Session = Depends(get_db)):
    time.sleep(1) # Giả lập delay
    
    # Logic trả lời tạm thời
    user_msg = request.message.lower()
    if "học phí" in user_msg:
        reply_text = "Học phí dự kiến của UIT năm 2026 dao động từ 30 - 50 triệu VNĐ/năm tùy chương trình đào tạo."
    elif "điểm chuẩn" in user_msg:
        reply_text = "Điểm chuẩn các ngành của UIT năm ngoái từ 25.5 đến 28.1 điểm. Bạn muốn hỏi cụ thể ngành nào?"
    else:
        reply_text = f"Hệ thống đang được nâng cấp để trả lời câu hỏi: '{request.message}'. Chức năng tra cứu thông minh bằng RAG sẽ sớm ra mắt!"

    # Lưu vào Database (Lịch sử hỏi đáp) kèm theo user_id thật
    new_history = ChatHistory(
        user_id=request.user_id,
        question=request.message,
        answer=reply_text,
        status="Đã trả lời"
    )
    db.add(new_history)
    db.commit()

    return ChatResponse(reply=reply_text, status="success")

# --- API MỚI: LẤY LỊCH SỬ THEO USER ---
@router.get("/history/{user_id}")
def get_user_history(user_id: str, db: Session = Depends(get_db)):
    histories = db.query(ChatHistory).filter(ChatHistory.user_id == user_id).order_by(ChatHistory.created_at.desc()).all()
    
    result = []
    for h in histories:
        # Cộng thêm 7 tiếng để chuyển từ giờ Quốc tế (UTC) sang giờ Việt Nam (UTC+7)
        local_time = h.created_at + timedelta(hours=7)
        
        result.append({
            "id": h.id,
            "date": local_time.strftime("%d/%m/%Y"),
            "time": local_time.strftime("%H:%M"), # Bây giờ giờ sẽ hiển thị chuẩn!
            "question": h.question,
            "answer": h.answer,
            "status": h.status
        })
    return result