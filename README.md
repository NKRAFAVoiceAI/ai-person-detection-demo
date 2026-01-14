# AI Person Detection with YOLOv8 (Google Colab – GPU T4)

โปรเจกต์นี้จัดทำขึ้นเพื่อใช้ **สาธิตการทำงานของ AI ตรวจจับบุคคล (Person Detection)**  
สำหรับนักเรียนระดับมัธยม โดยใช้ **YOLOv8** บน **Google Colab (GPU Tesla T4)**

ผู้เรียนจะได้เห็นครบทั้งกระบวนการ:

1. ตรวจจับคนจาก **ภาพนิ่ง**  
2. ตรวจจับคนจาก **วิดีโอ**  
3. ทำ **Fine-tune** โมเดลด้วย Public Dataset  
4. ใช้ **โมเดลที่ฝึกแล้ว (best.pt)** ตรวจจับซ้ำ  
5. เปรียบเทียบผล **ก่อน–หลัง** แบบชัดเจน  

---

## 🔗 Open in Google Colab

คลิกเพื่อเปิด Notebook เวอร์ชันสมบูรณ์สำหรับการสอนนักเรียน:

https://colab.research.google.com/github/NKRAFAVoiceAI/ai-person-detection-demo/blob/main/notebooks/AI_Person_Detection_YOLOv8_Full_Demo_Students_UPDATED.ipynb

> แนะนำให้เปิดด้วย **คอมพิวเตอร์** และตั้งค่า  
> Runtime → Change runtime type → **GPU**

---

## 🎯 วัตถุประสงค์การเรียนรู้

นักเรียนจะได้เรียนรู้:

- AI มองภาพและวิดีโออย่างไร  
- Bounding Box และ Confidence คืออะไร  
- การใช้ GPU ช่วยให้ประมวลผลเร็วขึ้น  
- Fine-tune คืออะไร และทำไมต้องใช้ Dataset  
- การนำโมเดลที่ฝึกแล้วไปใช้งานต่อจริง  

---

## 🗂 การเตรียม Dataset สำหรับ Fine-tune (YOLO Format)

Dataset คือชุดข้อมูลภาพพร้อมไฟล์ Label ที่บอกตำแหน่งวัตถุในภาพ  
YOLO ใช้โครงสร้างดังนี้:

dataset/
 ├─ images/
 │   ├─ train/
 │   └─ val/
 ├─ labels/
 │   ├─ train/
 │   └─ val/
 └─ data.yaml

รูปแบบไฟล์ Label (.txt):

class_id x_center y_center width height

ตัวอย่าง (ตรวจจับคน):

0 0.52 0.48 0.30 0.60

ขั้นตอนเตรียม Dataset:
1) เก็บภาพ  
2) ทำ Label (เช่น Roboflow, LabelImg)  
3) จัดโครงสร้าง YOLO  
4) บีบอัดเป็น .zip  
5) อัปโหลดเข้า Colab  
6) ใช้ model.train()  

---

## 🔍 ตัวอย่างการประยุกต์ใช้ YOLO ในการตรวจจับวัตถุอื่น ๆ

โมเดล YOLOv8 สามารถตรวจจับวัตถุได้มากกว่า 80 คลาส เช่น

ด้านความปลอดภัย / โรงเรียน:
- person (คน)
- backpack (กระเป๋า)
- cell phone (โทรศัพท์)
- umbrella (ร่ม)

ด้านการจราจร:
- car, motorcycle, bus, bicycle
- traffic light, stop sign

กีฬาและกิจกรรม:
- sports ball, tennis racket, skateboard

สัตว์:
- dog, cat, bird, horse

สิ่งของในชีวิตประจำวัน:
- bottle, cup, chair, laptop, book

---

## 🎯 การตรวจจับหลายคลาสพร้อมกัน

ตัวอย่างการตรวจจับ คน + รถ + มอเตอร์ไซค์ + รถบัส

```python
results = model.predict(
    source=img_path,
    classes=[0, 2, 3, 5],
    conf=0.25,
    device=0
)
```

ดูรายชื่อคลาสทั้งหมด:

```python
model.names
```

---

## 📁 โครงสร้างโปรเจกต์

ai-person-detection-demo/
│
├─ notebooks/
│   └─ AI_Person_Detection_YOLOv8_Full_Demo_Students_UPDATED.ipynb
│
├─ src/
│   ├─ infer.py
│   └─ train.py
│
├─ assets/
│   ├─ sample_images/
│   └─ sample_videos/
│
├─ docs/
│   ├─ CHECKLIST.md
│   └─ PRIVACY_ETHICS.md
│
└─ README.md

---

## ⚠️ ข้อควรคำนึงด้านจริยธรรม

- ไม่ใช้ภาพที่ละเมิดสิทธิส่วนบุคคล  
- แนะนำให้เบลอหน้า  
- ใช้เพื่อการศึกษาเท่านั้น  

---

## 📬 ผู้พัฒนา

จัดทำเพื่อการเรียนการสอนด้าน AI & Computer Vision
