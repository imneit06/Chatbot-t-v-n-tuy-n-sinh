# UIT Admission Chatbot

Đồ án cuối kỳ môn **SE104 - Nhập môn Công nghệ Phần mềm** tại **UIT**.

Nguyễn Xuân Tiến - 24521778
Phan Tấn Tiến - 24521780
Phạm Hồ Hữu Trí - 24521841

## Giới thiệu

Hệ thống chatbot hỗ trợ tư vấn tuyển sinh, cho phép:

- tra cứu ngành học
- tra cứu học phí
- tra cứu phương thức xét tuyển
- tra cứu tổ hợp môn
- tra cứu điểm chuẩn
- hỏi đáp từ tài liệu tuyển sinh bằng RAG

---

## Cấu trúc project

```bash
uit-admission-chatbot/
│
├── frontend/                          # giao diện người dùng
│   ├── public/
│   └── src/
│       ├── components/
│       │   ├── ChatBox/
│       │   ├── MessageList/
│       │   ├── SearchForm/
│       │   ├── Navbar/
│       │   └── AdminTable/
│       ├── pages/
│       │   ├── Home.jsx
│       │   ├── ChatPage.jsx
│       │   ├── LookupPage.jsx
│       │   ├── AdminPage.jsx
│       │   └── LoginPage.jsx
│       ├── services/
│       │   └── api.js
│       ├── App.jsx
│       └── main.jsx
│
├── backend/                           # server chính
│   ├── app/
│   │   ├── api/
│   │   │   ├── chat.py
│   │   │   ├── majors.py
│   │   │   ├── tuition.py
│   │   │   ├── admissions.py
│   │   │   ├── cutoff.py
│   │   │   ├── auth.py
│   │   │   └── admin.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   │
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── major.py
│   │   │   ├── tuition.py
│   │   │   ├── admission_method.py
│   │   │   ├── subject_combination.py
│   │   │   ├── cutoff_score.py
│   │   │   └── chat_history.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── chat.py
│   │   │   ├── major.py
│   │   │   ├── tuition.py
│   │   │   ├── admission.py
│   │   │   └── auth.py
│   │   │
│   │   ├── services/
│   │   │   ├── chat_service.py
│   │   │   ├── major_service.py
│   │   │   ├── tuition_service.py
│   │   │   ├── admission_service.py
│   │   │   ├── cutoff_service.py
│   │   │   └── history_service.py
│   │   │
│   │   ├── db/
│   │   │   ├── session.py
│   │   │   ├── base.py
│   │   │   └── seed.py
│   │   │
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── Dockerfile
│
├── rag/                               # module RAG tách riêng
│   ├── data/
│   │   ├── raw/
│   │   ├── processed/
│   │   └── chunks/
│   │
│   ├── loaders/
│   │   ├── pdf_loader.py
│   │   └── web_loader.py
│   │
│   ├── preprocessing/
│   │   ├── clean_text.py
│   │   └── split_sections.py
│   │
│   ├── chunking/
│   │   └── chunker.py
│   │
│   ├── embedding/
│   │   └── embedder.py
│   │
│   ├── vectorstore/
│   │   └── vectordb.py
│   │
│   ├── retrieval/
│   │   └── retriever.py
│   │
│   ├── generation/
│   │   └── generator.py
│   │
│   ├── pipeline/
│   │   ├── ingest_pipeline.py
│   │   └── chat_pipeline.py
│   │
│   └── scripts/
│       ├── ingest_docs.py
│       └── build_index.py
│
├── database/
│   ├── schema.sql
│   └── seed_data/
│       ├── majors.csv
│       ├── tuition.csv
│       ├── admission_methods.csv
│       ├── subject_combinations.csv
│       └── cutoff_scores.csv
│
├── docs/
│   ├── SRS.md
│   ├── usecase-diagram.png
│   ├── usecase-specification.md
│   ├── erd.png
│   ├── sequence-diagram.png
│   ├── architecture-diagram.png
│   ├── testcases.xlsx
│   └── project-plan.md
│
├── tests/
│   ├── backend/
│   ├── rag/
│   └── frontend/
│
├── .env.example
├── docker-compose.yml
├── README.md
└── .gitignore