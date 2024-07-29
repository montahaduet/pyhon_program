import csv
# file= open('file/info.csv')
# file_reader=csv.reader(file)
# data=list(file_reader)
# print(data)
# print(data[0][2])

# for row in file_reader:
#     print('row no = '+ str(file_reader.line_num)+''+str(row))

output_file=open('out.csv','a',newline='.')
output_file=csv.writer(output_file,delimiter='.')
output_file.writerow(['2','3','4'])
output_file.writerow(['23','12','45','10'])

