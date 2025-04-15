from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for idx, row in df.iterrows():
    _, topic, pages = row
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=topic, align="L", ln=1, border=0)
    #pdf.line(10,21,200,21)

    start_mm = 20; end_mm = 298; space_between_lines_mm = 10
    for y_mm in range(start_mm, end_mm, space_between_lines_mm):
        pdf.line(10, y_mm, 200, y_mm)

    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=10, txt=topic, align="R", ln=1)

    for num in range(pages-1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0, h=10, txt=topic, align="R", ln=1)

        start_mm = 20; end_mm = 298; space_between_lines_mm = 10
        for y_mm in range(start_mm, end_mm, space_between_lines_mm):
            pdf.line(10, y_mm,200, y_mm)

pdf.output("output.pdf")