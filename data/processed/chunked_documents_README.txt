Chunked dataset for UIT admission chatbot

Generated files:
- chunked_documents.jsonl
- chunked_documents.schema.json
- chunked_documents_stats.json

Current totals:
- total_chunks: 330

Chunking strategy:
- 1 chunk per major
- 1 chunk per program variant
- 1 overview chunk per curriculum
- 1 knowledge-blocks chunk per curriculum (if available)
- 1 specialization-tracks chunk per curriculum (if available)
- 1 graduation-options chunk per curriculum (if available)
- 1 chunk per semester plan
- course-catalog chunks batched at 15 courses per chunk
- 1 chunk per quota row
- 1 chunk per admission-combination row
- 1 chunk per timeline entry
- 1 chunk per registration-process entry
- 1 chunk per required-documents entry
- 1 chunk per FAQ entry
- 1 chunk per contact entry
- 1 chunk per tuition item
- 1 chunk per scholarship policy

Important note:
- Dataset is mixed-year. Admission data is mostly 2026.
- Tuition and scholarship data is 2025.
- Curriculum data is multi-year reference data.
- Use metadata/year filtering before retrieval to avoid mixing answers across years.
