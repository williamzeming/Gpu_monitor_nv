import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import psutil


p = psutil.Process(pid=pid)
p.cpu_percent(interval=None)
for i in range(100):
    usage = p.cpu_percent(interval=None)
    # do other things