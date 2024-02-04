#library for making html requests
import requests
#library for custom text using figlet
from pyfiglet import Figlet

#Banner
def banner():
    custom_setting = Figlet(font = 'doom')
    custom_banner = custom_setting.renderText("IP INFO by HARDIK")
    print(custom_banner)


def get_ip_info(ip_address):
    api_url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(api_url)

    if response.status_code == 200:
        
        data = response.json()
        #the data structure of data here is dictionary
        
        print("IP Address:", data.get("ip"))
        print("Country:", data.get("country"))
        print("Location:", data.get("city") + ", " + data.get("region") + ", " + data.get("country"))
        print("ISP:", data.get("org"))
        print("Postal:", data.get("postal"))
        print("Coordinates:", data.get("loc"))
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":  #used to determine whether the python script is being run as the main script
    banner()
    target_ip = input("Enter the target IP address: ")
    get_ip_info(target_ip)
