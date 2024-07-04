# ISO Transport Service on top of the TCP

## TL;DR

Giao thức này triển khai các dịch vụ của ISO transport service (TS) và ISO transport protocol (TP) bằng cách sử dụng những dịch vụ và giao diện được cung cấp bởi TCP.

Giao thức tương tự của ISO-over-TCP trong ARPA là TCP.

## ISO Protocol Suite

Bộ giao thức Internet ARPA và bộ giao thức ISO đều là các hệ thống phân lớp.

Bộ giao thức ISO trao đổi thông tin giữa các đối tượng đồng cấp (peers) bằng các đơn vị thông tin riêng lẻ được gọi là các đơn vị dữ liệu giao thức vận chuyển (transport protocol data unit - TPDU).

## The Model

ISO transport service (ISO 8072, xem thêm: [TSAP](tsap.md)) mô tả các dịch vụ do TS provider cung cấp và các giao diện được sử dụng để truy cập các dịch vụ đó. 

Giao thức này sử dụng ARPA Transmission Control Protocol (TCP) (RFC793) để cung cấp các dịch vụ và giao diện thỏa mãn ISO transport service (TS) và ISO transport protocol (ISO 8073) (TP).

```txt
+-----------+                                       +-----------+
|  TS-user  |                                       |  TS-user  |
+-----------+                                       +-----------+
    |                                                     |
    | TSAP interface                       TSAP interface |
    |  [ISO8072]                                          |
    |                                                     |
+----------+   ISO Transport Services on the TCP     +----------+
|  client  |-----------------------------------------|  server  |
+----------+              (this memo)                +----------+
    |                                                     |
    | TCP interface                         TCP interface |
    |  [RFC793]                                           |
    |                                                     |
```

Cụ thể hơn, giao thức ánh xạ các sự kiện và hành động được cung cấp bởi TCP sang các primitive mà được yêu cầu bởi TP. Ngoài ra, giao thức cũng cung cấp các primitive của TS cho TS user.

## Packet Format

Một sự khác biệt cơ bản giữa TCP và TP là TCP quản lý một octet (byte) stream liên tục, không có ranh giới rõ ràng. Trong khi đó, TP mong đợi thông tin được gửi và nhận trong các đối tượng riêng lẻ được gọi là các đơn vị dữ liệu dịch vụ mạng (NSDU). Có thể xem một NSDU là một TPDU.

Mỗi gói trong giao thức này, gọi là TPKT, được coi là một đối tượng bao gồm nhiều byte dữ liệu, có độ dài thay đổi. Một TPKT bao gồm hai phần: header và TPDU. Định dạng của header là cố định bất kể loại gói nào.

```txt
0                   1                   2                   3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|      vrsn     |    reserved   |          packet length        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

Với:
- vrsn (8 bit): luôn là 3 cho phiên bản của giao thức này.
- packet length (16 bit) (tối thiểu=7, tối đa=65535): chứa độ dài của toàn bộ gói tin, bao gồm cả tiêu đề gói. Điều này cho phép kích thước TPDU tối đa là 65531 byte.

Định dạng được sử dụng cho ED TPDU (expedited TPDU, các gói tin ưu tiên) gần giống với định dạng cho dữ liệu thông thường. Sự khác biệt duy nhất là giá trị được sử dụng cho `code` TPDU là ED, không phải DT:

```txt
0                   1                   2                   3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| header length | code  |credit |TPDU-NR and EOT|   user data   |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|      ...      |      ...      |      ...      |      ...      |
|      ...      |      ...      |      ...      |      ...      |
|      ...      |      ...      |      ...      |      ...      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

Ref: https://datatracker.ietf.org/doc/html/rfc1006