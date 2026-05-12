import math
import statistics

# 🔒 Safe standard deviation
def safe_stdev(values):
    if len(values) <= 1:
        return 1e-6
    stdev = statistics.stdev(values)
    return stdev if stdev > 1e-6 else 1e-6


# Gaussian Probability Function
def cal_probability(x, mean, stdev):
    exponent = math.exp(-((x - mean) ** 2) / (2 * (stdev ** 2)))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent


# Train Model
def train_model(dataset):
    classes = {}

    # Group by class
    for row in dataset:
        label = row[-1]
        classes.setdefault(label, []).append(row)

    summaries = {}

    # Compute mean & stdev for each feature
    for classValue, rows in classes.items():
        columns = list(zip(*rows))
        feature_summary = []

        for i in range(len(columns) - 1):  # exclude class column
            col = columns[i]
            mean = statistics.mean(col)
            stdev = safe_stdev(col)
            feature_summary.append((mean, stdev))

        summaries[classValue] = feature_summary

    return summaries


# Predict one row
def predict(summaries, input_row):
    probabilities = {}

    for classValue, classSummary in summaries.items():
        prob = 1

        for i in range(len(classSummary)):
            mean, stdev = classSummary[i]
            prob *= cal_probability(input_row[i], mean, stdev)

        probabilities[classValue] = prob

    return max(probabilities, key=probabilities.get)


# Accuracy calculation
def accuracy(test, predictions):
    correct = 0
    for i in range(len(test)):
        if test[i][-1] == predictions[i]:
            correct += 1

    return (correct / len(test)) * 100