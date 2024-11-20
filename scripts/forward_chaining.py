def forward_chaining(email):
    """
    Forward chaining algorithm to detect spam emails.
    Rules are based on detecting multiple spam indicators.
    """
    spam_keywords = ["free", "prize", "win", "offer", "deal", "exclusive", "bonus", "promotion"]
    if any(keyword in email.lower() for keyword in spam_keywords):
        return "Spam"

    suspicious_phrases = ["click now", "act fast", "limited time", "urgent action", "exclusive access"]
    if any(phrase in email.lower() for phrase in suspicious_phrases):
        return "Spam"

    if email.count("!") > 3:
        return "Spam"

    if "http://" in email.lower() or "https://" in email.lower():
        spammy_link_keywords = ["win", "prize", "claim", "offer", "deal"]
        if any(keyword in email.lower() for keyword in spammy_link_keywords):
            return "Spam"

    if email.startswith("Dear Customer") or email.startswith("Dear User"):
        return "Spam"

    if email.isupper():
        return "Spam"

    word_count = email.lower().split()
    spammy_word_count = sum(word in spam_keywords + suspicious_phrases for word in word_count)
    if spammy_word_count > 3:
        return "Spam"

    financial_terms = ["cash", "money", "lottery", "million", "reward"]
    if any(term in email.lower() for term in financial_terms):
        return "Spam"

    generic_greetings = ["hello friend", "dear customer", "dear user", "to whom it may concern"]
    if any(greeting in email.lower() for greeting in generic_greetings):
        return "Spam"

    if any(extension in email.lower() for extension in [".exe", ".zip", ".scr", ".bat", ".js"]):
        return "Spam"

    phishing_indicators = ["verify your account", "update your payment", "reset your password"]
    if any(phrase in email.lower() for phrase in phishing_indicators):
        return "Spam"

    return "Not Spam"


# Example Usage
emails = [
    "Congratulations! You've won a FREE PRIZE!!! Click now to claim your exclusive reward.",
    "Hello Friend, urgent action is required to verify your account. Click here: http://spam-link.com",
    "Meeting rescheduled. Please confirm your attendance.",
    "Special offer for a limited time! Get $1,000 cash bonus now!",
    "Your package delivery has been scheduled. Track your order here.",
]

# Classify emails
results = [forward_chaining(email) for email in emails]

# Print results
for idx, result in enumerate(results):
    print(f"Email {idx + 1}: {result}")