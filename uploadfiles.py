import os
import dropbox
from dropbox.files import writemode

class Transferdata:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_files(self,file_from,file_to):
        dbx = dropbox.dropbox(self.access_token)

        #enumerate local files recursively
    for root,dirs, files in os.walk(file_from):
        for filename in files:
            # construct the full local path
        local_path = os.path.join(root,filename)

            #construct the full Dropbox path
        relative_path = os.path.relpath(local_path,file_from)
        dropbox_path = os.path.join(file_to,relative_path)

            #upload the file
        with open(local_path,'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode-writemode('overwrite'))

def main():
    access_token = 'sl.BHnbKSwvukc1Y0gsPfw8Mk7M4yFHZu0ApDPgTvPhSqQ_baRLtjRUzULf-x8bjIsB7F3ji7jvRA_ziywgO5TULhl9wz_Xe8QniCNrwj0jmIOS4jmjTfOD7b_MnVvkMepUZlNWsWizbu_n'
    Transferdata = Transferdata(access_token)

    file_from = str(input("Enter the folder patht to transfer: "))
    file_to = input("Enter the full path to upload to dropbox: ") #This is the full path to upload the file to,including name that ypu wish the file to be called once uploaded

    #API v2
    transferData.upload_files(files_from,file_to)
    print("file has been moved !!!")
main()