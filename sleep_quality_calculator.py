import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def calculate_wake_time():
    try:
        # รับเวลานอนที่ผู้ใช้กรอก
        sleep_time_str = sleep_time_entry.get()
        
        # แปลงเวลานอนเป็น datetime
        sleep_time = datetime.strptime(sleep_time_str, "%H:%M")
        
        # คำนวณเวลาตื่นที่เหมาะสม (7-9 ชั่วโมง)
        sleep_duration = timedelta(hours=8)  # ใช้เวลานอน 8 ชั่วโมง (ปรับได้)
        wake_time = sleep_time + sleep_duration
        
        # แสดงผล
        messagebox.showinfo(
            "เวลาตื่นที่แนะนำ",
            f"เวลานอน: {sleep_time.strftime('%H:%M')}\nเวลาตื่นที่เหมาะสม: {wake_time.strftime('%H:%M')}"
        )
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกเวลาในรูปแบบ HH:MM (เช่น 22:30)")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Wake Time Calculator")
root.geometry("400x200")

# อินพุตเวลานอน
sleep_time_label = tk.Label(root, text="เวลานอน (ชั่วโมง:นาที):", font=("Arial", 12))
sleep_time_label.pack(pady=10)
sleep_time_entry = tk.Entry(root, font=("Arial", 12), justify="center", width=10)
sleep_time_entry.pack(pady=5)

# ปุ่มคำนวณ
calculate_button = tk.Button(
    root, text="คำนวณ", font=("Arial", 12), bg="#4caf50", fg="white",
    command=calculate_wake_time
)
calculate_button.pack(pady=10)

# รันโปรแกรม
root.mainloop()
