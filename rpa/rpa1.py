# RPA(Robotic Process Automation) : 자동화 프로그램
# ex) 엑셀자동화 프로그램
# 엑셀 pip install openpyxl
# 이미지 pip install pillow

# 엑셀 파일 생성
from openpyxl import Workbook

# 객체 생성
wb = Workbook()

wb.save("./rpa/sample.xlsx")
wb.close()
