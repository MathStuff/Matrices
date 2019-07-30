from typing import List

class dataframe:
    pass

class null:
    def __repr__(self):
        return 'null'
    def __str__(self):
        return 'null'
    def __call__(self):
        return null
        
null = null()

class date:
    """
    Date object, define patterns for the date and time data
    data: str; string format of the data
    pattern: str; string to format the data with. 
    delimiters: list of strings; delimiters to use
    
    Usage:
        day "d"
        month "m"
        year "y"

        hour "h"
        minute "n"
        second "s"
 
        milli "3"
        micro "6"
        nano "9"

        timezone "t"

        Create a pattern using the terms above. Example:

            Example pattern             Expected input pattern                     Expected input sample

             yyyy/mm/dd             -->  Year/Month/Day                        -->  2019/10/25
             dd hh:nn:ss            -->  Day Hours:Minutes:Seconds             -->  25 16:32:55
             yyyymmdd,ttttt,hh:nn   -->  YearMonthDay,timezone,Hours:Minutes   -->  19980409,UTC+3,21:45

    """
    def __init__(self,date:str,pattern:str,delimiters:List[str],config:str="default"):
        self.date = date
        self.delimiters = delimiters
        self.pattern = self.fixpattern(pattern)
    
    @staticmethod
    def fixpattern(pattern,cfg):
        if cfg == "default":
            day,month,year = "d","m","y"
            hour,minute,second = "h","n","s"
            milli,micro,nano = "3","6","9"
            tzone = "t"
            terms = [day,month,year,hour,minute,second,milli,micro,nano,tzone]
            delims = self.delimiters[:]

            #Assert given delimiters are valid
            for delimiter in delims:
                if delimiter in terms:
                    raise ValueError(f"Character {delimiter} can't be used as a delimiter")

            input_pattern_term_indices = {"d":0,"m":0,"y":0,"h":0,"n":0,"s":0,"3":0,"6":0,"9":0}
            delimiter_indices = {i:[] for i in delims}
            #Check for terms' every appearance
            for term in terms:
                #Regex pattern for repeated characters
                term_pattern = term + "+"
                
                #Find out what repeated characters patterns are
                partition = {i:[] for i in sorted(re.findall(term_pattern,pattern),reverse=True)}
                
                #Store starting and the ending points of the found patterns
                for part in list(partition.keys()):
                    pattern_copy = pattern[:]
                    while True:
                        lap = 0
                        try:
                            #Start getting all indices of the pattern
                            while part in pattern_copy:
                                l = len(part)
                                ind = pattern_copy.index(part)
                                #Replace the used part with question marks
                                pattern_copy = pattern_copy[:ind] + pattern_copy[ind+l:]
                        except:
                            #Store them
                            input_pattern_term_indices[term][part].append((ind+l*lap,ind+l*(lap+1)))
                            lap += 1
                        else:
                            #All indices stored, get to the next pattern
                            break
                #Should have input_pattern_term_indices -> {"d":{"ddd":[(1,4),(5,8)],"d":[(15,16)]},"m":...}
                
                #Create a regex pattern for the entire pattern using collected indices
                pass

    def __repr__(self):
        return "".join(re.findall(self.date,self.pattern))

class Group:
    def __init__(self,matrix_list,names):
        self.groups = [val[0] for val in matrix_list]
        self.table = [val[1] for val in matrix_list]
        self.grouped_by = names


    