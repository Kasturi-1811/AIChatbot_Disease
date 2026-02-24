from django.conf import settings
import google.genai as genai


def get_gemini_client():
    return genai.Client(api_key=settings.GEMINI_API_KEY)


def translate_text(text, target_language):
    if not text:
        return ""

    # 🚫 Avoid English → English translation
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
        client = get_gemini_client()

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception:
        # If API fails, return original text
        return text