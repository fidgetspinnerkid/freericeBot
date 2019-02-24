class Solver:
    def __init__(self):
        pass

    @staticmethod
    def add(string):
        numbers = string.replace(" ","")
        myList = numbers.split('+')
        firstNum = int(myList[0])
        secondNum = int(myList[1])
        return firstNum + secondNum
        
    @staticmethod
    def mult(string):
        numbers = string.replace(" ","")
        myList = numbers.split('x')
        firstNum = int(myList[0])
        secondNum = int(myList[1])
        return firstNum * secondNum

    @staticmethod
    def detect(string):
        if "+" in string:
            return Solver.add(string)
        else:
            return Solver.mult(string)
    
    #Find best fit word
    from nltk.corpus import wordnet

    def syn_eval_v1(word,c0,c1,c2,c3):
        syn_list=wordnet.synsets(word)
        for i in syn_list[0].lemmas():
            s=" ".join(i.name().split('_'))
            if(s==c0):
                return c0
            if s==c1:
                return c1
            if s==c2:
                return c2
            if s==c3:
                return c3
            else:
                raise ValueError('Word not found.')
    
    #Translate
    
    from googletrans import Translator
    
    def translate_to_en(word):
        tra=Translator()
        return tra.translate("hello").text
    
    
    #Capitals
    
     
    input = 'N\'Djamena'
    answers = ['Sudan', 'Libya', 'Cameroon', 'Chad']
    
    
    capitals_dic = {
        'Afghanistan': 'Kabul',
        'Albania': 'Tirana',
        'Algeria': 'Algiers',
        'Andorra': 'Andorra la Vella',
        'Angola': 'Luanda',
        'Antigua and Barbuda': 'Saint John\'s',
        'Argentina': 'Buenos Aires',
        'Armenia': 'Yerevan',
        'Australia': 'Canberra',
        'Austria': 'Vienna',
        'Azerbaijan': 'Baku',
        'The Bahamas': 'Nassau',
        'Bahrain': 'Manama',
        'Bangladesh': 'Dhaka',
        'Barbados': 'Bridgetown',
        'Belarus': 'Minsk',
        'Belgium': 'Brussels',
        'Belize': 'Belmopan',
        'Benin': 'Porto-Novo',
        'Bhutan': 'Thimphu',
        'Bolivia': 'La Paz (administrative); Sucre (judicial)',
        'Bosnia and Herzegovina': 'Sarajevo',
        'Botswana': 'Gaborone',
        'Brazil': 'Brasilia',
        'Brunei': 'Bandar Seri Begawan',
        'Bulgaria': 'Sofia',
        'Burkina Faso': 'Ouagadougou',
        'Burundi': 'Gitega (changed from Bujumbura in December 2018)',
        'Cambodia': 'Phnom Penh',
        'Cameroon': 'Yaounde',
        'Canada': 'Ottawa',
        'Cape Verde': 'Praia',
        'Central African Republic': 'Bangui',
        'Chad': 'N\'Djamena',
        'Chile': 'Santiago',
        'China': 'Beijing',
        'Colombia': 'Bogota',
        'Comoros': 'Moroni',
        'Republic of the Congo; Congo-Republic': 'Brazzaville',
        'Democratic Republic of the Congo; Congo-Democratic Republic': 'Kinshasa',
        'Costa Rica': 'San Jose',
        'Cote d\'Ivoire': ' Yamoussoukro (official); Abidjan (de facto)',
        'Croatia': 'Zagreb',
        'Cuba': 'Havana',
        'Cyprus': 'Nicosia',
        'Czech Republic': 'Prague',
        'Denmark': 'Copenhagen',
        'Djibouti': 'Djibouti',
        'Dominica': 'Roseau',
        'Dominican Republic': 'Santo Domingo',
        'East Timor (Timor-Leste)': 'Dili',
        'Ecuador': 'Quito',
        'Egypt': 'Cairo',
        'El Salvador': 'San Salvador',
        'Equatorial Guinea': 'Malabo',
        'Eritrea': 'Asmara',
        'Estonia': 'Tallinn',
        'Ethiopia': 'Addis Ababa',
        'Fiji': 'Suva',
        'Finland': 'Helsinki',
        'France': 'Paris',
        'Gabon': 'Libreville',
        'The Gambia': 'Banjul',
        'Georgia': 'Tbilisi',
        'Germany': 'Berlin',
        'Ghana': 'Accra',
        'Greece': 'Athens',
        'Grenada': 'Saint George\'s',
        'Guatemala': 'Guatemala City',
        'Guinea': 'Conakry',
        'Guinea-Bissau': 'Bissau',
        'Guyana': 'Georgetown',
        'Haiti': 'Port-au-Prince',
        'Honduras': 'Tegucigalpa',
        'Hungary': 'Budapest',
        'Iceland': 'Reykjavik',
        'India': 'New Delhi',
        'Indonesia': 'Jakarta',
        'Iran': 'Tehran',
        'Iraq': 'Baghdad',
        'Ireland': 'Dublin',
        'Israel': 'Jerusalem',
        'Italy': 'Rome',
        'Jamaica': 'Kingston',
        'Japan': 'Tokyo',
        'Jordan': 'Amman',
        'Kazakhstan': 'Astana',
        'Kenya': 'Nairobi',
        'Kiribati': 'Tarawa Atoll',
        'Korea, North; North Korea': 'Pyongyang',
        'Korea, South; South Korea': 'Seoul',
        'Kuwait': 'Kuwait City',
        'Kyrgyzstan': 'Bishkek',
        'Laos': 'Vientiane',
        'Latvia': 'Riga',
        'Lebanon': 'Beirut',
        'Lesotho': 'Maseru',
        'Liberia': 'Monrovia',
        'Libya': 'Tripoli',
        'Liechtenstein': 'Vaduz',
        'Lithuania': 'Vilnius',
        'Luxembourg': 'Luxembourg',
        'Macedonia': 'Skopje',
        'Madagascar': 'Antananarivo',
        'Malawi': 'Lilongwe',
        'Malaysia': 'Kuala Lumpur',
        'Maldives': 'Male',
        'Mali': 'Bamako',
        'Malta': 'Valletta',
        'Marshall Islands': 'Majuro',
        'Mauritania': 'Nouakchott',
        'Mauritius': 'Port Louis',
        'Mexico': 'Mexico City',
        'Micronesia': 'Federated States of: Palikir',
        'Moldova': 'Chisinau',
        'Monaco': 'Monaco',
        'Mongolia': 'Ulaanbaatar',
        'Montenegro': 'Podgorica',
        'Morocco': 'Rabat',
        'Mozambique': 'Maputo',
        'Myanmar (Burma)': 'Rangoon (Yangon); Naypyidaw or Nay Pyi Taw (administrative)',
        'Namibia': 'Windhoek',
        'Nauru': 'no official capital; government offices in Yaren District',
        'Nepal': 'Kathmandu',
        'Netherlands': 'Amsterdam; The Hague (seat of government)',
        'New Zealand': 'Wellington',
        'Nicaragua': 'Managua',
        'Niger': 'Niamey',
        'Nigeria': 'Abuja',
        'Norway': 'Oslo',
        'Oman': 'Muscat',
        'Pakistan': 'Islamabad',
        'Palau': 'Melekeok',
        'Panama': 'Panama City',
        'Papua New Guinea': 'Port Moresby',
        'Paraguay': 'Asuncion',
        'Peru': 'Lima',
        'Philippines': 'Manila',
        'Poland': 'Warsaw',
        'Portugal': 'Lisbon',
        'Qatar': 'Doha',
        'Romania': 'Bucharest',
        'Russia': 'Moscow',
        'Rwanda': 'Kigali',
        'Saint Kitts and Nevis': 'Basseterre',
        'Saint Lucia': 'Castries',
        'Saint Vincent and the Grenadines': 'Kingstown',
        'Samoa': 'Apia',
        'San Marino': 'San Marino',
        'Sao Tome and Principe': 'Sao Tome',
        'Saudi Arabia': 'Riyadh',
        'Senegal': 'Dakar',
        'Serbia': 'Belgrade',
        'Seychelles': 'Victoria',
        'Sierra Leone': 'Freetown',
        'Singapore': 'Singapore',
        'Slovakia': 'Bratislava',
        'Slovenia': 'Ljubljana',
        'Solomon Islands': 'Honiara',
        'Somalia': 'Mogadishu',
        'South Africa': 'Pretoria (administrative); Cape Town (legislative); Bloemfontein (judiciary)',
        'South Sudan': 'Juba',
        'Spain': 'Madrid',
        'Sri Lanka': 'Colombo; Sri Jayewardenepura Kotte (legislative)',
        'Sudan': 'Khartoum',
        'Suriname': 'Paramaribo',
        'Swaziland': 'Mbabane',
        'Sweden': 'Stockholm',
        'Switzerland': 'Bern',
        'Syria': 'Damascus',
        'Taiwan': 'Taipei',
        'Tajikistan': 'Dushanbe',
        'Tanzania': 'Dar es Salaam; Dodoma (legislative)',
        'Thailand': 'Bangkok',
        'Togo': 'Lome',
        'Tonga': 'Nuku\'alofa',
        'Trinidad and Tobago': 'Port-of-Spain,',
        'Tunisia': 'Tunis',
        'Turkey': 'Ankara',
        'Turkmenistan': 'Ashgabat',
        'Tuvalu': 'Vaiaku village, Funafuti province',
        'Uganda': 'Kampala',
        'Ukraine': 'Kyiv',
        'United Arab Emirates': 'Abu Dhabi',
        'United Kingdom': 'London',
        'United States of America': 'Washington, D.C.',
        'Uruguay': 'Montevideo',
        'Uzbekistan': 'Tashkent',
        'Vanuatu': 'Port-Vila',
        'Vatican City (Holy See)': 'Vatican City',
        'Venezuela': 'Caracas',
        'Vietnam': 'Hanoi',
        'Yemen': 'Sanaa',
        'Zambia': 'Lusaka',
        'Zimbabwe': 'Harare',
    }


    def cap_country(capcountry):
        for country, capital in capitals_dic.items():
            if str(country).find(str(capcountry)) != -1:
                return capital
            elif str(capital).find(str(capcountry)) != -1:
                return country


    def check_answers(capcountry_final):
        for answer in answers:
            if str(answer).find(str(capcountry_final)) != -1 or str(capcountry_final).find(str(answer)) != -1:
                return answer
            
            
    return(check_answers(cap_country(input)))



