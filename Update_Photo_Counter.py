import urllib3.request
import re

import os


# ct stores current time 
ct = datetime.datetime.now() 
print(ct,": Script Started to scan npeida pages ..") 

update_nithyanandapedia = 1

site = pywikibot.Site('en','nithyanandapedia')
site.login()

# Give the location of the file
loc = ("NPedia_URL_v0.3.xlsx")
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
rows=sheet.nrows-2
Total_Images =0
Total_Manuals=0
Total_Date_Pages=0
Total_Flyers=0
Total_Vidoes_Count=0
Total_Books_count=0
Total_Audio_count=0
Total_Articles_count=0
Total_Narration_count=0
Total_Title_count=0
Total_Transcript_count=0

#nPage_Name_value="January_01_2019"
i = 0
while i <= rows:
    i=i+1
    nPage_Name_value=str(sheet.cell_value(i, 0))
    if (len(nPage_Name_value)>125):
        nPage_Name_value=nPage_Name_value[0:125]
   # print(nPage_Name_value,len(nPage_Name_value))
    #print(nPage_Name_value)
    page = pywikibot.Page(site, nPage_Name_value)
    #<img ,#{#hsimg: ,# define string
    string = page.text
    substring1 = "hsimg:"
    substring2 = "<img"
    substring3 = "File:"
    count1 = string.count(substring1)
    count2 = string.count(substring2)
    count3 = string.count(substring3)
    Image_count=count1+count2+count3
   # print("Total Image Count of the Page",nPage_Name_value,"is :",Image_count)
    manuals_count= string.count("Category:Manuals")
    flyers_count= string.count("Category:Flyers & Banners") + string.count("Category: Flyers & Banners")+ string.count("Category:Flyer")+ string.count("Category: Flyer")+string.count("Category :Flyer")+string.count("Category :Flyers-and-Banners")+string.count("Category: Flyers-and-Banners")+string.count("Category:Flyers-and-Banners")
    datepages_count= string.count("[[Category: 20") + string.count("[[Category:20")
    Vidoes_Count= string.count("#evu") + string.count("#evt") + string.count("videoUrl")
    Audio_count = string.count("<soundcloud")
    Books_count= string.count("Category: Books") + string.count("Category:Books")+ string.count("Category :Books")
    Articles_count= string.count("[[Category:Articles") + string.count("[[Category: Articles") + string.count("[[Category :Articles")
    Narration_count= string.count("==Narration==")  
    Title_count= string.count("==Title==")
    Transcript_count= string.count("==Transcript==")
    
    #Adding to total
    Total_Images=Image_count+Total_Images
    Total_Manuals=manuals_count+Total_Manuals
    Total_Date_Pages=datepages_count+Total_Date_Pages
    Total_Flyers=flyers_count+Total_Flyers
    Total_Vidoes_Count=Vidoes_Count+Total_Vidoes_Count
    Total_Audio_count=Total_Audio_count+Audio_count
    Total_Books_count=Total_Books_count+Books_count
    Total_Articles_count=Total_Articles_count+Articles_count
    Total_Narration_count=Total_Narration_count+Narration_count
    Total_Title_count=Total_Title_count+Title_count
    Total_Transcript_count=Total_Transcript_count+Transcript_count
    if (i % 250 == 0):
      print(datetime.datetime.now()," : Completed scanning of ", i ,"number of Pages out of ", rows," Please wait ......")

print('Finished Scanning')
print("Total_Images:",Total_Images)
print("Total_Manuals:",Total_Manuals)
print("Total_Flyers:",Total_Flyers)
print("Total_Vidoes_Count:",Total_Vidoes_Count)
print("Total_Audio_count:",Total_Audio_count)
print("Total_Books_count:",Total_Books_count)
print("Total_Articles_count:",Total_Articles_count)
print("Total_Date_Pages:",Total_Date_Pages)
print("Total_Title_count:",Total_Title_count)
print("Total_Narration_count:",Total_Narration_count)
print("Total_Transcript_count:",Total_Transcript_count)

ct = datetime.datetime.now() 
print("Script Finished to scan mediawikipages ", ct)

#//*****************************************Update the Index Page***********************************************************************
file1 = open(r"E:\Sangha\front_page_counters\Ntruthwebsitehtml\index.html", encoding="utf8")  
index_page = file1.read()
file1.close()
phoneNumRegex = re.compile(r'\d\d\d\d\d\d\+')
mo = phoneNumRegex.search(index_page) 
Image_Count_current_page= mo.group()
print(Image_Count_current_page)
index_page=index_page.replace(Image_Count_current_page,Total_Images)
f = open(r"E:\Sangha\front_page_counters\Ntruthwebsitehtml\index.html", "w", encoding="utf-8")
f.write(index_page)
f.close()
#//*****************************************Update the Index Page***********************************************************************
