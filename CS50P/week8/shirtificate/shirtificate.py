from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 40)
        # Calculating width of title and setting cursor position:
        width = self.get_string_width(self.title) + 6
        self.set_x((210 - width) / 2)
        # Setting colors for frame, background and text:
        self.set_draw_color(0, 0, 0)
        self.set_fill_color(0, 0, 0)
        self.set_text_color(255, 255, 255)
        # Printing title:
        self.cell(width, 30, self.title, border=1, align="C", new_x="LMARGIN", new_y="NEXT", fill=True,)
        # Performing a line break:
        self.ln(20)

    def add_shirt(self, image):
        self.image(image, w=180, y=60, x=15)


    def add_text(self, text):
        self.set_font('helvetica', "B", size=26)
        self.set_y(120)
        # Calculating width of title and setting cursor position:
        width = self.get_string_width(text) + 6
        self.set_x((210 - width) / 2)
        self.set_text_color(255, 255, 255)
        self.cell(width, 20, text, align="C", new_x="LMARGIN", new_y="NEXT")



name = input("Name: ")
pdf = PDF()
pdf.set_title("CS50 Shirtificate")
pdf.add_page()
pdf.add_shirt("shirtificate.png")
pdf.add_text(f"{name} took CS50")

pdf.output("shirtificate.pdf")

