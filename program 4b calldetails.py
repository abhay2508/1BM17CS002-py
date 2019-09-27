
class CallDetail:
    def __init__(self,phoneno,called_no,duration,call_type):
        self.__phoneno=phoneno
        self.__called_no=called_no
        self.__duration=duration
        self.__call_type=call_type
        print(self.__dict__)
   

class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        self.list_of_call_objects=[]
        for i in list_of_call_string:
            phoneno,called_no,duration,call_type=map(str,i.split(","))
            self.list_of_call_objects.append(CallDetail(phoneno,called_no,duration,call_type))
    #def finlist(self):
        #print(self.list_of_call_objects)
        #print(self.__dict__)

call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
x=Util()
x.parse_customer(list_of_call_string)
#x.finlist()
