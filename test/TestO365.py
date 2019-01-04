from pyo365 import Account

my_credentials = ('2cffd357-331f-4a5e-a460-df4f4b39bbf2', 'muazSCTF033|tzyKKG87*?~')

account = Account(credentials=my_credentials)

storage = account.storage()  # here we get the storage instance that handles all the storage options.

# list all the drives:
drives = storage.get_drives()

# get the default drive
my_drive = storage.get_default_drive()  # or get_drive('drive-id')

# get some folders:
root_folder = my_drive.get_root_folder()
attachments_folder = my_drive.get_special_folder('attachments')

# iterate over the first 25 items on the root folder
for item in root_folder.get_items(limit=25):
    if item.is_folder:
        print(item.get_items(2))  # print the first to element on this folder.
    elif item.is_file:
        if item.is_photo:
            print(item.camera_model)  # print some metadata of this photo
        elif item.is_image:
            print(item.dimensione)  # print the image dimensions
        else:
            # regular file:
            print(item.mime_type)  # print the mime type