"""Inference script for person detection using YOLOv8 (Ultralytics).

Local usage:
  python -m src.infer --source path/to/image_or_video --weights yolov8n.pt --conf 0.25 --save

Note:
- COCO class 0 = person. We filter with classes=[0].
"""

from __future__ import annotations

import argparse
from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--source", required=True, help="Path/URL to image/video, or directory.")
    p.add_argument("--weights", default="yolov8n.pt", help="YOLO weights (e.g., yolov8n.pt)")
    p.add_argument("--conf", type=float, default=0.25, help="Confidence threshold")
    p.add_argument("--device", default=None, help="e.g. 0 for CUDA:0, or 'cpu'")
    p.add_argument("--save", action="store_true", help="Save outputs to runs/")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    model = YOLO(args.weights)
    model.predict(
        source=args.source,
        conf=args.conf,
        classes=[0],
        device=args.device,
        save=args.save,
        verbose=True,
    )
    print("Done.")


if __name__ == "__main__":
    main()
