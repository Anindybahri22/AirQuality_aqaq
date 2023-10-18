import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import datetime 
sns.set(style='dark')
#Data Source
airquality_df = pd.read_csv ('PRSA_Data_Gucheng_20130301-20170228.csv')
#Data Cleaning
airquality_df=airquality_df.fillna(method='bfill').fillna(method='ffill')
airquality_df['datetime'] = airquality_df['year'].astype(str) + '-' + airquality_df['month'].astype(str) + '-' + airquality_df['day'].astype(str) + ' ' + airquality_df['hour'].astype(str) + ':00:00'
column_to_move = airquality_df.pop('datetime')
airquality_df.insert(1,'datetime', column_to_move)
airquality_df['datetime'] = pd.to_datetime(airquality_df['datetime'])
drop_feature = ['No', 'year', 'month', 'day','hour', 'station']
airquality_df.drop(drop_feature, axis=1, inplace=True)

st.markdown(
    """
    # Air Quality Dashboard
    - Nama : Anindy Bahri
    - Email: anindibahri22@gmail.com
    - Id Dicoding: anindy_bahri_tnne
    ---
    """
)
with st.sidebar:
    # Menambahkan logo awan
    st.image("awan3.png")
    # Menambahkan Periode Tahun
    st.text('Rentang Waktu')
    date_observation = pd.to_datetime(st.date_input(
        label='Pilih Tanggal',
        min_value=datetime.date(2013, 3, 1),
        max_value=datetime.date(2017, 2, 28),
        value=datetime.date(2013, 3, 1)
    ))
start_date = pd.to_datetime(date_observation.strftime('%Y-%m-%d') + ' 0:00:00')
end_date = pd.to_datetime(date_observation.strftime('%Y-%m-%d') + ' 23:00:00')
airquality_daily = airquality_df[(airquality_df['datetime'] >= start_date) & (airquality_df['datetime'] <= end_date)]
#airquality_daily = airquality_df[(airquality_df['datetime'] >= start_date) & (airquality_df['datetime'] <= end_date)]
st.header('Air Quality')
st.write(start_date)
st.write(end_date)
st.write(start_date.strftime('%d %B %Y'))
col1, col2, col3, col4, col5, col6 = st.columns(6)
#st.write(airquality_daily)
#st.write(airquality_df)

with col1:
    st.header(airquality_daily['PM2.5'].mean().round(2))
    st.write(f'(µg/m³) PM2.5')
with col2:
    st.header(airquality_daily['PM10'].mean().round(2))
    st.write(f'(µg/m³) PM10')
with col3:
    st.header(airquality_daily['SO2'].mean().round(2))
    st.write(f'(µg/m³) SO2')
col1, col2, col3 = st.columns(3)
with col1:
    st.header(airquality_daily['NO2'].mean().round(2))
    st.write(f'(µg/m³) NO2')
with col2:
    st.header(airquality_daily['CO'].mean().round(2))
    st.write(f'(µg/m³) CO')
with col3:
    st.header(airquality_daily['O3'].mean().round(2))
    st.write(f'(µg/m³) O3')
#st.write(type(airquality_daily))

#print(type(airquality_daily))    
tab_pm25, tab_pm10, tab_so2, tab_no2, tab_co, tab_o3, tab_temp, tab_press, tab_dew, tab_rain = st.tabs(['PM2.5','PM10','SO2', 'NO2', 'CO', 'O3', 'Temperature','Preassure', 'Dew Point','Rain'])
with tab_pm25:
    st.line_chart(data=airquality_daily, x='datetime', y="PM2.5", use_container_width=True)
with tab_pm10:
    st.line_chart(data=airquality_daily, x='datetime', y="PM10", color='#ffaa0088', use_container_width=True)
with tab_so2:
    st.line_chart(data=airquality_daily, x='datetime', y="SO2", color='#ffaa0088', use_container_width=True)
with tab_no2:
    st.line_chart(data=airquality_daily, x='datetime', y="NO2", color='#ffaa0088', use_container_width=True)
with tab_co:
    st.line_chart(data=airquality_daily, x='datetime', y="CO", color='#ffaa0088', use_container_width=True)
with tab_o3:
    st.line_chart(data=airquality_daily, x='datetime', y="O3", color='#ffaa0088', use_container_width=True)
with tab_temp:
    st.line_chart(data=airquality_daily, x='datetime', y="TEMP", color='#ffaa0088', use_container_width=True)
with tab_press:
    st.line_chart(data=airquality_daily, x='datetime', y="PRES", color='#ffaa0088', use_container_width=True)
with tab_dew:
    st.line_chart(data=airquality_daily, x='datetime', y="DEWP", color='#ffaa0088', use_container_width=True)
with tab_rain:
    st.line_chart(data=airquality_daily, x='datetime', y="RAIN", color='#ffaa0088', use_container_width=True)