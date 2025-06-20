import google.generativeai as genai
import os
from dotenv import load_dotenv

from retriever.embedder import get_embedding
from retriever.retriever import build_store
from prompts.prompt_template import prompt_template

import json
import re
store = build_store()

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable not set.")
genai.configure(api_key=API_KEY)

def classify_with_rag(user_input):
    query_vec = get_embedding(user_input)
    context = store.search(query_vec, k=3)

    context_texts = "\n".join([c['complaint_text'] for c in context if 'complaint_text' in c])

    prompt = prompt_template.format(context=context_texts, complaint=user_input)
    model = genai.GenerativeModel('gemini-2.0-flash')
    try:
        response = model.generate_content(prompt)
        raw = response.text
        cleaned = re.sub(r"```json|```", "", raw).strip()
        return json.loads(cleaned)   # in dictionary format
    except Exception as e:
        print(f"Error during API call: {e}")
        return {
        "error": str(e)
    }
    
    
# testing input    
# test_complaint = "The water taps are completely dry, no water for days!"
# classification_output = classify_with_rag(test_complaint)
# print(f"Classification result for '{test_complaint}':\n{classification_output}")
