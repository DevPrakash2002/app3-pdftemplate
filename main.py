from fpdf import FPDF
import pandas as pd
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=14)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    pdf.line(10, 20, 200, 20)
    for i in range(2,265):
        pdf.line(10, 10*i, 200, 10*i)

    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=6)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')



    for i in range(row['Pages'] - 1):
        pdf.add_page()
        for i in range(2, 265):
            pdf.line(10, 10 * i, 200, 10 * i)
        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=6)
        pdf.set_text_color(180, 180, 180)
        # noinspection PyTypeChecker
        pdf.cell(w=0, h=10, txt=row["Topic"], align='R')

pdf.output('output.pdf')