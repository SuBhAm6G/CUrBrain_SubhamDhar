import tkinter as tk
from tkinter import font


def main():
	root = tk.Tk()
	root.title("SUBHAM DHAR")
	root.configure(bg="black")

	canvas = tk.Canvas(root, width=1100, height=300, bg="black", highlightthickness=0)
	canvas.pack(padx=20, pady=20)

	text = "SUBHAM DHAR"
	colors = ["#ff1744", "#ff9100", "#ffee00", "#00e676", "#00b0ff", "#7c4dff"]
	x = 550
	y = 150
	headline_font = ("Arial", 64, "bold")

	font_obj = font.Font(font=headline_font)
	total_width = font_obj.measure(text)
	current_x = x - total_width / 2
	for index, letter in enumerate(text):
		canvas.create_text(
			current_x + font_obj.measure(letter) / 2,
			y,
			text=letter,
			fill=colors[index % len(colors)],
			font=headline_font,
		)
		current_x += font_obj.measure(letter)

	root.mainloop()


if __name__ == "__main__":
	main()
