from openpyxl import load_workbook

# 打开Excel文件
wb = load_workbook(r'C:\Users\Administrator\Desktop\测试.xlsx')
# 定位对应表单
sheet = wb['Sheet1']
# 最大行
print('最大行：{0}'.format(sheet.max_row))
# 最大列
print('最大行：{0}'.format(sheet.max_column))
hang = sheet.max_row
lie = sheet.max_column
# print(type(hang))
for i in range(hang):
    for j in range(lie):
        # print(i+1, j+1)
        res = sheet.cell(i+1, j+1).value
        if res != None:
            print(i+1, j+1, end=' ')
            print(res)

# 定位单元格，取出行列值
res = sheet.cell(1, 1).value

print(res)
