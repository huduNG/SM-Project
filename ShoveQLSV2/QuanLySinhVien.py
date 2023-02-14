import math
from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self) -> None:
        pass
    listSinhVien = []
    
    # Hàm tạo ID tăng dần
    def generateID(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    
    def soLuongSinhVien(self):
        return self.listSinhVien. __len__()
    
    # Khởi tạo một sinh viên mới
    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Giới tính: ")
        age = int(input("Độ tuổi: "))
        diemToan = float(input("Nhập điểm Toán: "))
        diemLy = float(input("Nhập điểm Lý: "))
        diemHoa = float(input("Nhập điểm Hóa: "))
        sv = SinhVien(svId, name, sex, age, diemToan, diemLy, diemHoa)
        self.tinhDTB(sv)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
        
    # Tìm kiếm sinh viên trong danh sách
    def updateSinhVien(self, ID):
        sv:SinhVien = self.findByID(ID)
    # Nếu tồn tại thì nhập thông tin sinh viên
        if (sv != None):
            # Nhập thông tin sinh viên
            name = input("Nhập tên sinh viên: ")
            sex = input("Giới tính: ")
            age = int(input("Nhập tuổi: "))
            diemToan = float(input("Nhập điểm Toán: "))
            diemLy = float(input("Nhập điểm Lý: "))
            diemHoa = float(input("Nhập điểm Hóa: "))
            # Cập nhật thông tin
            sv._name = name
            sv._sex = sex
            sv._age = age
            sv._diemToan = diemToan
            sv._diemLy = diemLy
            sv._diemHoa = diemHoa
            self.tinhDTB(sv)
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh viên có ID = {} không tồn tại.".format(ID))
            
    # Hàm sắp xếp danh sách sinh viên theo ID tăng dần
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
        
    # Hàm sắp xếp danh sách sinh viên theo tên tăng dần
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
        
    # Hàm sắp xếp danh sách sinh viên theo điểm trung bình tăng dần
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)
        
    # Hàm tìm kiếm sinh viên theo ID
    # Trả về một sinh viên
    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
    
    # Hàm tìm kiếm sinh viên theo tên
    # Trả về một danh sách sinh viên
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                 if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    
    # Hàm xóa sinh viên theo ID
    def deleteById(self, ID):
        isDelete = False
        # Tìm kiếm sinh viên theo ID
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    # Hàm tính điểm trung bình cho sinh viên
    def tinhDTB(self, sv:SinhVien):
        diemTB = (sv._diemToan + sv._diemLy + sv._diemHoa) / 3
        # Làm tròn điểm trung bình với 2 chữ số thập phân
        sv._diemTB = math.ceil(diemTB * 100) / 100
        
    # Hàm xếp loại học lực cho nhân viên
    def xepLoaiHocLuc(self, sv:SinhVien):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Giỏi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Khá"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"
            
    # Hàm hiển thị danh sách sinh viên ra màn hình console
    def showSinhVien(self, listSV):
        # Hiển thị tiêu đề cột
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Age", "Toan", "Ly", "Hoa", "Diem TB", "Hoc Luc"))
        # hien thi danh sach sinh vien
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                      .format(sv._id, sv._name, sv._sex, sv._age, sv._diemToan, sv._diemLy, 
                              sv._diemHoa, sv._diemTB, sv._hocLuc))
        print("\n")
    
    # Hàm trả về danh sách sinh viên hiện tại
    def getListSinhVien(self):
        return self.listSinhVien