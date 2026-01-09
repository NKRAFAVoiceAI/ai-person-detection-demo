"""Training / fine-tuning script for YOLOv8 on a custom dataset (YOLO format).

Expected:
  datasets/mydata/
    images/train, images/val
    labels/train, labels/val
    data.yaml

Usage:
  python -m src.train --data datasets/mydata/data.yaml --model yolov8n.pt --epochs 3
"""

from __future__ import annotations

import argparse
from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--data", required=True, help="Path to data.yaml")
    p.add_argument("--model", default="yolov8n.pt", help="Base model weights")
    p.add_argument("--epochs", type=int, default=3)
    p.add_argument("--imgsz", type=int, default=640)
    p.add_argument("--batch", type=int, default=16)
    p.add_argument("--device", default=None, help="0 or 'cpu'")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    model = YOLO(args.model)
    model.train(
        data=args.data,
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        device=args.device,
    )
    print("Training complete. Check runs/ folder.")


if __name__ == "__main__":
    main()
