prompt_template = """
You are an assistant that classifies government complaints.
Context (similar past complaints):
{context}

Now classify the following complaint and assign:
- Category (Water, Electricity, Roads, Sanitation, Healthcare)
- Priority (Low, Medium, High)

Complaint: {complaint}
Return your response in this JSON format:
{{ "category": "...", "priority": "..." }}
"""
