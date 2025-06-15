import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

print(filepaths)


for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr = filename.split('-')[0]
    invoice_date = filename.split('-')[1]

    pdf.set_font('Times', size=14, style='B')
    pdf.cell(w=50, h=6, txt=f"Invoice nr.{invoice_nr}", align='L', ln=1)
    pdf.cell(w=50, h=6, txt=f"Date {invoice_date}", align='L', ln=1)

    # Add table
    pdf.ln()
    col_width = 38
    row_height = 8
    pdf.set_font('Times', size=12, style='B')

    for col_name in df.columns:
        col_name = col_name.replace("_", " ").title()
        pdf.cell(w=col_width, h=row_height, txt=col_name, align='C', border=1)
    pdf.ln(row_height)

    pdf.set_font('Times', size=8)

    for index, row in df.iterrows():
        for item in row:
            pdf.cell(w=col_width, h=row_height, txt=str(item), align='C', border=1)
        pdf.ln(row_height)


    pdf.output(f"PDFs/{filename}.pdf")
