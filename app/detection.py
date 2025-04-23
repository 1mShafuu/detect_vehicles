from ultralytics import YOLO
from PIL import Image
from app.utils import save_cropped_object

model = YOLO('models/yolov8m.pt')

VEHICLE_CLASSES = {'car', 'bicycle'}
MIN_WIDTH = 20
MIN_HEIGHT = 20
COORD_TOLERANCE = 10


def is_duplicate(new_box, existing_boxes, tolerance=COORD_TOLERANCE):
    x1, y1, x2, y2 = new_box
    for ex in existing_boxes:
        ex_x1, ex_y1, ex_x2, ex_y2 = ex
        if (abs(x1 - ex_x1) <= tolerance and
            abs(y1 - ex_y1) <= tolerance and
            abs(x2 - ex_x2) <= tolerance and
            abs(y2 - ex_y2) <= tolerance):
            return True
    return False


def detect_vehicles(image_path: str):
    image = Image.open(image_path).convert("RGB")
    results = model.predict(image_path)[0]

    detections = []
    seen_boxes = []

    for box in results.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        if label in VEHICLE_CLASSES:
            xyxy = box.xyxy[0].tolist()
            x1, y1, x2, y2 = map(int, xyxy)
            w, h = x2 - x1, y2 - y1

            if w < MIN_WIDTH or h < MIN_HEIGHT:
                continue

            if is_duplicate((x1, y1, x2, y2), seen_boxes):
                continue

            seen_boxes.append((x1, y1, x2, y2))

            cropped_path = save_cropped_object(image, (x1, y1, x2, y2), label)
            detections.append({
                "vehicle_name": label,
                "image_path": cropped_path
            })

    return detections


