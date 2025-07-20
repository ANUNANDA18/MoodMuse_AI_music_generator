def detect_mood(text):
    text = text.lower()
    if 'happy' in text or 'joy' in text:
        return 'happy'
    elif 'sad' in text or 'depressed' in text:
        return 'sad'
    elif 'energy' in text or 'excited' in text:
        return 'energetic'
    elif 'focus' in text or 'concentrate' in text:
        return 'focused'
    else:
        return 'happy'  # default mood
