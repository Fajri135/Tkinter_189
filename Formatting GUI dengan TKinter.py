import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi():
    try:
        # Mengambil nilai dari entry dan mengonversinya ke float
        nilai_mata_pelajaran = [float(entry.get()) for entry in entries]
        
        # Contoh logika sederhana untuk prediksi (ganti dengan model nyata)
        if sum(nilai_mata_pelajaran) / len(nilai_mata_pelajaran) >= 75:
            prediksi = "Teknologi Informasi"  # Jika rata-rata >= 75, prodi diprediksi Teknologi Informasi
        else:
            prediksi = "Umum"  # Jika rata-rata < 75, prodi diprediksi Umum
        
        # Menampilkan hasil prediksi pada label
        label_hasil.config(text=f"Prediksi Prodi: {prediksi}")
    except ValueError:
        # Menangkap kesalahan jika input bukan angka dan menampilkan pesan kesalahan
        messagebox.showerror("Input Error", "Silakan masukkan nilai yang valid (angka).")

# Fungsi untuk mereset input dan hasil
def reset_input():
    for entry in entries:
        entry.delete(0, tk.END)  # Menghapus teks di setiap entry
    label_hasil.config(text="")  # Mengosongkan label hasil

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Menetapkan judul jendela
root.geometry("400x600")  # Menentukan ukuran jendela

# Label judul
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
label_judul.pack(pady=10)  # Menambahkan label ke jendela dengan padding vertikal

# Membuat frame untuk menampung input nilai
frame_input = tk.Frame(root)
frame_input.pack(pady=20)  # Menambahkan frame ke jendela dengan padding vertikal

# Membuat 10 input nilai mata pelajaran
entries = []  # List untuk menyimpan entry
for i in range(10):
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}")
    label.grid(row=i, column=0, padx=5, pady=5)  # Menempatkan label dalam grid
    entry = tk.Entry(frame_input)
    entry.grid(row=i, column=1, padx=5, pady=5)  # Menempatkan entry dalam grid
    entries.append(entry)  # Menyimpan referensi entry ke list

# Button untuk menampilkan hasil prediksi
btn_prediksi = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
btn_prediksi.pack(pady=10)  # Menambahkan tombol ke jendela dengan padding vertikal

# Button untuk mereset input
btn_reset = tk.Button(root, text="Reset", command=reset_input)
btn_reset.pack(pady=5)  # Menambahkan tombol reset ke jendela dengan padding vertikal

# Label untuk menampilkan hasil prediksi
label_hasil = tk.Label(root, text="", font=("Arial", 12))
label_hasil.pack(pady=10)  # Menambahkan label hasil ke jendela dengan padding vertikal

# Menjalankan aplikasi
root.mainloop()  # Memulai loop utama aplikasi