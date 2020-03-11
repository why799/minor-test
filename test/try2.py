trans1={0: "zero",1: "one",2: "two",3: "three", 4: "four",5: "five",6: "six",7: "seven",8: "eight",9: "nine"}
trans2={10: "ten",11: "eleven",12: "twelve",13: "thirteen",14: "fourteen",15: "fifteen", 16: "sixteen",17: "seventeen",18: "eighteen",19: "nineteen",2: "twenty",3: "thirty",4: "forty",5: "fifty",6: "sixty", 7: "seventy",8: "eighty",9: "ninety"}
for us_num in range(0,100):
        if us_num >= 0 and us_num < 10:
          print(trans1[us_num])
        elif us_num > 9 and us_num < 20:
           print(trans2[us_num])
        elif us_num > 19 and us_num < 100:
           if(us_num%10==0):
             print(trans2[us_num//10])
           else:
            tens = trans2[us_num//10]+' '+trans1[us_num%10]
            print(tens)




