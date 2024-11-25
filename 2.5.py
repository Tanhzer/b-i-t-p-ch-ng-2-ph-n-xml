from xml.dom.minidom import parse
#Tải và phân tích tập tin XML
tai_lieu = parse("sample.xml")
#Lấy danh sách các phần tử 'name' trong tài liệu XML
ten_ptu = tai_lieu.getElementsByTagName("name")
#In ra tên của từng phần tử 'name'
for phan_tu in ten_ptu:
    print(phan_tu.firstChild.data)
