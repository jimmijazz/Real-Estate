#Crimes over the last year per suburb

import requests, json, openpyxl, string
from openpyxl.cell import get_column_letter

#Open Workbook and set sheet to 'crimes'
workbook = openpyxl.load_workbook('/Users/Joshua/Desktop/Python/Real Estate/Crime/crimes.xlsx')
sheet = workbook.get_sheet_by_name('crimes')
suburbs = ('/Users/Joshua/Desktop/Python/Real Estate/suburb_id.txt')

#List of QPS offence codes
offence_type_list = ['1','8','14','17','21','27','28','29','30','35','39','45','47','51','52','54','55']

#Convert numbers to letter of the alphabet for excel columns
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']

counter=0
with open(suburbs) as f:
    for suburb in f:

        for offence_type in range(len(offence_type_list)):

            #Get Crime Data 1/1/2010 - Current
            crime_url = ('https://data.police.qld.gov.au/api/qpsmeshblock?boundarylist=1_'+suburb+'&startdate=1262304000&enddate=1453420800&offences='+offence_type_list[offence_type])
            crime_data = requests.get(crime_url)
            crime_data = crime_data.json()

            #For each OffenceInfo
            for i in range(len(crime_data['Result'])):
                #For each item in OffenceInfo
                for ii in range(len(crime_data['Result'][i]['OffenceInfo'])):
                    stats_list = list(crime_data['Result'][i]['OffenceInfo'][ii].keys())
                    #For each individual QpsOffenceId
                    counter += 1

                    for j in range(len(crime_data['Result'][i]['OffenceInfo'][ii])):
                        # print(crime_data['Result'][i]['OffenceInfo'][ii])
                        stat_title = stats_list[j]
                        sheet[str(alphabet[j])+str(counter)] = str(crime_data['Result'][i]['OffenceInfo'][ii][(stat_title)])
        print(counter) #prints total number of crimes

        #List dictionary keys as list
        #http://stackoverflow.com/questions/16819222/how-to-return-dictionary-keys-as-a-list-in-python-3-3
        #For number of crimes of that offence

        workbook.save('crimes.xlsx')
