import numpy as np
import tkinter as tk
from tkinter import messagebox
import pickle

# Custom dataset
data = [
    ('fever,cough,sore_throat', 'flu'),
    ('fever,cough', 'flu'),
    ('cough,sore_throat', 'flu'),
    ('fever,sore_throat', 'flu'),
    ('fever', 'flu'),
    ('cough', 'flu'),
    ('sore_throat', 'flu'),
    ('headache,nausea,sensitivity_to_light', 'migraine'),
    ('headache,nausea', 'migraine'),
    ('nausea,sensitivity_to_light', 'migraine'),
    ('headache,sensitivity_to_light', 'migraine'),
    ('headache', 'migraine'),
    ('nausea', 'migraine'),
    ('sensitivity_to_light', 'migraine'),
    ('chest_pain,shortness_of_breath', 'heart_disease'),
    ('chest_pain', 'heart_disease'),
    ('shortness_of_breath', 'heart_disease'),
]

# Extract all unique symptoms
all_symptoms = set()
for symptoms, _ in data:
    all_symptoms.update(symptoms.split(','))
all_symptoms = list(all_symptoms)

# Diseases
diseases = list(set(disease for _, disease in data))

# Label map
label_map = {d: i for i, d in enumerate(diseases)}

# One-hot encode function
def one_hot(symptoms_str):
    vec = np.zeros(len(all_symptoms))
    symptoms = [s.strip() for s in symptoms_str.split(',')]
    for s in symptoms:
        if s in all_symptoms:
            vec[all_symptoms.index(s)] = 1
    return vec

# Prepare X and y
X = np.array([one_hot(symptoms) for symptoms, _ in data])
y = np.array([label_map[disease] for _, disease in data])

# Train Naive Bayes
n_classes = len(diseases)
class_counts = np.bincount(y)
priors = class_counts / len(y)
feature_probs = np.zeros((n_classes, X.shape[1]))
for i in range(n_classes):
    class_mask = (y == i)
    feature_counts = np.sum(X[class_mask], axis=0) + 1  # Laplace smoothing
    feature_probs[i] = feature_counts / (class_counts[i] + len(all_symptoms) * 1)  # Adjusted smoothing for better generalization

# Predict function
def predict(symptoms_str):
    vec = one_hot(symptoms_str)
    log_probs = np.log(priors)
    for f in range(len(vec)):
        p = feature_probs[:, f]
        if vec[f] == 1:
            log_probs += np.log(p)
        else:
            log_probs += np.log(1 - p)
    pred = np.argmax(log_probs)
    # Softmax for confidence
    max_log = np.max(log_probs)
    probs = np.exp(log_probs - max_log)
    probs /= np.sum(probs)
    conf = probs[pred] * 100
    return diseases[pred], conf

# Suggestions dictionary
suggestions = {
    'flu': 'Take rest, stay hydrated. If fever > 102°F, consult a doctor.',
    'migraine': 'Avoid bright lights, rest in a dark room. If persistent, consult a doctor.',
    'heart_disease': 'Seek immediate medical attention.'
}

# Save model components (optional, for persistence)
model_data = {
    'all_symptoms': all_symptoms,
    'diseases': diseases,
    'priors': priors,
    'feature_probs': feature_probs,
}
with open('model.pkl', 'wb') as f:
    pickle.dump(model_data, f)

# GUI
root = tk.Tk()
root.title('🏥 Smart Symptom Checker')

label = tk.Label(root, text='Enter symptoms (comma separated):')
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

def check_diagnosis():
    symptoms = entry.get().strip()
    if not symptoms:
        messagebox.showwarning('Input Error', 'Please enter at least one symptom.')
        return
    try:
        disease, conf = predict(symptoms)
        suggestion = suggestions.get(disease, 'Consult a doctor for further advice.')
        result = f'Possible Condition: {disease}\nConfidence: {conf:.2f}%\nSuggestion: {suggestion}'
        messagebox.showinfo('Diagnosis Result', result)
    except Exception as e:
        messagebox.showerror('Error', str(e))

button = tk.Button(root, text='Check Diagnosis', command=check_diagnosis)
button.pack(pady=10)

root.mainloop()