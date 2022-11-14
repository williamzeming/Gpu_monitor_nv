from tkinter import Tk, Label, LEFT
from pynvml import nvmlInit, nvmlDeviceGetHandleByIndex, nvmlDeviceGetTemperature, nvmlDeviceGetFanSpeed, \
    nvmlDeviceGetPowerUsage, nvmlDeviceGetUtilizationRates, nvmlDeviceGetClockInfo, nvmlDeviceGetMemoryInfo, \
    nvmlDeviceGetTotalEnergyConsumption, nvmlShutdown

root = Tk()
root.geometry('400x240+50+50')
root.title("GPU Monitor")

root.attributes("-alpha", 0.8)
root.attributes("-topmost", True)


def closeWindow():
    nvmlShutdown()
    root.destroy()


root.protocol('WM_DELETE_WINDOW', closeWindow)

lb = Label(root, font=("microsoft yahei", 18, "bold"), justify=LEFT, bg='white', fg="black")
lb.pack(anchor="w", fill="both", expand=1)


def show():
    info = []
    nvmlInit()
    handle = nvmlDeviceGetHandleByIndex(0)

    try:
        gpuTemperature = nvmlDeviceGetTemperature(handle, 0)
        temper = "Temperature: " + str(gpuTemperature) + " °C"+ "\n"
        info.append(temper)
    except:
        pass

    try:
        Fan1 = nvmlDeviceGetFanSpeed(handle)
        gpuFan = "GPU Fan: " + str(Fan1) + " %"+ "\n"
        info.append(gpuFan)
    except:
        pass

    try:
        power = "Power usage: " + str(round(nvmlDeviceGetPowerUsage(handle) / 1000, 1)) + " W"+ "\n"
        info.append(power)
    except:
        pass

    try:
        utilization = nvmlDeviceGetUtilizationRates(handle)
        occ = "GPU Occ: " + str(utilization.gpu) + " %"+ "\n"
        info.append(occ)
    except:
        pass

    try:
        clock = nvmlDeviceGetClockInfo(handle, 0)
        clockR = "Clock: " + str(clock) + " MHz"+ "\n"
        info.append(clockR)
    except:
        pass
    try:
        memory = nvmlDeviceGetMemoryInfo(handle)
        memoryUsed = "Memory: " + str(round(memory.used / memory.total * 100, 1)) + "%"+ "\n"
        info.append(memoryUsed)
    except:
        pass
    try:
        energy = round(nvmlDeviceGetTotalEnergyConsumption(handle) / 3600000000, 4)
        totEnergy = "Total energy: " + str(energy) + " kWh"
        info.append(totEnergy)
    except:
        pass

    res = ""
    for i in info:
        res = res + i
    lb.config(text=res)

    lb.after(2000, show)


show()

root.mainloop()
