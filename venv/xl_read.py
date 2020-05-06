import xlrd
from tkinter.filedialog import askopenfilename

filename = askopenfilename()

Wb_obj = xlrd.open_workbook(filename)
sheet = Wb_obj.sheet_by_index(0)

for i in range(sheet.nrows):
    print(sheet.cell_value(i, i))