import bs4 as bs
import requests
import yfinance as yf
import datetime


def get_data():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    tickers = [s.replace('\n', '') for s in tickers]
    start = datetime.datetime(2018, 11, 1)
    end = datetime.datetime(2021, 10, 31)
    data = yf.download(tickers, start=start, end=end)
    # print(data)
    # print(type(data))
    print("Saving the stock data in pickle format for future use...")
    data.to_pickle("./data/stock_data_3year.pkl")
    print("Stock data saved in pickle format.")


if __name__ == "__main__":
    get_data()
