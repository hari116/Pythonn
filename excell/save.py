import openpyxl
import xlsxwriter

wb2 = openpyxl.load_workbook('test.xlsx')
sheet2 = wb2.get_sheet_by_name('Sheet1')
a2 = sheet2['A1']
b2 = sheet2['B1']
c2 = sheet2['C1']
sheet2['B1'] = 80
sheet2['C1'] = '=(A1+B1)'
wb2.save('test.xlsx')
wb2.close()
print(a2.value, b2.value, c2.value)
