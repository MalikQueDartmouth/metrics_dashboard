import streamlit as st
import pandas_datareader as pdr
import datetime as datetime
from streamlit_extras.metric_cards import style_metric_cards # beautify metric card with css

def main():
    st.set_page_config(layout='wide', initial_sidebar_state='expanded')
    
    st.sidebar.header('Metrics Dashboard `v1.0`')
    st.sidebar.markdown("""
                        ---
                        Created by Malik Franklin
                        """)
    start_date = datetime.date(2018, 1, 1)
    
    #  Federal Reserve Economic Data Service
    data_source = 'fred'
    
    unemployment_rate_code = 'UNRATE'
    dow_jones_code = "DJIA"
    snp_code = 'SP500'
    mortgage_code = 'MORTGAGE30US'
    personal_savings_rate_code = 'PSAVERT'
    
    treasury_yield_code = 'DGS10' #  10-year Treasury Rate
    aaa_index_yield_code = 'BAMLC0A1CAAAEY'
    bbb_index_yield_code = 'BAMLC0A4CBBBEY'
    hy_index_yield_code = 'BAMLH0A0HYM2EY'
    fed_funds_rate_code = 'FEDFUNDS'
    
    cpi_series_code = 'CPIAUCSL'
    cpi_less_food_energy_series_code = 'CPILFESL'
    sticky_price_cpi_code = "CORESTICKM159SFRBATL"
    five_yr_inflation_rate_code = "T5YIE"
    ten_yr_inflation_rate_code = "T10YIE"
        
    #  Fetch data
    unemployment_rate_df = pdr.DataReader(unemployment_rate_code, data_source, start_date)
    dow_jones_df = pdr.DataReader(dow_jones_code, data_source, start_date)
    snp_data_df = pdr.DataReader(snp_code, data_source, start_date)
    mortgate_data_df = pdr.DataReader(mortgage_code, data_source, start_date)
    savings_df = pdr.DataReader(personal_savings_rate_code, data_source, start_date)
    
    treasury_yield_df = pdr.DataReader(treasury_yield_code, data_source, start_date)
    aaa_df = pdr.DataReader(aaa_index_yield_code, data_source, start_date)
    bbb_df = pdr.DataReader(bbb_index_yield_code, data_source, start_date)
    hy_df = pdr.DataReader(hy_index_yield_code, data_source, start_date)
    fed_funds_df = pdr.DataReader(fed_funds_rate_code, data_source, start_date)
    
    cpi_df = pdr.DataReader(cpi_series_code, data_source, start_date)
    cpi_less_food_energy_df = pdr.DataReader(cpi_less_food_energy_series_code, data_source, start_date)
    sticky_price_cpi_df = pdr.DataReader(sticky_price_cpi_code, data_source, start_date)
    five_yr_inflation_rate_df = pdr.DataReader(five_yr_inflation_rate_code, data_source, start_date)
    ten_yr_inflation_rate_df = pdr.DataReader(ten_yr_inflation_rate_code, data_source, start_date)
    
    data_label_dict = {
        unemployment_rate_code : "Unemployment Rate",
        dow_jones_code : "Dow Jones Industrial Average",
        snp_code : "S&P 500",
        mortgage_code : "30-Year Fixed Rate Mortgage Average in the United States",
        personal_savings_rate_code : "Personal Saving Rate",
        
        treasury_yield_code : "Market Yield on U.S. Treasury Securities at 10-Year Constant Maturity, Quoted on an Investment Basis",
        aaa_index_yield_code : "ICE BofA AAA US Corporate Index Effective Yield",
        bbb_index_yield_code : "ICE BofA BBB US Corporate Index Effective Yield",
        hy_index_yield_code : "ICE BofA US High Yield Index Effective Yield",
        fed_funds_rate_code : "Federal Funds Effective Rate",
        
        cpi_series_code : "Consumer Price Index for All Urban Consumers: All Items in U.S. City Average",
        cpi_less_food_energy_series_code : "Consumer Price Index for All Urban Consumers: All Items Less Food and Energy in U.S. City Average",
        sticky_price_cpi_code : "Sticky Price Consumer Price Index less Food and Energy",
        five_yr_inflation_rate_code : "5-Year Breakeven Inflation Rate",
        ten_yr_inflation_rate_code : "10-Year Breakeven Inflation Rate",
        
    }
    
    data_dict = {
        unemployment_rate_code : unemployment_rate_df,
        dow_jones_code : dow_jones_df,
        mortgage_code : mortgate_data_df,
        snp_code : snp_data_df,
        personal_savings_rate_code : savings_df,
        
        treasury_yield_code : treasury_yield_df,
        aaa_index_yield_code : aaa_df,
        bbb_index_yield_code : bbb_df,
        hy_index_yield_code : hy_df,
        fed_funds_rate_code : fed_funds_df,
        
        cpi_series_code : cpi_df,
        cpi_less_food_energy_series_code : cpi_less_food_energy_df,
        sticky_price_cpi_code : sticky_price_cpi_df,
        five_yr_inflation_rate_code : five_yr_inflation_rate_df,
        ten_yr_inflation_rate_code : ten_yr_inflation_rate_df,
        
        }
        
    
    unemploy_rate_T0 = float(unemployment_rate_df[unemployment_rate_code].iloc[-1])
    unemploy_rate_T1 = float(unemployment_rate_df[unemployment_rate_code].iloc[-2])
    unemploy_rate_delta = unemploy_rate_T0 - unemploy_rate_T1
    
    dow_jones_T0 = float(dow_jones_df[dow_jones_code].iloc[-1])
    dow_jones_T1 = float(dow_jones_df[dow_jones_code].iloc[-2])
    dow_jones_delta = dow_jones_T0 - dow_jones_T1
    
    snp_data_T0 = float(snp_data_df[snp_code].iloc[-1])
    snp_data_T1 = float(snp_data_df[snp_code].iloc[-2])
    snp_data_delta = snp_data_T0 - snp_data_T1
    
    mortgate_data_T0 = float(mortgate_data_df[mortgage_code].iloc[-1])
    mortgate_data_T1 = float(mortgate_data_df[mortgage_code].iloc[-2])
    mortgate_data_delta = mortgate_data_T0 - mortgate_data_T1
    
    savings_T0 = float(savings_df[personal_savings_rate_code].iloc[-1])
    savings_T1 = float(savings_df[personal_savings_rate_code].iloc[-2])
    savings_delta = savings_T0 - savings_T1
    
    ten_yr_treas_T0 = float(treasury_yield_df[treasury_yield_code].iloc[-1])
    ten_yr_treas_T1 = float(treasury_yield_df[treasury_yield_code].iloc[-2])
    ten_yr_delta = ten_yr_treas_T0 - ten_yr_treas_T1
    
    aaa_T0 = float(aaa_df[aaa_index_yield_code].iloc[-1])
    aaa_T1 = float(aaa_df[aaa_index_yield_code].iloc[-2])
    aaa_delta = aaa_T0 - aaa_T1
    
    bbb_T0 = float(bbb_df[bbb_index_yield_code].iloc[-1])
    bbb_T1 = float(bbb_df[bbb_index_yield_code].iloc[-2])
    bbb_delta = bbb_T0 - bbb_T1
    
    hy_T0 = float(hy_df[hy_index_yield_code].iloc[-1])
    hy_T1 = float(hy_df[hy_index_yield_code].iloc[-2])
    hy_delta = hy_T0 - hy_T1
    
    fed_funds_T0 = float(fed_funds_df[fed_funds_rate_code].iloc[-1])
    fed_funds_T1 = float(fed_funds_df[fed_funds_rate_code].iloc[-2])
    fed_funds_delta = fed_funds_T0 - fed_funds_T1
    
    
    cpi_T0 = float(cpi_df[cpi_series_code].iloc[-1])
    cpi_T1 = float(cpi_df[cpi_series_code].iloc[-2])
    cpi_delta = cpi_T0 - cpi_T1

    cpi_less_food_energy_T0 = float(cpi_less_food_energy_df[cpi_less_food_energy_series_code].iloc[-1])
    cpi_less_food_energy_T1 = float(cpi_less_food_energy_df[cpi_less_food_energy_series_code].iloc[-2])
    cpi_less_food_energy_delta = cpi_less_food_energy_T0 - cpi_less_food_energy_T1
    
    sticky_price_cpi_T0 = float(sticky_price_cpi_df[sticky_price_cpi_code].iloc[-1])
    sticky_price_cpi_T1 = float(sticky_price_cpi_df[sticky_price_cpi_code].iloc[-2])
    sticky_price_cpi_delta = sticky_price_cpi_T0 - sticky_price_cpi_T1

    five_yr_inflation_rate_T0 = float(five_yr_inflation_rate_df[five_yr_inflation_rate_code].iloc[-1])
    five_yr_inflation_rate_T1 = float(five_yr_inflation_rate_df[five_yr_inflation_rate_code].iloc[-2])
    five_yr_inflation_rate_delta = five_yr_inflation_rate_T0 - five_yr_inflation_rate_T1
    
    ten_yr_inflation_rate_T0 = float(ten_yr_inflation_rate_df[ten_yr_inflation_rate_code].iloc[-1])
    ten_yr_inflation_rate_T1 = float(ten_yr_inflation_rate_df[ten_yr_inflation_rate_code].iloc[-2])
    ten_yr_inflation_rate_delta = ten_yr_inflation_rate_T0 - ten_yr_inflation_rate_T1
    
    container = st.container(border=True)
    with container:
        st.markdown("### Key Indicators & Metrics")
        
    
        col1, col2, col3, col4, col5 = st.columns(5)
    
        # row 1
        col1.metric("Unemployment Rate",f'{unemploy_rate_T0:,.3f}', f'{unemploy_rate_delta:.3f}',delta_color="inverse")
        col2.metric("DJIA", f'{dow_jones_T0:,.0f}',f'{dow_jones_delta:,.0f}',delta_color="inverse")
        col3.metric("Savings Rate",f'{savings_T0:,.3f}', f'{savings_delta:.3f}')
        col4.metric("S&P 500", f'{snp_data_T0:,.0f}', f'{snp_data_delta:.0f}')
        col5.metric("30Yr Mortgage Rate",f'{mortgate_data_T0:,.3f}', f'{mortgate_data_delta:.3f}',delta_color="inverse")
        
        # row 2
        col1.metric("10-Year Treasury",f'{ten_yr_treas_T0:,.3f}', f'{ten_yr_delta:.3f}',delta_color="inverse")
        col2.metric("BofA AAA US Corporate Index", f'{aaa_T0:.3f}',f'{aaa_delta:.3f}',delta_color="inverse")
        col3.metric("BofA BBB US Corporate Index", f'{bbb_T0:.3f}',f'{bbb_delta:.3f}',delta_color="inverse")
        col4.metric("BofA US High Yield Index", f'{hy_T0:.3f}',f'{hy_delta:.3f}',delta_color="inverse")
        col5.metric("Federal Funds Effective Rate", f'{fed_funds_T0:.3f}',f'{fed_funds_delta:.3f}',delta_color="inverse")
        
        # row 3
        col1.metric("CPI - All",f'{cpi_T0:.1f}', f'{cpi_delta:.1f}',delta_color="inverse")
        col2.metric("CPI - All Items Less Food and Energy",f'{cpi_less_food_energy_T0:.1f}', f'{cpi_less_food_energy_delta:.1f}',delta_color="inverse")
        col3.metric("Sticky Price Consumer Price Index less Food and Energy",f'{sticky_price_cpi_T0:.1f}', f'{sticky_price_cpi_delta:.1f}',delta_color="inverse")
        col4.metric("5-Year Breakeven Inflation Rate",f'{five_yr_inflation_rate_T0:.1f}', f'{five_yr_inflation_rate_delta:.1f}',delta_color="inverse")
        col5.metric("10-Year Breakeven Inflation Rate",f'{ten_yr_inflation_rate_T0:.1f}', f'{ten_yr_inflation_rate_delta:.1f}',delta_color="inverse")
        
    
    # this is used to style the metric card
        style_metric_cards(border_left_color="#031c34")
            
    st.sidebar.subheader('Line chart parameters')
    plot_data = st.sidebar.selectbox('Select data', (unemployment_rate_code,
                                                     dow_jones_code,
                                                     mortgage_code,
                                                     snp_code,
                                                     personal_savings_rate_code,
                                                     treasury_yield_code,
                                                     aaa_index_yield_code,
                                                     bbb_index_yield_code,
                                                     hy_index_yield_code,
                                                     fed_funds_rate_code,
                                                     cpi_series_code,
                                                     cpi_less_food_energy_series_code,
                                                     sticky_price_cpi_code,
                                                     five_yr_inflation_rate_code,
                                                     ten_yr_inflation_rate_code,
                                                     ),index=0)

    with st.expander("Graph of Selected Data"):
        st.markdown(f'### {data_label_dict[plot_data]}')
        st.line_chart (
            data_dict[plot_data],
            x=None,
            y=plot_data,
            height=250
            )    

if __name__ == '__main__':
    main()