Binance Futures Trading Bot (Testnet)

Due to regional restrictions, Binance Testnet API responses may return empty or limited data. However, API integration and request structure are correctly implemented.



Overview



This is a Python-based CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).



Features



\* Place MARKET and LIMIT orders

\* Supports BUY and SELL

\* Command-line interface using argparse

\* Input validation for symbol, side, type, quantity, and price

\* Logging of requests, responses, and errors



\-------------------------------------------------------------------------------------------



Project Structure



trading\_bot/

│

├── bot/

│   ├── \_\_init\_\_.py

│   ├── client.py

│   ├── orders.py

│   ├── validators.py

│   └── logging\_config.py

│

├── cli.py

├── requirements.txt

├── .env

├── trading\_bot.log

└── README.md



\-------------------------------------------------------------------------------------------



Setup Instructions



1\. Clone the repository

git clone <your-repo-link>

cd trading\_bot



2\. Install dependencies

pip install -r requirements.txt



3\. Configure environment variables

Create a `.env` file:



API\_KEY=your\_api\_key

API\_SECRET=your\_api\_secret

BASE\_URL=https://testnet.binancefuture.com



\-------------------------------------------------------------------------------------------



Usage



MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001



LIMIT Order

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000



\-------------------------------------------------------------------------------------------



Output



The CLI prints:



\* Order ID

\* Status

\* Executed Quantity



\-------------------------------------------------------------------------------------------

Logging



All requests, responses, and errors are logged in:



trading\_bot.log



\-------------------------------------------------------------------------------------------



Assumptions



\* Binance API keys are configured correctly

\* Testnet access may vary based on region



