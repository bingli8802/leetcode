class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        day, mon, year = date.split(" ")
        
        month_map = {"Jan":"01", "Feb":"02", 
                     "Mar":"03", "Apr":"04", 
                     "May":"05", "Jun":"06", 
                     "Jul":"07", "Aug":"08", 
                     "Sep":"09", "Oct":"10", 
                     "Nov":"11", "Dec":"12"}
        mon = month_map[mon]
        day = day[:-2]
        
        # return "%s-%s-%02d" % (year, mon, int(day)
        return "%s-%s-%02d" % (year, mon, int(day))

