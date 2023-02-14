from QuanLySinhVien import QuanLySinhVien
# Khởi tạo một đối tượng QuanLySinhVien để quản lý sinh viên
qlsv = QuanLySinhVien()
while (1==1):
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("The Menu")
    print("1. Thêm sinh viên.")
    print("2. Cập nhật thông tin sinh viên bởi ID. ")
    print("3. Xóa sinh viên bởi ID. ")
    print("4. Tìm kiếm sinh viên theo tên. ")
    print("5. Sắp xếp sinh viên theo điểm trung bình (GPA). ")
    print("6. Sắp xếp sinh viên theo tên. ")
    print("7. Sắp xếp sinh viên theo ID. ")
    print("8. Hiển thị danh sách sinh viên. ")
    print("0. Thoát")
    
    key = int(input("Nhập tùy chọn: "))
    if (key == 1):
        print("\n1. Thêm sinh viên. ")
        qlsv.nhapSinhVien()
        print("\nThêm sinh viên thành công! ")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cập nhật thông tin sinh viên. ")
            print("\nNhap ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
            print("\nCập nhật danh sách sinh viên thành công! ")
        else:
            print("\nDanh sách sinh viên trống! ")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xóa sinh viên. ")
            print("\nNhap ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSinh viên có id = ", ID, "đã bị xóa. ")
            else:
                print("\nSinh viên có id = ", ID, "không tồn tại. ")
        else:
            print("\nDanh sách sinh viên trống!")
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tìm kiếm sinh viên theo tên.")
            print("\nNhập tên để tìm kiếm: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sách sinh viên trống! ")
    elif (key ==5):
        if (qlsv.soLuongSinhVien() >0 ):
            print("\n5. Sắp xếp sinh viên theo điểm trung bình (GPA). ")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống! ")
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sắp xếp sinh viên theo tên. ")
            qlsv.sortByName()    
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else: 
            print("\nDanh sách sinh viên trống! ")
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Sắp xếp sinh viên theo ID. ")
            qlsv.sortByID()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống! ")
    elif (key == 8):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n8. Hiển thị danh sách sinh viên. ")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống! ")
    elif (key == 0):
        print("\nBạn đã chọn thoát chương trình! ")
        break
    else:
        print("\nKhông có chức năng này! ")
        print("\nVui lòng chọn chức năng khác trong Menu! ")