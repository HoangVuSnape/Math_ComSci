Đây là phần tìm hiểu về navie bayes

# Link
- [Naive Bayes](https://machinelearningcoban.com/2017/08/08/nbc/)
- [code scratch NB](https://viblo.asia/p/ml-from-scratch-thuat-toan-phan-loai-naive-bayes-viblo-aNj4vXOqL6r)

- https://machinelearningcoban.com/2017/07/17/mlemap/

- https://www.youtube.com/watch?v=lFJbZ6LVxN8
- https://www.youtube.com/watch?v=O2L2Uv9pdDA
- https://www.youtube.com/watch?v=H3EjCKtlVog


- [Bernoulli- medium](https://towardsdatascience.com/bernoulli-naive-bayes-explained-a-visual-guide-with-code-examples-for-beginners-aec39771ddd6)
-  [Gau NB- medium](https://towardsdatascience.com/gaussian-naive-bayes-explained-a-visual-guide-with-code-examples-for-beginners-04949cef383c)
- https://www.instagram.com/p/C_CUwtAyVI3/?img_index=7
https://cafedev.vn/tu-hoc-ml-bo-phan-loai-naive-bayes/?utm_source=chatgpt.com

Code 
- [Spam NB](https://colab.research.google.com/github/pmuens/lab/blob/master/x-from-scratch/naive-bayes-from-scratch.ipynb#scrollTo=j1XZWQdzknVT)
- 

![](assets/images/Pasted%20image%2020250101182544.png)


![](assets/images/Pasted%20image%2020250102151708.png)
![](assets/images/Pasted%20image%2020250102151720.png)
# Bernoullio Naive Bayes
![](assets/images/Pasted%20image%2020250102160740.png)

![](assets/images/Pasted%20image%2020250102153620.png)

Đầu vào của Bernouliio là Binary nên là phải convert ,  thường dùng là onehot encoding cho label. 
![](assets/images/Pasted%20image%2020250102153745.png)

## Các bước thực hiện: 
1. **Tính xác suất của mỗi lớp (class) trong dữ liệu huấn luyện.** 
2. **Với mỗi đặc trưng và lớp, tính xác suất của đặc trưng có giá trị 1 và 0 dựa trên lớp đó.** 
3. **Đối với một trường hợp mới:** - Với mỗi lớp, nhân xác suất của lớp đó với xác suất của từng giá trị đặc trưng (0 hoặc 1) ứng với lớp đó. 
4. **Dự đoán:** - Lớp được dự đoán là lớp có xác suất kết quả cao nhất.

![](assets/images/Pasted%20image%2020250102161642.png)


### Bước 1: Tính toán xác suất các lớp
![](assets/images/Pasted%20image%2020250102162125.png)

### Bước 2**Tính xác suất đặc trưng**: Đối với mỗi đặc trưng và mỗi lớp, thực hiện tính toán:

- (Số lượng trường hợp mà đặc trưng có giá trị 0 trong lớp này) / (Tổng số trường hợp trong lớp này)
- (Số lượng trường hợp mà đặc trưng có giá trị 1 trong lớp này) / (Tổng số trường hợp trong lớp này)
![](assets/images/Pasted%20image%2020250102162250.png)
Cùng là tính như trên nhưng mà là toàn bộ feature

![](assets/images/Pasted%20image%2020250102162303.png)
![](assets/images/Pasted%20image%2020250102162336.png)

![](assets/images/Pasted%20image%2020250102162351.png)

## Test 
![](assets/images/Pasted%20image%2020250102162424.png)
![](assets/images/Pasted%20image%2020250102162436.png)
Sau khi tính ra và cho xác xuất thì sẽ so sánh y và y^. 

![](assets/images/Pasted%20image%2020250102162450.png)

## Chú ý
Bernoulli Naive Bayes có một số tham số quan trọng:

- **Alpha (α):** Đây là tham số làm mịn (smoothing). Nó thêm một lượng nhỏ vào mỗi đặc trưng để tránh xác suất bằng 0. Giá trị mặc định thường là 1.0 (Laplace smoothing), như đã được minh họa trước đó.
- **Binarize:** Nếu các đặc trưng của bạn chưa phải dạng nhị phân, ngưỡng này sẽ chuyển đổi chúng. Bất kỳ giá trị nào lớn hơn ngưỡng này sẽ trở thành 1, và bất kỳ giá trị nào nhỏ hơn sẽ trở thành 0.

![](assets/images/Pasted%20image%2020250102163125.png)

Đối với **BernoulliNB** trong scikit-learn, các đặc trưng số thường được chuẩn hóa thay vì được nhị phân hóa thủ công. Mô hình sau đó sẽ tự động chuyển đổi các giá trị đã chuẩn hóa này sang nhị phân, thường sử dụng 0 (giá trị trung bình) làm ngưỡng.

- **Fit Prior:** Xác định việc học xác suất tiên nghiệm của các lớp (class prior probabilities) hay giả định xác suất tiên nghiệm đồng đều (50/50).
![](assets/images/Pasted%20image%2020250102163152.png)
### **Ưu điểm và Nhược điểm của Bernoulli Naive Bayes**

#### **Ưu điểm:**

1. **Đơn giản:**
    - Dễ dàng triển khai và hiểu.
2. **Hiệu quả:**
    - Huấn luyện và dự đoán nhanh, hoạt động tốt ngay cả với không gian đặc trưng lớn.
3. **Hiệu suất với dữ liệu nhỏ:**
    - Có thể hoạt động tốt ngay cả khi dữ liệu huấn luyện bị hạn chế.
4. **Xử lý dữ liệu có chiều cao:**
    - Hoạt động tốt với tập dữ liệu có nhiều đặc trưng, đặc biệt trong các bài toán phân loại văn bản.

#### **Nhược điểm:**

1. **Giả định độc lập:**
    - Giả định rằng tất cả các đặc trưng là độc lập, điều này thường không đúng trong dữ liệu thực tế.
2. **Giới hạn cho đặc trưng nhị phân:**
    - Chỉ hoạt động với dữ liệu nhị phân trong dạng thuần túy.
3. **Nhạy cảm với dữ liệu đầu vào:**
    - Hiệu suất phụ thuộc nhiều vào cách các đặc trưng được nhị phân hóa.
4. **Vấn đề tần suất bằng không:**
    - Nếu không sử dụng làm mịn, xác suất bằng 0 có thể ảnh hưởng mạnh đến kết quả dự đoán.

---

### **Nhận xét cuối cùng**

Thuật toán Bernoulli Naive Bayes là một mô hình máy học đơn giản nhưng mạnh mẽ dành cho phân loại nhị phân. Nó đặc biệt xuất sắc trong các ứng dụng như phân tích văn bản và phát hiện thư rác, nơi các đặc trưng thường là nhị phân. Với tốc độ và hiệu quả vượt trội, nó hoạt động tốt ngay cả với các tập dữ liệu nhỏ và có chiều cao.

Dù giả định độc lập giữa các đặc trưng có vẻ không thực tế, Bernoulli Naive Bayes thường cho kết quả chính xác tương đương với các mô hình phức tạp hơn. Đây là một công cụ cơ bản đáng tin cậy và hữu ích trong phân loại thời gian thực.
# Gaussian Naive Bayes
![](assets/images/Pasted%20image%2020250103203437.png)
![](assets/images/Pasted%20image%2020250103203453.png)

## Feature probability calculation 
![](assets/images/Pasted%20image%2020250102161316.png)

![](assets/images/Pasted%20image%2020250102161343.png)
![](assets/images/Pasted%20image%2020250102161409.png)

![](assets/images/Pasted%20image%2020250103203611.png)


![](assets/images/Pasted%20image%2020250103203630.png)
![](assets/images/Pasted%20image%2020250103203644.png)
![](assets/images/Pasted%20image%2020250102230325.png)![](assets/images/Pasted%20image%2020250103215306.png)