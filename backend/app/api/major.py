from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.major import Major
from app.schemas.major import MajorCreate, MajorResponse

router = APIRouter()

@router.get("/", response_model=list[MajorResponse])
def get_majors(db: Session = Depends(get_db)):
    return db.query(Major).all()

@router.post("/", response_model=MajorResponse)
def create_major(major: MajorCreate, db: Session = Depends(get_db)):
    db_major = db.query(Major).filter(Major.code == major.code).first()
    if db_major:
        raise HTTPException(status_code=400, detail="Mã ngành này đã tồn tại!")
    
    new_major = Major(**major.model_dump())
    db.add(new_major)
    db.commit()
    db.refresh(new_major)
    return new_major

@router.delete("/{major_id}")
def delete_major(major_id: int, db: Session = Depends(get_db)):
    major = db.query(Major).filter(Major.id == major_id).first()
    if not major:
        raise HTTPException(status_code=404, detail="Không tìm thấy ngành học")
    db.delete(major)
    db.commit()
    return {"message": "Đã xóa thành công"}