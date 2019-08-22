

import os
import tkinter.filedialog
import tkinter

def main():

    root = tkinter.Tk()
    files = tkinter.filedialog.askopenfilenames(parent=root, title='choose files')
    print(files)
    folder_path = os.path.dirname(files[0])


    index = int(input("From Which Number Do You Want To Begin?"))

    for filename in files:
       old_name=filename
       new_name=os.path.join(folder_path,str(index)+".jpeg")
       os.rename(old_name, new_name)
       index += 1



'''
path=input(" On Which Folder Do You Want To ReName?")
 for filename in os.listdir(path):
       old_name=os.path.join(path,filename)
       new_name=os.path.join(path,str(index)+".jpeg")
       os.rename(old_name, new_name)
       index += 1
'''

if __name__ == '__main__':
    main()