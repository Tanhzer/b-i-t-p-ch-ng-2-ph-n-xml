from xml.dom import minidom
# Tải và phân tích file XML
ten_file = "sample.xml"  # Đường dẫn tới file XML
doc = minidom.parse(ten_file)
# Lấy thông tin từ các phần tử
ten_cty = doc.getElementsByTagName("name")[0].firstChild.data
print("Tên Cty:", ten_cty)
staffs = doc.getElementsByTagName("staff")
for nhan_vien in staffs:
    nhan_vien_id = nhan_vien.getAttribute("id")
    nhan_vien_name = nhan_vien.getElementsByTagName("name")[0].firstChild.data
    nhan_vien_salary = nhan_vien.getElementsByTagName("salary")[0].firstChild.data
    print(f"Staff ID: {nhan_vien_id}")
    print(f"Tên: {nhan_vien_name}")
    print(f"Salary: {nhan_vien_salary}")
    print("-----------------------------")
