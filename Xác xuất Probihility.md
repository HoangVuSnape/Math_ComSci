
Trials and events 

Experriment                      Outcome/ event
	||                          -> 
	Trials     

Không gian mẫu =Omega

H: Head
T: tail of coin 


event: sự kiện xuất hiện 

# exercise 1
Toss a coin twice

Omega = {T, T}, {T, H}, {H, T}, {H, H} = 4

A = {T, T} = 1  
B = one H, one T == {HT, TH} 
C = First toss i H == {HH, HT} 
-> 
- P(a) = 1/4
- P(B) = 2/4
- P(C) = 2/4


A \ B: Only A. 

P(A U B U C) = 
Để tính P(A∪B∪C)P(A \cup B \cup C)P(A∪B∪C), ta sử dụng công thức tổng quát cho xác suất của hợp ba sự kiện:

P(A∪B∪C)=P(A)+P(B)+P(C)−P(A∩B)−P(A∩C)−P(B∩C)+P(A∩B∩C)P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)P(A∪B∪C)=P(A)+P(B)+P(C)−P(A∩B)−P(A∩C)−P(B∩C)+P(A∩B∩C)

Giải thích từng phần:

- P(A)P(A)P(A), P(B)P(B)P(B), và P(C)P(C)P(C) là xác suất của các sự kiện riêng biệt.
- P(A∩B)P(A \cap B)P(A∩B), P(A∩C)P(A \cap C)P(A∩C), và P(B∩C)P(B \cap C)P(B∩C) là xác suất của giao nhau giữa các cặp sự kiện.
- P(A∩B∩C)P(A \cap B \cap C)P(A∩B∩C) là xác suất của giao nhau ba sự kiện.

Nếu các sự kiện AAA, BBB, và CCC là độc lập (hoặc có các thông tin bổ sung về mối quan hệ giữa chúng), bạn có thể rút gọn công thức cho phù hợp.

### 1. **Xác suất (Probability - P)**

Xác suất là một số đo lường khả năng xảy ra của một sự kiện. Nó được tính trong không gian mẫu và không yêu cầu bất kỳ điều kiện bổ sung nào.

- **Công thức tính**: 
$$
P(A) = \frac{\text{Số kết quả có lợi cho A}}{\text{Tổng số kết quả có thể xảy ra}}
$$


Trong đó, 
$$
A \text{ là sự kiện mà ta muốn tính xác suất.}
$$

Ví dụ:
Khi tung một con xúc xắc, xác suất ra một số chẵn (2, 4, hoặc 6) là:

$$
P(\text{Số chẵn}) = \frac{3}{6} = 0.5
$$

Ở đây, xác suất là xác suất đơn giản, không có điều kiện gì.

![](assets/images/Pasted%20image%2020241206144636.png)


## Exercise 2:
To calculate \( P(A \cap B) \), which represents the probability of both events happening together:

- **B**: Red ball on the 1st pick.
- **A**: Black ball on the 2nd pick.

### Step 1: Understanding the Problem
- You have a total of 10 balls: 4 red balls and 6 black balls.
- You are performing two trials (picking twice without replacement).
- We are interested in finding \( P(A \cap B) \), the probability that you first pick a red ball (event B) and then pick a black ball (event A) on the second pick.

### Step 2: Calculate \( P(B) \) - Probability of picking a red ball on the first pick
The probability of picking a red ball on the first pick is the ratio of the number of red balls to the total number of balls in the bag:

$$
P(B) = \frac{4}{10} = 0.4
$$

### Step 3: Calculate \( P(A | B) \) - Probability of picking a black ball on the second pick given a red ball was picked on the first pick
After a red ball is picked, there are 9 balls left, and 6 of them are black. Thus, the probability of picking a black ball on the second pick, given that the first ball was red, is:

$$
P(A | B) = \frac{6}{9} = \frac{2}{3}
$$

### Step 4: Calculate$$ P(A \cap B) $$ - Probability of both events happening together
The probability of both events \( A \) and \( B \) occurring is the product of the probabilities of \( B \) (red ball on the first pick) and \( A | B \) (black ball on the second pick, given the first was red):

$$
P(A \cap B) = P(B) \times P(A | B) = \frac{4}{10} \times \frac{6}{9} = \frac{24}{90} = \frac{4}{15}
$$

Thus, the probability of picking a red ball on the first pick and a black ball on the second pick is:

$$
P(A \cap B) = \frac{4}{15}
$$

## Exercise 3: Xác xuất với nhiều Điều kiện
- Giải định
 3 classes
 Class1:  6 M and 4 F
 Class2:  10 M and 5 F
 Class1:  15 M and 10 F

A: Choose 1 F
B: Choose 1 student in Class 2

=> P (A giao B) = P(A|B) P(B) = 

----------------
Exercise : 
![](assets/images/Pasted%20image%2020241214095424.png)
Select random student . A. female
P(A)
### Cách 1:
![](assets/images/Pasted%20image%2020241214095619.png)
Solution 2:
- ![](assets/images/Pasted%20image%2020241214095806.png)
- ![](assets/images/Pasted%20image%2020241214095852.png)

## Exercise 4: 
![](assets/images/Pasted%20image%2020241214100634.png)
![](assets/images/Pasted%20image%2020241214100646.png)
![](assets/images/Pasted%20image%2020241214100657.png)

## Exercise 5
- 
- ![](assets/images/Pasted%20image%2020241214101709.png)
	- ![](assets/images/Pasted%20image%2020241214101737.png)
- ![](assets/images/Pasted%20image%2020241214102032.png)