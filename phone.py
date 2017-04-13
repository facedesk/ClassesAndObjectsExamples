 class phone:
 	def __init__(self,phone_number):
 		self.keys=[1,2,3,4,5,6,7,8,9]
 		self.dialtone="bwwwwwwwb"
 		self.phonenumber= phone_number
 		self.speaker= Speaker()
 		self.receiver= Receiver()
 	

 Classroom1Phone=phone("41412312434")
 Classroom2Phone=phone("4145424322")
 CavotosPersonalPhone=phone("0000000001")

