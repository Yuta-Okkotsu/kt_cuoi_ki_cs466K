from point_data import *

StudentPoint = {
    'Điểm 1' : 0,
    'Điểm 2' : 0,
    'Điểm 3' : 0,
}
while True:
    print('\n----------------------Chương trình nhập điểm----------------------')
    print('Tên các cột điểm: Điểm 1, Điểm 2, Điểm 3')
    tenCotDiem = input('Nhập tên cột điểm muốn nhập: ')
    if tenCotDiem == 'exit':
        break
    elif tenCotDiem == 'Điểm 1':
        while True:
            diem = int(input('Mời nhập điểm muốn nhập: '))
            if diem >= 0 and diem <= 10:
                break
            else:
                print('Điểm chỉ nằm trong khoảng [0,10]')
        StudentPoint['Điểm 1'] = diem
    elif tenCotDiem == 'Điểm 2':
        while True:
            diem = int(input('Mời nhập điểm muốn nhập: '))
            if diem >= 0 and diem <= 10:
                break
            else:
                print('Điểm chỉ nằm trong khoảng [0,10]')
        StudentPoint['Điểm 2'] = diem
    elif tenCotDiem == 'Điểm 3':
        while True:
            diem = int(input('Mời nhập điểm muốn nhập: '))
            if diem >= 0 and diem <= 10:
                break
            else:
                print('Điểm chỉ nằm trong khoảng [0,10]')
        StudentPoint['Điểm 3'] = diem
    else:
        print('Nhập cho đúng tên cột điểm hoặc bấm exit để thoát chương trình!!!')
    print(StudentPoint)
    
print('Tổng số điểm:', PointSum(StudentPoint))
print('Điểm trung bình cộng:', PointAverage(StudentPoint))
print('Điểm cao nhất và thấp nhất:', PointMaxMin(StudentPoint))



