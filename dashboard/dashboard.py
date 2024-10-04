import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df_day = pd.read_csv('bike_sharing_daily.csv')
df_hour = pd.read_csv('bike_sharing_hourly.csv')

st.title('Bike Sharing Analysis Dashboard')

# Plot 1: Total rental tiap jam
st.header('Pertanyaan 1: Pada jam berapa sepeda paling sering disewa?')
st.subheader('Total Rental tiap jamnya (selang 2 tahun)')
total_rent_each_hour = df_hour.groupby('hr').agg({'cnt': 'sum'})
fig1, ax1 = plt.subplots()
sns.barplot(x=total_rent_each_hour.index, y=total_rent_each_hour['cnt'], ax=ax1)
ax1.set_ylabel('Total Rental')
ax1.set_xlabel('Pukul')
ax1.set_title('Total Rental tiap jamnya  selama 2 tahun')
st.pyplot(fig1)

# Plot 2: Top 5 jam dengan total rental tertinggi
st.subheader('Top 5 jam dengan total rental tertinggi')
top_5_hours = total_rent_each_hour.sort_values('cnt', ascending=False).head()
fig2, ax2 = plt.subplots()
sns.barplot(x=top_5_hours.index, y=top_5_hours['cnt'], ax=ax2)
ax2.set_ylabel('Total Rental')
ax2.set_xlabel('Pukul')
ax2.set_title('5 Total Rental tertinggi tiap jamnya  selama 2 tahun')
st.pyplot(fig2)

st.text("Berdasarkan data yang ditampilkan para penyewa lebih suka menyewa\n" +
        "pada jam 5 sore yang dimana rentang penyewaan favorit adalah\n" +
        "pukul 4 sore hingga pukul 7 malam dan pukul 8 pagi\n" +
        "dengan data sebagai berikut :\n" +
            "1. pukul 17.00 = 336860 penyewaan\n" +
            "2. pukul 18.00 = 309772 penyewaan\n" +
            "3. pukul 8.00 = 261001 penyewaan\n" +
            "4. pukul 16.00 = 227748 penyewaan\n" +
            "5. pukul 19.00 = 226789 penyewaan\n\n" +

        "Dapat disimpulkan penyewa lebih suka menyewa sepeda pada sore hari\n"+
        "dan pagi hari pukul 8")

# Plot 3: Pie chart registered vs casual
st.header('Pertanyaan 2: Seberapa nyaman penyewa untuk melakukan registrasi?')
st.subheader('Penyewa Teregristrasi vs Casual/non-registrasi')
colors = ['#00a1f7', '#d1250f']
fig3, ax3 = plt.subplots()
ax3.pie(
    [df_day['registered'].sum(), df_day['casual'].sum()],
    labels=['Registered', 'Casual'],
    autopct='%1.1f%%',
    colors=colors,
    explode=(0.1, 0)
)
ax3.set_title('Teregristrasi vs Casual/non-registrasi')
st.pyplot(fig3)
st.text("Berdasarkan data yang ditampilkan dapat disimpulkan bahwa sebanyak 81,2% penyewa\n" +
        "nyaman untuk melakukan registrasi dengan 18,8% sisanya tidak cukup nyaman untuk\n" +
        "melakukan registrasi sebelum menyewa")

st.subheader('Insight :')
st.text("- dihasilkan bahwa penyewa paling banyak memilih pukul 5 sore untuk menyewa sepeda\n" +
"- dapat dilihat juga bahwa 81,2% jumlah penyewaan dilakukan oleh penyewa yang telah teregristrasi")

st.header("Kesimpulan")
st.text("- Sebagian besar penyewa lebih suka untuk melakukan penyewaan di sore hari\n"+
        "  dari pukul 4 hingga 7 malam dan pagi hari pukul 8 dengan puncak penyewaan\n"+
        "  pada pukul 5 dan sedikitnya penyewa terendah pada tengah malam pukul 12\n"+
        "  hingga pukul 5 dini hari\n" +
        "- dari total penyewaan berkisar 3.292.679 sewa sebanyak 81,2% penyewaan\n"+
        "  dilakukan oleh penyewa yang telah teregristrasi\n"+
        "  dibandingkan dengan 18,8% penyewaan yang dilakukan oleh secara casual\n"+
        "  atau belum teregristrasi.\n"+
        "  Hal ini mengindikasikan bahwa penyewa lebih banyak yang merasa cukup nyaman\n"+
        "  meregristasikan dirinya dalam penyewaan dibandingkan yang casual")
