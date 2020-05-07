
class Parkingmanager:

	

	def __init__(self, vehiclenumber, vehicletype, fourwheeler_slots, twowheeler_slots,intime,exittime):
		self.vehiclenumber=vehiclenumber
		self.vehicletype=vehicletype
		self.fourwheeler_slots=fourwheeler_slots
		self.twowheeler_slots=twowheeler_slots
		self.intime=intime
		self.exittime=exittime


	# def exittime(self):
	# 	self.y=dt.now()
	# 	print(f"you left at {self.y}")

	def enter4(self):
		self.fourwheeler_slots-=1

	def enter2(self):
		self.twowheeler_slots-=1

	def exit4(self):
		self.fourwheeler_slots+=1
	def exit2(self):
		self.twowheeler_slots+=1
	
	def slotsleft(self):
		print(f"no of 4 wheeler slots left = {self.fourwheeler_slots}")
		print(f"no of 2 wheeler slots left = {self.twowheeler_slots}")




		

# p = Parkingmanager('ka1234', '4' , 100 , 50)
# p.enter4()
# p.slotsleft()
# p.enter2()
# p.slotsleft()

	


