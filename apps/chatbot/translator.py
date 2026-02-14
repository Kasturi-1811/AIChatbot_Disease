from google import genai
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def translate_text(text, target_language):
    if not text:
        return ""

    # 🚨 Prevent unnecessary English → English calls
    if target_language.lower() in ["en", "english"]:
        return text

    prompt = f"""
Translate the following healthcare-related content into {target_language}.

Rules:
- Keep medical meaning accurate.
- Keep it natural and culturally appropriate.
- Do NOT add extra explanation.
- Only return translated text.

Text:
{text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt,
        )
        return response.text.strip()
    except Exception:
        # If quota exceeded, return original English
        return text
