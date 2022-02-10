import requests
api = "https://ipwhois.app/json/"

print('''\033[31m
 _  ___             _____               _             
 | |/ (_)_ __ __ _  |_   _| __ __ _  ___| | _____ _ __ 
 | ' /| | '__/ _` |   | || '__/ _` |/ __| |/ / _ \ '__|
 | . \| | | | (_| |   | || | | (_| | (__|   <  __/ |   
 |_|\_\_|_|  \__,_|   |_||_|  \__,_|\___|_|\_\___|_|   \033[0;0m
            by: kira0666@protonmail.com                                                                                                                            
''')
ip = input("\033[31m-----> IP:\033[31m ")

request = requests.get(api + ip).json()
print("\033[36m [+]Endereco IP:\033[0;0m              {}".format(request['ip']))
print("\033[36m Ativo:\033[0;0m                       {}".format(request['success']))
print("\033[36m Tipo:\033[0;0m                        {}".format(request['type']))
print("\033[36m Continente:\033[0;0m                  {}".format(request['continent']))
print("\033[36m Codigo do Continente:\033[0;0m        {}".format(request['continent_code']))
print("\033[36m País:\033[0;0m                        {}".format(request['country']))
print("\033[36m Codigo do País:\033[0;0m              {}".format(request['country_code']))
print("\033[36m Bandeira:\033[0;0m                    {}".format(request['country_flag']))
print("\033[36m Capital:\033[0;0m                     {}".format(request['country_capital']))
print("\033[36m DDD:\033[0;0m                         {}".format(request['country_phone']))
print("\033[36m Países Vizinhos:\033[0;0m             {}".format(request['country_neighbours']))
print("\033[36m Cidade:\033[0;0m                      {}".format(request['city']))
print("\033[36m Latitude:\033[0;0m                    {}".format(request['latitude']))
print("\033[36m Longitude:\033[0;0m                   {}".format(request['longitude']))
print("\033[36m ASN:\033[0;0m                         {}".format(request['asn']))
print("\033[36m ORG:\033[0;0m                         {}".format(request['org']))
print("\033[36m ISP:\033[0;0m                         {}".format(request['isp']))
print("\033[36m Fuso Horario:\033[0;0m                {}".format(request['timezone_name']))
print("\033[36m Fuso Horario DST Offset:\033[0;0m     {}".format(request['timezone_dstOffset']))
print("\033[36m Fuso Horario GMT Offset:\033[0;0m     {}".format(request['timezone_gmtOffset']))
print("\033[36m F H GMT:\033[0;0m                     {}".format(request['timezone_gmt']))
print("\033[36m Codigo da Moeda:\033[0;0m             {}".format(request['currency_code']))
print("\033[36m Simbolo da Moeda:\033[0;0m            {}".format(request['currency_symbol']))
print("\033[36m Taxa de Cambio:\033[0;0m              {}".format(request['currency_rates']))
print("\033[36m Moeda:\033[0;0m                       {}".format(request['currency_plural']))
print("\033[36m Requisicoes Concluidas:\033[0;0m      {}".format(request['completed_requests']))
print("\033[36m Proxy:\033[0;0m                       Unknown")
print("""

contato: kira0666@protonmail.com
""")
