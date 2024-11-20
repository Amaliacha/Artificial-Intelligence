import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from forward_chaining import forward_chaining
from backward_chaining import backward_chaining

data = pd.read_csv('data/spam_dataset.csv')

# y_true to integers: 1 for 'spam', 0 for 'not spam'
y_true = data['Label'].apply(lambda x: 1 if x == 'Spam' else 0)

goal = "spam"
spam_keywords = ["free", "prize", "click", "offer", "exclusive", "act now"]

data['Forward_Prediction'] = data['Email'].apply(forward_chaining)

data['Backward_Prediction'] = data['Email'].apply(lambda email: backward_chaining(email, goal, spam_keywords))

forward_preds = data['Forward_Prediction'].apply(lambda x: 1 if x == 'Spam' else 0)  
backward_preds = data['Backward_Prediction']  

fc_accuracy = accuracy_score(y_true, forward_preds)
fc_precision = precision_score(y_true, forward_preds, pos_label=1)  
fc_recall = recall_score(y_true, forward_preds, pos_label=1)  
fc_f1 = f1_score(y_true, forward_preds, pos_label=1)  

bc_accuracy = accuracy_score(y_true, backward_preds)
bc_precision = precision_score(y_true, backward_preds, pos_label=1)  
bc_recall = recall_score(y_true, backward_preds, pos_label=1)  
bc_f1 = f1_score(y_true, backward_preds, pos_label=1)  

# Save results to a file
with open('results/metrics_results.txt', 'w') as file:
    file.write("Forward-Chaining Results:\n")
    file.write(f"Accuracy: {fc_accuracy:.2f}\n")
    file.write(f"Precision: {fc_precision:.2f}\n")
    file.write(f"Recall: {fc_recall:.2f}\n")
    file.write(f"F1 Score: {fc_f1:.2f}\n")
    file.write("\n")
    file.write("Backward-Chaining Results:\n")
    file.write(f"Accuracy: {bc_accuracy:.2f}\n")
    file.write(f"Precision: {bc_precision:.2f}\n")
    file.write(f"Recall: {bc_recall:.2f}\n")
    file.write(f"F1 Score: {bc_f1:.2f}\n")
