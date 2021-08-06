from flask import Flask
import pywhatkit
import requests
server = Flask(__name__)
bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
response = requests.get(bitcoin_api_url)
response_json = response.json()
ifttt_webhook_url = 'https://maker.ifttt.com/trigger/test_event/with/key/b5QL1J128e4pswOdrujjKN'
requests.post(ifttt_webhook_url)

@server.route("/")
def hello():
    pywhatkit.sendwhatmsg("+5491144039194","Probando el bot desde python, te amo linda",19,44)
    return "Mensaje Enviado!"

if __name__ == "__main__":
   server.run(host='0.0.0.0')