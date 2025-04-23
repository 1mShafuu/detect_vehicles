from pydantic import BaseModel
from typing import List


class DetectionResult(BaseModel):
    vehicle_name: str
    image_path: str
