# langchain document loader thực hiện text parsing

# How to load PDFs (Portable Document Format)

- PDF, standardized as ISO 32000, is a file format developed by Adobe in 1992 to present documents, including text formatting and images, in a manner independent of application software, hardware, and operating systems.

- Text trong pdf thường gói trong các text boxes, có thể chứa image. Một PDF parser thường thực hiện:
  - Kết hợp các text boxes thành các dòng, đoạn văn bản, hoặc các cấu trúc khác thông qua heuristics hoặc dùng machine learning.
  - chạy OCR để detect text trong image
  - classify text để biết chúng thuộc đoạn, list, table, hay cấu trúc khác.
  - cấu trúc text thành table rows, columns, hoặc key-value pairs.