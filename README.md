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

## 📁 โครงสร้างโปรเจกต์

```
ai-person-detection-demo/
│
├─ notebooks/
│   └─ AI_Person_Detection_YOLOv8.ipynb
│
└─ README.md
```

---

## 🧠 เทคโนโลยีที่ใช้

- **YOLOv8 (Ultralytics)**
- **Google Colab (Tesla T4 GPU)**
- **Python**
- **OpenCV / FFmpeg**
- **COCO8 Public Dataset**

---

## 👨‍🏫 แนวทางการใช้ในห้องเรียน

เหมาะสำหรับ:

- วิชาคอมพิวเตอร์ / AI / STEM  
- กิจกรรม Open House / ค่าย AI  
- อบรมครู / นักเรียน  
- การสาธิตพื้นฐาน Machine Learning  

ระยะเวลาแนะนำ:
- เดโมสั้น: 30 นาที  
- สอนเต็มรูปแบบ: 1–2 ชั่วโมง  

---

## ⚠️ ข้อควรคำนึงด้านจริยธรรม

- ไม่ใช้ภาพที่ละเมิดสิทธิส่วนบุคคล  
- แนะนำให้เบลอหน้า  
- ใช้เพื่อการศึกษาเท่านั้น  
- อธิบายให้นักเรียนเข้าใจเรื่อง **AI Ethics**  

---

## 📌 หมายเหตุสำคัญ

- ไฟล์วิดีโอ Output จะถูกแปลงเป็น **MP4**  
- แสดงผลในหน้า Colab ได้ทันที  
- ไม่มีการดาวน์โหลดไฟล์โดยอัตโนมัติ  

---

## 📬 ผู้พัฒนา
ดร.พีรณัฐ  คำศรีสุข และ เรืออากาศเอก อานนท์  บางเสน
จัดทำเพื่อการเรียนการสอนด้าน **Artificial Intelligence & Computer Vision** สำหรับนักเรียนระดับมัธยมศึกษา
