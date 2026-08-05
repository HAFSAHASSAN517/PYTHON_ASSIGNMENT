#Fetch current weather data from a public API (e.g. OpenMeteo) and display temp/humidity
import requests
url = "https://open-meteo.com/en/docs?hourly=temperature_2m,relative_humidity_2m,rain,wind_speed_10m"
response = requests.get(url)
if response.status_code ==200:
    data = response.json()
    tem = data.get("temperature_2m")
    hum = data.get("relative_humidity_2m")
    wind_speed = data.get("wind_speed_10m")
    print(f"temperature : {tem} ")
    print(f"humidity : {hum}")
    print(f"wind_speed : {wind_speed}")
else:
        print("failed to fetch data from API ")
#Call a public REST API (e.g. JSONPlaceholder) and display a list of users in a formatted table
import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
if response.status_code ==200:
    users = response.json()
    for user in users:
        user_id = user.get("id")
        user_name = user.get("name")
        user_email = user.get("email")
        user_phone = user.get("phone")
        print(f"ID :{user_id}  | name : {user_name}  | email : {user_email}  | phone :{user_phone}")
else:
    print("failed to fetch data from API")        
            
        
#Write a function that calls an API with error handling for 404, 500, and timeout errors
import requests
def fd_from_API(url , timeout=5):
    try:
        response = requests.get(url,timeout = timeout)
        response.raise_for_status()
        print("successfully feteched data")   
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print("error 404 : resource not found")
        elif response.status_code == 500:
            print("error 500 :internal server not found")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.Timeout:
        print("Error: Request timed out")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return None
print("test 1 : valid url")
fd_from_API("https://jsonplaceholder.typicode.com/users")
print("test 2 : invalid endpoint")
fd_from_API("https://jsonplaceholder.typicode.com/invalid_endpoint")
print("test 3 : internal server error")
fd_from_API("https://httpstat.us/500")
#LLM Task: Use the Claude or OpenAI API to send a prompt and print the response in the terminal
import anthropic
client = anthropic.Anthropic(" YOUR_API_KEY")
message =client.messages.create( 
                                model = "claude-fable-5", 
                                tokens = 100,
                                messages =  [{"role": "user", "content": "Hello, can you tell me a joke?"}])
print(message.content[0].text)
#Build a currency converter that fetches live exchange rates from a public API and converts between 3 currencies
import requests
def _currency_convertor(amount,from_currency ,to_currency):
     try:
          url =f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
          response = requests.get(url)
          response.raise_for_status()
          data = response.json()
          rates = data.get("rates" , {})
          print("currency convertor")
          print("------------------- EUR,PKR,AUD")        
          
          
          if to_currency in rates:
              rate = rates[to_currency]
              converted_amount = amount*rate
              print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
              return converted_amount
          else:
              print("error: target currency not supported")
     except requests.exceptions.RequestException as e:
          print(f"An error occurred: {e}")
     except ValueError:
         print("error: invalid amount entered")      
if __name__ == "__main__":
    _currency_convertor(100,"USD","EUR")
    _currency_convertor(100,"EUR","AUD")                   
    _currency_convertor(100,"AUD","USD")                   
                       
