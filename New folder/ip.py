# import urllib3
# import json

# while True:
#     ip = input("Enter Target IP: ")
#     url = f"http://ip-api.com/json/{ip}"
    
#     # Create a connection pool using urllib3
#     http = urllib3.PoolManager()
    
#     # Make the request
#     response = http.request('GET', url)
    
#     # Check if the request was successful (status code 200)
#     if response.status == 200:
#         data = response.data.decode('utf-8')
#         values = json.loads(data)

#         print("IP: " + values.get("query", ""))
#         print("City: " + values.get("city", ""))
#         print("Region: " + values.get("regionName", ""))
#         print("Country: " + values.get("country", ""))
#         print("ISP: " + values.get("isp", ""))
#         print("AS: " + values.get("as", ""))
#     else:
#         print(f"Error: Unable to retrieve data. Status code: {response.status}")

#     ask_again = input("Do you want to track another IP? (yes/no): ").lower()
#     if ask_again != "yes":
#         break

# import requests

# API_KEY = 'your_api_key'  # Replace 'your_api_key' with your actual API key from IPstack

# def track_ip(ip):
#     url = f"http://api.ipstack.com/{ip}?access_key={API_KEY}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()

#         print("IP: " + data.get("ip", ""))
#         print("City: " + data.get("city", ""))
#         print("Region: " + data.get("region_name", ""))
#         print("Country: " + data.get("country_name", ""))
#         print("Latitude: " + str(data.get("latitude", "")))
#         print("Longitude: " + str(data.get("longitude", "")))
#         print("ISP: " + data.get("isp", ""))
#         print("AS: " + data.get("as", ""))
#     else:
#         print(f"Error: Unable to retrieve data. Status code: {response.status_code}")

# if __name__ == "__main__":
#     while True:
#         target_ip = input("Enter the IP address to track: ")
#         track_ip(target_ip)

#         ask_again = input("Do you want to track another IP? (yes/no): ").lower()
#         if ask_again != "yes":
#             break

