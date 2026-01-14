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

[Open in Colab](https://colab.research.google.com/github/NKRAFAVoiceAI/ai-person-detection-demo/blob/main/notebooks/AI_Person_Detection_YOLOv8.ipynb)

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

```
dataset/
 ├─ images/
 │   ├─ train/
 │   └─ val/
 ├─ labels/
 │   ├─ train/
 │   └─ val/
 └─ data.yaml
```

### รูปแบบไฟล์ Label (.txt)
```
class_id x_center y_center width height
```

ตัวอย่าง (ตรวจจับคน):
```
0 0.52 0.48 0.30 0.60
```

### ขั้นตอนเตรียม Dataset
1) เก็บภาพ  
2) ทำ Label (เช่น Roboflow, LabelImg)  
3) จัดโครงสร้าง YOLO  
4) บีบอัดเป็น .zip  
5) อัปโหลดเข้า Colab  
6) ใช้ `model.train()`  

รายละเอียดเชิงปฏิบัติอยู่ใน Google Colab Notebook

---

## 📁 โครงสร้างโปรเจกต์

```
ai-person-detection-demo/
│
├─ notebooks/
│   └─ AI_Person_Detection_YOLOv8_Full_Demo_Students.ipynb
│
└─ README.md
```

---

## 🧠 เทคโนโลยีที่ใช้

- YOLOv8 (Ultralytics)
- Google Colab (Tesla T4 GPU)
- Python
- OpenCV / FFmpeg
- COCO8 Public Dataset

---

## 👨‍🏫 แนวทางการใช้ในห้องเรียน

เหมาะสำหรับ:

- วิชาคอมพิวเตอร์ / AI / STEM  
- กิจกรรม Open House / ค่าย AI  
- อบรมครู / นักเรียน  

---

## ⚠️ ข้อควรคำนึงด้านจริยธรรม

- ไม่ใช้ภาพที่ละเมิดสิทธิส่วนบุคคล  
- แนะนำให้เบลอหน้า  
- ใช้เพื่อการศึกษาเท่านั้น  

---

## 📌 หมายเหตุสำคัญ

- วิดีโอ Output แสดงเป็น MP4 ใน Colab  
- ไม่มีการดาวน์โหลดอัตโนมัติ  

---

## 📬 ผู้พัฒนา

จัดทำเพื่อการเรียนการสอนด้าน AI & Computer Vision
