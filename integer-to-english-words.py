# Time O(n)
# Space O(1) recursive stack O(3)
class Solution:
    def __init__(self):
        self.below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens_set = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
        self.triples = ["", " Thousand", " Million", " Billion"]

    def numberToWords(self, num: int) -> str:
        result = ""
        i = 0
        if num == 0: return "Zero"
        while num > 0:
            triplet = num % 1000
            if triplet != 0:
                wording = self.readTriplet(triplet)
                result = wording + self.triples[i] + (" " + result if result else "")
            i += 1
            num = num // 1000
        return result

    def readTriplet(self, num: int) -> str:
        #print(num, num % 10, num // 10, num % 100, num // 100)
        if num < 20: return self.below_20[num]
        elif num < 100: return self.tens_set[num // 10] + (" " + self.readTriplet(num % 10) if num % 10 != 0 else "")
        else: return self.below_20[num // 100] + " " + "Hundred" + (" " + self.readTriplet(num % 100) if num % 100 != 0 else "")