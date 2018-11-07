import string, random

class Solution_0001:
    
    def generate_random_str(self,groups,number,lengh): #多少组激活码，每组激活码长度有几个激活码，每个激活码有几位

        coupon_list = []

        for i in range(groups):
            group = "-".join(["".join(random.sample(string.ascii_letters + string.digits,lengh)) for i in range(number)])
            coupon_list.append(group)
        return coupon_list

coupon = Solution_0001()
coupon_list = coupon.generate_random_str(10,4,4)
print(coupon_list)
filename = "0001.txt"
with open(filename,'w') as file:
    for i in coupon_list:
        file.write(i+"\n")


