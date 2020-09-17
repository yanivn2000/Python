
import os
from enum import IntEnum

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def RepresentsFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

root_folder = "//Volumes//GoogleDrive//My Drive//Brands//Gifffted//Reports//"

marketplace="US" #input("Please enter Marketplace (US, CA, UK, DE, IT, FR, ES): ")
f_st= open(root_folder + marketplace + "//ST//all.tsv" , "r")
#f_ap= open(root_folder + marketplace + "//AP//all.tsv", "r")
search_term="boss"#input("Please enter search term: ")

class Header(IntEnum):
   Date = 0,
   Portfiolio_Name = 1,
   Currency = 2,
   Campaign_Name = 3,
   Ad_Group_Name = 4,
   Targeting = 5,
   Match_Type = 6,
   Customer_Search_Term = 7,
   Impressions = 8,
   Clicks = 9,
   CTR = 10,
   CPC = 11,
   Spend = 12,
   Seven_Day_Total_Sales = 13,
   ACoS = 14,
   RoAS = 15,
   Seven_Day_Total_Orders = 16,
   Seven_Day_Total_Units = 17,
   Seven_Day_Total_Rate = 18,
   Seven_Day_Advertised_SKU_Units = 19,
   Seven_Day_Other_SKU_Units = 20,
   Seven_Day_Advertised_SKU_Sales = 21,
   Seven_Day_Other_SKU_Sales = 22

class Header_Calc(IntEnum):
   BASE = 8,
   Impressions = 8,
   Clicks = 9,
   CTR = 10,
   CPC = 11,
   Spend = 12,
   Seven_Day_Total_Sales = 13,
   ACoS = 14,
   RoAS = 15,
   Seven_Day_Total_Orders = 16,
   Seven_Day_Total_Units = 17,
   Seven_Day_Total_Rate = 18,
   Seven_Day_Advertised_SKU_Units = 19,
   Seven_Day_Other_SKU_Units = 20,
   Seven_Day_Advertised_SKU_Sales = 21,
   Seven_Day_Other_SKU_Sales = 22,
   LAST=22

output_header = [
   "Search term",
   "Impressions",
   "Clicks",
   "CTR",
   "CPC",
   "Spend",
   "Seven_Day_Total_Sales",
   "ACoS",
   "RoAS",
   "Seven_Day_Total_Orders",
   "Seven_Day_Total_Units",
   "Seven_Day_Total_Rate",
   "Seven_Day_Advertised_SKU_Units",
   "Seven_Day_Other_SKU_Units",
   "Seven_Day_Advertised_SKU_Sales",
   "Seven_Day_Other_SKU_Sales"]

list = []
for line in f_st:
  list.append(line.replace("%","")
              .replace("$","")
              .replace("\n","")
              .split('\t'))

filtered_list = {}

count=0
for i in range(len(list)):
    current_st=list[i][int(Header.Customer_Search_Term)]
    if(search_term.lower() in current_st.lower()):
        if(filtered_list.get(current_st) == None):
            filtered_list[current_st] = [0]*int(Header_Calc.LAST-Header_Calc.BASE+1)
        for j in range(Header_Calc.BASE,Header_Calc.LAST):
            calc_val = list[i][j].strip()
            if(RepresentsInt(calc_val) or RepresentsFloat(calc_val)):
                filtered_list[current_st][j-Header_Calc.BASE] += float(calc_val)

#fix CTR and ACOS
for key in filtered_list:
    Clicks = filtered_list[key][Header_Calc.Clicks - Header_Calc.BASE]
    Impressions = filtered_list[key][Header_Calc.Impressions - Header_Calc.BASE]
    Orders = filtered_list[key][Header_Calc.Seven_Day_Total_Orders - Header_Calc.BASE]
    Sales = filtered_list[key][Header_Calc.Seven_Day_Total_Sales - Header_Calc.BASE]
    Spend = filtered_list[key][Header_Calc.Spend - Header_Calc.BASE]
    if(Impressions == 0):
        filtered_list[key][Header_Calc.CTR - Header_Calc.BASE] = 0
    else:
        filtered_list[key][Header_Calc.CTR - Header_Calc.BASE] = Clicks / Impressions
    if(Sales == 0):
        filtered_list[key][Header_Calc.ACoS - Header_Calc.BASE] = 1000
    else:
        filtered_list[key][Header_Calc.ACoS - Header_Calc.BASE] = Spend / Sales

#print(filtered_list)
#Output
f = open("report.tsv", "a")
f.truncate(0)
line=""
for key in output_header:
    line += key + "\t"
f.write(line + "\n")
for key in filtered_list:
    line = "\t".join(format(x, "10.3f") for x in filtered_list[key])
    f.write(key + "\t" + line + "\n")
f.close()