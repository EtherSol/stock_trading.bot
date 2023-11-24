# define asset
# OUT: STRING

# INITIAL CHECK
# check the position: ask the broker if we have an open position with "asset"
# IN: Asset (string)
# OUT: True (exists) / False(does not exist)


# check if tradable: ask the broker/ API if "asset" is tradeable
# IN: asset (string)
# OUT: True (exists) / False (does not exist)


# GENERAL TREND
# load 30 minutes candles: demand the API the 30 min candles
# IN: asset (or whatever the API needs), time range+, candle size+
# OUT: 30 minute candles (OHLC for every candle)

# perform general trend analysis: detect interesting trend (UP/ DOWN/ NO TREND)
# IN: 30 min candles data (Close data)
# OUT: UP/ DOWN / No Trend (strings)

#############
# LOOP until timeout reached (ex. 30 min)
# STEP 1: load 5 min candles
# IN: asset (or whatever the API needs), time range+, candle size+
# OUT: 5 min candles (OHLC for every candle)


# STEP 2: perform instant trend analysis: confirm the trend dected by GT analysis
# IN: 5 min candles data (Close data), output of the GT analysis (UP/ DOWN string)
# OUT: True (confirmed) / False (not confirmed)

# STEP 3: perform RSI analysis
# IN: 5 min candles data (Close data), output of the GT analysis (UP/ DOWN string)
# OUT: True (confirmed) / False (not confirmed)
# perform stochastic analysis


# SUBMIT ORDER
# STEP 4: submit order
# check position

# "ENTER POSITION" MODE (LOOP)
# check take profit
# check stop loss
# check stoch crossing

# GET OUT
# check order
# check position

# wait 15 minutes
# back to the beginning
