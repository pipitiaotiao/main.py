import xlrd
def excel():
    data = xlrd.open_workbook('导出关系数据0102 的副本.xls')
    table = data.sheets()[0]

    friends_id = []
    for i in range(table.nrows):
        user_id = []
        cells = table.row_values(i)
        name1 = cells[0]
        name2 = cells[1]
        user_id.append(name1)
        user_id.append(name2)
        friends_id.append(user_id)
    return friends_id
a = excel()
#print(a)

list=[]
def countchar(var):
    result = {}
    for key in a:   #第一个元素 ['100000163225268', '100003812812018']
        list.append(key[1])
    for i in var:
        if i in result:
            result[i] = result[i]+1
        else:
            result[i] = 1
    return result
s=countchar(list)
#print(s)

b = sorted(s.items(), key=lambda x: x[1], reverse=True)#正序排序
#print(b)
res = b[0:10:1]   #前十排名
#print(res)

c = [x[0] for x in res]#只取排名前十的id
#print(c)

i = 0
x = 0
y = []
for i in c:
    for x in a:
        if i == x[1]:
            #print(x[0])
            y.append(x[0])
print(y)
# result2 = str(res)
# with open(r'C:\Users\16317\PycharmProjects\pythonProject3\111.txt', mode='w') as f:
#  for i in res:
#    f.write(result2)


import xlwt
def data_write(y):
    file = xlwt.workbook(encoding='utf-8')
    sheet = file.add_sheet(u'final', cell_overwrite_ok=True)
    i = 0
    for data in y:
        for j in range(len(data)):
            sheet.write(i, j, data[j])
        i = i + 1
    file.save('结果.xlsx')

#输出到txt文本，在excel把十共同好友列表输入excel
#mysql 的 安装和链接   增删改查。。