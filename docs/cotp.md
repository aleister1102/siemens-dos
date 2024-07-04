# ISO Transport Protocol - Connection Oriented Transport Protocol (ISO 8073, RFC 905, X.224)

## TL;DR

Là giao thức giúp cung cấp các chức năng vận chuyển dữ liệu tương tự như TCP trong mạng ARPA, bao gồm multiplexing, demultiplexing, phát hiện lỗi, sửa lỗi và thậm chí là QoS.

## Introduction

ISO transport protocol (TP) nằm giữa transport service definition (xem thêm [TS](ts.md)) và network service definition:

```txt
-------------------------TRANSPORT SERVICE DEFINITION------------
     Transport     | --- Reference to aims --------------
     Protocol      |
     Specification | --- Reference to assumptions -------
-------------------------NETWORK SERVICE DEFINITION--------------
```

## Features

Các chức năng của TP mà được sử dụng trong tất cả các gói tin:
- Vận chuyển TPDU
- Multiplexing và demultiplexing
- Error detection
- Error recovery

Các chức năng khác:
- Thiết lập kết nối
- Vận chuyển dữ liệu
- Giải phóng kết nối

## Classes and Options

Các chức năng ở trong TP được chia thành nhiều lớp (class) và tùy chọn (option). Một lớp sẽ bao gồm một tập các chức năng. Các tùy chọn giúp chỉ định những chức năng trong một lớp mà có thể được hoặc không được sử dụng.

Danh sách các lớp:
- (a) Class 0: Simple Class.
- (b) Class 1: Basic Error recovery Class.
- (c) Class 2: Multiplexing Class.
- (d) Class 3: Error Recovery and Multiplexing Class.
- (e) Class 4: Error Detection and Recovery Class.

Việc quyết định xem class và option nào được sử dụng sẽ được thỏa thuận trong quá trình thiết lập kết nối.

## Connection establishment

Một TC được thiết lập bằng cách một thực thể vận chuyển (initiator) gửi một CR TPDU tới thực thể vận chuyển khác (responder), và responder sẽ trả lời bằng một CC TPDU. Trong quá trình trao đổi này, tất cả thông tin và tham số cần thiết cho các thực thể vận chuyển hoạt động sẽ được trao đổi hoặc thương lượng.

## Structure and encodings of TPDUs:

Bảng định danh cho các loại TPDU:

```txt
+-------------------------------------------------------------+
|                       | Validity within   |       |         |
|                       |     classes       |  see  |  Code   |
|                       |-------------------| Clause|         |
|                       | 0 | 1 | 2 | 3 | 4 |       |         |
|-----------------------|-------------------|-------|---------|
|CR Connection Request  | x | x | x | x | x | 13.3  |1110 xxxx|
|-----------------------|---|---|---|---|---|-------|---------|
|CC Connection Confirm  | x | x | x | x | x | 13.4  |1101 xxxx|
|-----------------------|---|---|---|---|---|-------|---------|
|DR Disconnect Request  | x | x | x | x | x | 13.5  |1000 0000|
|-----------------------|---|---|---|---|---|-------|---------|
|DC Disconnect Confirm  |   | x | x | x | x | 13.6  |1100 0000|
|-----------------------|---|---|---|---|---|-------|---------|
|DT Data                | x | x | x | x | x | 13.7  |1111 0000|
|-----------------------|---|---|---|---|---|-------|---------|
|ED Expedited Data      |   | x | NF| x | x | 13.8  |0001 0000|
|-----------------------|---|---|---|---|---|-------|---------|
|AK Data Acknowledgement|   |NRC| NF| x | x | 13.9  |0110 zzzz|
|-----------------------|---|---|---|---|---|-------|---------|
|EA Expedited Data      |   | x | NF| x | x | 13.10 |0010 0000|
|Acknowledgement        |   |   |   |   |   |       |         |
|-----------------------|---|---|---|---|---|-------|---------|
|RJ Reject              |   | x |   | x |   | 13.11 |0101 zzzz|
|-----------------------|---|---|---|---|---|-------|---------|
|ER TPDU Error          | x | x | x | x | x | 13.12 |0111 0000|
|-----------------------|---|---|---|---|---|-------|---------|
|                       |   |   |   |   |   |   -   |0000 0000|
|                       |---|---|---|---|---|-------|---------|
|not available          |   |   |   |   |   |   -   |0011 0000|
| (see note)            |---|---|---|---|---|-------|---------|
|                       |   |   |   |   |   |   -   |1001 xxxx|
|                       |---|---|---|---|---|-------|---------|
|                       |   |   |   |   |   |   -   |1010 xxxx|
+-------------------------------------------------------------+
```

Mỗi TPDU sẽ chứa một số nguyên các octet (byte). Các octet ở trong TPDU được đánh số từ 1 đến 8, các bit bên trong một octet cũng tương tự.

Mỗi TPDU sẽ bao gồm:
- Header:
    - Length indicator (LI)
    - Phần cố định (fixed part)
    - Phần có thể thay đổi (variable part), nếu có
- Data, nếu có:

```txt
octet    1   2 3 4 ... n   n+1  ...    p  p+1 ...end
        +---+-------------+--------------+-----------+
        | LI| fixed part  | variable part| data field|
        +---+-------------+--------------+-----------+
        <---------------   header ------>
```

### LI (Length Indicator)

Ở trong octet đầu tiên của TPDU, với giá trị lớn nhất là 254 (1111 1110). Giá trị này là kích thước của header cùng với các tham số (fixed part hoặc variable part), ngoại trừ user data và bản thân trường LI.

### Fixed part

Định nghĩa các tham số được sử dụng thường xuyên, bao gồm cả TPDU code (trong octet thứ 2).

Các TPDU code thường thấy:
- 1110 xxxx     Connection Request
- 1101 xxxx     Connection Confirm
- 0101 xxxx     Reject
- 0110 xxxx     Data Acknowledgement

### Variable part

Định nghĩa các tham số ít được sử dụng. Số lượng các tham số có trong phần này được tính bằng cách lấy LI trừ đi kích thước của fixed part.

Mỗi tham số có cấu trúc như sau:

```txt
         Bits   8    7    6    5    4    3    2    1
Octets          +------------------------------------+
 n+1            |          Parameter Code            |
                |------------------------------------|
 n+2            |          Parameter Length          |
                |          Indication (e.g. m)       |
                |------------------------------------|
 n+3            |                                    |
                |          Parameter Value           |
 n+2+m          |                                    |
                +------------------------------------|
```

Với:
- Parameter code là định danh của tham số. Không có parameter code nào sử dụng bit 7 và 8 là 00.
- Parameter length là kích thước của tham số (phần parameter value)
- Parameter value là giá trị của tham số

Thứ tự của các tham số được định nghĩa trong phần này là tùy ý. Nếu có bất kỳ một tham số nào bị lặp thì tham số được định nghĩa sau sẽ được sử dụng.

## Connection Request (CR) TPDU

Kích thước của CR TPDU không được vượt quá 128 byte.

### Fixed part

```txt
 1    2        3        4       5   6    7    8    p  p+1...end
+--+------+---------+---------+---+---+------+-------+---------+
|LI|CR CDT|     DST - REF     |SRC-REF|CLASS |VARIAB.|USER     |
|  |1110  |0000 0000|0000 0000|   |   |OPTION|PART   |DATA     |
+--+------+---------+---------+---+---+------+-------+---------+
```

Với:
- CDT là 4 bit đầu tiên của octet thứ 2. Giá trị của nó là 0000 đối với class 0 và class 1.
- SRC-REF là tham chiếu được chọn bởi thực thể khởi tạo TC.
- Bit 8-5 của octet thứ 7 sẽ chỉ định class. Các giá trị tương ứng với các class là: 
    - 0000: Class 0
    - 0001: Class 1
    - 0010: Class 2
    - 0011: Class 3
    - 0100: Class 4
- Trong khi đó, bit 4-1 của octet thứ 7 sẽ chỉ định các option. Các giá trị tương ứng với các option là:

```txt
+-----|-----------------------------------------------+
| BIT |                  OPTION                       |
|-----|-----------------------------------------------|
|  4  |  0   always                                   |
|     |                                               |
|  3  |  0   always                                   |
|     |                                               |
|  2  | =0   use of normal formats in all classes     |
|     | =1   use of extended formats in Classes 2,3,4 |
|     |                                               |
|  1  | =0   use of explicit flow control in Class 2  |
|     | =1   no use of explicit flow control in       |
|     |      Class 2                                  |
+-----------------------------------------------------+
```

### Variable part

Các tham số được phép (cho class 0):
- Transport Service Access Point Identifier (TSAP-ID):
    - Parameter code: 
        - 1100 0001 nếu là định danh TSAP của bên gửi (calling TSAP)
        - 1100 0010 nếu là định danh TSAP của bên nhận (called TSAP).
    - Parameter length: kích thước của định danh.
    - Parameter value: định danh của TSAP.
    - Nếu TSAP-ID được cung cấp ở trong request thì gói tin confirm cũng phải cung cấp TSAP-ID.
- TDPU size: kích thước TDPU đề xuất với đơn vị là octet bao gồm các cả trường header:
    - Parameter code: 1100 0000.
    - Parameter length: 1 octet.
    - Parameter value:
        - 0000 1101  8192 octets (không cho phép trong class 0)
        - 0000 1100  4096 octets (không cho phép trong class 0)
        - 0000 1011  2048 octets
        - 0000 1010  1024 octets
        - 0000 1001   512 octets
        - 0000 1000   256 octets
        - 0000 0111   128 octets
    - Giá trị mặc định là 0000 0111 (128 octets).

### User data

Gói tin CR có class 0 sẽ không chứa user data.

## Connection Confirm (CC) TPDU

Cấu trúc:

```txt
  1      2     3   4   5   6     7     8     p   p+1 ...end
+---+----+---+---+---+---+---+-------+--------+-------------+
|LI | CC  CDT|DST-REF|SRC-REF| CLASS |VARIABLE| USER        |
|   |1101|   |   |   |   |   | OPTION|  PART  | DATA        |
+---+----+---+---+---+---+---+-------+--------+-------------+
```

### Fixed part

- CC: 1101 ở bit 8-5 của octet thứ 2.
- CDT: 0000 đối với class 0 ở bit 4-1 của octet thứ 2.
- DST-REF: tham chiếu của thực thể khởi tạo TC.
- SRC-REF: tham chiếu của thực thể trả lời TC.
- Class và option: giống như CR TPDU.

### Variable part

Là các tham số được chọn từ CR TPDU.

### User data

Gói tin CC có class 0 sẽ không chứa user data.

## Data (DT) TPDU

Đối với class 0 và class 1 thì cấu trúc sẽ là:

```txt
  1       2         3          4       5             ... end
+----+-----------+-----------+------------ - - - - - -------+
| LI |    DT     |  TPDU-NR  | User Data                    |
|    | 1111 0000 |  and EOT  |                              |
+----+-----------+-----------+------------ - - - - - -------+
```

### Fixed part

- DT: 1111 0000
- EOT: nếu có giá trị là 1 thì có nghĩa là TPDU hiện tại là gói tin cuối cùng của chuỗi các TDPU. Giá trị nằm ở bit 8 của octet thứ 3 đối với class 0 và class 1.
- TPDU-NR: TDPU sequence number, có giá trị là 0 đối với class 0.

### User data

Chứa dữ liệu của TPDU. Kích thước dữ liệu bị giới hạn bởi kích thước TPDU mà đã được thỏa thuận trừ đi 3 octet (đối với class 0 và class 1). Nếu variable part có tồn tại thì cũng sẽ làm giảm kích thước của dữ liệu có trong TPDU.

Ref: https://datatracker.ietf.org/doc/html/rfc905