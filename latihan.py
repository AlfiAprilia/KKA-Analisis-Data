#Library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilai_siswa.csv') #Baca dataset
data.info() #menampilkan informasi data set
data.head() #menampilkan 5 data pertama
data.describe() #menampilkan statistik deskriptif dari dataset

#menghitung rata-rata, median, dan modus 
print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

#menampilkan nilai per matapelajaran
matematika = data[data['Matpel'] == 'Matematika']
print(matematika)
BahasaIndonesia = data[data['Matpel'] == 'Bahasa Indonesia']
print(BahasaIndonesia)
BahasaInggris = data[data['Matpel'] == 'Bahasa Inggris']
print(BahasaInggris)
Fisika = data[data['Matpel'] == 'Fisika']
print(Fisika)
Produktif = data[data['Matpel'] == 'Produktif']
print(Produktif)

#menampilkan nilai maximum dan minimum
data.groupby('Matpel') ['Nilai'].agg(['max','min'])

#membuat grafik batang rata-rata nilai per mapel
rata = data.groupby('Matpel') ['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai Rapor Per Matpel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

#membuat diagram boxplot
sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai Per Mata Pelajaran')
plt.show()