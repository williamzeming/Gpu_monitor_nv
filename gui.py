from tkinter import *
import pynvml

root = Tk()
root.geometry('400x200+50+50')
root.title("GPU Monitor")

root.attributes("-alpha", 0.8)
root.attributes("-topmost", True)


def closeWindow():
    pynvml.nvmlShutdown()
    root.destroy()


root.protocol('WM_DELETE_WINDOW', closeWindow)

# 设置文本标签
lb = Label(root, font=("微软雅黑", 20, "bold"), justify=LEFT, bg='white', fg="black")
lb.pack(anchor="w", fill="both", expand=1)


#


def showtime():
    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    gpuTemperature = pynvml.nvmlDeviceGetTemperature(handle, 0)
    temper = "Temperature: " + str(gpuTemperature) + " °C"
    Fan1 = pynvml.nvmlDeviceGetFanSpeed(handle)
    gpuFan = "GPU Fan: " + str(Fan1) + " %"
    power = "Power usage: " + str(round(pynvml.nvmlDeviceGetPowerUsage(handle) / 1000, 1)) + " W"
    utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
    occ = "GPU Occ: " + str(utilization.gpu) + " %"  # gpu利用率
    res = temper + "\n" + gpuFan + "\n" + power + "\n" + occ
    lb.config(text=res)
    # 每隔 1秒钟执行time函数
    lb.after(3000, showtime)


showtime()
# 显示窗口

root.mainloop()
