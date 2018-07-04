#     ____  _ __             _          ___    ____  ____
#    / __ )(_) /__________  (_)___     /   |  / __ \/  _/
#   / __  / / __/ ___/ __ \/ / __ \   / /| | / /_/ // /
#  / /_/ / / /_/ /__/ /_/ / / / / /  / ___ |/ ____// /
# /_____/_/\__/\___/\____/_/_/ /_/  /_/  |_/_/   /___/

#   ______                     __      __
#  /_  __/__  ____ ___  ____  / /___ _/ /____
#   / / / _ \/ __ `__ \/ __ \/ / __ `/ __/ _ \
#  / / /  __/ / / / / / /_/ / / /_/ / /_/  __/
# /_/  \___/_/ /_/ /_/ .___/_/\__,_/\__/\___/
#                  /_/

# Description: How to take an API and wrap it so requests to it pay you bitcoin.
# Repo: Bitcoin API Template (github.com/cryptopelago/bitcoin-api-template)
# License: Unlicense (unlicense.org)

# Load libraries
import requests
import urllib
import json
import yaml
from flask import Flask, request
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

# Init Flask, Wallet and Payment
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# Add 402 = payment required
@app.route('/YoutTube')
@payment.required(9600)
def lookup_string():
    something = request.args.get('URL')
    link = requests.get('http://api.daniil.it/?url='+something)
    return link.text

# Add Manifest
@app.route('/manifest')
def docs():
    '''
    Serves the app manifest to the 21 crawler.
    '''
    with open('manifest.yaml', 'r') as f:
        manifest_yaml = yaml.load(f)
    return json.dumps(manifest_yaml)

# Init Host
if __name__=='__main__':
    app.run(host='::', port='your_port')
