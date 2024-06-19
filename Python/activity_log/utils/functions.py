from datetime import datetime


def check(widget):
    if widget.get() == '':
        widget.config(
            border_color = 'red'
        )
        return False
    return True



def days_count(start_date, end_date):
    start_date = datetime.strptime(start_date, "%m/%d/%Y").date()
    end_date = datetime.strptime(end_date, "%m/%d/%Y").date()
    return (end_date - start_date).days

def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

if __name__ == "__main__":
    print("Hello World!")