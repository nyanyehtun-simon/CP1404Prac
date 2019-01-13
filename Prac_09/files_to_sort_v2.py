import shutil
import os


def main():
    # input_category_list = {'Docs': [], 'Images': [], 'Spreadsheets': [], 'Text': []}

    # Dummy input data without user input
    input_category_list = {'Docs': ['doc', 'docx', 'txt'], 'Images': ['png', 'gif', 'jpg'], 'Spreadsheets': ['xls', 'xlsx'], 'text': []}

    # doc_file_category = input('What category would you like to sort doc files into?')
    # input_category_list[doc_file_category].append('doc')
    #
    # docx_file_category = input('What category would you like to sort docx files into?')
    # input_category_list[docx_file_category].append('docx')
    #
    # png_file_category = input('What category would you like to sort png files into?')
    # input_category_list[png_file_category].append('png')
    #
    # gif_file_category = input('What category would you like to sort gif files into?')
    # input_category_list[gif_file_category].append(('gif'))
    #
    # txt_file_category = input('What category would you like to sort txt files into?')
    # input_category_list[txt_file_category].append('txt')
    #
    # xls_file_category = input('What category would you like to sort xls files into?')
    # input_category_list[xls_file_category].append(('xls'))
    #
    # xlsx_file_category = input('What category would you like to sort xlsx files into?')
    # input_category_list[xlsx_file_category].append('xlsx')
    #
    # jpg_file_category = input('What category would you like to sort jpg files into?')
    # input_category_list[jpg_file_category].append('jpg')

    print(input_category_list)

    os.chdir('FilesToSort')
    for folder_name in input_category_list.keys():
        try:
            os.mkdir(folder_name)
        except FileExistsError:
            print('Folder {} already exists'.format(folder_name))

    for key, extension_list in input_category_list.items():
        pass

    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        for folder_name, extension_list in input_category_list.items():

            extension = filename.split('.')[1]
            if extension in extension_list:
                # just move the file to new folder location
                shutil.move(filename, folder_name + '/' + filename)

    return

    # Change to desired directory
    # os.chdir('FilesToSort')

    existing_dirs = []

    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            existing_dirs.append(filename)
            continue

        extension = filename.split('.')[1]
        if extension not in existing_dirs:
            # create a new dir
            try:
                os.mkdir(extension)
                existing_dirs.append(extension)
            except FileExistsError:
                print('File already exists')

        # just move the file to new folder location
        shutil.move(filename, extension + '/' + filename)

main()
