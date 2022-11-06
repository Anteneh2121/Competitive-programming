class Solution:
    def numberToWords(self, num: int) -> str:
        ones = ("", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine")
        teens = ("Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen")
        tens = ("", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety")
        
        def num_to_string(num):
            string = None
            if num // 10 ** 9:
                string = num_to_string(num // 10 ** 9) + " Billion " + num_to_string(num % 10 ** 9)
            elif num // 10 ** 6:
                string =  num_to_string(num // 10 ** 6) + " Million " + num_to_string(num % 10 ** 6)
            elif num // 10 ** 3:
                string =  num_to_string(num // 10 ** 3) + " Thousand " + num_to_string(num % 10 ** 3)
            elif num // 10 ** 2:
                string =  num_to_string(num // 10 ** 2) + " Hundred " + num_to_string(num % 10 ** 2)
            elif num // 10 == 1:
                string =  teens[num % 10]
            elif num // 10 > 1:
                string =  tens[num // 10] + " " + num_to_string(num % 10)
            else:
                string = ones[num]
            return string.strip()
                                                                                  
        if not num:
            return "Zero"
                                                                                  
        return num_to_string(num)
