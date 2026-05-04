# Laporan Praktikum Analisis Data Penjualan (ECOMMERCE)

## 1. Business Question

Tujuan dari analisis ini adalah menjawab beberapa pertanyaan bisnis berikut:

* Produk apa yang termasuk **underperformer** (harga tinggi tapi jarang terjual)?
* Bagaimana cara mengelompokkan pelanggan berdasarkan perilaku belanja (**RFM Analysis**)?
* Kategori produk mana yang paling efisien dalam menghasilkan penjualan?
* Apakah peningkatan promosi berpengaruh terhadap total penjualan?


## 2. Data Wrangling

Tahapan pembersihan dan persiapan data yang dilakukan:

* Mengubah tipe data `OrderDate` menjadi format datetime
* Membuat kolom baru seperti `Month` untuk analisis tren
* Mengecek dan memastikan tidak ada nilai kosong (missing values)
* Menyesuaikan nama kolom dengan dataset (misalnya `TotalAmount` вместо `Total_Sales`)
* Karena tidak tersedia:

  * `CustomerID` → diganti menggunakan `City`
  * `Ad_Budget` → menggunakan `Reviews` sebagai pendekatan promosi


## 3. Insights

### a. Underperformer Product (Scatter Plot)

* Produk dengan harga di atas rata-rata cenderung memiliki jumlah penjualan lebih rendah
* Hal ini menunjukkan kemungkinan harga terlalu tinggi sehingga menghambat pembelian


### b. RFM Analysis (Segmentasi)

* Kota dengan skor **Recency rendah, Frequency tinggi, dan Monetary tinggi** merupakan segmen terbaik
* Segmen ini berpotensi menjadi pelanggan loyal


### c. Efisiensi Kategori (Bar Chart)

* Beberapa kategori menghasilkan penjualan tinggi dengan jumlah review rendah → **lebih efisien**
* Kategori lain memiliki banyak review tetapi penjualan rendah → **kurang efisien**


### d. Uji Hipotesis (Promosi vs Penjualan)

* Data menunjukkan bahwa kelompok dengan tingkat promosi lebih tinggi memiliki rata-rata penjualan yang lebih besar
* Namun, perbedaan ini belum tentu signifikan secara statistik


## 4. Recommendation

Berdasarkan hasil analisis, berikut rekomendasi untuk perusahaan:

* **Evaluasi harga produk mahal** yang memiliki penjualan rendah
* **Fokus pada pelanggan loyal** (hasil RFM) dengan memberikan voucher atau promo khusus
* **Optimalkan strategi pemasaran** pada kategori yang kurang efisien
* **Tingkatkan promosi secara terarah**, bukan hanya memperbesar budget tanpa strategi


## 5. Keterbatasan Analisis

* Tidak tersedia data `CustomerID`, sehingga segmentasi menggunakan pendekatan `City`
* Tidak tersedia `Ad_Budget`, sehingga digunakan `Reviews` sebagai indikator promosi
* Hasil analisis masih bersifat eksploratif dan dapat ditingkatkan dengan data yang lebih lengkap


## Tools yang Digunakan

* Python
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn


## Penutup

Analisis ini memberikan gambaran awal terkait performa produk, perilaku pelanggan, dan efektivitas strategi pemasaran. Dengan data yang lebih lengkap, hasil analisis dapat menjadi lebih akurat dan mendalam.
