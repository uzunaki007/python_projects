#1st of all we have to install the module qrcode from the python console
#for intalling the module you have to code the following
#pip install qrcode
import qrcode as qr  #qr here is used as an allias
img=qr.make("https://www.linkedin.com/in/sitanshu-chakraborty-914907219/")
img.save("mylinkedin.png") #the qr is now saved in .png format
