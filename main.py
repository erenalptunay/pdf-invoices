import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")


for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr = filename.split('-')[0]
    invoice_date = filename.split('-')[1]

    pdf.set_font('Times', size=14, style='B')
    pdf.cell(w=50, h=7, txt=f"Invoice nr.{invoice_nr}", align='L', ln=1)
    pdf.cell(w=50, h=7, txt=f"Date {invoice_date}", align='L', ln=1)

    # Add table
    pdf.ln(5)
    col_width = 38
    row_height = 7
    pdf.set_font('Times', size=12, style='B')

    for col_name in df.columns:
        col_name = col_name.replace("_", " ").title()
        pdf.cell(w=col_width, h=row_height, txt=col_name, align='L', border=1)
    pdf.ln(row_height)

    pdf.set_font('Times', size=8, style='B')

    for index, row in df.iterrows():
        for item in range(len(row)):
            pdf.cell(w=col_width, h=row_height, txt=str(row.iloc[item]), align='L', border=1)
        pdf.ln(row_height)

    # Add Total Price
    total_price = int(df["total_price"].sum())
    for i in range(len(df.columns)-1):
        pdf.cell(w=col_width, h=row_height, align='L', border=1)
    pdf.cell(w=col_width, h=row_height, txt=f"{total_price}", align='L', border=1)

    # Add Total Price text
    pdf.ln(10)
    pdf.set_font('Times', size=10, style='B')
    pdf.cell(w=50, h=7, txt=f"The total amount is {total_price} Euros.", align='L', ln=1)

    # Add the company logo and name
    pdf.ln()
    pdf.image("logo.png", w=10)
    pdf.cell(w=20, h=7, txt=f"Company Name", align='L')

    pdf.output(f"PDFs/{filename}.pdf")
