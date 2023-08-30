import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("时间到！")

if __name__ == "__main__":
    focus_minutes = int(input("请输入专注时长（分钟）：30"))
    focus_timer(focus_minutes)
