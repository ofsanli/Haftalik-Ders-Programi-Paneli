# 📖 Haftalık Ders Programı Paneli

Okullardaki öğretmenler, dersler, sınıflar ve özel derslikler arasındaki çakışmaları otomatik engelleyerek haftalık ders programı oluşturan ve yöneten web tabanlı okul yönetim sistemi.

---

## ✨ Öne Çıkan Özellikler

- 👨‍🏫 **Öğretmen Yönetimi**: Öğretmen branşı, haftalık maksimum ders saati limiti ve gelinemeyen gün/saat kısıtlamaları.
- 📚 **Ders Müfredatı**: Sınıflara göre tekli ve çiftli ders blokları atama.
- 🏫 **Derslik Tahsisi**: Spor Salonu, Resim Atölyesi, Müzik Odası, Fen Laboratuvarı ve Satranç Sınıfı için otomatik boş derslik rezervasyonu.
- 🧠 **Sezgisel Çakışma Önleyici Motor (Heuristic Motor)**: Öğretmen, sınıf ve derslik çakışması olmadan sıfır hata ile haftalık ders programı oluşturur.
- 🎨 **Ders Renk Kodlaması**: Her ders için özel pastel renkler ve vurgular ile 1 saniyede okunabilir haftalık program tablosu.
- 📊 **PDF & Excel Çıktısı**: A4 Yatay Türkçe karakter destekli PDF ve şık başlık bantlı Excel (.xlsx) indirme desteği.

---

## 🛠️ Kullanılan Teknolojiler

- **Backend**: Python 3.11, FastAPI, Uvicorn
- **Veritabanı**: SQLite 3 (WAL Modu & Foreign Key kısıtlamaları)
- **Frontend**: HTML5, CSS3 (Flexbox & CSS Grid), Vanilla JavaScript (ES6+)
- **Raporlama**: ReportLab (PDF), OpenPyXL (Excel)

---

## 🚀 Kurulum ve Çalıştırma

### Yöntem 1: Tek Tıkla Başlatma (Windows)
Klasör içinde yer alan **`run.bat`** dosyasına çift tıklayın. Otomatik olarak sanal ortamı aktif eder, uvicorn sunucusunu başlatır ve varsayılan tarayıcınızı açar.

### Yöntem 2: Manuel Başlatma

1. Sanal ortam oluşturun ve aktif edin:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate   # Windows
   ```

2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

3. Sunucuyu başlatın:
   ```bash
   uvicorn main:app --reload
   ```

4. Tarayıcınızda açın:
   - **Özet Ekran**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - **Yönetim Paneli**: [http://127.0.0.1:8000/panel](http://127.0.0.1:8000/panel)
   - **Swagger API Dokümanı**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
