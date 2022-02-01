import dropbox


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A_lzK0WnasvAKYSCBMAyvYm71ZgTka5JRP8kjf7x25JrDXoz50sNsUl_bFKwrejqg_BHWHMNTsulJRnwv1Zt1MgeNCeXqM9ft3K_ApVxdEixUa8Lj8O2BsaB-xAnKLr3Nu7zYIZDJ5U7'
    transferData = TransferData(access_token)

    file_from = input("Enter the file you want to upload......")
    file_to = input("Please write the path of the file........")

    transferData.upload_file(file_from, file_to)

main()
    