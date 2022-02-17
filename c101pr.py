
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def uploadFile(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)
        with open (file_from,'rb') as f:
          dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
          print("fileUploaded")
def main():
    print("Welcome to python based dropbox cloud storage services !")
    print ("")

    access_token = "sl.BCPCa0-11Tr4434_1BGwAyZq8ebf5xs2hyw3lSWb7ilJULJW4CCn8JVLzGW8XC-IwJWXJCo5uThUgVH_MTQcIvOwf9h2ub9KuMSN-Brc1oQbUh-TXXJPJDTDEWluCIcIpTLVbHP6_gDz"
    transferData = TransferData(access_token)
    
    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  

    transferData.uploadFile(file_from, file_to)
    print("file has been moved !!!")
    
main()    