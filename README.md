Noi chua du lieu crawl

Các công đoạn cần thiết để preprocessing:
- Chuyển đổi encoding sang utf-8: 
	+) Xác định loại encoding:
		Sử dụng code mẫu, yêu cầu cài đặt lib chatdet của python 
			https://pypi.python.org/pypi/chardet
			http://chardet.readthedocs.io/en/latest/usage.html
	+) Convert sang utf8. Trên linux sử dụng iconv 
		Câu lệnh: iconv -f encoding_nguồn -t encoding_đích input_file -o output_file
			Ví dụ: iconv -f ASCII -t UTF-8 sample.txt -o output.txt
