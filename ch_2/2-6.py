# %% chart demo
import matplotlib.pyplot as plt # 匯入繪圖模組

font = {"family": "Apple LiGothic"} # 設定中文字型

plt.rc("font", **font) # 全域套用字型設定
# %% chart demo
import matplotlib.pyplot as plt # 匯入繪圖模組

listX = [2015, 2016, 2019, 2023]
listY = [50000, 10000, 20000, 100000]
# 繪製listX與listY的折線圖，設定顏色、線寬、線型、標籤、標記形狀及大小
plt.plot(listX, listY, color="r", lw=4, ls="--", label="銷售業績", marker="s", ms=6)
plt.legend() # 顯示圖例
plt.show() # 顯示圖表

# %% chart demo
font = {"family": "Apple LiGothic"} # 設定中文字型

plt.rc("font", **font) # 全域套用字型設定

listX = [2014, 2017, 2019]
listY = [0, 50000, 100000]

# 繪製listX與listY的折線圖，設定顏色、線寬、線型、標籤、標記形狀及大小
plt.plot(listX, listY, color="b", lw=2, ls="-.", label="歷年銷售量", marker="*", ms=8)
plt.legend() # 顯示圖例
plt.show() # 顯示圖表