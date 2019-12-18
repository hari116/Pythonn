import xlwings as xw

wbxl=xw.Book('test.xlsx')
wbxl.sheets['Sheet1'].range('C1').value
