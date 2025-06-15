# Invoice Generation Project

A Python-based automated invoice generation system that converts Excel spreadsheets into professional PDF invoices.

## 📋 Overview

This project automatically processes Excel files containing invoice data and generates formatted PDF invoices with company branding. It's designed to streamline the invoice creation process for businesses by converting structured data into professional-looking documents.

## 🚀 Features

- **Batch Processing**: Automatically processes multiple Excel files from a directory
- **Professional PDF Generation**: Creates well-formatted PDF invoices with tables and styling
- **Company Branding**: Includes company logo and name on invoices
- **Automatic Calculations**: Calculates and displays total amounts
- **Flexible Data Structure**: Supports standard invoice data formats
- **File Organization**: Separates input Excel files and output PDFs into organized directories

## 📁 Project Structure

```
invoice-generation/
├── invoices/
│   ├── 10001-2023.1.18.xlsx
│   ├── 10002-2023.1.18.xlsx
│   └── 10003-2023.1.18.xlsx
├── PDFs/
│   ├── 10001-2023.1.18.pdf
│   ├── 10002-2023.1.18.pdf
│   └── 10003-2023.1.18.pdf
├── logo.png
├── main.py
└── README.md
```

## 📊 Excel File Format

The Excel files should contain the following columns:
- `product_id`: Unique identifier for each product
- `product_name`: Description of the product/service
- `amount_purchased`: Quantity of items
- `price_per_unit`: Unit price
- `total_price`: Total cost (amount × price per unit)

### Example Data Structure:
| product_id | product_name | amount_purchased | price_per_unit | total_price |
|------------|--------------|------------------|----------------|-------------|
| 8198129    | Water Pump   | 2                | 151            | 302         |
| 4772822    | Microscope   | 1                | 37             | 37          |

## 🛠️ Installation

### Required Dependencies
Install the required packages using pip:

```bash
pip install pandas openpyxl fpdf2 pathlib
```

### Alternative Installation
You can also install dependencies from a requirements file:

```bash
pip install -r requirements.txt
```

Create a `requirements.txt` file with:
```
pandas>=1.3.0
openpyxl>=3.0.0
fpdf2>=2.5.0
```

## 📝 Usage

### 1. Prepare Your Files
- Place your Excel invoice files in the `invoices/` directory
- Ensure files follow the naming convention: `{invoice_number}-{date}.xlsx`
- Add your company logo as `logo.png` in the root directory

### 2. Run the Script
Execute the main script:

```bash
python main.py
```

### 3. Output
Generated PDF invoices will be saved in the `PDFs/` directory with the same filename as the source Excel file.

## 🔧 Configuration

### File Naming Convention
Excel files should be named using the format: `{invoice_number}-{date}.xlsx`
- Example: `10001-2023.1.18.xlsx`
- The script extracts invoice number and date from the filename

### Customizing the PDF Layout
You can modify the following aspects in `main.py`:
- **Page orientation**: Change `orientation` parameter in `FPDF()`
- **Font styles**: Modify `pdf.set_font()` calls
- **Table dimensions**: Adjust `col_width` and `row_height` variables
- **Logo size**: Change the `w` parameter in `pdf.image()`

### Company Information
Update the company name in the script:
```python
pdf.cell(w=20, h=7, txt=f"Your Company Name", align='L')
```

## 📄 Generated Invoice Features

Each generated PDF invoice includes:
- **Header**: Invoice number and date
- **Product Table**: Detailed breakdown of products/services
- **Total Calculation**: Automatic sum of all items
- **Company Branding**: Logo and company name
- **Professional Formatting**: Clean, business-appropriate styling

## 📞 Support

For support and questions:
- Create an issue in the repository
- Check the troubleshooting section above
- Review the code comments for implementation details

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

*This project simplifies invoice generation by automating the conversion of Excel data to professional PDF invoices, saving time and ensuring consistency in business documentation.*