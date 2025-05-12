
# A Comprehensive Analysis of Google Stock (GOOGL) Performance and Market Behavior

**Author:** Anani A. Assoutovi  
**Affiliation:** Independent Researcher / Data Scientist  
**Email:** booking.helices4s@icloud.com  
**LinkedIn:** www.linkedin.com/in/ananiassoutovi  
**Date:** May 12, 2025  

## Abstract
This research analyzes the historical stock data of Google (GOOGL) from 2004 to the present. Utilizing technical analysis tools, statistical summaries, and anomaly detection techniques, the paper explores trends, volatility, indicators, and events that have shaped Google's market performance. The analysis is based on a dataset from Kaggle and employs Python-based data science techniques.

---

## 1. Introduction
Google (Alphabet Inc.) has been a dominant force in the technology sector. Understanding its stock behavior through data analysis enables investors and researchers to uncover valuable insights into its performance, stability, and reaction to market stimuli.

---

## 2. Data Source & Preparation

- **Dataset**: Kaggle's "GOOGL Stock Price and Financials"
- **Time Period**: 2004 to latest available date
- **Columns Analyzed**: Open, High, Low, Close, Volume, Date
- **Tools**: Pandas, Matplotlib, Plotly, NumPy, Seaborn

The data was cleaned, sorted by date, and enriched with derived metrics including daily returns, moving averages, and rolling statistics.

---

## 3. Statistical Overview

Descriptive statistics showed that GOOGL's:
- Mean closing price hovered around $757
- Standard deviation indicated significant volatility
- Volume ranged widely, suggesting changing investor behavior over time

---

## 4. Return Analysis

Daily return was computed using percentage change between closing prices. A distribution analysis revealed:
- Mean daily return of ~0.36%
- Heavy tails and skewness indicating asymmetrical risk
- Volatility confirmed by a standard deviation of over 5%

---

## 5. Correlation Study

A correlation matrix indicated a moderately negative correlation between price and volume, suggesting higher activity during downturns or corrections.

---

## 6. Technical Indicators

- **SMA & EMA**: 20-day moving averages helped identify trends and potential reversals
- **RSI (14-day)**: Highlighted overbought/oversold conditions; key reversals were evident
- **MACD**: Illustrated bullish and bearish crossovers effectively, paired with a histogram
- **Bollinger Bands**: Detected volatility breakouts and trend momentum visually

---

## 7. Performance Comparison

An annual return summary showed:
- **Best year**: 2005 (+84.92%)
- **Worst year**: 2022 (−137.47%)

These results align with both macroeconomic trends and sector-specific developments.

---

## 8. Market Anomaly Detection

Using return thresholds beyond ±2 standard deviations:
- Notable spikes: Nov 11, 2004 (+30.27%)
- Notable crashes: Jul 19, 2022 (−95.08%)

These anomalies were linked to [global events](https://theweek.com/briefing/daily-briefing/1015227/10-things-you-need-to-know-today-july-19-2022) and quarterly earnings reactions.

---

## 9. Conclusion

This analysis provides a well-rounded view of GOOGL's stock behavior. Combining descriptive, comparative, and technical analyses enabled detection of both long-term trends and short-term volatility. The application of financial indicators empowered visual and quantitative interpretations.

**Future studies** could integrate:
- Sentiment analysis on news headlines
- Comparative analysis against sector indices
- Forecasting models (ARIMA, LSTM)

---

## References
- Kaggle Dataset: https://www.kaggle.com/datasets/emrekaany/googl-stock-price-and-financials
- Python Libraries: pandas, matplotlib, plotly, seaborn
