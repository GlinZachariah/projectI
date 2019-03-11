#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
from PyPDF2 import PdfFileReader
import re
import os
syspath =os.path.dirname(os.path.realpath(__file__))
syspath = syspath.replace('\\', '/')
mediapath=syspath+"/media/output/"

course=["APPLIED ELECTRONICS & INSTRUMENTATION ENGINEERING","ELECTRONICS & COMMUNICATION ENGG","COMPUTER SCIENCE & ENGINEERING","ELECTRICAL AND ELECTRONICS ENGINEERING","INFORMATION TECHNOLOGY","MECHANICAL ENGINEERING","CIVIL ENGINEERING"]
subject_split_format=r"AE[0-9]+|EE[0-9]+|CS[0-9]+|IT[0-9]+|EC[0-9]+|CE[0-9]+|ME[0-9]+|HS[0-9]+"
reg_split_format=r"RET[0-9]+AE[0-9]+|RET[0-9]+EE[0-9]+|RET[0-9]+CS[0-9]+|RET[0-9]+IT[0-9]+|RET[0-9]+EC[0-9]+|RET[0-9]+CE[0-9]+|RET[0-9]+ME[0-9]+"
filename=["AE","EC","CS","EE","IT","ME","CE"]

def text_extractor(path):
    finalpage="";
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        for pg in range(pdf.numPages):
            page = pdf.getPage(pg)
            text = page.extractText()
            finalpage+=text
    return finalpage
			
def split_courses(pages,dat):
    simplePattern=r" ?\[Full ?Time\] ?Course ?Code ?Course"
    #fix subject order if necessary
    
    pre=re.split(course[0]+simplePattern ,pages)
    # pre= pages.split(course[0]+simplePattern)
    temp=re.split(course[1]+simplePattern ,pre[1])
    # temp=pre[1].split(course[1]+simplePattern)
    applied = temp[0]
    temp=re.split(course[2]+simplePattern ,temp[1])
    # temp=temp[1].split(course[2]+simplePattern)
    ec=temp[0]
    temp=re.split(course[3]+simplePattern ,temp[1])
    # temp=temp[1].split(course[3]+simplePattern)
    cse=temp[0]
    temp=re.split(course[4]+simplePattern ,temp[1])
    # temp=temp[1].split(course[4]+simplePattern)
    eee=temp[0]
    temp=re.split(course[5]+simplePattern ,temp[1])
    # temp=temp[1].split(course[5]+simplePattern)
    it=temp[0]
    temp=re.split(course[6]+simplePattern ,temp[1])
    # temp=temp[1].split(course[6]+simplePattern)
    mech=temp[0]
    temp=temp[1].split(dat)
    civil=temp[0]
    ls= [applied,ec,cse,eee,it,mech,civil]
    count=0
    for newl in ls:
        split_subjects(newl,count)
        count+=1

def split_subjects(newl,cnt):
    sub1_dt={}
    newval=newl.split("Register NoCourse Code (Grade)")
    subject_code = re.findall(subject_split_format, newval[0])
    subject_name = re.split(subject_split_format, newval[0])[1:]
    if len(subject_code) == len(subject_name):
        for i in range(len(subject_code)):
            sub1_dt[subject_code[i]]=subject_name[i]
    else:
        print("Subject count error")
        return
    make_csv(newval,cnt,subject_code)

def make_csv(newval,cnt,subject_code):
    reg_no = re.findall(reg_split_format, newval[1])
    sub_list = re.split(reg_split_format, newval[1])[1:]
    with open(mediapath+"result_"+filename[cnt]+".csv", mode='w',newline='') as csv_file:
            result_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # result_writer = csv.writer(csv_file, delimiter=',', escapechar="'", quoting=csv.QUOTE_NONE)
            result_writer.writerow(['University No. ,'+','.join(subject_code)])
            print("working")
            for i in range(len(reg_no)):
                df=reg_no[i].strip().split(",")
                cdf=sub_list[i]
                cdf_list = cdf.split(",")
                row=df[0]+','
                grade=''
                for k in subject_code:
                    flag=0
                    for l in cdf_list:
                        if  l.strip()[:5]in k:
                            flag=1
                            grade=l.strip()[:-1].split("(")[1]
                            grade=grade+','
                            row+=grade
                    if flag==0:
                        grade=','
                        row+=grade
                result_writer.writerow([row])
    with open(mediapath+"result_"+filename[cnt]+".csv", 'r') as f, open(mediapath+"result_RET_"+filename[cnt]+".csv", 'w') as fo:
        for line in f:
            fo.write(line.replace('"', '').replace("'", ""))
    os.remove(mediapath+"result_"+filename[cnt]+".csv")
        
    

def res_gen(path,dat):
    print(path)
    print("************")
    path=syspath+path
    print(syspath)
    print(path)
    # path = input('Enter filename : (result_RET.pdf)')
    # path="result_RET.pdf"
    # order= input('Enter order of courses')
    # input the last end date to split the document
    # if path == "":
        # path="result_RET.pdf"
    page = text_extractor(path)
    split_courses(page,dat)
    # print (page)