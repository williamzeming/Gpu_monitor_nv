from tkinter import Tk, Label, LEFT
from pynvml import nvmlInit, nvmlDeviceGetHandleByIndex, nvmlDeviceGetTemperature, nvmlDeviceGetFanSpeed, \
    nvmlDeviceGetPowerUsage, nvmlDeviceGetUtilizationRates, nvmlDeviceGetClockInfo, nvmlDeviceGetMemoryInfo, \
    nvmlDeviceGetTotalEnergyConsumption, nvmlShutdown

root = Tk()
root.geometry('400x230+50+50')
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
    nvmlInit()
    handle = nvmlDeviceGetHandleByIndex(0)
    gpuTemperature = nvmlDeviceGetTemperature(handle, 0)
    temper = "Temperature: " + str(gpuTemperature) + " °C"
    Fan1 = nvmlDeviceGetFanSpeed(handle)
    gpuFan = "GPU Fan: " + str(Fan1) + " %"
    power = "Power usage: " + str(round(nvmlDeviceGetPowerUsage(handle) / 1000, 1)) + " W"
    utilization = nvmlDeviceGetUtilizationRates(handle)
    occ = "GPU Occ: " + str(utilization.gpu) + " %"  # gpu利用率

    clock = nvmlDeviceGetClockInfo(handle, 0)
    clockR = "Clock: " + str(clock) + " MHz"
    memory = nvmlDeviceGetMemoryInfo(handle)
    memoryUsed = "Memroy: " + str(round(memory.used / memory.total * 100, 1)) + "%"
    energy = round(nvmlDeviceGetTotalEnergyConsumption(handle) / 3600000000, 4)
    totEnergy = "Total energy: " + str(energy) + " kWh"
    res = temper + "\n" + gpuFan + "\n" + occ + "\n" + clockR + "\n" + memoryUsed + "\n" + power + "\n" + totEnergy
    lb.config(text=res)

    lb.after(3000, show)


show()

root.mainloop()
