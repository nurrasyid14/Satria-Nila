# Dataset Documentation - Satria-Nila

Folder ini berisi dataset untuk melatih dan mengevaluasi model Machine Learning pada proyek **SATRIA**. Dataset diatur berdasarkan dua konteks operasional yang berbeda:
1. **Water Suitability Assessment**: Menggunakan dataset `Refined_...` untuk melakukan penilaian titik waktu (*snapshot assessment*) terhadap kelayakan air.
2. **Environmental Monitoring**: Menggunakan dataset `AQUAIR` untuk pemantauan berkelanjutan (*continuous monitoring*) terhadap kualitas udara di fasilitas *hatchery*(pembenihan).

---

## 1. Refined Aquaculture Water Suitability Signals
**File:** `Refined_Aquaculture_Water_Suitability_Signals.csv`

### Deskripsi Umum
Dataset ini adalah dataset turunan (refined) yang dirancang khusus untuk klasifikasi tingkat kelayakan air dalam budidaya perikanan, khususnya untuk ikan air tawar seperti Nila (Tilapia). Dataset ini mencakup berbagai parameter fisikokimia dan biologis air.

### Sumber & Konteks
*   **Sumber:** [Kaggle - Refined Aquaculture Water Suitability Signals](https://www.kaggle.com/datasets/sandhyapalaniappan/refined-aquaculture-water-suitability-signals)
*   **Jenis Ikan:** Ikan air tawar, khususnya **Ikan Nila (Tilapia)**.
*   **Latar Belakang:** Digunakan untuk Fase 1 proyek SATRIA yaitu **Water Suitability Assessment**.

### Daftar Fitur (Kolom)
Dataset ini memiliki 17 kolom, yang terdiri dari:

| Fitur | Deskripsi | Satuan |
| :--- | :--- | :--- |
| **Temperature** | Suhu air kolam | °C |
| **Turbidity (cm)** | Tingkat kekeruhan air | cm |
| **Dissolved Oxygen (mg/L)** | Oksigen terlarut dalam air | mg/L |
| **Biochemical Oxygen Demand (mg/L)** | Kebutuhan oksigen biologis | mg/L |
| **Carbon Dioxide (CO2)** | Kandungan Karbon Dioksida | mg/L |
| **pH** | Tingkat keasaman air | 0 - 14 |
| **Total Alkalinity (mg L-1)** | Kapasitas penetralan asam | mg/L |
| **Total Hardness (mg L-1)** | Kandungan mineral (kalsium/magnesium) | mg/L |
| **Calcium (mg L-1)** | Kandungan kalsium spesifik | mg/L |
| **Ammonia (mg L-1)** | Kadar Amonia (beracun bagi ikan) | mg/L |
| **Nitrite (mg L-1)** | Kadar Nitrit | mg/L |
| **Phosphorus (mg L-1)** | Kadar Fosfor | mg/L |
| **Hydrogen Sulfide (mg L-1)** | Kadar Gas H2S | mg/L |
| **Plankton Count (No. L-1)** | Jumlah plankton per liter | No./L |
| **Water Quality Label** | Label kualitas (Reduced/Moderate/Optimal) | - |
| **Suitability Tier** | Kelas kelayakan (0/1/2) | - |
| **Description** | Penjelasan tekstual mengenai kondisi air | - |

---

## 2. AQUAIR: Indoor Environmental Quality Dataset
**Direktori:** `data/Aquair/`
**File:** `AQUAIR_1.csv`, `AQUAIR_2.csv`

### Deskripsi Umum
AQUAIR adalah dataset kualitas udara dalam ruangan (Indoor Environmental Quality - IEQ) beresolusi tinggi yang dikumpulkan khusus untuk pemantauan akuakultur pintar. Dataset ini bersifat *time-series* dengan pengambilan data setiap 5 menit.

### Sumber & Konteks
*   **Sumber:** [Figshare - AQUAIR Dataset](https://figshare.com/articles/dataset/AQUAIR_Dataset/28934375) | [ArXiv Paper](https://arxiv.org/abs/2509.24069)
*   **Jenis Ikan:** Ikan **Trout** (*Oncorhynchus mykiss*).
*   **Lokasi Pengambilan:** Fasilitas hatchery (pembenihan) ikan di Amghass, Azrou, Maroko.
*   **Rentang Waktu:** 14 Oktober 2024 hingga 9 Januari 2025.
*   **Tujuan:** Digunakan untuk Fase 2 proyek SATRIA yaitu **Environmental Monitoring** dan prediksi anomali udara yang dapat mempengaruhi kondisi air.

### Daftar Fitur (Kolom)
| Fitur | Deskripsi | Satuan |
| :--- | :--- | :--- |
| **timestamp(UTC)** | Waktu perekaman data (zona waktu UTC) | YYYY-MM-DD HH:MM:SS |
| **score** | Skor kualitas udara keseluruhan (indeks internal) | 0 - 100 |
| **temp** | Suhu udara di dalam ruangan | °C |
| **humid** | Kelembapan relatif udara | % RH |
| **co2** | Konsentrasi Karbon Dioksida | ppm |
| **voc** | *Total Volatile Organic Compounds* | ppb |
| **pm25** | Partikulat halus berukuran ≤ 2.5 µm | µg/m³ |
| **pm10** | Partikulat terhirup berukuran ≤ 10 µm | µg/m³ |

---

## Ringkasan Penggunaan dalam Proyek
1.  **Water Quality Model:** Menggunakan dataset `Refined_...` untuk melatih model klasifikasi guna menentukan apakah air dalam kondisi *Optimal*, *Moderate*, atau *Reduced*.
2.  **Air Quality Model (Future):** Menggunakan dataset `AQUAIR` untuk melakukan peramalan (*forecasting*) polutan udara yang dapat menjadi indikator awal sebelum kualitas air memburuk.
