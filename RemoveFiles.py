import os
import shutil
import time
def main():
    deletedFolderCount=0
    deletedFileCount=0
    path="/C:\Users\sorok\Desktop\Sacrefice"
    days=1
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for rootFolder,folders,files in os.walk(path):
            if seconds >= getFileorFolderage(rootFolder):
                removeFolder(rootFolder)
                deletedFolderCount=deletedFolderCount+1
                break
            else:
                for Folder in folders:
                    FolderPath=os.path.join(rootFolder,Folder)
                    if seconds >= getFileorFolderage(FolderPath):
                        removeFolder(FolderPath)
                        deletedFolderCount=deletedFolderCount+1
                for file in files:
                    FilesPath=os.path.join(rootFolder,file)
                    if seconds >= getFileorFolderage(FilesPath):
                        removeFile(FilesPath)
                        deletedFilesCount=deletedFilesCount+1
                    else:
                        if seconds>=getFileorFolderAge(path):
                            removeFile(FilesPath)
                            deletedFilesCount=deletedFilesCount+1
    else:
        print(f'"{path}"is not found')
        deletedFileCount+=1
    print("Total Folder Deleted:{deletedFolderCount}")
    print("Total File Deleted:{deletedFileCount}")
def removeFolder(path):
    if not shutil.rmtree (path):
        print("path is removed successfully")
    else: 
        print("Unable to Delete the File")    
def removeFile(path):
    if not os.remove (path):
        print("path is removed successfully")
    else: 
        print("Unable to Delete the File")    
def getFileorFolderAge(path):
    ctime=os.stat(path).st_ctime
    return ctime
if __name__=='__main__':
    main()