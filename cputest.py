# CPU实时监控
# 作者：木子君羡
# import matplotlib
# matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import psutil as p

POINTS = 300
fig, ax = plt.subplots()
ax.set_ylim([0, 100])
ax.set_xlim([0, POINTS])
ax.set_autoscale_on(False)
ax.set_xticks([])
ax.set_yticks(range(0, 101, 10))
ax.grid(True)
# 执行用户进程的时间百分比
user = [None] * POINTS
# 执行内核进程和中断的时间百分比
sys = [None] * POINTS
# CPU处于空闲状态的时间百分比
idle = [None] * POINTS
l_user, = ax.plot(range(POINTS), user, label='User %')
l_sys, = ax.plot(range(POINTS), sys, label='Sys %')
l_idle, = ax.plot(range(POINTS), idle, label='Idle %')
ax.legend(loc='upper center', ncol=4, prop=font_manager.FontProperties(size=10))
bg = fig.canvas.copy_from_bbox(ax.bbox)

def cpu_usage():
    t = p.cpu_times()
    return [t.user, t.system, t.idle]

before = cpu_usage()

def get_cpu_usage():
    global before
    now = cpu_usage()
    delta = [now[i] - before[i] for i in range(len(now))]
    total = sum(delta)
    before = now
    return [(100.0*dt)/(total+0.1) for dt in delta]

def OnTimer(ax):
    global user, sys, idle, bg
    tmp = get_cpu_usage()
    user = user[1:] + [tmp[0]]
    sys = sys[1:] + [tmp[1]]
    idle = idle[1:] + [tmp[2]]
    l_user.set_ydata(user)
    l_sys.set_ydata(sys)
    l_idle.set_ydata(idle)
    while True:
        try:
            ax.draw_artist(l_user)
            ax.draw_artist(l_sys)
            ax.draw_artist(l_idle)
            break
        except:
            pass
    ax.figure.canvas.draw()

def start_monitor():
    timer = fig.canvas.new_timer(interval=100)
    timer.add_callback(OnTimer, ax)
    timer.start()
    plt.show()
    plt.savefig("a.png")

if __name__ == '__main__':
    start_monitor()