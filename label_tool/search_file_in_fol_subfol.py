import os
"""
def create_file_list(path):
    return_list = []
    for subdir, dirs, filenames in os.walk(path):
        #print subdir
        for file_list in filenames:
            for file_name in file_list:
                if file_name.endswith((".txt")):
                    return_list.append(file_name)
                    print(subdir + file_name)
    return return_list

"""

folder_location = '/media/vkchcp0013/mstu_hpat/1.ARTIFICIAL_INTELLIGENCE/2.TRAINING/3.Darknet/yolo_annotation_tool/Yolo-Annotation-Tool-New-/Labels'
#file_list = create_file_list(folder_location)


for subdir, dirs, files in os.walk(folder_location):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".txt"):
            print (filepath)
