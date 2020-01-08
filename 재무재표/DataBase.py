import GetFinancialStatements as GF
import GetStockInfo as GS
import sqlite3


def Create_DB():
    con = sqlite3.connect("c:/Users/kdy/stock.db")
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS `Kosdaq_info` (
	`Name`	TEXT,
	`Code`	TEXT,
	`Business`	TEXT,
	`Product`	TEXT,
	`Listed_Date`	TEXT,
	`Settlement_Date`	TEXT,
	`Representative_Name`	TEXT,
	`Homepage`	TEXT,
	`Region`	TEXT
    ); 
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `Kospi_info` (
    	`Name`	TEXT,
    	`Code`	TEXT,
    	`Business`	TEXT,
    	`Product`	TEXT,
    	`Listed_Date`	TEXT,
    	`Settlement_Date`	TEXT,
    	`Representative_Name`	TEXT,
    	`Homepage`	TEXT,
    	`Region`	TEXT
        ); 
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `Konex_info` (
    	`Name`	TEXT,
    	`Code`	TEXT,
    	`Business`	TEXT,
    	`Product`	TEXT,
    	`Listed_Date`	TEXT,
    	`Settlement_Date`	TEXT,
    	`Representative_Name`	TEXT,
    	`Homepage`	TEXT,
    	`Region`	TEXT
        ); 
        """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS `Kosdaq_Qfinance` (
	`Name`	TEXT,
	`Code`	TEXT,
	`Date`	TEXT,
	`SalesAccount`	TEXT,
	`OperatingProfit`	TEXT,
	`NetIncome`	TEXT,
	`CSNI`	TEXT,
	`NCSNI`	TEXT,
	`TotalAsset`	TEXT,
	`TotalDebt`	TEXT,
	`TotalCapital`	TEXT,
	`ConShare`	TEXT,
	`NConShare`	TEXT,
	`CashCapital`	TEXT,
	`DebtRatio`	TEXT,
	`ReserveRatio`	TEXT,
	`BusinessProfitRatio`	TEXT,
	`CSNetProfitRatio`	TEXT,
	`ROA`	TEXT,
	`ROE`	TEXT,
	`EPS`	TEXT,
	`BPS`	TEXT,
	`DPS`	TEXT,
	`PER`	TEXT,
	`PBR`	TEXT,
	`NumOutstandingShares`	TEXT,
	`DividendYieldRatio`	TEXT
);""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `Kospi_Qfinance` (
    	`Name`	TEXT,
    	`Code`	TEXT,
    	`Date`	TEXT,
    	`SalesAccount`	TEXT,
    	`OperatingProfit`	TEXT,
    	`NetIncome`	TEXT,
    	`CSNI`	TEXT,
    	`NCSNI`	TEXT,
    	`TotalAsset`	TEXT,
    	`TotalDebt`	TEXT,
    	`TotalCapital`	TEXT,
    	`ConShare`	TEXT,
    	`NConShare`	TEXT,
    	`CashCapital`	TEXT,
    	`DebtRatio`	TEXT,
    	`ReserveRatio`	TEXT,
    	`BusinessProfitRatio`	TEXT,
    	`CSNetProfitRatio`	TEXT,
    	`ROA`	TEXT,
    	`ROE`	TEXT,
    	`EPS`	TEXT,
    	`BPS`	TEXT,
    	`DPS`	TEXT,
    	`PER`	TEXT,
    	`PBR`	TEXT,
    	`NumOutstandingShares`	TEXT,
    	`DividendYieldRatio`	TEXT
    );""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `Konex_Qfinance` (
    	`Name`	TEXT,
    	`Code`	TEXT,
    	`Date`	TEXT,
    	`SalesAccount`	TEXT,
    	`OperatingProfit`	TEXT,
    	`NetIncome`	TEXT,
    	`CSNI`	TEXT,
    	`NCSNI`	TEXT,
    	`TotalAsset`	TEXT,
    	`TotalDebt`	TEXT,
    	`TotalCapital`	TEXT,
    	`ConShare`	TEXT,
    	`NConShare`	TEXT,
    	`CashCapital`	TEXT,
    	`DebtRatio`	TEXT,
    	`ReserveRatio`	TEXT,
    	`BusinessProfitRatio`	TEXT,
    	`CSNetProfitRatio`	TEXT,
    	`ROA`	TEXT,
    	`ROE`	TEXT,
    	`EPS`	TEXT,
    	`BPS`	TEXT,
    	`DPS`	TEXT,
    	`PER`	TEXT,
    	`PBR`	TEXT,
    	`NumOutstandingShares`	TEXT,
    	`DividendYieldRatio`	TEXT
    );""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `Kosdaq_Afinance` (
    	`Name`	TEXT,
    	`Code`	TEXT,
    	`Date`	TEXT,
    	`SalesAccount`	TEXT,
    	`OperatingProfit`	TEXT,
    	`NetIncome`	TEXT,
    	`CSNI`	TEXT,
    	`NCSNI`	TEXT,
    	`TotalAsset`	TEXT,
    	`TotalDebt`	TEXT,
    	`TotalCapital`	TEXT,
    	`ConShare`	TEXT,
    	`NConShare`	TEXT,
    	`CashCapital`	TEXT,
    	`DebtRatio`	TEXT,
    	`ReserveRatio`	TEXT,
    	`BusinessProfitRatio`	TEXT,
    	`CSNetProfitRatio`	TEXT,
    	`ROA`	TEXT,
    	`ROE`	TEXT,
    	`EPS`	TEXT,
    	`BPS`	TEXT,
    	`DPS`	TEXT,
    	`PER`	TEXT,
    	`PBR`	TEXT,
    	`NumOutstandingShares`	TEXT,
    	`DividendYieldRatio`	TEXT
    );""")
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS `Kospi_Afinance` (
        	`Name`	TEXT,
        	`Code`	TEXT,
        	`Date`	TEXT,
        	`SalesAccount`	TEXT,
        	`OperatingProfit`	TEXT,
        	`NetIncome`	TEXT,
        	`CSNI`	TEXT,
        	`NCSNI`	TEXT,
        	`TotalAsset`	TEXT,
        	`TotalDebt`	TEXT,
        	`TotalCapital`	TEXT,
        	`ConShare`	TEXT,
        	`NConShare`	TEXT,
        	`CashCapital`	TEXT,
        	`DebtRatio`	TEXT,
        	`ReserveRatio`	TEXT,
        	`BusinessProfitRatio`	TEXT,
        	`CSNetProfitRatio`	TEXT,
        	`ROA`	TEXT,
        	`ROE`	TEXT,
        	`EPS`	TEXT,
        	`BPS`	TEXT,
        	`DPS`	TEXT,
        	`PER`	TEXT,
        	`PBR`	TEXT,
        	`NumOutstandingShares`	TEXT,
        	`DividendYieldRatio`	TEXT
        );""")
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS `Konex_Afinance` (
        	`Name`	TEXT,
        	`Code`	TEXT,
        	`Date`	TEXT,
        	`SalesAccount`	TEXT,
        	`OperatingProfit`	TEXT,
        	`NetIncome`	TEXT,
        	`CSNI`	TEXT,
        	`NCSNI`	TEXT,
        	`TotalAsset`	TEXT,
        	`TotalDebt`	TEXT,
        	`TotalCapital`	TEXT,
        	`ConShare`	TEXT,
        	`NConShare`	TEXT,
        	`CashCapital`	TEXT,
        	`DebtRatio`	TEXT,
        	`ReserveRatio`	TEXT,
        	`BusinessProfitRatio`	TEXT,
        	`CSNetProfitRatio`	TEXT,
        	`ROA`	TEXT,
        	`ROE`	TEXT,
        	`EPS`	TEXT,
        	`BPS`	TEXT,
        	`DPS`	TEXT,
        	`PER`	TEXT,
        	`PBR`	TEXT,
        	`NumOutstandingShares`	TEXT,
        	`DividendYieldRatio`	TEXT
        );""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `Kosdaq_invest_info` (
    	`Name`	TEXT,
    	`Code`	TEXT,
    	`Price`	TEXT,
    	`PER`	TEXT,
    	`PBR`	TEXT,
    	`PSR`	TEXT
        ); 
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `Kospi_invest_info` (
        `Name`	TEXT,
    	`Code`	TEXT,
    	`Price`	TEXT,
    	`PER`	TEXT,
    	`PBR`	TEXT,
    	`PSR`	TEXT
        ); 
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `Konex_invest_info` (
        `Name`	TEXT,
    	`Code`	TEXT,
    	`Price`	TEXT,
    	`PER`	TEXT,
    	`PBR`	TEXT,
    	`PSR`	TEXT
        ); 
        """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS `Kosdaq_exp_invest_info` (
        	`Name`	TEXT,
        	`Code`	TEXT,
        	`Price`	TEXT,
        	`PER`	TEXT,
        	`PBR`	TEXT,
        	`PSR`	TEXT
            ); 
            """)
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS `Kospi_exp_invest_info` (
            `Name`	TEXT,
        	`Code`	TEXT,
        	`Price`	TEXT,
        	`PER`	TEXT,
        	`PBR`	TEXT,
        	`PSR`	TEXT
            ); 
            """)
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS `Konex_exp_invest_info` (
            `Name`	TEXT,
        	`Code`	TEXT,
        	`Price`	TEXT,
        	`PER`	TEXT,
        	`PBR`	TEXT,
        	`PSR`	TEXT
            ); 
            """)

    con.commit()
    con.close()


def Insert_DB_info():
    kosdaq_stocks = GS.download_stock_codes('kosdaq')
    kospi_stocks = GS.download_stock_codes('kospi')
    konex_stocks = GS.download_stock_codes('konex')

    con = sqlite3.connect("c:/Users/kdy/stock.db")
    cursor = con.cursor()
    for i in range(len(kosdaq_stocks)):
        cursor.execute("INSERT INTO Kosdaq_info VALUES(?,?,?,?,?,?,?,?,?)", kosdaq_stocks.loc[i])
    for i in range(len(kospi_stocks)):
        cursor.execute("INSERT INTO Kospi_info VALUES(?,?,?,?,?,?,?,?,?)", kospi_stocks.loc[i])
    for i in range(len(konex_stocks)):
        cursor.execute("INSERT INTO Konex_info VALUES(?,?,?,?,?,?,?,?,?)", konex_stocks.loc[i])
    con.commit()
    con.close()

#Sector Kospi_info, Kosdaq_info, Konex_info
def Get_DB_info(Sector):
    con = sqlite3.connect("c:/Users/kdy/stock.db")
    cursor = con.cursor()
    #cursor.execute("SELECT * FROM Konex_info WHERE Name = ?;","유비온")
    cursor.execute("SELECT * FROM " + Sector)
    stock = cursor.fetchall()
    return stock


def Insert_DB_Qfinance():
    kospi = Get_DB_info("Kospi_info")
    kosdaq = Get_DB_info("Kosdaq_info")
    konex = Get_DB_info("Konex_info")
    #print(kospi)

    con = sqlite3.connect("c:/Users/kdy/stock.db")
    cursor = con.cursor()

    for i in kospi:
        temp = GF.StockFinance(i[1])
        temp.D_NetQuarterFinance()
        for j in temp.D_A:
            record = [i[0],i[1],j]
            record.extend(temp.D_A[j].values())
            if len(record) == 27:
                cursor.execute("INSERT INTO Kospi_Qfinance VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", record)
        del(temp)

    for i in kosdaq:
        temp = GF.StockFinance(i[1])
        temp.D_NetQuarterFinance()
        for j in temp.D_A:
            record = [i[0], i[1], j]
            record.extend(temp.D_A[j].values())
            if len(record) == 27:
                cursor.execute("INSERT INTO Kosdaq_Qfinance VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",record)
        del (temp)

    for i in konex:
        temp = GF.StockFinance(i[1])
        temp.D_NetQuarterFinance()
        for j in temp.D_A:
            record = [i[0], i[1], j]
            record.extend(temp.D_A[j].values())
            if len(record) == 27:
                cursor.execute("INSERT INTO Konex_Qfinance VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",record)
        del (temp)

    con.commit()
    con.close()

def Insert_DB_Afinance():
    kospi = Get_DB_info("Kospi_info")
    kosdaq = Get_DB_info("Kosdaq_info")
    konex = Get_DB_info("Konex_info")
    #print(kospi)

    con = sqlite3.connect("c:/Users/kdy/stock.db")
    cursor = con.cursor()

    for i in kospi:
        temp = GF.StockFinance(i[1])
        temp.D_AnnualFinance()
        for j in temp.D_Y:
            record = [i[0],i[1],j]
            record.extend(temp.D_Y[j].values())
            if len(record) == 27:
                cursor.execute("INSERT INTO Kospi_Afinance VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", record)
        del(temp)

    for i in kosdaq:
        temp = GF.StockFinance(i[1])
        temp.D_AnnualFinance()
        for j in temp.D_Y:
            record = [i[0], i[1], j]
            record.extend(temp.D_Y[j].values())
            if len(record) == 27:
                cursor.execute("INSERT INTO Kosdaq_Afinance VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",record)
        del (temp)

    for i in konex:
        temp = GF.StockFinance(i[1])
        temp.D_AnnualFinance()
        for j in temp.D_Y:
            record = [i[0], i[1], j]
            record.extend(temp.D_Y[j].values())
            if len(record) == 27:
                cursor.execute("INSERT INTO Konex_Afinance VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",record)
        del (temp)

    con.commit()
    con.close()

def Insert_DB_invest(parayear):
    kospi = Get_DB_info("Kospi_info")
    kosdaq = Get_DB_info("Kosdaq_info")
    konex = Get_DB_info("Konex_info")

    con = sqlite3.connect("c:/Users/kdy/stock.db")
    cursor = con.cursor()
    totalnum = 0

    year = str(parayear)

    kospi_record = []
    kosdaq_record = []
    konex_record = []

    count = 0
    for i in kospi:
        break
        temp = GF.StockFinance(i[1])
        temp.getPrice()

        record = [i[0], i[1]]
        record.extend(" ")
        record[2] = temp.Price["Price"]

        price = int(record[2].replace(',', ''))
        cursor.execute(
            "SELECT NetIncome, NumOutstandingShares,TotalAsset, TotalDebt,SalesAccount FROM Kospi_Afinance WHERE Code = ? AND Date like ?",
            (i[1], year + "%")
        )
        recent_data = cursor.fetchall()
        if (len(recent_data) is not 0):
            if (recent_data[0][1] is "0" or recent_data[0][1] is "\xa0"):
                cursor.execute(
                    "SELECT NetIncome, NumOutstandingShares,TotalAsset, TotalDebt,SalesAccount FROM Kospi_Afinance WHERE Code = ? AND Date like ?",
                    (i[1], str(int(year) - 1) + "%")
                )
                recent_data2 = cursor.fetchall()
                if (recent_data2[0][1] is "0" or recent_data2[0][1] is "\xa0"):
                    continue
                totalnum = int(recent_data2[0][1].replace(',', ''))
            else:
                totalnum = int(recent_data[0][1].replace(',', ''))

            # PER
            record.extend(" ")
            if (recent_data[0][0] is not "\xa0" and recent_data[0][1] is not "\xa0"):
                if (recent_data[0][0] is "0" or recent_data[0][1] is "0"):
                    continue
                PER = float(price / float(int(recent_data[0][0].replace(',', '')) * 100000 / totalnum))
                record[3] = str(round(PER, 2))

            # PBR
            record.extend(" ")
            if (recent_data[0][2] is not "\xa0" and recent_data[0][3] is not "\xa0"):
                if (recent_data[0][2] is recent_data[0][3]):
                    continue
                PBR = float(price / float((int(recent_data[0][2].replace(',', '')) - int(
                    recent_data[0][3].replace(',', ''))) * 100000 / totalnum))
                record[4] = str(round(PBR, 2))

            # PSR
            record.extend(" ")
            if (recent_data[0][4] is not "\xa0"):
                if (recent_data[0][4] is "0"):
                    continue
                PSR = float(price / float(int(recent_data[0][4].replace(',', '')) * 100000 / totalnum))
                record[5] = str(round(PSR, 2))

            print(record)
            kospi_record.extend(" ")
            kospi_record[count] = record
            count += 1
            del (temp)

    count = 0
    for i in kosdaq:
        print(i[1])
        temp = GF.StockFinance(i[1])
        temp.getPrice()

        record = [i[0], i[1]]
        record.extend(" ")
        record[2] = temp.Price["Price"]

        price = int(record[2].replace(',', ''))
        cursor.execute(
            "SELECT NetIncome, NumOutstandingShares,TotalAsset, TotalDebt,SalesAccount FROM Kosdaq_Afinance WHERE Code = ? AND Date like ?",
            (i[1], year + "%")
        )
        recent_data = cursor.fetchall()
        if (len(recent_data) is not 0):
            if (recent_data[0][1] is "0" or recent_data[0][1] is "\xa0"):
                cursor.execute(
                    "SELECT NetIncome, NumOutstandingShares,TotalAsset, TotalDebt,SalesAccount FROM Kosdaq_Afinance WHERE Code = ? AND Date like ?",
                    (i[1], str(int(year) - 1) + "%")
                )
                recent_data2 = cursor.fetchall()
                if (recent_data2[0][1] is "0" or recent_data2[0][1] is "\xa0"):
                    continue
                totalnum = int(recent_data2[0][1].replace(',', ''))
            else:
                totalnum = int(recent_data[0][1].replace(',', ''))

            # PER
            record.extend(" ")
            if (recent_data[0][0] is not "\xa0" and recent_data[0][1] is not "\xa0"):
                if (recent_data[0][0] is "0" or recent_data[0][1] is "0"):
                    continue
                PER = float(price / float(
                    int(recent_data[0][0].replace(',', '')) * 100000 / totalnum))
                record.extend(" ")
                record[3] = str(round(PER, 2))

            # PBR
            record.extend(" ")
            if (recent_data[0][2] is not "\xa0" and recent_data[0][3] is not "\xa0"):
                if (recent_data[0][2] is recent_data[0][3]):
                    continue
                PBR = float(price / float((int(recent_data[0][2].replace(',', '')) - int(
                    recent_data[0][3].replace(',', ''))) * 100000 / totalnum))
                record[4] = str(round(PBR, 2))

            # PSR
            record.extend(" ")
            if (recent_data[0][4] is not "\xa0"):
                if (recent_data[0][4] is "0"):
                    continue
                PSR = float(price / float(int(recent_data[0][4].replace(',', '')) * 100000 / totalnum))
                record[5] = str(round(PSR, 2))

            print(record)
            kosdaq_record.extend(" ")
            kosdaq_record[count] = record
            count += 1
            del (temp)

    count = 0
    for i in konex:
        print(i[1])
        temp = GF.StockFinance(i[1])
        temp.getPrice()

        record = [i[0], i[1]]
        record.extend(" ")
        record[2] = temp.Price["Price"]

        price = int(record[2].replace(',', ''))
        cursor.execute(
            "SELECT NetIncome, NumOutstandingShares,TotalAsset, TotalDebt,SalesAccount FROM Konex_Afinance WHERE Code = ? AND Date like ?",
            (i[1], year + "%")
        )
        recent_data = cursor.fetchall()
        if (len(recent_data) is not 0):
            if (recent_data[0][1] is "0" or recent_data[0][1] is "\xa0"):
                cursor.execute(
                    "SELECT NetIncome, NumOutstandingShares,TotalAsset, TotalDebt,SalesAccount FROM Konex_Afinance WHERE Code = ? AND Date like ?",
                    (i[1], str(int(year) - 1) + "%")
                )
                recent_data2 = cursor.fetchall()
                if (recent_data2[0][1] is "0" or recent_data2[0][1] is "\xa0"):
                    continue
                totalnum = int(recent_data2[0][1].replace(',', ''))
            else:
                totalnum = int(recent_data[0][1].replace(',', ''))
            # PER
            record.extend(" ")
            if (recent_data[0][0] is not "\xa0" and recent_data[0][1] is not "\xa0"):
                if (recent_data[0][0] is "0" or recent_data[0][1] is "0"):
                    continue
                PER = float(price / float(int(recent_data[0][0].replace(',', '')) * 100000 / totalnum))
                record[3] = str(round(PER, 2))

            # PBR
            record.extend(" ")
            if (recent_data[0][2] is not "\xa0" and recent_data[0][3] is not "\xa0"):
                if (recent_data[0][2] is recent_data[0][3]):
                    continue
                PBR = float(price / float((int(recent_data[0][2].replace(',', '')) - int(
                    recent_data[0][3].replace(',', ''))) * 100000 / totalnum))
                record[4] = str(round(PBR, 2))

            # PSR
            record.extend(" ")
            if (recent_data[0][4] is not "\xa0"):
                if (recent_data[0][4] is "0"):
                    continue
                PSR = float(price / float(int(recent_data[0][4].replace(',', '')) * 100000 / totalnum))
                record[5] = str(round(PSR, 2))

            print(record)
            konex_record.extend(" ")
            konex_record[count] = record
            count += 1
            del (temp)

    # for i in kospi_record:
    #     if len(i) == 6:
    #         cursor.execute("INSERT INTO Kospi_invest_info VALUES(?,?,?,?,?,?)",i)
    # for i in kosdaq_record:
    #     if len(i) == 6:
    #         cursor.execute("INSERT INTO Kosdaq_invest_info VALUES(?,?,?,?,?,?)", i)
    # for i in konex_record:
    #     if len(i) == 6:
    #         cursor.execute("INSERT INTO Konex_invest_info VALUES(?,?,?,?,?,?)", i)
    con.commit()
    con.close()


def Insert_DB_exp_invest(parayear):
    kospi = Get_DB_info("Kospi_info")
    kosdaq = Get_DB_info("Kosdaq_info")
    konex = Get_DB_info("Konex_info")

    con = sqlite3.connect("c:/Users/kdy/stock.db")
    cursor = con.cursor()
    totalnum = 0

    year = str(parayear)

    kospi_record = []
    kosdaq_record = []
    konex_record = []

    count = 0
    for i in kospi:
        print(i[1])
        temp = GF.StockFinance(i[1])
        temp.getPrice()

        record = [i[0], i[1]]
        record.extend(" ")
        record[2] = temp.Price["Price"]

        price = int(record[2].replace(',',''))
        cursor.execute(
            "SELECT NetIncome, NumOutstandingShares,TotalAsset, TotalDebt,SalesAccount FROM Kospi_Afinance WHERE Code = ? AND Date like ?",
            (i[1], year + "%")
        )
        recent_data = cursor.fetchall()
        if(len(recent_data) is not 0):
            if (recent_data[0][1] is "0" or recent_data[0][1] is "\xa0"):
                cursor.execute(
                    "SELECT NetIncome, NumOutstandingShares,TotalAsset, TotalDebt,SalesAccount FROM Kospi_Afinance WHERE Code = ? AND Date like ?",
                    (i[1], str(int(year)-1) + "%")
                )
                recent_data2 = cursor.fetchall()
                if (recent_data2[0][1] is "0" or recent_data2[0][1] is "\xa0"):
                    continue
                totalnum = int(recent_data2[0][1].replace(',', ''))
            else:
                totalnum = int(recent_data[0][1].replace(',', ''))

            # PER
            record.extend(" ")
            if(recent_data[0][0] is not "\xa0" and recent_data[0][1] is not "\xa0"):
                if (recent_data[0][0] is "0" or recent_data[0][1] is "0"):
                    continue
                PER = float( price / float(int(recent_data[0][0].replace(',','')) * 100000 / totalnum))
                record[3] = str(round(PER,2))


            #PBR
            record.extend(" ")
            if (recent_data[0][2] is not "\xa0" and recent_data[0][3] is not "\xa0"):
                if (recent_data[0][2] is recent_data[0][3]):
                    continue
                PBR = float( price / float((int(recent_data[0][2].replace(',','')) - int(recent_data[0][3].replace(',', ''))) * 100000 / totalnum))
                record[4] = str(round(PBR,2))

            #PSR
            record.extend(" ")
            if (recent_data[0][4] is not "\xa0"):
                if (recent_data[0][4] is "0"):
                    continue
                PSR = float(price / float(int(recent_data[0][4].replace(',', '')) * 100000 / totalnum))
                record[5] = str(round(PSR,2))

            print(record)
            kospi_record.extend(" ")
            kospi_record[count] = record
            count += 1
            del (temp)

    count = 0
    for i in kosdaq:
        print(i[1])
        temp = GF.StockFinance(i[1])
        temp.getPrice()

        record = [i[0], i[1]]
        record.extend(" ")
        record[2] = temp.Price["Price"]

        price = int(record[2].replace(',', ''))
        cursor.execute(
            "SELECT NetIncome, NumOutstandingShares,TotalAsset, TotalDebt,SalesAccount FROM Kosdaq_Afinance WHERE Code = ? AND Date like ?",
            (i[1], year)
        )
        recent_data = cursor.fetchall()
        if (len(recent_data) is not 0):
            if (recent_data[0][1] is "0" or recent_data[0][1] is "\xa0"):
                cursor.execute(
                    "SELECT NetIncome, NumOutstandingShares,TotalAsset, TotalDebt,SalesAccount FROM Kosdaq_Afinance WHERE Code = ? AND Date like ?",
                    (i[1], str(int(year) - 1) + "%")
                )
                recent_data2 = cursor.fetchall()
                if (recent_data2[0][1] is "0" or recent_data2[0][1] is "\xa0"):
                    continue
                totalnum = int(recent_data2[0][1].replace(',', ''))
            else:
                totalnum = int(recent_data[0][1].replace(',', ''))

            # PER
            record.extend(" ")
            if (recent_data[0][0] is not "\xa0" and recent_data[0][1] is not "\xa0"):
                if (recent_data[0][0] is "0" or recent_data[0][1] is "0"):
                    continue
                PER = float(price / float(
                    int(recent_data[0][0].replace(',', '')) * 100000 / totalnum))
                record.extend(" ")
                record[3] = str(round(PER, 2))


            # PBR
            record.extend(" ")
            if (recent_data[0][2] is not "\xa0" and recent_data[0][3] is not "\xa0"):
                if (recent_data[0][2] is recent_data[0][3]):
                    continue
                PBR = float(price / float((int(recent_data[0][2].replace(',', '')) - int(
                    recent_data[0][3].replace(',', ''))) * 100000 / totalnum))
                record[4] = str(round(PBR, 2))

            # PSR
            record.extend(" ")
            if (recent_data[0][4] is not "\xa0"):
                if (recent_data[0][4] is "0"):
                    continue
                PSR = float(price / float(int(recent_data[0][4].replace(',', '')) * 100000 / totalnum))
                record[5] = str(round(PSR, 2))

            print(record)
            kosdaq_record.extend(" ")
            kosdaq_record[count] = record
            count += 1
            del (temp)

    count = 0
    for i in konex:
        print(i[1])
        temp = GF.StockFinance(i[1])
        temp.getPrice()

        record = [i[0], i[1]]
        record.extend(" ")
        record[2] = temp.Price["Price"]

        price = int(record[2].replace(',',''))
        cursor.execute(
            "SELECT NetIncome, NumOutstandingShares,TotalAsset, TotalDebt,SalesAccount FROM Konex_Afinance WHERE Code = ? AND Date like ?",
            (i[1], year)
        )
        recent_data = cursor.fetchall()
        if (len(recent_data) is not 0):
            if (recent_data[0][1] is "0" or recent_data[0][1] is "\xa0"):
                cursor.execute(
                    "SELECT NetIncome, NumOutstandingShares,TotalAsset, TotalDebt,SalesAccount FROM Konex_Afinance WHERE Code = ? AND Date like ?",
                    (i[1], str(int(year) - 1) + "%")
                )
                recent_data2 = cursor.fetchall()
                if (recent_data2[0][1] is "0" or recent_data2[0][1] is "\xa0"):
                    continue
                totalnum = int(recent_data2[0][1].replace(',', ''))
            else:
                totalnum = int(recent_data[0][1].replace(',', ''))
            # PER
            record.extend(" ")
            if(recent_data[0][0] is not "\xa0" and recent_data[0][1] is not "\xa0"):
                if (recent_data[0][0] is "0" or recent_data[0][1] is "0"):
                    continue
                PER = float( price / float(int(recent_data[0][0].replace(',','')) * 100000 / totalnum))
                record[3] = str(round(PER,2))


            #PBR
            record.extend(" ")
            if (recent_data[0][2] is not "\xa0" and recent_data[0][3] is not "\xa0"):
                if (recent_data[0][2] is recent_data[0][3]):
                    continue
                PBR = float( price / float((int(recent_data[0][2].replace(',','')) - int(recent_data[0][3].replace(',', ''))) * 100000 / totalnum))
                record[4] = str(round(PBR,2))

            #PSR
            record.extend(" ")
            if (recent_data[0][4] is not "\xa0"):
                if (recent_data[0][4] is "0"):
                    continue
                PSR = float(price / float(int(recent_data[0][4].replace(',', '')) * 100000 / totalnum))
                record[5] = str(round(PSR,2))

            print(record)
            konex_record.extend(" ")
            konex_record[count] = record
            count += 1
            del (temp)

    # for i in kospi_record:
    #     if len(i) == 6:
    #         cursor.execute("INSERT INTO Kospi_exp_invest_info VALUES(?,?,?,?,?,?)",i)
    # for i in kosdaq_record:
    #     if len(i) == 6:
    #         cursor.execute("INSERT INTO Kosdaq_exp_invest_info VALUES(?,?,?,?,?,?)", i)
    # for i in konex_record:
    #     if len(i) == 6:
    #         cursor.execute("INSERT INTO Konex_exp_invest_info VALUES(?,?,?,?,?,?)", i)
    con.commit()
    con.close()


if __name__ == "__main__":
    #Create_DB()
    #Insert_DB_info()
    #Insert_DB_Afinance()
    Insert_DB_invest(2019)



