from googletrans import Translator


def translate_text(text, source_lang, target_lang):
    translator = Translator()
    result = translator.translate(text, src=source_lang, dest=target_lang)
    return result.text


def russian_to_english(text):
    return translate_text(text, 'ru', 'en')


def english_to_russian(text):
    return translate_text(text, 'en', 'ru')
