# Tutorial for Developing An Advanced Stock Dashboard for the S&P 500 for the 2025 Posit Table Contest"


This tutorial breaks down the development of an R Shiny application titled **S&P 500 Monitoring Dashboard** for the 2025 Posit Table Dashboard. This app effectively combines interactive financial data visualization (`plotly`), beautiful data tables (`gt`, `gtExtras`), web scraping (`rvest`), and external API integration (`riingo`, `ellmer`/Gemini AI) within a custom, sleek dark theme.
You can access the app through this [link](https://ozancanozdemir.shinyapps.io/sp500-monitoring-dashboard/)

## 1. Project Overview and Key Technologies

This application is divided into several functional panels:
1.  **Market Overview**: Top 10 S&P 500 companies by market cap, presented in a `gt` table with sparkline trends.
2.  **Stock Details**: Interactive selection, real-time price header, key statistics, and a daily/comparison price chart (`plotly`).
3.  **Fundamental Analysis**: Sortable table of key fundamental metrics.
4.  **Market News & AI**: News headlines (`riingo`) with sentiment analysis (`sentimentr`) and a large language model assistant (`ellmer`/Gemini AI).
5.  **Portfolio Calculator**: Simple portfolio backtesting and metric calculation.

### 📚 Core R Packages Used

| Category | Packages | Purpose |
| :--- | :--- | :--- |
| **App & UI** | `shiny`, `htmltools`, `shinyLP` | Application framework, custom HTML/CSS theming. |
| **Data Fetching**| `quantmod`, `rvest`, `xml2`, `riingo` | Fetching stock data (Yahoo), web scraping (S\&P 500, fundamentals), and news (Tiingo). |
| **Data Viz/Tables**| `gt`, `gtExtras`, `plotly`, `svglite` | Creating highly styled, professional data tables and interactive charts. |
| **AI Integration**| `ellmer`, `shinychat` | Connecting to the Gemini API for the financial assistant. |
| **Utilities** | `dplyr`, `stringr`, `lubridate`, `zoo` | Data cleaning, manipulation, and time series handling. |

***

## 2. Setting up the Environment and Helper Functions

The application starts by loading all necessary libraries and defining utility functions.

### 2.1. Icon and Theming Setup

The **`ICON_MAP`** list defines custom `font-awesome` icons used in the statistics boxes, setting the inline CSS style for specific colors.

### 2.2. Web Scraping: `get_sp500_tickers()`

This crucial helper function scrapes the S&P 500 ticker list from Wikipedia.

* It uses **`rvest::read_html()`** and **`rvest::html_table()`** to extract the data.
* It includes robust error handling (`tryCatch`) and a hardcoded **fallback list** if scraping fails.
* **Logo Generation**: It uses a Google Favicon service URL (`https://www.google.com/s2/favicons?sz=64&domain=...`) to dynamically generate company logos based on their domain, enhancing the visual appeal of the selection inputs and tables.

### 2.3. Data Retrieval and Sparklines

* **`pf_get_prices_for_sparkline()`**: Uses **`quantmod::getSymbols(src = "yahoo")`** to fetch the last 30 days of closing prices for a list of tickers, storing the data as a list of numeric vectors for use in `gt` sparklines.
* **`spark_area_svg()`**: This complex function uses **`ggplot2`** and **`svglite::stringSVG()`** to generate a data URI containing the SVG code for a colored area sparkline. This is essential for rendering the sparklines directly within the `gt` table cells without external image hosting.

***

## 3. The Custom Dark UI (`ui.R`)

The dashboard's premium look is achieved entirely through custom CSS within the `tags$head` section of the `ui`.

### 3.1. Custom CSS Theme

The CSS (embedded using `tags$style(HTML(...))`):
* Sets a dark blue/black **linear-gradient** background for the `body`.
* Uses modern fonts like **'Inter'** and **'JetBrains Mono'** (a monospace font often used for finance/coding) for a sleek, technical look.
* Applies distinct background colors (`#131722`, `#1e2431`, `#252b3d`) and border colors (`#2a2e39`) to various elements (`.main-container`, `.stock-header`, `.stat-card`, `.selectize-input`) to create a layered, visually separated design.
* Defines distinct colors for price changes: **Green (`#26a69a`) for up** and **Red (`#ef5350`) for down**.
* Customizes scrollbars, inputs (`selectize-input`), and the fixed **`app-footer`** for consistency.

### 3.2. Layout Structure

The `fluidPage` uses a simple **three-column layout** within the `main-container` (which is a custom-styled `div`):

* **Top Half (Left)**: Market Cap Table, Fundamental Metrics Table.
* **Top Half (Right)**: Stock Selector, Custom Header (`uiOutput("top_header_ui")`), Key Stats Cards, Price Tables (`gt_output`), and the Main Chart (`plotlyOutput`).
* **Bottom Half**: Riingo News (`gt_output`) and AI Chat (`chat_mod_ui`).
* **Bottom Global**: Portfolio Calculator Panel.

***

## 4. The Server Logic (`server.R`)

The server manages data retrieval, reactive computations, and rendering of all outputs.

### 4.1. Stock Data Reactives

* **`stock_data1`** and **`stock_data2`**: These `reactive` objects call `get_stock_data()` (which uses `quantmod::getSymbols`) to fetch stock prices based on the selected ticker(s) and time interval. They are triggered by changes in `ticker1`, `interval`, or the manual **REFRESH DATA** button (`input$refresh`).

### 4.2. Dynamic Header & Stats

* **`output$top_header_ui`**: This `renderUI` function dynamically generates the header HTML, including the company logo, name, and the formatted last price and daily change.
    * **`make_stock_header()`** retrieves the logo and name.
    * **`make_price_bar()`** calculates the last price and daily percentage change, assigning a **`.price-up`** (green) or **`.price-down`** (red) CSS class for visual feedback.
* The statistical `renderText` outputs (Volume, 52W High/Low, Avg Volume) use the `stock_data1()` reactive.

### 4.3. Advanced GT Table Rendering

The dashboard uses three major `gt` tables, each with heavy customization:

#### A. Key Stats Table (`output$key_stats_table`)

This table shows Market Cap, Revenue, and a 30-day price trend for the top stocks.

* **Data Preparation**: The data is sourced from **`get_market_cap_data()`**, which scrapes a stock analysis website using `rvest`.
* **Logo/Name Formatting**: The `Name_Logo` column is transformed using **`gt::text_transform`** to embed the logo image (`<img>` tag) next to the company name, thanks to the custom HTML/CSS used.
* **Market Cap Visualization**: **`gtExtras::gt_plt_bar()`** creates a simple bar chart inside the cell to show relative market capitalization.
* **Revenue Visualization**: **`gtExtras::gt_color_box()`** adds a background color box based on the revenue value.
* **Sparkline Trend**: This uses **`gt::text_transform`** to call the custom **`spark_area_svg()`** helper, embedding the generated SVG data URI as the cell content.

#### B. Daily Prices Table (`output$price_table1`)

This table shows the last 5 days of OHLC (Open, High, Low, Close) and key technical indicators (RSI, MACD).

* **Indicator Calculation**: Inside `create_table()`, technical analysis is performed using **`quantmod::RSI()`** and **`quantmod::MACD()`**.
* **Conditional Formatting**:
    * **Change/Change %**: Uses a complex `text_transform` to show green (▲) or red (▼) arrows and text color based on the price movement.
    * **RSI**: Uses **`gt::tab_style`** with `gt::cells_body` to highlight the cell background when RSI is **overbought (>= 70)** or **oversold (<= 30)**.

#### C. Riingo News Table (`output$riingo_news_gt`)

This table displays news headlines based on the selected ticker and source.

* **News Fetching**: **`riingo_news_data()`** uses `riingo::riingo_news()` (requires a Tiingo API token, which is hardcoded in this example: `TIINGO_TOKEN <- "8c7094ec74e7fc1ceca99a468fc4770df03dd0ec"`)
* **Sentiment Analysis**: **`sentimentr::sentiment_by()`** is used to quickly classify the headline sentiment as 'Positive', 'Negative', or 'Neutral'.
* **Visualization**:
    * **Source Logo**: A `text_transform` embeds the news source logo (`<img>` tag).
    * **Sentiment Highlight**: `gt::tab_style` conditionally colors the background and text of the `Sentiment` column based on the computed label (Green/Red/Gray).

### 4.4. Interactive Plotting (`output$price_plot`)

* **Candlestick Chart (No Compare)**: When `input$compare_mode` is `FALSE`, the code uses **`plotly::plot_ly(type = "candlestick")`** to display the OHLC data, setting custom increasing/decreasing colors (`#26a69a` / `#ef5350`).
* **Normalized Comparison (Compare Mode)**: When `TRUE`, it calculates the **percentage change** from the first day for both selected stocks and uses **`plotly::add_lines()`** to plot their performance curves on the same normalized Y-axis, which is the standard practice for performance comparison.

### 4.5. Portfolio Backtesting

The **Portfolio Calculator** section implements classic financial backtesting logic:

* **`pf_get_prices()`**: Downloads the closing prices for the selected tickers.
* **`pf_returns()`**: Calculates daily returns ($R_t = \frac{P_t}{P_{t-1}} - 1$).
* **`pf_port_ret()`**: Calculates the portfolio's daily return ($\sum w_i R_{i,t}$) based on the user-inputted weights (`pf_weights()`).
* **`pf_equity()`**: Calculates the portfolio's cumulative value over time based on the initial capital ($Equity_t = Capital \times \prod (1 + R_{port,t})$).
* **Metrics**: Calculates key performance indicators:
    * **CAGR (Compound Annual Growth Rate)**: Annualized return.
    * **Volatility**: Annualized standard deviation of returns.
    * **Sharpe Ratio**: Measures return per unit of risk ($\frac{Annualized Return - Risk-Free Rate}{Annualized Volatility}$).
* **`output$pf_alloc_table`**: Displays the final allocation using the custom **`weight_pill_html()`** function, which creates a slick, dynamically filled progress bar for the weight percentage within the `gt` table.

### 4.6. AI Chat Integration

* The code sets up a reactive `chat_client` using the **`ellmer::chat_google_gemini()`** function from the `ellmer` package.
* Users must input their **Gemini API Key** and click **SET API KEY** to initialize the client.
* The `system_prompt` is used to instruct the AI to act as an "expert financial advisor and stock analyst," ensuring relevant responses.
* **`chat_mod_server("stock_chat", chat_client())`** connects the initialized AI client to the `shinychat` UI module, making the chat functionality live.
