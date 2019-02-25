#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import re
from PyPDF2 import PdfFileReader

sub=["APPLIED ELECTRONICS & INSTRUMENTATION ENGINEERING","CIVIL ENGINEERING","MECHANICAL ENGINEERING","ELECTRONICS & COMMUNICATION ENGG","COMPUTER SCIENCE & ENGINEERING","ELECTRICAL AND ELECTRONICS ENGINEERING"]
subject_split_format=r"AE[0-9]+|EE[0-9]+|CS[0-9]+|IT[0-9]+|EC[0-9]+|CE[0-9]+|ME[0-9]+|HS[0-9]+"
reg_split_format=r"RET[0-9]+AE[0-9]+|RET[0-9]+EE[0-9]+|RET[0-9]+CS[0-9]+|RET[0-9]+IT[0-9]+|RET[0-9]+EC[0-9]+|RET[0-9]+CE[0-9]+|RET[0-9]+ME[0-9]+"
sub1_dt={}
sub1_list_dt={}

document_name ="result_RET.csv"

def text_extractor(path):
    finalpage="";
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        page = pdf.getPage(0)
        text = page.extractText()
        simpleText="[Full Time]Course CodeCourse"
        val=text.split(sub[0]+simpleText)
        newval=val[1].split("Register NoCourse Code (Grade)")
        x = re.findall(subject_split_format, newval[0])
        y = re.split(subject_split_format, newval[0])[1:]
        # print(x)
        # print(y)
        if len(x) == len(y):
            for i in range(len(x)):
                sub1_dt[x[i]]=y[i]
        else:
            print("failed")
        # print (sub1_dict)
        m = re.findall(reg_split_format, newval[1])
        n = re.split(reg_split_format, newval[1])[1:]
        # print(newval[1])
        n[0]=n[0].strip()
        df=n[0].split(',')
        with open(document_name, mode='w') as csv_file:
            result_writer = csv.writer(csv_file, delimiter='^', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            result_writer.writerow(['University No. ,'+','.join(list(sub1_dt.keys()))])
            row=m[0]
            for i in range(len(df)):
                for j in range(len(sub1_dt)):
                    if list(sub1_dt.keys())[j] in df[i]:
                        # print(list(sub1_dt.keys())[j]+ " =>"+df[i] )
                        x= df[i][:-1].strip().split("(")[1]
                        x=","+x
                        # x = re.split(r',',)
                        row+=x
                        # print(x)
            result_writer.writerow([row])
        # q=re.split(, df[0])
        # print(n[0])
        print(df)
        # print(q[0])
        print(m)
        # print(list(sub1_dt.keys())[1])


			


if __name__ == '__main__':
    path = 'result_RET.pdf'

    text_extractor(path)