import datetime
from fpdf import FPDF

# Define your report content and data here
report_title = "Monthly Sales Report"
sales_data = {
    "January": 15000,
    "February": 18000,
    "March": 22000,
    "April": 19000,
    "May": 21000,
}

# Create a PDF report using the FPDF library
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, report_title, align='C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f"Generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, data):
        self.set_font('Arial', '', 12)
        for month, sales in data.items():
            self.cell(40, 10, month, 0)
            self.cell(0, 10, f"${sales:,}", 0, 1)

# Generate the PDF report
pdf = PDFReport()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.chapter_title("Monthly Sales Summary")
pdf.chapter_body(sales_data)

pdf.output("monthly_sales_report.pdf")
print("PDF report generated successfully!")
