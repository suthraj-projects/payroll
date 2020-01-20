"""
    AUTHOR: Sutharsan Rajaratnam
    DATE: November 17, 2019
    APPLICATION: Payroll Web Application
    PURPOSE: File Upload
"""

import os

#FUNCTION: Used to check if file extension is allowed
def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


#FUNCTION: Check folder path, create folder path directories if they do not exist
def checkPathExists(folder_path):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print ("SUCCESS: Folder path created - '%s' " %(folder_path))
    except:
        print ("ERROR: Failed folder path check - '%s' " %(folder_path))
        
        
#FUNCTION: Saves uploaded file on the server
def upload_file(upload_path, file):
#    print "Saving uploaded file"
    #filename = secure_filename(file.filename)
    filename = ""
    try:
        checkPathExists(upload_path)
        
        filename = file.filename
        savePath = os.path.join(upload_path, filename)
        file.save(savePath)
    except:
        #print bcolors.WARNING + "ERROR: Table '" + dropTableName + "' does not exist in database "  + bcolors.ENDC
        print ("ERROR: Upload of file '%s' failed" %(filename))
        