import tkinter


class PomodoroBrain:

    def __init__(self):
        self.WORK_MIN = 25
        self.SHORT_BREAK_MIN = 5
        self.LONG_BREAK_MIN = 20
        self.cycles = 0

    def next_session(self):
        self.cycles += 1

        if self.cycles % 8 == 0:
            return self.LONG_BREAK_MIN * 60, "long_break"
        elif self.cycles % 2 == 0:
            return self.SHORT_BREAK_MIN * 60, "short_break"
        else:
            return self.WORK_MIN * 60, "work"

    def get_completed_sessions(self):
        return self.cycles // 2

    def reset(self):
        self.cycles = 0


class PomodoroView:

    def __init__(self, controller):
        self.COLORS = {
            "bg": "#f7f5dd",
            "work": "#9bdeac",
            "short_break": "#e2979c",
            "long_break": "#e7305b",
        }
        self.FONT_NAME = "Courier"
        self.controller = controller

        # UI
        self.window = tkinter.Tk()
        self.window.title("Pomodoro Timer")
        self.window.config(
            bg=self.COLORS["bg"],
            padx=100,
            pady=50,
        )

        self.status_title = tkinter.Label(
            text="Timer",
            fg=self.COLORS["work"],
            bg=self.COLORS["bg"],
            font=(self.FONT_NAME, 50),
        )
        self.status_title.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(
            width=200,
            height=224,
            bg=self.COLORS["bg"],
            highlightthickness=0,
        )
        self.tomato_image = tkinter.PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 112, image=self.tomato_image)
        self.timer_text = self.canvas.create_text(
            100,
            130,
            text="00:00",
            fill="white",
            font=(self.FONT_NAME, 35, "bold"),
        )
        self.canvas.grid(column=1, row=1)

        self.start_button = tkinter.Button(
            text="Start",
            font=(self.FONT_NAME, 25),
            command=self.controller.pressed_start,
        )
        self.start_button.grid(column=0, row=2)

        self.reset_button = tkinter.Button(
            text="Reset",
            font=(self.FONT_NAME, 25),
            command=self.controller.pressed_reset,
        )
        self.reset_button.grid(column=2, row=2)

        self.check_marks = tkinter.Label(
            text="",  # ✔
            fg=self.COLORS["work"],
            bg=self.COLORS["bg"],
            font=(self.FONT_NAME, 30),
        )
        self.check_marks.grid(column=1, row=2)

    def update_status_title(self, title_text, title_color):
        self.status_title.config(text=title_text, fg=title_color)

    def update_timer(self, minutes, seconds):
        self.canvas.itemconfig(
            self.timer_text, text=f"{int(minutes):02}:{int(seconds):02}"
        )

    def update_check_marks(self, marks):
        self.check_marks.config(text=marks)

    def reset_timer_ui(self):
        self.update_status_title("Timer", self.COLORS["work"])
        self.update_timer(0, 0)
        self.update_check_marks("")

    def mainloop(self):
        self.window.mainloop()


class PomodoroTimer:

    def __init__(self):
        self.brain = PomodoroBrain()
        self.view = PomodoroView(self)
        self.timer = None

    def countdown(self, duration):
        minutes, seconds = divmod(duration, 60)
        self.view.update_timer(minutes, seconds)

        if duration > 0:
            self.timer = self.view.window.after(1000, self.countdown, duration - 1)
        else:
            self.pressed_start()

    def pressed_start(self):
        duration, status = self.brain.next_session()
        completed_sessions = self.brain.get_completed_sessions()

        self.countdown(duration)

        self.view.update_status_title(
            f"{"Work" if status == "work" else "Break"}", self.view.COLORS[status]
        )

        self.view.update_check_marks(f"{"✔" * completed_sessions}")

    def pressed_reset(self):
        if self.timer:
            self.view.window.after_cancel(self.timer)

        self.brain.reset()
        self.view.reset_timer_ui()

    def run(self):
        self.view.mainloop()


if __name__ == "__main__":
    pomodoro_timer = PomodoroTimer()
    pomodoro_timer.run()
