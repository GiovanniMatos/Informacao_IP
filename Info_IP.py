import requests
import folium
import os
api = "https://ipwhois.app/json/"


print('''\033[31m
 _____               _             
|_   _| __ __ _  ___| | _____ _ __ 
  | || '__/ _` |/ __| |/ / _ \ '__|
  | || | | (_| | (__|   <  __/ |   
  |_||_|  \__,_|\___|_|\_\___|_|   
  \033[0;0m
                                                                                                                       
''')
ip = input("\033[31m-----> IP:\033[31m ")
marcador = input("Nome da sessão (opcional): ")

request = requests.get(api + ip).json()

def info():

  print(f"""
  \033[36m [+]Endereco IP:\033[0;0m              {request['ip']}
  \033[36m Ativo:\033[0;0m                       {request['success']} 
  \033[36m Tipo:\033[0;0m                        {request['type']}   
  \033[36m Continente:\033[0;0m                  {request['continent']}
  \033[36m Codigo do Continente:\033[0;0m        {request['continent_code']}
  \033[36m País:\033[0;0m                        {request['country']}
  \033[36m Codigo do País:\033[0;0m              {request['country_code']}
  \033[36m Bandeira:\033[0;0m                    {request['country_flag']}
  \033[36m Capital:\033[0;0m                     {request['country_capital']}
  \033[36m DDD:\033[0;0m                         {request['country_phone']}
  \033[36m Países Vizinhos:\033[0;0m             {request['country_neighbours']}
  \033[36m Cidade:\033[0;0m                      {request['city']}
  \033[36m Latitude:\033[0;0m                    {request['latitude']}
  \033[36m Longitude:\033[0;0m                   {request['longitude']}
  \033[36m ASN:\033[0;0m                         {request['asn']}
  \033[36m ORG:\033[0;0m                         {request['org']}
  \033[36m ISP:\033[0;0m                         {request['isp']}
  \033[36m Fuso Horario:\033[0;0m                {request['timezone_name']}
  \033[36m Fuso Horario DST Offset:\033[0;0m     {request['timezone_dstOffset']}
  \033[36m Fuso Horario GMT Offset:\033[0;0m     {request['timezone_gmtOffset']}
  \033[36m F H GMT:\033[0;0m                     {request['timezone_gmt']}
  \033[36m Codigo da Moeda:\033[0;0m             {request['currency_code']}
  \033[36m Simbolo da Moeda:\033[0;0m            {request['currency_symbol']}
  \033[36m Taxa de Cambio:\033[0;0m              {request['currency_rates']}
  \033[36m Moeda:\033[0;0m                       {request['currency_plural']}""")
if __name__ == '__main__':
  info()
  
latitude = request['latitude']
longitude = request['longitude']
mymap = folium.Map(location=[latitude, longitude], zoom_start=12)

# marca a localização das coordenadas no mapa
folium.Marker([latitude, longitude], tooltip=marcador).add_to(mymap)
mymap.save('mapa.html')
abrir = input("\nAbrir no mapa? (S/N): ")
if abrir == "s" or abrir == 'S':
  os.system('mapa.html')
elif abrir == "n" or abrir == 'N':
  exit
else:
  exit
  