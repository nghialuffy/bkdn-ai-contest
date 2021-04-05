# Xây dựng 1 website có tên là “BKDN AI Contest” sử dụng Web Framework Django với các chức năng:

## 1. Yêu cầu chức năng:

    a. Trang login:

        i. Cần phân quyền người dùng:

            1. Admin

            2. Người tạo cuộc thi AI

            3. Người tham gia cuộc thi

    b. Trang Home:

        i. Có thể xem thông tin ngày giờ tổ chức các cuộc thi.
        
        ii. Có thể xem chi tiết từng cuộc thi bao gồm: đề thi, bảng ranking (xếp hạng theo độ chính xác),...
    
    c. Trang Admin:
        
        i. Có thể quản lý account
        
        ii. Có thể quản lý các cuộc thiiii. Quản lý ngôn ngữ (Python, Java, C/C++...) cho phép sử dụng
    
    d. Trang dành cho người tạo cuộc thi:
        i. Có thể quản lý các đề bài thi bao gồm: Yêu cầu, dữ liệu mẫu, dữ liệu huấn luyện, dữ liệu kiểm thử
        
        ii. Có thể upload code kiểm tra ouput của code kiểm thử của thí sinh trên dữ liệu kiểm thử có độ chính xác là bao nhiêu.
        
        iii. Có thể quản lý thời gian cuộc thi gồm: thời hạn đăng ký, thời gian bắt đầu, thời gian kết thúc, thời gian thực thi code kiểm thử.
        
        iv. Có thể thêm hoặc xóa đăng ký thông qua danh sách account của thí sinh.
        
        v. Có thể kiểm tra code của các thí sinh
        
    e. Trang dành cho thí sinh:
    
        i. Có thể xem thông tin các cuộc thi

        ii. Có thể đăng ký tham gia cuộc thi

        iii. Có thể nộp: mô hình đã train bằng file, Code huấn luyện và code kiểm thử. Có thể lựa chọn ngôn ngữ (Python, Java, C/C++...) để thực thi code kiểm thử

## 2. Yêu cầu kỹ thuật:

    a. Mỗi lần thí sinh upload mô hình và code kiểm thử, hệ thống phải tự động build code và thực thi code đó, đồng thời thực thi code kiểm tra để tính độ chính xác của mô hình, cập nhật bảng ranking. Phải tính đến trường hợp thời gian thưc thi quá lâu thì phải hủy process.

    b. Có thể triển khai trên 100 thí sinh cùng kết nối và tham gia cuộc thi

    c. Triển khai cấu hình trên Ubuntu Server 18.04 LTS. Viết tài liệu triển khai.

    d. Triển khai đặt tên miền và cài đặt chứng thực SSL. Viết tài liệu triển khai.