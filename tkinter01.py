import tkinter as tk                #Baris ini mengimpor modul tkinter untuk membuat antarmuka GUI. Modul messagebox diimpor untuk menampilkan kotak dialog atau pesan kepada pengguna.
from tkinter import messagebox

def hasil_prediksi():       #Mendefinisikan fungsi hasil_prediksi(), yang akan dijalankan saat tombol "Hasil Prediksi" ditekan.
    for entry in nilai_entries:
        if entry.get().strip() == "": #input kosong di dalam daftar nilai_entries. Jika ada, akan menampilkan pesan peringatan di hasil_label dengan warna merah dan menghentikan eksekusi fungsi.
            hasil_label.config(text="Harap isi semua nilai mata pelajaran.", fg="red")
            return
    try:   #Blok try mencoba mengonversi input pengguna menjadi integer dan memverifikasi bahwa nilainya berada dalam rentang 0 hingga 100. Jika ada nilai di luar rentang, 
           #kotak pesan messagebox akan ditampilkan dengan informasi bahwa nilai harus berada di antara 0 dan 100.
        for entry in nilai_entries:
            nilai = int(entry.get())
            if not (0 <= nilai <=100):
                messagebox.showinfo("Ingpo", "Nilai harus antara 0 dan 100.")
                return
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:    #Jika ada input yang bukan angka, blok except akan menangani ValueError dan menampilkan pesan kesalahan melalui messagebox.
            messagebox.showerror("Input Error", "Pastikan semua input adalah angka")
            return
    # Fungsi untuk menghasilkan tulisan saat button hasil prediksi ditekan
    hasil_label.config(text="Prodi Pilihan: Teknologi Informasi", fg="black")#Bagian ini mengatur teks dan warna di hasil_label setelah verifikasi nilai berhasil. Teks yang ditampilkan adalah "Prodi Pilihan: Teknologi Informasi."

# Membuat window utama
#Membuat window utama untuk aplikasi GUI dan mengatur judul window menjadi "Aplikasi Prediksi Prodi Pilihan."
window = tk.Tk()
window.title("Aplikasi Prediksi Prodi Pilihan")

# Menambahkan label judul
judul_label = tk.Label(window, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

nilai_entries = []
#Membuat label judul dengan teks "Aplikasi Prediksi Prodi Pilihan" menggunakan font Arial ukuran 16, dan menempatkannya di baris pertama window dengan grid
for i in range(10):
    label = tk.Label(window, text=f"Nilai Mata Pelajaran {i+1} :")
    label.grid(row=i+1, column=0, padx=1, pady=5, sticky="w")
    entry = tk.Entry(window)
    entry.grid(row=i+1, column=1, padx=1, pady=5)
    nilai_entries.append(entry)



# Menambahkan button untuk memprediksi prodi pilihan
prediksi_button = tk.Button(window, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=10)

# Menambahkan label untuk menampilkan hasil prediksi
hasil_label = tk.Label(window, text="", font=("Arial", 14))
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
window.mainloop()