from ftplib import FTP

ftp = FTP("127.0.0.1")
ftp.login("user", "12345")

print("Files:", ftp.nlst())  # list files
with open("upload.txt", "rb") as f:
    ftp.storbinary("STOR upload.txt", f)  # upload file

with open("downloaded.txt", "wb") as f:
    ftp.retrbinary("RETR upload.txt", f.write)  # download file

ftp.quit()
