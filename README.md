# CRYPTO_INFO

## Summary
This script is for getting all futures crypto information that is needed in trading bots 

This will retrieve the data from Binance, at first, but it will be updated for Bybit exchante too and bingx

This scrpt will extract data as price precision, quantity precision, minimun cost and price, max leverag for the crypto

At first all data is needed, except leverage, for storing in database
<br>
## Needs
- Python 3.10+
- PostgreSQL 15
- Create a Database 
<br>
## Install

1. Clone the repository
```bash
        # Via SSH
        git clone git@github.com:trapala85mx/crytpo_info.git

        # Via HTTPS
        git clone git clone https://github.com/trapala85mx/crytpo_info.git
```
2. Move inside the folder
```bash
        cd crypto_info
```
3. Create your virtual environment. I did it via venv<br>
```bash
        python3.10 -m venv env
```
4. Install requirements
```bash
        pip install -r requirements.txt
```

## Congfiguration
After cloned and installed requirements, you need to set some configuration settings:
1. Rename .env_example to .env
```bash
        mv .env_example .env
```
2. Open the file and fill the variables with ypu PostgreSQL configuration data

## Running
Now you are ready to run the script
```bash
        python main.py
```
After execute, you will have the info for all cryptos in futures of every exchange

## NOTES
As i mentioned before, for now it will retrieve the data from BINANCE FUTURES only, i will update any change in updates sections

## TO DO
- Implement Bybit Exchange<br>
- Implement Bingx Exchange<br>
- Implement MySQL Database<br>
- Implement SQLite Database<br>

## UPDATES
Nothing to report for now