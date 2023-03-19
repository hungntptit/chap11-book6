# chap11-book6

Chương 11 Sách 6. Designing Microservices using Django

Cần tạo project rồi copy các file code sang.

4 project django chạy ở các cổng khác nhau, dùng database riêng: 
- user_service - postgres - 8000
- product_service - postgres - 3001
- shipment_service - sqlite - 5000
- payment_service - sqlite - 4001

Với mỗi project dùng postgres cần tạo user và database như trong sách. Khi migrate trong django có thể không được thì cần đổi owner của database là user tương ứng.


