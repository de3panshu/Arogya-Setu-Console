import os
import mysql.connector
from prettytable import PrettyTable


## checking for the database exist or not, if not creating the database.
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
myresult = mycursor.fetchall();
isDBexist = False;
for x in myresult:
  if x == ("arogyasetuapp",):
  	isDBexist=True;
if isDBexist == False:
	mycursor.execute("CREATE DATABASE arogyasetuapp");
## database creation ends here.

## creating user tables.
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "arogyasetuapp"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW Tables;")
myresult = mycursor.fetchall();
isTableExist = False;
for x in myresult:
  if x == ("user",):
  	isTableExist=True;
if isTableExist == False:
	mycursor.execute("CREATE TABLE USER(name char(40), mobile char(10), state int(2), city int(2),risk int, covid char(3));");

## table creation done succesfully
states = {
	1 : "Andaman and Nicobar Island",
	2 : "Andhra Pradesh",
	3 : "Arunachal Pradesh",
	4 : "Assam",
	5 : "Bihar",
	6 : "Chandigarh",
	7 : "Chhattisgarh",
	8 : "Dadra and Nagar Haveli",
	9 : "Daman and Diu",
	10: "Delhi",
	11: "Goa",
	12: "Gujarat",
	13: "Haryana",
	14: "Himachal Pradesh",
	15: "Jammu and Kashmir",
	16: "Jharkhand",
	17: "Karnataka",
	18: "Kerala",
	19: "Ladakh",
	20: "Lakshadweep",
	21: "Madhya Pradesh",
	22: "Maharashtra",
	23: "Manipur",
	24: "Meghalaya",
	25: "Mizoram",
	26: "Nagaland",
	27: "Odisha",
	28: "Pondicherry",
	29: "Punjab",
	30: "Rajasthan",
	31: "Sikkim",
	32: "Tamil Nadu",
	33: "Telangana",
	34: "Tripura",
	35: "Uttarakhand",
	36: "Uttar Pradesh",
	37: "West Bengal"
}

districts = {
	1 : {1:"Nicobar", 2:"North And Middle Andaman", 3:"South Andaman", 4:"Others"},
	2 : {1:"Anantapur", 2:"Chittoor", 3:"Cuddapah", 4:"East Godavari" ,5:"Guntur",6:"Krishna",7:"Kurnool",8:"Nellore",9:"Prakasam",10:"Srikakulam",11:"Vishakapatnam",12:"Vizianagaram",13:"West Godavari",14:"Others"},
	3 : {1:"Anjaw",2:"Changlang",3:"Dimang Valley",4:"East Kameng",5:"East Siang",6:"Itanagar",7:"Kamle",8:"Kra Daadi",9:"Kurung Kumey",10:"Lepa Rada",11:"Lohit",12:"Longding",13:"Lower Dibang Valley",14:"Lower Subansiri",15:"Namsai",16:"Pakke  Kessang",17:"Papum Pare",18:"Shi Yomi",19:"Siang",20:"Tawang",21:"Tirap",22:"Upper iang",23:"Upper Subansiri",24:"West Kameng",25:"West Siang",26:"Others"},
	4 : {1: "Baksa",2:"Barpet",3:"Bishwanath",4:"Bongaigaon",5:"Cachar",6:"Charaideo",7:"Chirang",8:"Darrang",9:"Dhemaji",10:"Dhubri",11:"Dibrugarh",12:"Dima Hasao",13:"Goalpara",14:"Golaghat",15:"Hailakandi",16:"Hojai",17:"Jorhat",18:"Kamrup",19:"Kamrup Metropolitan",20:"Karbi Anglong",21:"Karimganj",22:"Kokrajhar",23:"Lakhimpur",24:"Majuli",25:"Morigaon",26:"Nagaon",27:"Nalbari",28:"Others",29:"Sivasagar",30:"Sonitpur",31:"South Salamara-Mankachar",32:"Tinsukia",33:"Udalguri",34:"West Karbi Anglong"},
	5 : {1: "Araria",2:"Arwal",3:"Aurangabad",4:"Banka",5:"Begusarai",6:"Bhagalpur",7:"Bhojpur",8:"Buxar",9:"Darbhanga",10:"East Champaran",11:"Gaya",12:"Gopalganj",13:"Jamui",14:"Jehanabad",15:"Kaimur",16:"Katihar",17:"Khagaria",18:"Kishanganj",19:"Lakhisarai",20:"Madhepura",21:"Madhubani",22:"Munger",23:"Muzaffarpur",24:"Nalanda",25:"Nawada",26:"Others",27:"Patna",28:"Purnia",29:"Rohtas",30:"Saharsa",31:"Samastipur",32:"Saran",33:"Seikhpura",34:"Sheohar",35:"Sitamarhi",36:"Siwan",37:"Supaul",38:"Vaishali",39:"West Champaran"},
	6 : {1:"Chandigarh",2:"Others"},
	7 : {1:"Balod",2:"Baloda Bazar",3:"Balrampur",4:"Bastar",5:"Bemetara",6:"Bijapur",7:"Bilaspur",8:"Dantewada (South Bastar)",9:"Dhamtari",10:"Durg",11:"Gariyaband",12:"Janjgir-Champa",13:"Jashpur",14:"Kabirdham (Kawardha)",15:"Kanker (North Bastar)",16:"Kondagaon",17:"Korba",18:"Korea (Koriya)",19:"Mahasamund",20:"Mungeli",21:"Narayanpur",22:"Raigarh",23:"Raipur",24:"Rajnandgaon",25:"Sukma",26:"Surajpur",27:"Surguja"},
	8 : {1:"Dadra & Nagar Haveli"},
	9 : {1:"Daman",2:"Diu"},
	10: {1:"Central Delhi",2:"East Delhi",3:"New Delhi",4:"North Delhi",5:"North East Delhi",6:"North West Delhi",7:"Shahdara",8:"South Delhi",9:"South East Delhi",10:"South West Delhi",11:"West Delhi"},
	11: {1:"North Goa",2:"South Goa"},
	12: {1:"Ahmedabad",2:"Amreli",3:"Anand",4:"Aravalli",5:"Banaskantha (Palanpur)",6:"Bharuch",7:"Bhavnagar",8:"Botad",9:"Chhota Udepur",10:"Dahod",11:"Dangs (Ahwa)",12:"Devbhoomi Dwarka",13:"Gandhinagar",14:"Gir Somnath",15:"Jamnagar",16:"Junagadh",17:"Kachchh",18:"Kheda (Nadiad)",19:"Mahisagar",20:"Mehsana",21:"Morbi",22:"Narmada (Rajpipla)",23:"Navsari",24:"Panchmahal (Godhra)",25:"Patan",26:"Porbandar",27:"Rajkot",28:"Sabarkantha (Himmatnagar)",29:"Surat",30:"Surendranagar",31:"Tapi (Vyara)",32:"Vadodara",33:"Valsad"},
	13: {1:"Ambala",2:"Bhiwani",3:"Charkhi Dadri",4:"Faridabad",5:"Fatehabad",6:"Gurugram (Gurgaon)",7:"Hisar",8:"Jhajjar",9:"Jhajjar",10:"Jind",11:"Kaithal",12:"Karnal",13:"Kurukshetra",14:"Mahendragarh",15:"Nuh",16:"Palwal",17:"Panchkula",18:"Panipat",19:"Rewari",20:"Rohtak",21:"Sirsa",22:"Sonipat",23:"Yamunanagar"},
	14: {1:"Bilaspur",2:"Chamba",3:"Hamirpur",4:"Kangra",5:"Kinnaur",6:"Kullu",7:"Lahaul & Spiti",8:"Mandi",9:"Shimla",10:"Sirmaur (Sirmour)",11:"Solan",12:"Una"},
	15: {1:"Anantnag",2:"Bandipore",3:"Baramulla",4:"Budgam",5:"Doda",6:"Ganderbal",7:"Jammu",8:"Kathua",9:"Kishtwar",10:"Kulgam",11:"Kupwara",12:"Poonch",13:"Pulwama",14:"Rajouri",15:"Ramban",16:"Reasi",17:"Samba",18:"Shopian",19:"Srinagar",20:"Udhampur"},
	16: {1:"Bokaro",2:"Chatra",3:"Deoghar",4:"Dhanbad",5:"Dumka",6:"East Singhbhum",7:"Garhwa",8:"Giridih",9:"Godda",10:"Gumla",11:"Hazaribag",12:"Jamtara",13:"Khunti",14:"Koderma",15:"Latehar",16:"Lohardaga",17:"Pakur",18:"Palamu",19:"Ramgarh",20:"Ranchi",21:"Sahibganj",22:"Seraikela-Kharsawan",23:"Simdega",24:"West Singhbhum"},
	17: {1:"Bagalkot",2:"Ballari (Bellary)",3:"Belagavi (Belgaum)",4:"Bengaluru (Bangalore) Rural",5:"Bengaluru (Bangalore) Urban",6:"Bidar",7:"Chamarajanagar",8:"Chikballapur",9:"Chikkamagaluru (Chikmagalur)",10:"Chitradurga",11:"Dakshina Kannada",12:"Davangere",13:"Dharwad",14:"Gadag",15:"Hassan",16:"Haveri",17:"Kalaburagi (Gulbarga)",18:"Kodagu",19:"Kolar",20:"Koppal",21:"Mandya",22:"Mysuru (Mysore)",23:"Raichur",24:"Ramanagara",25:"Shivamogga (Shimoga)",26:"Tumakuru (Tumkur)",27:"Udupi",28:"Uttara Kannada (Karwar)",29:"Vijayapura (Bijapur)",30:"Yadgir"},
	18: {1:"Alappuzha",2:"Ernakulam",3:"Idukki",4:"Kannur",5:"Kasaragod",6:"Kollam",7:"Kottayam",8:"Kozhikode",9:"Malappuram",10:"Palakkad",11:"Pathanamthitta",12:"Thiruvananthapuram",13:"Thrissur",14:"Wayanad"},
	19: {1:"Kargil",2:"Leh"},
	20: {1:"Lakshadweep"},
	21: {1:"Agar Malwa",2:"Alirajpur",3:"Anuppur",4:"Ashoknagar",5:"Balaghat",6:"Barwani",7:"Betul",8:"Bhind",9:"Bhopal",10:"Burhanpur",11:"Chhatarpur",12:"Chhindwara",13:"Damoh",14:"Datia",15:"Dewas",16:"Dhar",17:"Dindori",18:"Guna",19:"Gwalior",20:"Harda",21:"Hoshangabad",22:"Indore",23:"Jabalpur",24:"Jhabua",25:"Katni",26:"Khandwa",27:"Khargone",28:"Mandla",29:"Mandsaur",30:"Morena",31:"Narsinghpur",32:"Neemuch",33:"Panna",34:"Raisen",35:"Rajgarh",36:"Ratlam",37:"Rewa",38:"Sagar",39:"Satna",40:"Sehore",41:"Seoni",42:"Shahdol",43:"Shajapur",44:"Sheopur",45:"Shivpuri",46:"Sidhi",47:"Singrauli",48:"Tikamgarh",49:"Ujjain",50:"Umaria",51:"Vidisha"},
	22: {1:"Ahmednagar",2:"Akola",3:"Amravati",4:"Aurangabad",5:"Beed",6:"Bhandara",7:"Buldhana",8:"Chandrapur",9:"Dhule",10:"Gadchiroli",11:"Gondia",12:"Hingoli",13:"Jalgaon",14:"Jalna",15:"Kolhapur",16:"Latur",17:"Mumbai City",18:"Mumbai Suburban",19:"Nagpur",20:"Nanded",21:"Nandurbar",22:"Nashik",23:"Osmanabad",24:"Palghar",25:"Parbhani",26:"Pune",27:"Raigad",28:"Ratnagiri",29:"Sangli",30:"Satara",31:"Sindhudurg",32:"Solapur",33:"Thane",34:"Wardha",35:"Washim",36:"Yavatmal"},
	23: {1:"Bishnupur",2:"Chandel",3:"Churachandpur",4:"Imphal East",5:"Imphal West",6:"Jiribam",7:"Kakching",8:"Kamjong",9:"Kangpokpi",10:"Noney",11:"Pherzawl",12:"Senapati",13:"Tamenglong",14:"Tengnoupal",15:"Thoubal",16:"Ukhrul"},
	24: {1:"East Garo Hills",2:"East Jaintia Hills",3:"East Khasi Hills",4:"North Garo Hills",5:"Ri Bhoi",6:"South Garo Hills",7:"South West Garo Hills",8:"South West Khasi Hills",9:"West Garo Hills",10:"West Jaintia Hills",11:"West Khasi Hills"},
	25: {1:"Aizawl",2:"Champhai",3:"Kolasib",4:"Lawngtlai",5:"Lunglei",6:"Mamit",7:"Saiha",8:"Serchhip"},
	26: {1:"Dimapur",2:"Kiphire",3:"Kohima",4:"Longleng",5:"Mokokchung",6:"Mon",7:"Peren",8:"Phek",9:"Tuensang",10:"Wokha",11:"Zunheboto"},
	27: {1:"Angul",2:"Balangir",3:"Balasore",4:"Bargarh",5:"Bhadrak",6:"Boudh",7:"Cuttack",8:"Deogarh",9:"Dhenkanal",10:"Gajapati",11:"Ganjam",12:"Jagatsinghapur",13:"Jajpur",14:"Jharsuguda",15:"Kalahandi",16:"Kandhamal",17:"Kendrapara",18:"Kendujhar (Keonjhar)",19:"Khordha",20:"Koraput",21:"Malkangiri",22:"Mayurbhanj",23:"Nabarangpur",24:"Nayagarh",25:"Nuapada",26:"Puri",27:"Rayagada",28:"Sambalpur",29:"Sonepur",30:"Sundargarh"},
	28: {1:"Karaikal",2:"Mahe",3:"Puducherry",4:"Yanam"},
	29: {1:"Amritsar",2:"Barnala",3:"Bathinda",4:"Faridkot",5:"Fatehgarh Sahib",6:"Fazilka",7:"Ferozepur",8:"Gurdaspur",9:"Hoshiarpur",10:"Jalandhar",11:"Kapurthala",12:"Ludhiana",13:"Mansa",14:"Moga",15:"Muktsar",16:"Nawanshahr",17:"Pathankot",18:"Patiala",19:"Rupnagar",20:"Sahibzada",21:"Sangrur",22:"Tarn Taran"},
	30: {1:"Ajmer",2:"Alwar",3:"Banswara",4:"Baran",5:"Barmer",6:"Bharatpur",7:"Bhilwara",8:"Bikaner",9:"Bundi",10:"Chittorgarh",11:"Churu",12:"Dausa",13:"Dholpur",14:"Dungarpur",15:"Hanumangarh",16:"Jaipur",17:"Jaisalmer",18:"Jalore",19:"Jhalawar",20:"Jhunjhunu",21:"Jodhpur",22:"Karauli",23:"Kota",24:"Nagaur",25:"Pali",26:"Pratapgarh",27:"Rajsamand",28:"Sawai Madhopur",29:"Sikar",30:"Sirohi",31:"Sri Ganganagar",32:"Tonk",33:"Udaipur"},
	31: {1:"East Sikkim",2:"North Sikkim",3:"South Sikkim",4:"West Sikkim"},
	32: {1:"Ariyalur",2:"Chengalpattu",3:"Chennai",4:"Coimbatore",5:"Cuddalore",6:"Dharmapuri",7:"Dindigul",8:"Erode",9:"Kallakurichi",10:"Kanchipuram",11:"Kanyakumari",12:"Karur",13:"Krishnagiri",14:"Madurai",15:"Nagapattinam",16:"Namakkal",17:"Nilgiris",18:"Perambalur",19:"Pudukkottai",20:"Ramanathapuram",21:"Ranipet",22:"Salem",23:"Sivaganga",24:"Tenkasi",25:"Thanjavur",26:"Theni",27:"Thoothukudi",28:"Tiruchirappalli",29:"Tirunelveli",30:"Tirupathur",31:"Tiruppur",32:"Tiruvallur",33:"Tiruvannamalai",34:"Tiruvarur",35:"Vellore",36:"Viluppuram",37:"Virudhunagar"},
	33: {1:"Adilabad",2:"Bhadradri Kothagudem",3:"Hyderabad",4:"Jagtial",5:"Jangaon",6:"Jayashankar Bhoopalpally",7:"Jogulamba Gadwal",8:"Kamareddy",9:"Karimnagar",10:"Khammam",11:"Komaram Bheem Asifabad",12:"Mahabubabad",13:"Mahabubnagar",14:"Mancherial",15:"Medak",16:"Medchal",17:"Nagarkurnool",18:"Nagarkurnool",19:"Nalgonda",20:"Nirmal",21:"Nizamabad",22:"Peddapalli",23:"Rajanna Sircilla",24:"Rangareddy",25:"Sangareddy",26:"Siddipet",27:"Suryapet",28:"Vikarabad",29:"Wanaparthy",30:"Warangal (Rural)",31:"Warangal (Urban)",32:"Yadadri Bhuvanagiri"},
	34: {1:"Dhalai",2:"Gomati",3:"Khowai",4:"North Tripura",5:"Sepahijala",6:"South Tripura",7:"Unakoti",8:"West Tripura"},
	35: {1:"Almora",2:"Bageshwar",3:"Chamoli",4:"Champawat",5:"Dehradun",6:"Haridwar",7:"Nainital",8:"Pauri Garhwal",9:"Pithoragarh",10:"Rudraprayag",11:"Tehri Garhwal",12:"Udham Singh Nagar",13:"Uttarkashi"},
	36: {1: "Agra",2:"Aligarh",3:"Allahabad",4:"Ambedkar Nagar",5:"Amethi",6:"Amroha (J.P. Nagar)",7:"Auraiya",8:"Azamgarh",9:"Baghpat",10:"Bahraich",11:"Ballia",12:"Balrampur",13:"Banda",14:"Barabanki",15:"Bareilly",16:"Basti",17:"Bhadohi",18:"Bijnor",19:"Budaun",20:"Bulandshahr",21:"Chandauli",22:"Chitrakoot",24:"Deoria",25:"Etah",26:"Etawah",27:"Faizabad",28:"Farrukhabad",29:"Fatehpur",30:"Firozabad",31:"Gautam Buddha Nagar",32:"Ghaziabad",33:"Ghazipur",34:"Gonda",35:"Gorakhpur",36:"Hamirpur",37:"Hapur",38:"Hardoi",39:"Hathras",40:"Jalaun",41:"Jaunpur",42:"Jhansi",43:"Kannauj",44:"Kanpur",45:"Dehat",46:"Kanpur Nagar",47:"Kanshiram Nagar",48:"Kaushambi",49:"Kushinagar",50:"Lakhimpur - Kheri",51:"Lalitpur",52:"Lucknow",53:"Maharajganj",54:"Mahoba",55:"Mainpuri",56:"Mathura",57:"Mau",58:"Meerut",59:"Mirzapur",60:"Moradabad",61:"Muzaffarnagar",62:"Pilibhit",63:"Pratapgarh",64:"RaeBareli",65:"Rampur",66:"Saharanpur",67:"Sambhal (Bhim Nagar)",68:"Sant Kabir Nagar",69:"Shahjahanpur",70:"Shamali (Prabuddh Nagar)",71:"Shravasti",72:"Siddharth Nagar",73:"Sitapur",74:"Sonbhadra",75:"Sultanpur",76:"Unnao",77:"Varanasi"},
	37: {1:"Alipurduar",2:"Bankura",3:"Birbhum",4:"Cooch Behar",5:"Dakshin Dinajpur",6:"Darjeeling",7:"Hooghly",8:"Howrah",9:"Jalpaiguri",10:"Jhargram",11:"Kalimpong",12:"Kolkata",13:"Malda",14:"Murshidabad",15:"Nadia",16:"North 24 Parganas",17:"Paschim",18:"Medinipur",19:"Paschim (West) Burdwan",20:"Purba Burdwan",21:"Purba Medinipur",22:"Purulia",23:"South 24 Parganas",24:"Uttar Dinajpur"}
}

loginFlag = True
exitFlag = False
dashboardFlag = False
#userdetails
username = "XYZ"
usermobile = "0000000000"
userstate = -1
usercity = -1
risk = 0
covid = "NO"
'''def bgCheck():
	cwd = os.getcwd() # current working directory
	cwd = os.path.join(cwd,"covid updates") # cwd\covid updates\
	directory = ""
	for state in states:
		directory = str(sos.path.join(cwd,states[state])) # 
		if not os.path.exists(directory):
			os.makedirs(directory)
		##	print("\n",states[state],"\n")
		for city in districts[state]:
			#file name with complete path.
			(open(directory+"/"+districts[state][city]+".txt","a+")).close();
		##	print(" | ",districts[state][city])
'''
def register_user():
	#update incoming details to user database 
	#if already exist return false otherwise true.
	result = False
	'''
	user_details = open(USER_FILE,"a")
	if search_user() == False:
    	
		user_details.write(username+"\n")
		user_details.write(usermobile+"\n")
		user_details.write(str(userstate)+"\n")
		user_details.write(str(usercity)+"\n")
		result = True
	user_details.close()
	'''
	global mycursor
	global username
	global userstate
	global usercity
	global usermobile
	global risk
	global covid
	global states
	global districts
	query = "INSERT INTO USER VALUES('"+username+"','"+usermobile+"',"+str(userstate)+","+str(usercity)+","+str(risk)+",'"+covid+"');"
	if search_user() == False:
		mycursor.execute(query);
		if mycursor.rowcount>0:
			result = True;
	else:
		print("\nYou are already register as",username)
	return result

def get_user_details():
	
	global username
	global usermobile
	global userstate
	global usercity
	global risk
	global covid
#	print(username,usermobile,userstate,usercity,risk,covid); ## need to be comment out at the end
	username = input("\t            Enter your name: ")
	usermobile = input("\t Enter your mobile number: ")
	count = 1
	for state in states:
		print(count," ",states[state]);
		count=count+1
	userstate = int(input("\t          Enter your state: "))
	count = 1;
	for city in districts[userstate]:
		print(count," ",districts[userstate][city])
		count=count+1
	usercity = int(input("\t            Enter your city: "))
	risk = 0
	covid = "NO"
#	print(username,usermobile,userstate,usercity,risk,covid); ## need to be comment out at the end
def search_user():
		#search user details via global usermobile and put all those data in global variables
	res = False
	global mycursor
	global usermobile;
	global username
	global userstate
	global usercity
	global risk
	global covid
	query = "select * from user where mobile = '"+usermobile+"';"
	mycursor.execute(query);
	dbResult = mycursor.fetchall()
	if mycursor.rowcount>0:
		res = True
		for x in dbResult:
			username = x[0]
			usermobile = x[1]
			userstate = int(x[2])
			usercity = int(x[3])
			userrisk = int(x[4])
			covid = x[5]
		#if x==(usermobile,):
		#	res=True
			
	#user_details = open(USER_FILE,"r")
	'''	for mobile in user_details:
		if usermobile+"\n" == mobile:
			res = True
	user_details.close()
	'''
	return res
	
def display_covid_updates():
	print("===================================== STATE WISE COVID UPDATES =====================================\n")
	#print("+---------------------------------+----------------------+-------------------------+----------------+")
	#print("|             State               |   Total Population   |   Affected Population   |   Percentage   |")#35 20
	#print("+---------------------------------+----------------------+-------------------------+----------------+")
	global mycursor
	global states
	global districts
	t = PrettyTable(['State', 'Total Population','Affected Population','Percentage'])
	#t.add_rows([['Name', 'Age'], ['Alice', 24], ['Bob', 19]])
	#print(t.draw())
	for state in states:
		mycursor.execute("SELECT count(*) from user where state ="+str(state)+";")
		myresult = mycursor.fetchall()
		tp = int(myresult[0][0])
		mycursor.execute("SELECT count(*) from user where state ="+str(state)+" && covid = 'YES';")
		myresult = mycursor.fetchall()
		ap = int(myresult[0][0])
		if tp == 0:
			per = 0.0
		else:
			per = ap*100/tp
		t.add_row([states[state],tp,ap,str(per)+"%"])
		#print(states[state]+" | "+str(tp)+" | "+str(ap)+" | "+str(per)+"%")
	print(t)	
	# covid  updates of userstate citywise
	global userstate

	t = PrettyTable(['State','Total Population','Affected Population','Percentage'])
	print("\n\n===================================== "+states[userstate]+" COVID UPDATES =====================================\n")
	for city in districts[userstate]:
		mycursor.execute("SELECT count(*) from user where state ="+str(userstate)+" && city ="+str(city)+";")
		myresult = mycursor.fetchall()
		tp = int(myresult[0][0])
		mycursor.execute("SELECT count(*) from user where state ="+str(userstate)+" && city ="+str(city)+" && covid = 'YES';")
		myresult = mycursor.fetchall()
		ap = int(myresult[0][0])
		if tp == 0:
			per = 0.0
		else:
			per = ap*100/tp
		t.add_row([districts[userstate][city],tp,ap,str(per)+"%"])
		#print(districts[userstate][city]+" | "+str(tp)+" | "+str(ap)+" | "+str(per)+"%")
	print(t)
def asses_yourself():
	#get  some inputs related  to covid sysmtomps estimate the risk
	risk = 100
	question = 1

	if question==1:
		ans = int(input("\nEnter your age: "))
		if ans>18 and ans<50:
			risk = risk-10;
		question=2

	if question==2:
		ans = input("\nHave you taken vaccination(Y/N): ")
		if ans=="Y" or ans=='y':
			risk=risk-10
			question=3
		elif ans=="N" or ans=="n":
			question=7

	if question==3:
		ans = int(input("\n1:First dose\n2:Both doses\nNumber of doses taken by you:"))
		if ans==1:
			risk=risk-20
		elif ans==2:
			risk = risk-40
		question = 4

	if question==4:
		ans == input("\nDid you have covid in the past 3 months or after vaccination?(Y/N): ")
		if ans=="Y" or ans=="y":
			question=5
		elif ans=="N" or ans=="n":
			question=7

	if question==5:
		print("\n1: Within a week\n2: Within 1-2 weeks\n3: Within 3-4 weeks\n4: After 4 weeks")
		ans = int(input("\nHow many days after  vaccination you become covid positive? :"))
		
		if ans==1: risk=risk+10
		elif ans==2: risk=risk+7
		elif ans==3: risk=risk+5
		elif ans==4: risk = risk+3 
		question=6

	if question==6:
		print("\n1: No symptoms\n2: Mild\n3: Took medication, no hospital\n4: Hospitalisation of oxygen\n5: Critical illness requiring high oxygen or ICU")
		ans = int(input("\nSeverity of symptoms: "))
		if ans==2: risk=risk+10
		elif ans==3: risk=risk+15
		elif ans==4: risk=risk+20
		elif ans==5: risk = risk+25 
		question=7
	if question==7:
		print("\n1:Cough\n2:Fever\n3:Sore throat\n4:Chest congestion or  runny nose\n5:Body Ache\n6:Difficulty in breathing\n7:Loss of senses of smell and taste\n8: Pink eyes\n9: None of the above")
		ans = int(input("\nAre you currently experiencing any of the following symptoms: ")) 
		while ans>0 and ans<9:
			risk=risk+1
		if risk>100:
			risk=100
	print("\nYou are at ",risk,"%% risk.....\n")
	global mycursor
	global usermobile
	query = "UPDATE USER SET risk = "+str(risk)+" where mobile='"+usermobile+"';"
	mycursor.execute(query)

def allUpdates(): #it calculates and return the percentage of the people are affected
	global mycursor
	mycursor = mydb.cursor()
	mycursor.execute("select count(*) from user;")
	myresult = mycursor.fetchall();
	tp = int(myresult[0][0])
	mycursor.execute("select count(*) from user where covid = 'YES';")
	myresult = mycursor.fetchall();
	ap = int(myresult[0][0])
	if tp == 0:
		per = 0.0
	else:
		per = ap*100/tp
	return per

#bgCheck(); it is now of now use when i switched to MYSQL

while exitFlag == False:

	while loginFlag:
		os.system("cls")
		print("\t\t\t\tWelcome To AROGYA SETU APP")
		print("\n\n1.Register Yourself\n2.Login\n0.EXIT")
		opt = input()
		if opt == "1":
			get_user_details()
			if register_user():
				print("Congratulation, You are succesfully register.")
				loginFlag = False
				dashboardFlag = True
				print("press Enter key to continue...")
			else:
				print("Something went wrong, may be you are already register try to login.")
		elif opt == "2":
			usermobile = input("\tEnter your mobile number: ")
			if search_user():
				print("You are Logged in.")
				loginFlag = False
				dashboardFlag = True
				print("Press Enter key to continue...")
			else:
				print("Something went wrong, may be you are not register\nregister yourself")
		elif opt == "0":
			dashboardFlag = False
			loginFlag = False
			exitFlag = True;
		else:
			print("Choose correct option")		
		input()
	while dashboardFlag == True:
		os.system("cls")
		print("\n\n\t\t------------ Welcome "+username+", Hope you are well, Almost "+str(allUpdates())+"% population are get affected------------\n1.COVID updates\n2.Asses Yourself\n3.Update your covid report\n0.Logout")
		opt = input()
		
		if opt == "1":
			display_covid_updates()
		elif opt == "2":
			asses_yourself()
		elif opt == '3':
			print("\nAre You testes Covid Positive(Y/N): ")
			isPositive = input();
			if isPositive == "y" or isPositive =="Y":
				isPositive = "YES"
			elif isPositive == "N" or isPositive == "n":
				isPositive = "NO"

			if isPositive =="YES" or isPositive =="NO":
				
			
				query = "UPDATE USER SET covid='"+isPositive+"' WHERE mobile = '"+usermobile+"';"
				mycursor.execute(query)
		elif opt == "0":
			dashboardFlag = False
			loginFlag = True;	
		else:
			print("Choose correct option")
		input()

'''
1.when searched load user details  to the variables
2.get covid updates
'''