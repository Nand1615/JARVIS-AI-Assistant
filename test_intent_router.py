from core.question_analyzer import classify_question, get_answer_strategy
from core.search_engine import search_web
from core.verifier import verify_prime_minister
from core.answer_generator import generate_final_answer
from core.question_normalizer import normalize_question


raw_question = "Ayushman Bharat"
question = normalize_question(raw_question)


# Phase 1: Analyze question
q_type = classify_question(question)
strategy = get_answer_strategy(q_type)

# Phase 2: Search (only if required)
if strategy.get("needs_search"):
    results = search_web(question)
else:
    results = []

# Phase 3: Verify
verification = verify_prime_minister(results)

# Phase 4: Final answer
final_answer = generate_final_answer(
    question,
    verification,
    concise=True
)

print(final_answer)
