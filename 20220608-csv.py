import pandas

# with open('xiaoshuaib.csv', mode='w') as csv_file:
#     fieldnames = ['你是谁', '你几岁', '你多高']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'你是谁': '小帅b', '你几岁': '18岁', '你多高': '18cm'})
#     writer.writerow({'你是谁': '小帅c', '你几岁': '19岁', '你多高': '17cm'})
#     writer.writerow({'你是谁': '小帅d', '你几岁': '20岁', '你多高': '16cm'})

b = ['小帅b', '小帅c', '小帅d']
c = ['18岁', '19岁', '20岁']
d = ['18cm', '17cm', '16cm']

df = pandas.DataFrame({'你是谁': b, '你几岁': c, '你多高': d})
df.to_csv("xsb.csv", index=False, sep=',')

# xiaoshuaib = pandas.read_csv('xiaoshuaib.csv', encoding='gbk')
# print(xiaoshuaib)
