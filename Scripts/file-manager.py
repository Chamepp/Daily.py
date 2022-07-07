# Imports
import os
import json
import shutil


# Main
if __name__ == "__main__":
    ext = 0
    def folder_manager(path,exception_file,extensions):
        global ext

        # File Exception and Importing
        with open(exception_file,'r',encoding='utf-8') as exct_file:
            execptions = exct_file.read()
        execptions = set(execptions.split('\n'))

        # Directory Change
        if os.path.isdir(path):
            os.chdir(path)

        # Check List
        if type( extensions) is not list:
            raise Exception('Expected a list object.')
        extensions = set( extensions)

        # Generate List Of Files
        all_files = {file.lower() for file in os.listdir(path) if os.path.isfile(file)}
        all_files = all_files - execptions

        # Capitalizing File Names
        for file in all_files:
            _name, _ext = os.path.splitext(file)
            os.rename(os.path.join(path,file),('.'.join([_name.title(),_ext[1:]])))


        # List Of Number Files
        rename_files = {file for file in all_files if file.split('.')[1] in  extensions}

        # List Of Extention Files
        for file_ in rename_files:
            name, ext = os.path.splitext(file_)
            ext = ext[1:]
            folder_name = ext 


            # Creating Folder
            if ext == '':
                continue

            if os.path.exists(os.path.join(path,ext)):
                os.rename(os.path.join(path,ext),os.path.join(path,ext))
                shutil.move(os.path.join(path,file_),os.path.join(path,ext,file_))
                
            else:
                if os.path.exists(os.path.join(path,folder_name)):
                    shutil.move(os.path.join(path,file_),os.path.join(path,folder_name,file_))

                else:
                    os.makedirs(os.path.join(path,folder_name))
                    shutil.move(os.path.join(path,file_),os.path.join(path,folder_name,file_))

        # Deleting Folders
        for folder in os.listdir(path):
            if os.path.isdir(folder):
                if len(os.listdir(os.path.join(path,folder))) == 0:
                    os.rmdir(os.path.join(path,folder))
                    continue




    def code_runner():

        # Gather Data
        path = input('\nEnter the Path of folder you want to Manage.\nPlease make sure what this script does by reading the Readme.md file.\nEnter Here : ')
        while os.path.isdir(path) == False:
            print('The given path is not valid! Please enter a correct Path.')
            path = input('\nEnter the Path of folder you want to Manage.\nPlease make sure what this script does by reading the Readme.md\nEnter Here : ')
            if os.path.isdir(path) == True:
                break

        # File Exception
        exception_file = input('\nEnter the path of Exception file.\nEnter here : ')
        while os.path.isfile(exception_file) == False:
            print('The given path is not valid! Please enter a correct Path.')
            exception_file = input('\nEnter the path of Exception file.\nEnter here : ')
            if os.path.isfile(exception_file) == True:
                break

        # Extention Data
        with open('all-file-extensions.json','r') as json_pointer:
            json_file_exts = json.load(json_pointer)

        extensions = input('\nEnter  extensions of files you want to dump.\nExample - \"dll,exe,txt\" .Don\'t enclose in Inverted commas and seperate  extensions with comma.\nEnter here : ')
        extensions =  extensions.replace(' ','')
        extensions =  extensions.split(',')

        for ext in  extensions:
            ext_json = ext.upper()
            while ext_json not in json_file_exts:
                print(f'{ext} is a Invalid  extension! Please Enter a valid  extension.')
                extensions = input('\nEnter  extensions of files you want to dump.\nExample - \"dll,exe,txt\" .Don\'t enclose in Inverted commas and seperate  extensions with comma.\nEnter here : ')
                extensions =  extensions.replace(' ','')
                extensions =  extensions.split(',')
                for ext in  extensions:
                    ext_json = ext.upper()
                    if ext_json in json_file_exts:
                        break


        folder_manager(path=path,exception_file=exception_file, extensions= extensions)
        print('\nCompleted! Thanks for using this script.')

    code_runner()
