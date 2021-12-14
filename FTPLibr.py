import ftplib
 
ftp = ftplib.FTP("ftpupload.net")
ftp.login("epiz_29176489")
 
data = []
 
ftp.dir(data.append)
 
ftp.quit()
 
for line in data:
    print "-", line
