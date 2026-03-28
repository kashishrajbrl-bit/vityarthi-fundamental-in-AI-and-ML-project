from collections import deque
from sklearn.tree import DecisionTreeClassifier
import numpy as np
# Symptoms dataset (encoded)
# [fever, cough, chest_pain, headache]
X = np.array([
    [1, 1, 0, 0],  # Flu
    [0, 0, 1, 0],  # Cardiologist
    [0, 0, 0, 1],  # Neurologist
    [1, 0, 0, 1],  # General Physician
    [0, 1, 0, 0],  # ENT
])
y = np.array([0, 1, 2, 0, 3])
model = DecisionTreeClassifier()
model.fit(X, y)
doctor_types = ["General Physician", "Cardiologist", "Neurologist", "ENT"]
def predict_doctor(symptoms):
    pred = model.predict([symptoms])[0]
    return doctor_types[pred]
graph = {
    "Home": ["Clinic_A", "Clinic_B"],
    "Clinic_A": ["Hospital_X"],
    "Clinic_B": ["Hospital_Y"],
    "Hospital_X": [],
    "Hospital_Y": []
}
doctors = {
    "Clinic_A": "General Physician",
    "Clinic_B": "ENT",
    "Hospital_X": "Cardiologist",
    "Hospital_Y": "Neurologist"
}
def bfs_find_doctor(start, required_specialist):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        if node in doctors and doctors[node] == required_specialist:
            return node, path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None, []
def dfs_all_doctors(start, required_specialist, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(start)
    path.append(start)
    results = []
    if start in doctors and doctors[start] == required_specialist:
        results.append((start, path.copy()))
    for neighbor in graph[start]:
        if neighbor not in visited:
            results.extend(dfs_all_doctors(neighbor, required_specialist, visited, path))
    path.pop()
    visited.remove(start)
    return results
def main():
    print("Enter symptoms (1 = Yes, 0 = No):")
    fever = int(input("Fever: "))
    cough = int(input("Cough: "))
    chest_pain = int(input("Chest Pain: "))
    headache = int(input("Headache: "))
    symptoms = [fever, cough, chest_pain, headache]
    specialist = predict_doctor(symptoms)
    print(f"\nRecommended Specialist: {specialist}")
    location, path = bfs_find_doctor("Home", specialist)
    if location:
        print(f"\nNearest Doctor at: {location}")
        print("Path:", " → ".join(path))
    else:
        print("No nearby doctor found!")
    print("\nAll available doctor paths (DFS):")
    all_paths = dfs_all_doctors("Home", specialist)
    for loc, p in all_paths:
        print(f"{loc}: {' → '.join(p)}")
main()