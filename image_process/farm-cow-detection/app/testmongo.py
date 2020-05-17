from mymongodb import mongoConn
import datetime

mydb = mongoConn() 


dirname = "test_image"
filename = "1.jpg"
#with open('{dirname}/{filename}'.format(filename=filename, dirname=dirname), 'rb') as image:
    #int(filename.split(".")[0])%5 + 1
f = open('{dirname}/{filename}'.format(filename=filename, dirname=dirname), 'rb')
image = f.read()
#print(image)

key = "".join(filename.split("."))
res = mydb.insertimage({key: image})
print(res)

image = mydb.query(res)[key]
#mydb.getall()
print(image[0:100])
#mydb.getall()