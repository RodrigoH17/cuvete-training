from ultralytics import YOLO
from config import DATASET_DIR, RESULTS_DIR, MODEL_NAME, EPOCHS, IMG_SIZE, BATCH_SIZE, RUN_NAME


def main():
    model = YOLO(MODEL_NAME)

    model.train(
        data=str(DATASET_DIR),
        epochs=EPOCHS,
        imgsz=IMG_SIZE,
        batch=BATCH_SIZE,
        project=str(RESULTS_DIR),
        name=RUN_NAME
    )


if __name__ == "__main__":
    main()