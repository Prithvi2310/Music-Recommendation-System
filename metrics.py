import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score, average_precision_score
from sklearn.metrics import ndcg_score
from sklearn.metrics import mean_squared_error
import pandas as pd

# Example ground truth dataset
ground_truth = {
    'Danny Boy': ['Drink, Drink, Drink', 'The Rose Of Tralee', 'Beyaz Entarisiyle Kar Gibi Kız', 'Return/Gone', 'River'],
    'Shape of you': ["Baby, It's Cold ", 'Touch', 'One Kiss', 'Outside', 'Treasure']
}

# Sample recommendations from the system
recommendations = {
    'Danny Boy': ['The Rose Of Tralee', 'Beyaz Entarisiyle Kar Gibi Kız', 'Return/Gone','Paranoid', 'Silencio'],
    'Shape of you': ["Baby, It's Cold Outside", 'Godless', 'Breathing', 'Outside', 'Nessun Dorma']
}

# Function to calculate precision
def calculate_precision(recommendations, ground_truth):
    precision_scores = []
    for key in recommendations:
        true_positive = len(set(recommendations[key]) & set(ground_truth[key]))
        total_recommended = len(recommendations[key])
        precision = true_positive / total_recommended
        precision_scores.append(precision)
    return np.mean(precision_scores)

# Function to calculate recall
def calculate_recall(recommendations, ground_truth):
    recall_scores = []
    for key in recommendations:
        true_positive = len(set(recommendations[key]) & set(ground_truth[key]))
        total_relevant = len(ground_truth[key])
        recall = true_positive / total_relevant
        recall_scores.append(recall)
    return np.mean(recall_scores)

# Function to calculate F1 score
def calculate_f1(precision, recall):
    if precision + recall == 0:
        return 0
    return 2 * (precision * recall) / (precision + recall)

# Calculate precision, recall, and F1 score
precision = calculate_precision(recommendations, ground_truth)
recall = calculate_recall(recommendations, ground_truth)
f1 = calculate_f1(precision, recall)

print("The precision is: ", precision)
print("The recall is: ", recall)
print("The F1 Score is: ", f1)

# Function to calculate MAP (Mean Average Precision)
def calculate_map(recommendations, ground_truth):
    map_scores = []
    for key in recommendations:
        y_true = [1 if rec in ground_truth[key] else 0 for rec in recommendations[key]]
        map_scores.append(average_precision_score([1] * len(ground_truth[key]), y_true))
    return np.mean(map_scores)

# Function to calculate NDCG (Normalized Discounted Cumulative Gain)
def calculate_ndcg(recommendations, ground_truth):
    ndcg_scores = []
    for key in recommendations:
        relevance = [1 if rec in ground_truth[key] else 0 for rec in recommendations[key]]
        ndcg_scores.append(ndcg_score([relevance], [relevance]))
    return np.mean(ndcg_scores)

# Calculate MAP, NDCG, and RMSE
map_score = calculate_map(recommendations, ground_truth)
ndcg_score_result = calculate_ndcg(recommendations, ground_truth)


print("The MAP is: ", map_score)
print("The NDGC is :", ndcg_score_result)
