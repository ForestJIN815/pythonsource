from openpyxl import Workbook


def write_excel_template(filename, sheetname, listdata):
    wb = Workbook()
    ws = wb.active

    # 제목열 너비 조절
    ws.column_dimensions["A"].width = 100
    # 시트명 변경
    ws.title = sheetname

    # 데이터 추가
    for item in listdata:
        ws.append(item)

    # 엑셀 저장
    wb.save("./" + filename)
    wb.close()


# test
if __name__ == "__main__":
    listdata = [
        [1, 10, 8, 5, 14, 26, 12],
        [2, 7, 3, 7, 15, 24, 18],
        [3, 9, 5, 8, 8, 12, 4],
        [4, 7, 8, 7, 17, 21, 18],
    ]
    write_excel_template("temp1.xlsx", "test", listdata)
