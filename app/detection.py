from ultralytics import YOLO
from PIL import Image
from app.utils import save_cropped_object

model = YOLO('/models/yolov8m.pt')

VEHICLE_CLASSES = {'car', 'bicycle'}
MIN_WIDTH = 20
MIN_HEIGHT = 20


def detect_vehicles(image_path: str):
    image = Image.open(image_path).convert("RGB")
    results = model.predict(image_path)[0]

    detections = []
    for box in results.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        if label in VEHICLE_CLASSES:
            xyxy = box.xyxy[0].tolist()
            x1, y1, x2, y2 = map(int, xyxy)
            w, h = x2 - x1, y2 - y1
            if w < MIN_WIDTH or h < MIN_HEIGHT:
                continue  # Пропускаем слишком маленькие

            cropped_path = save_cropped_object(image, xyxy, label)
            detections.append({
                "vehicle_name": label,
                "image_path": cropped_path
            })

    return detections


# image_path = "test_img.jpg"
# detections = detect_vehicles(image_path)
# print(detections)
