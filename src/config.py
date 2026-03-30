# src/config.py

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_DIR = PROJECT_ROOT / "dataset"
MODELS_DIR = PROJECT_ROOT / "models"
RESULTS_DIR = PROJECT_ROOT / "results"

MODEL_NAME = "yolo11n-cls.pt"
EPOCHS = 30
IMG_SIZE = 224
BATCH_SIZE = 16

RUN_NAME = "first_training"