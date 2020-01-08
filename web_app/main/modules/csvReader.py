"""
    AUTHOR: Sutharsan Rajaratnam
    DATE: November 17, 2019
    APPLICATION: Payroll Web Application
    PURPOSE: Read and process CSV files

"""

import csv

def importCSVUpload_dict(filepath, filename):
    print "Importing CSV using Dictionary... "
    
    path = filepath + filename
    key = "date"
    
    csvData_list    = []
    csvData_footer  = []
    with open(path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row_dict in csv_reader:
            if (row_dict['date'] == "report id"): 
                csvData_footer.append(row_dict)
            else:
                csvData_list.append(row_dict)
    return csvData_list, csvData_footer
