from tkinter import *
import pynvml
from time import strftime
root = Tk()
root.geometry('500x350+300+300')
# root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
root.title("C语言中文网出品")
# 设置文本标签
lb = Label(root, font=("微软雅黑", 50, "bold"), bg='#87CEEB', fg="#B452CD")
lb.pack(anchor="center", fill="both", expand=1)

def showtime():
    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    gpuTemperature = pynvml.nvmlDeviceGetTemperature(handle, 0)
    temper = "GPU: " + str(gpuTemperature)
    Fan1 = pynvml.nvmlDeviceGetFanSpeed(handle)
    gpuFan = "GPUFan: " + str(Fan1)
    power = "Power usage" + str(pynvml.nvmlDeviceGetPowerUsage(handle) / 1000)
    utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
    occ = "GPUOcc:" + str(utilization.gpu)  # gpu利用率
    res = temper + "\n" + gpuFan + "\n" + power + "\n" + occ
    lb.config(text=res)
    # 每隔 1秒钟执行time函数
    lb.after(1000, showtime)
# 定义鼠标处理事件，点击时间切换为日期样式显示
# def mouseClick(event):
#     global mode
#     if mode == 'time':
#         # 点击切换mode样式为日期样式
#         mode = 'date'
#     else:
#         mode = 'time'
# lb.bind("<Button>", mouseClick)
# 调用showtime()函数
showtime()
# 显示窗口
mainloop()