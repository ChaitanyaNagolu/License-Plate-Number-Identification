import pandas as pd

def evaluate_accuracy(results, ground_truth_path="ground_truth.csv"):
    df_gt = pd.read_csv(ground_truth_path)
    correct = 0
    for img_name, pred_text in results.items():
        true_text = df_gt[df_gt["image_name"] == img_name]["plate_number"].values
        if true_text and true_text[0].lower().strip() in pred_text.lower():
            correct += 1
    accuracy = correct / len(results) if results else 0
    return accuracy
