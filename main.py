import pandas as pd
import matplotlib.pyplot as plt

path = "salsabilladheawan.xlsx"

dataraw = pd.read_excel(path, skiprows=7)
dataraw = dataraw.iloc[:, 1:8]
dataraw.columns = ["NIM", "Name", "KUIS", "UTS", "UAS", "Nilai", "Grade"]

print(dataraw)

datafrq = pd.crosstab(index=dataraw["Grade"], columns="Frekuensi")
print("\n=== Tabel Frekuensi ===")
print(datafrq)

plt.style.use('ggplot')
plt.figure(figsize=(8, 5))
plt.plot(datafrq.index, datafrq['Frekuensi'], marker='s', color='#2ca02c', linewidth=2.5, linestyle='--')
plt.title('Grafik Garis: Frekuensi Grade Mahasiswa', fontsize=14, fontweight='bold')
plt.xlabel('Grade', fontsize=12)
plt.ylabel('Frekuensi', fontsize=12)
plt.show()


plt.figure(figsize=(8, 5))
colors_bar = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
bars = plt.bar(datafrq.index, datafrq['Frekuensi'], color=colors_bar, edgecolor='black')
plt.title('Grafik Batang: Frekuensi Grade Mahasiswa', fontsize=14, fontweight='bold')
plt.xlabel('Grade', fontsize=12)
plt.ylabel('Frekuensi', fontsize=12)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.3, int(yval), ha='center', va='bottom', fontweight='bold')
plt.show()

plt.figure(figsize=(7, 7))
explode = (0.05, 0, 0, 0, 0, 0) 
plt.pie(datafrq['Frekuensi'], labels=datafrq.index, autopct='%1.1f%%', startangle=90, 
        colors=colors_bar, explode=explode, shadow=True)
plt.title('Pie Chart: Persentase Grade Mahasiswa', fontsize=14, fontweight='bold')
plt.show()


dataraw["Nilai"] = pd.to_numeric(dataraw["Nilai"], errors='coerce')
dt = dataraw["Nilai"]

stats = dt.describe()
stats['Standard Error'] = dt.sem()
stats['Median'] = dt.median()
stats['Mode'] = dt.mode().iloc[0]
stats['variance'] = dt.var()
stats['range'] = dt.max() - dt.min()
stats['skewness'] = dt.skew()
stats['kurtosis'] = dt.kurtosis()

print("\n=== Hasil Statistika Deskriptif ===")
print(stats.round(3))