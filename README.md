# 💰 CatatDuit – Aplikasi Pencatatan Keuangan Pribadi

CatatDuit adalah aplikasi web untuk mencatat pemasukan dan pengeluaran harian secara praktis. Aplikasi ini memiliki fitur autentikasi pengguna, manajemen transaksi, kategori keuangan, dan ringkasan grafik.

---

## 📁 Struktur Folder


---

## 🚀 Fitur Utama

- Autentikasi pengguna (Login & Register)
- CRUD Transaksi (Pemasukan & Pengeluaran)
- Kategori transaksi
- Ringkasan bulanan
- Grafik mingguan/bulanan
- Responsive UI/UX

---

## 🛠️ Teknologi yang Digunakan

### Frontend
- React JS
- React Router
- Tailwind CSS
- Axios (untuk komunikasi ke backend)

### Backend
- Python 3
- Pyramid Web Framework
- PostgreSQL
- JSON Web Token (JWT) untuk autentikasi

---

## ⚙️ Cara Menjalankan Aplikasi

### 📦 1. Jalankan Backend
```bash
cd backend
python -m venv env
source env/bin/activate  # atau `env\Scripts\activate` di Windows
pip install -r requirements.txt
pserve development.ini --reload
 2. Jalankan Frontend
bash
Salin
Edit
cd frontend
npm install
npm run dev
