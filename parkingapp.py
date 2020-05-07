
import datetime
from datetime import datetime as dt 

class Parkingmanager:

	

	def __init__(self, vehiclenumber, vehicletype, fourwheeler_slots, twowheeler_slots,intime,exittime):
		self.vehiclenumber=vehiclenumber
		self.vehicletype=vehicletype
		self.fourwheeler_slots=fourwheeler_slots
		self.twowheeler_slots=twowheeler_slots
		self.intime=intime
		self.exittime=exittime


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


print("welcome to the parking lot")
details={}

while True:
	print('-'*30)
	ch=int(input("what would you like to do \n 1.enter \n 2.exit \n-->"))

	if ch==1:
		vehiclenumber=input("enter your vehiclenumber")
		vehicletype=int(input("enter whether your vehicle is a 2 wheeler of 4 wheeler"))
		fourwheeler_slots=100
		twowheeler_slots=50
		intime=dt.now()
		exittime=0
		vehicledetails=Parkingmanager(vehiclenumber,vehicletype,fourwheeler_slots,twowheeler_slots,intime,exittime)
		details[vehiclenumber]=vehicledetails
		print(f"\n WELCOME! \n you have entered at {intime} ")
		print('-'*10)


		if vehicletype==4:
			vehicledetails.enter4()
			vehicledetails.slotsleft()

		elif vehicletype==2:
			vehicledetails.enter2()
			vehicledetails.slotsleft()

	elif ch==2:
		
		vehiclenumber=input("enter your vehiclenumber")
		exittime=dt.now()
		vehicledetails=details[vehiclenumber]
		print(f"\n you have exited at {exittime} \n THANK YOU VISIT AGAIN")
		print('-'*10)	

		if vehicletype==4:
			vehicledetails.exit4()
			vehicledetails.slotsleft()
			
		if vehicletype==2:
			vehicledetails.exit2()
			vehicledetails.slotsleft()
		
	else:
		break