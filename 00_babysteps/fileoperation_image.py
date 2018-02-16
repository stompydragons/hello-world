#This program copies the input image into the output image file, 10 bytes at a
#time

inputFile = open('christmaswho.jpg', 'rb')
outputFile = open('myoutputimage.jpg', 'wb')

msg = inputFile.read(10)

while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10)

inputFile.close()
outputFile.close()
