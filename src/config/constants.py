"""
Static, non-secret constants used throughout the application 
Anything that can change at runtime / per - environment belongs in `settings.py`
(loaded from environmnt variables) instead of here

"""

## ---- Support ingestion file types ----
SUPPORTED_EXTENSIONS = [".pdf", ".docx", ".txt", ".csv", ".xlsx", ".png", ".jpg", ".pptx"]


## ---- Checking defaults (overridable via env, see `settings.py`) ----
DEFAULT_CHUNK_SIZE = 800
DEFAULT_CHUNK_OVERLAP = 120

## ---- retrieval defaults ----
DEFAULT_TOP_K_RETRIEVAL = 8
DEFAULT_TOP_K_RERANK = 4
HYBRID_ALPHA = 0.5  # weighted between Dense vecotr search(1.0) and sparse keyword(BM25) search(0.0)


## ---- Agent / Graph node naes (used by LangGraph state machine) ----
MODEL_PLANNER = "planner"
MODEL_RETRIEVER = "retriever"
MODEL_VALIDATOR = "validator"
MODEL_ANSWER = "answer"


## ---- Guardrails limits ----
MAX_INPUT_TOKENS = 4000
MAX_OUTPUT_TOKENS = 2000
BLOCKED_KEYWORDS = ["ignore previous instructions", "ignore previous directions", "ignore previous context", "ignore previous messages", "system prompt", "jailbreak"]

## ---- Chroma Schema ----
# Chroma has no fixed schema (unlike weaviate) - this is kept only as a
# referrence list of the mtadata keys the app expects chunks to carry 

CHROMA_TEXT_PROPERTY = "content"
CHROMA_METADATA_PROPERTIES = ["source", "page", "chunk_id", "doc_type"]

# ---- Monitoring ----
METRICS_NAMESPACE = "enterprise_rag"