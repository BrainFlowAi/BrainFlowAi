"""
BrainFlow AI - Open Source Project
Purpose: Use AI to process brain signals (EEG, EMG, etc.) for neuro-assistive applications.

"""
from methods.process_data import load_brain_signal
from methods.process_data import preprocess_signal
from methods.train import train_model
from methods.train import predict_signal

Main runner
if __name__ == "__main__":
    file_path = "./data/raw/brain_signals.csv"  # Can be easily replaced with any dataset
    raw_data = load_brain_signal(file_path)
    processed = preprocess_signal(raw_data)
    train_model(processed)
    