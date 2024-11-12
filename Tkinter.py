import tkinter as tk
from tkinter import ttk

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi():
    hasil_label.config(text="Prodi yang diprediksi: Teknologi Informasi")

# Inisialisasi aplikasi
app = tk.Tk()
app.title("Aplikasi Prediksi Prodi Pilihan")

# Label judul
judul_label = ttk.Label(app, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

# Input untuk nilai mata pelajaran
nilai_entries = []
for i in range(1, 11):
    label = ttk.Label(app, text=f"Nilai Mata Pelajaran {i}:")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="W")
    
    entry = ttk.Entry(app)
    entry.grid(row=i, column=1, padx=10, pady=5)
    nilai_entries.append(entry)

# Tombol hasil prediksi
prediksi_button = ttk.Button(app, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil prediksi
hasil_label = ttk.Label(app, text="", font=("Arial", 12))
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
app.mainloop()
