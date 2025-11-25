import math

print("\n計算BMI值")
height=float(input("請輸入你的身高(公尺): "))  # 取得身高輸入
weight=float(input("請輸入你的體重(公斤): "))  # 取得體重輸入
bmi=weight/(height**2)  # BMI計算公式
print(f"\n你的BMI值為{round(bmi,2)}")

print("\n\n計算攝氏溫度轉華氏溫度")
tempC=float(input("請輸入攝氏溫度: "))  # 取得攝氏溫度
tempF=tempC * 9.0/5.0 + 32.0  # 攝氏轉華氏公式
print(f"\n攝氏溫度{tempC:.2f}度=華氏溫度{tempF:.2f}度")

print("\n\n計算直角三角形 面積及斜邊長")
shortEdge=float(input("請輸入直角三角形短的邊長: "))  # 短邊
longEdge=float(input("請輸入直角三角形長的邊長: "))   # 長邊
slopeEdge=math.sqrt(shortEdge**2 + longEdge**2)  # 畢氏定理求斜邊
area=shortEdge * longEdge / 2  # 三角形面積公式
print(f"\n此直角三角形的斜邊長為{slopeEdge:.2f}")
print(f"此直角三角形的面積為{area:.2f}")