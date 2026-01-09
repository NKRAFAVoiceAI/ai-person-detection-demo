# AI Person Detection Demo (YOLOv8) — GitHub + Google Colab (T4-ready)

โครงการตัวอย่างสำหรับ “การสาธิตการใช้งานปัญญาประดิษฐ์ (AI) เพื่อการตรวจจับบุคคล”
ออกแบบให้ผู้ช่วยวิทยากรเปิดแล้วใช้งานได้ทันทีบน **Google Colab (GPU: T4)**

## สิ่งที่ทำได้
- Inference ตรวจจับบุคคล (Person Detection) ด้วย YOLOv8 (Ultralytics)
- รันบน Google Colab (ไม่ต้องติดตั้งในเครื่อง)
- รองรับภาพ/วิดีโอ และแสดงผลในโน้ตบุ๊ก
- (ตัวเลือก) Fine-tune บน dataset รูปแบบ YOLO เพื่อสาธิต before/after

## Quick start (วันจริงแนะนำ)
1) Upload repo นี้ขึ้น GitHub  
2) เปิด `notebooks/AI_Person_Detection_YOLOv8.ipynb` ใน Google Colab  [Open in Colab](https://colab.research.google.com/github/NKRAFAVoiceAI/ai-person-detection-demo/blob/main/notebooks/AI_Person_Detection_YOLOv8.ipynb)
3) ตั้งค่า **Runtime → Change runtime type → GPU (T4)**  
4) Run all

## โครงสร้างโฟลเดอร์
```
ai-person-detection-yolo-colab/
  notebooks/
    AI_Person_Detection_YOLOv8.ipynb
  src/
    infer.py
    train.py
  assets/
    sample_images/
    sample_videos/
  docs/
    CHECKLIST.md
    PRIVACY_ETHICS.md
  requirements.txt
  LICENSE
  .gitignore
```

## Notes (สำคัญ)
- โมเดลฐานใช้ COCO pretrained weights (`yolov8n.pt`/`yolov8s.pt`)
- COCO class id = 0 คือ `person` จึงกรองเฉพาะบุคคลด้วย `classes=[0]`
