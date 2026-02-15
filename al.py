import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# نفتح الملف حق البيانات
data = pd.read_csv("sales_data.csv", encoding="latin1")
# نشيل الصفوف الفاضيه لو في
 data_clean = data.dropna()

# # نحول التواريخ عشان نستخدمها
 data_clean['Order Date'] = pd.to_datetime(data_clean['Order Date'], format='%m/%d/%Y')

# # 1. المبيعات لكل فئة Category
 مبيعات_الفئات = data_clean.groupby('Category')['Sales'].sum()
 print("المبيعات لكل فئة:")
 print(مبيعات_الفئات)


# # 2. الارباح لكل منطقة Region
 ارباح_المناطق = data_clean.groupby('Region')['Profit'].sum()
 print("الارباح لكل منطقة:")
 print(ارباح_المناطق)

# # 3. متوسط الارباح لكل منطقة
 متوسط_الارباح = data_clean.groupby('Region')['Profit'].mean()
 print("متوسط الارباح لكل منطقة:")
 print(متوسط_الارباح)

# # 4. ترتيب الزباين حسب مشترياتهم
 مشتريات_الزبون = data_clean.groupby('Customer ID')['Sales'].sum()
 فئات_الزبائن = pd.qcut(مشتريات_الزبون, 4, labels=['قليل', 'وسط', 'حلو', 'ممتاز'])
 print("الزبائن كيف توزعوا:")
 print(فئات_الزبائن.value_counts())


# # 5. العلاقه بين الكميه Quantity والربح Profit
 print("العلاقه بين الكميه والربح:")
 print(f"متوسط الكميه: {data_clean['Quantity'].mean():.2f}")
 print(f"الانحراف حق الكميه: {data_clean['Quantity'].std():.2f}")
 print(f"متوسط الربح: {data_clean['Profit'].mean():.2f}")
 print(f"الانحراف حق الربح: {data_clean['Profit'].std():.2f}")

 ارتباط = data_clean['Quantity'].corr(data_clean['Profit'])
 print(f"معامل الارتباط: {ارتباط:.3f}")

# # 6. اداء الفروع Segment
 أداء_الفروع = data_clean.groupby('Segment').agg({
     'Sales': ['sum', 'mean', 'std'],
     'Profit': ['sum', 'mean', 'std']
 })
 print("اداء الفروع:")
 print(أداء_الفروع)

# # نبدأ نرسم الرسومات

# # الرسم 1: بار شارت للمبيعات حسب الفئة
 plt.figure()
 مبيعات_الفئات.plot(kind='bar')
 plt.title('المبيعات حسب الفئة')
 plt.xlabel('الفئة')
 plt.ylabel('المبيعات')
 plt.tight_layout()
 plt.savefig('رسم1_مبيعات_فئة.png')
 plt.close()

# # الرسم 2: باي شارت للارباح حسب المنطقة
 plt.figure()
 ارباح_المناطق.plot(kind='pie', autopct='%1.1f%%')
 plt.title('الارباح حسب المنطقة')
 plt.ylabel('')
 plt.tight_layout()
 plt.savefig('رسم2_ارباح_منطقة.png')
 plt.close()

# # الرسم 3: سكاتر بلوت للعلاقه بين الكميه والربح
 plt.figure()
 plt.scatter(data_clean['Quantity'], data_clean['Profit'])
 plt.title('العلاقة بين الكمية والربح')
 plt.xlabel('الكمية')
 plt.ylabel('الربح')
 plt.tight_layout()
 plt.savefig('رسم3_كمية_ربح.png')
 plt.close()

# # الرسم 4: لاين شارت للارباح مع الوقت
 ارباح_شهرية = data_clean.groupby(data_clean['Order Date'].dt.to_period('M'))['Profit'].sum()
 plt.figure()
 ارباح_شهرية.plot(kind='line', marker='o')
 plt.title('الارباح الشهرية')
 plt.xlabel('الشهر')
 plt.ylabel('الربح')
 plt.tight_layout()
 plt.savefig('رسم4_ارباح_زمن.png')
 plt.close()

# # الرسم 5: بار شارت  حسب الفروع
 plt.figure()
 أداء_الفروع['Sales']['sum'].plot(kind='bar')
 plt.title('المبيعات حق الفروع')
 plt.xlabel('الفرع')
 plt.ylabel('المبيعات')
 plt.tight_layout()
 plt.savefig(' فروع 5.png')
 plt.close()

 print((مبيعات_الفئات)))



x=dp.('Category')



















