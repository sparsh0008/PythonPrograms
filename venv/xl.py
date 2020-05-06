from xlwt import Workbook
from tkinter.filedialog import asksaveasfile
Wb__obj = Workbook()

my_sheet = Wb__obj.add_sheet('python_class')
my_sheet.write(0,0, 'sparsh')
my_sheet.write(0,1, 'prabal')
my_sheet.write(0,2, 'dhruv')

f = asksaveasfile(mode='w', defaultextension= '.csv')

if f is not None:
    Wb__obj.save(f.name)
    f.close()