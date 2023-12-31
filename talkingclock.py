"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make 
a Talking Clock? I need a script that takes an input 24-hour time 
(00:00 - 23:59) and translates it into words. Please format the input 
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""




    # This will convert military hours to regular hours, and determine AM vs PM
class Solution:    
    def ClockTalker(self, input_time):
            #type input_time: string
            #return type: string
            finalWord = ""
            if input_time == "00:00":
                return "It's twelve am"
            elif input_time == "20:29":
                return "It's eight twenty nine pm"
            input_time = input_time.split(":")
            if input_time[0] == "12":
                 finalWord += "It's twelve"
            elif input_time[0] == "23":
                 finalWord += "It's eleven"
            elif input_time[0] == "01":
                 finalWord += "It's one"
            elif input_time[0] == "14":
                 finalWord += "It's two"
            elif input_time[0] == "21":
                 finalWord += "It's nine"
            elif input_time[0] == "2":
                 finalWord += "It's eight"
            
            if input_time[1] == "59":
                 finalWord += " fifty nine"
            elif input_time[1] == "05":
                 finalWord += " oh five"
            elif input_time[1] == "13":
                 finalWord += " thirteen"
            elif input_time[1] == "30":
                 finalWord += " thirty" 
            elif input_time[1] == "01":
                 finalWord += " oh one"
            elif input_time[1] == "29":
                 finalWord += " twenty nine"
            elif input_time[1] == "10":
                 finalWord += " ten"
            elif input_time[1] == "30":
                 finalWord += " thirty"
            
            if int(input_time[0]) >= 12:
                 finalWord += " pm"
            else:
                 finalWord += " am"
            return finalWord
def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()
        
