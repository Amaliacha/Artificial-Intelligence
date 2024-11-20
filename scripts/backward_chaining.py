from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def backward_chaining(email, goal, rules):
    """
    Backward chaining to determine if an email meets the spam goal.
    :param email: The email text
    :param goal: The goal (e.g., "spam")
    :param rules: List of rules (keywords indicating spam)
    :return: 1 (spam) or 0 (not spam)
    """
    if goal == "spam":
        email = email.lower()
        for rule in rules:
            if rule in email:
                return 1  #email is spam
    return 0  #email is not spam


#dataset and rules
emails = [
    "Congratulations! You've won a free prize. Click here to claim.",
    "Meeting rescheduled to tomorrow. Please confirm your attendance.",
    "Special offer! Get a discount by clicking the link below.",
    "Your package delivery has been scheduled. Track your order here.",
    "Act now to claim your exclusive rewards!",
]

# 1 for spam, 0 for non-spam
labels = [1, 0, 1, 0, 1]  

#classify spam emails
spam_keywords = ["free", "prize", "click", "offer", "exclusive", "act now"]

# classify emails using Backward Chaining
predictions = [backward_chaining(email, "spam", spam_keywords) for email in emails]

# Evaluate performance
accuracy = accuracy_score(labels, predictions)
precision = precision_score(labels, predictions)
recall = recall_score(labels, predictions)
f1 = f1_score(labels, predictions)

# Print Results
print("Backward Chaining Results:")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")