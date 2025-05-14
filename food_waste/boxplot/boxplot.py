# Kütüphaneleri import ettim.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setimi çağırdım.
data = pd.read_csv('Data.csv')

# Tedarik zinciri aşamalarını Türkçeye çevirdim.
translation = {
    "Pre-harvest": "Hasat Öncesi",
    "Harvest": "Hasat",
    "Post-harvest": "Hasat Sonrası",
    "Farm": "Çiftlik",
    "Grading": "Sınıflandırma",
    "Storage": "Depolama",
    "Transport": "Taşıma",
    "Trader": "Tüccar",
    "Processing": "İşleme",
    "Packing": "Paketleme",
    "Distribution": "Dağıtım",
    "Market": "Pazar",
    "Wholesale": "Toptan Satış",
    "Retail": "Perakende",
    "Food Services": "Yiyecek Hizmetleri",
    "Households": "Hanehalkı",
    "Export": "İhracat",
    "Whole supply chain": "Tüm Tedarik Zinciri"
}

# İngilizce kelimeleri Türkçeleri ile değiştirdim.
data['food_supply_stage_tr'] = data['food_supply_stage'].map(translation)

# Son 10 yıl verisini getirdim.
max_year = data['year'].max()
last_10_years = data[data['year'] >= (max_year - 9)]

# Grafik çizimi
plt.figure(figsize=(14, 10))

# Boxplot
sns.boxplot(
    x='loss_percentage',
    y='food_supply_stage_tr',
    data=last_10_years,
    palette='tab20',
    showfliers=False
)

# Scatter plot
sns.stripplot(
    x='loss_percentage',
    y='food_supply_stage_tr',
    data=last_10_years,
    hue='food_supply_stage_tr',
    palette='tab20',
    dodge=False,
    size=3,
    alpha=0.7,
    jitter=True
)

# Başlık ve etiketler
plt.title(f'Son 10 Yılda ({max_year-9}-{max_year}) Tedarik Zinciri Aşamalarına Göre Gıda Kayıp Yüzdesi Dağılımı', fontsize=18)
plt.xlabel('Kayıp Yüzdesi (%)', fontsize=14)
plt.ylabel('Tedarik Zinciri Aşaması', fontsize=14)
plt.xlim(0, 60)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Türkçe legend
plt.legend(
    title='Tedarik Zinciri Aşaması',
    bbox_to_anchor=(1.05, 1),
    loc='upper left'
)

plt.tight_layout()
plt.show()
