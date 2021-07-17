# USA 2020




Solar_PV_cen = [act for act in ee if 'electricity production, photovoltaic, 570kWp open ground installation, multi-Si' == act['name'] and 'RoW' == act['location']][0]
Solar_PV_decen = [act for act in ee if 'electricity production, photovoltaic, 3kWp facade installation, multi-Si, laminated, integrated' == act['name'] and 'RoW' == act['location']][0]
CSP = [act for act in ee if 'electricity production, solar thermal parabolic trough, 50 MW' == act['name'] and 'RoW' == act['location']][0]
Wind_onshore = [act for act in ee if 'electricity production, wind, <1MW turbine, onshore' == act['name'] and 'RoW' == act['location']][0]
Wind_offshore = [act for act in ee if 'electricity production, wind, 1-3MW turbine, offshore' == act['name'] and 'RoW' == act['location']][0]
Wave = [act for act in ee if 'electricity production, wave' == act['name'] and 'GLO' == act['location']][0]
Hydro = [act for act in ee if 'electricity production, hydro, reservoir, alpine region' == act['name'] and 'RoW' == act['location']][0]
Other_renewables = [act for act in ee if 'electricity production, deep geothermal' == act['name'] and 'RoW' == act['location']][0]
Nuclear = [act for act in ee if 'electricity production, nuclear, boiling water reactor' == act['name'] and 'RoW' == act['location']][0]
Coal_ST = [act for act in ee if 'electricity production, hard coal' == act['name'] and 'RoW' == act['location']][0]
Oil_ST = [act for act in ee if 'electricity production, oil' == act['name'] and 'RoW' == act['location']][0]
Natural_gas_OC = [act for act in ee if 'electricity production, natural gas, conventional power plant' == act['name'] and 'RoW' == act['location']][0]
Biomass_ST = [act for act in ee if 'electricity production, wood, future' == act['name'] and 'GLO' == act['location']][0]
IGCC = [act for act in ee if 'Electricity, at power plant/hard coal, IGCC, no CCS/2025' == act['name'] and 'GLO' == act['location']][0]
Oil_CC = [act for act in ee if 'electricity production, oil' == act['name'] and 'RoW' == act['location']][0]
Natural_gas_CC = [act for act in ee if 'electricity production, natural gas, combined cycle power plant' == act['name'] and 'RoW' == act['location']][0]
Biomass_CC = [act for act in ee if 'Electricity, at BIGCC power plant 450MW, no CCS/2025' == act['name'] and 'GLO' == act['location']][0]
Coal_CCS = [act for act in ee if 'Electricity, at power plant/hard coal, pre, pipeline 200km, storage 1000m/2025' == act['name'] and 'GLO' == act['location']][0]
Oil_CCS = [act for act in ee if 'Electricity, at power plant/natural gas, post, pipeline 200km, storage 1000m/2025' == act['name'] and 'GLO' == act['location']][0]
Natural_gas_CCS = [act for act in ee if 'Electricity, at power plant/natural gas, pre, pipeline 200km, storage 1000m/2025' == act['name'] and 'GLO' == act['location']][0]
Biomass_CCS = [act for act in ee if 'Electricity, at BIGCC power plant 450MW, pre, pipeline 200km, storage 1000m/2025' == act['name'] and 'GLO' == act['location']][0]
Coal_CHP = [act for act in ee if 'heat and power co-generation, hard coal' == act['name'] and 'RoW' == act['location']][0]
Oil_CHP = [act for act in ee if 'heat and power co-generation, oil' == act['name'] and 'RoW' == act['location']][0]
Natural_gas_CHP = [act for act in ee if 'heat and power co-generation, natural gas, combined cycle power plant, 400MW electrical' == act['name'] and 'RoW' == act['location']][0]
Biomass_CHP = [act for act in ee if 'heat and power co-generation, wood chips, 6667 kW, state-of-the-art 2014' == act['name'] and 'RoW' == act['location']][0]
Coal_CHP_CCS = [act for act in ee if 'Electricity, at power plant/hard coal, pre, pipeline 200km, storage 1000m/2025' == act['name'] and 'GLO' == act['location']][0]
Oil_CHP_CCS = [act for act in ee if 'Electricity, at power plant/natural gas, pre, pipeline 200km, storage 1000m/2025' == act['name'] and 'GLO' == act['location']][0]
Natural_gas_CHP_CCS = [act for act in ee if 'Electricity, at power plant/natural gas, pre, pipeline 200km, storage 1000m/2025' == act['name'] and 'GLO' == act['location']][0]
Biomass_CHP_CCS = [act for act in ee if 'Electricity, at wood burning power plant 20 MW, truck 25km, post, pipeline 200km, storage 1000m/2025' == act['name'] and 'GLO' == act['location']][0]


us_2020 = ee.new_activity(code = 'us_2020', name = "USA 2020", unit = "unit")

us_2020.new_exchange(input = Solar_PV_cen.key, amount = df['USA_Num'][0], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Solar_PV_decen.key, amount = df['USA_Num'][1], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = CSP.key, amount = df['USA_Num'][2], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Wind_onshore.key, amount = df['USA_Num'][3], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Wind_offshore.key, amount = df['USA_Num'][4], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Wave.key, amount = df['USA_Num'][5], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Hydro.key, amount = df['USA_Num'][6], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Other_renewables.key, amount = df['USA_Num'][7], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Nuclear.key, amount = df['USA_Num'][8], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Coal_ST.key, amount = df['USA_Num'][9], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Oil_ST.key, amount = df['USA_Num'][10], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Natural_gas_OC.key, amount = df['USA_Num'][11], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Biomass_ST.key, amount = df['USA_Num'][12], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = IGCC.key, amount = df['USA_Num'][13], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Oil_CC.key, amount = df['USA_Num'][14], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Natural_gas_CC.key, amount = df['USA_Num'][15], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Biomass_CC.key, amount = df['USA_Num'][16], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Coal_CCS.key, amount = df['USA_Num'][17], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Oil_CCS.key, amount = df['USA_Num'][18], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Natural_gas_CCS.key, amount = df['USA_Num'][19], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Biomass_CCS.key, amount = df['USA_Num'][20], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Coal_CHP.key, amount = df['USA_Num'][21], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Oil_CHP.key, amount = df['USA_Num'][22], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Natural_gas_CHP.key, amount = df['USA_Num'][23], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Biomass_CHP.key, amount = df['USA_Num'][24], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Coal_CHP_CCS.key, amount = df['USA_Num'][25], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Oil_CHP_CCS.key, amount = df['USA_Num'][26], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Natural_gas_CHP_CCS.key, amount = df['USA_Num'][27], unit = "kilowatt hour", type = 'technosphere').save()
us_2020.new_exchange(input = Biomass_CHP_CCS.key, amount = df['USA_Num'][28], unit = "kilowatt hour", type = 'technosphere').save()

us_2030 = ee.new_activity(code = 'us_2030', name = "USA 2030", unit = "unit")

us_2030.new_exchange(input = Solar_PV_cen.key, amount = df['USA_Num'][29], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Solar_PV_decen.key, amount = df['USA_Num'][30], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = CSP.key, amount = df['USA_Num'][31], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Wind_onshore.key, amount = df['USA_Num'][32], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Wind_offshore.key, amount = df['USA_Num'][33], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Wave.key, amount = df['USA_Num'][34], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Hydro.key, amount = df['USA_Num'][35], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Other_renewables.key, amount = df['USA_Num'][36], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Nuclear.key, amount = df['USA_Num'][37], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Coal_ST.key, amount = df['USA_Num'][38], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Oil_ST.key, amount = df['USA_Num'][39], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Natural_gas_OC.key, amount = df['USA_Num'][40], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Biomass_ST.key, amount = df['USA_Num'][41], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = IGCC.key, amount = df['USA_Num'][42], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Oil_CC.key, amount = df['USA_Num'][43], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Natural_gas_CC.key, amount = df['USA_Num'][44], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Biomass_CC.key, amount = df['USA_Num'][45], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Coal_CCS.key, amount = df['USA_Num'][46], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Oil_CCS.key, amount = df['USA_Num'][47], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Natural_gas_CCS.key, amount = df['USA_Num'][48], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Biomass_CCS.key, amount = df['USA_Num'][49], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Coal_CHP.key, amount = df['USA_Num'][50], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Oil_CHP.key, amount = df['USA_Num'][51], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Natural_gas_CHP.key, amount = df['USA_Num'][52], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Biomass_CHP.key, amount = df['USA_Num'][53], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Coal_CHP_CCS.key, amount = df['USA_Num'][54], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Oil_CHP_CCS.key, amount = df['USA_Num'][55], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Natural_gas_CHP_CCS.key, amount = df['USA_Num'][56], unit = "kilowatt hour", type = 'technosphere').save()
us_2030.new_exchange(input = Biomass_CHP_CCS.key, amount = df['USA_Num'][57], unit = "kilowatt hour", type = 'technosphere').save()

us_2040 = ee.new_activity(code = 'us_2040', name = "USA 2040", unit = "unit")

us_2040.new_exchange(input = Solar_PV_cen.key, amount = df['USA_Num'][58], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Solar_PV_decen.key, amount = df['USA_Num'][59], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = CSP.key, amount = df['USA_Num'][60], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Wind_onshore.key, amount = df['USA_Num'][61], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Wind_offshore.key, amount = df['USA_Num'][62], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Wave.key, amount = df['USA_Num'][63], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Hydro.key, amount = df['USA_Num'][64], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Other_renewables.key, amount = df['USA_Num'][65], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Nuclear.key, amount = df['USA_Num'][66], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Coal_ST.key, amount = df['USA_Num'][67], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Oil_ST.key, amount = df['USA_Num'][68], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Natural_gas_OC.key, amount = df['USA_Num'][69], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Biomass_ST.key, amount = df['USA_Num'][70], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = IGCC.key, amount = df['USA_Num'][71], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Oil_CC.key, amount = df['USA_Num'][72], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Natural_gas_CC.key, amount = df['USA_Num'][73], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Biomass_CC.key, amount = df['USA_Num'][74], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Coal_CCS.key, amount = df['USA_Num'][75], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Oil_CCS.key, amount = df['USA_Num'][76], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Natural_gas_CCS.key, amount = df['USA_Num'][77], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Biomass_CCS.key, amount = df['USA_Num'][78], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Coal_CHP.key, amount = df['USA_Num'][79], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Oil_CHP.key, amount = df['USA_Num'][80], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Natural_gas_CHP.key, amount = df['USA_Num'][81], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Biomass_CHP.key, amount = df['USA_Num'][82], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Coal_CHP_CCS.key, amount = df['USA_Num'][83], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Oil_CHP_CCS.key, amount = df['USA_Num'][84], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Natural_gas_CHP_CCS.key, amount = df['USA_Num'][85], unit = "kilowatt hour", type = 'technosphere').save()
us_2040.new_exchange(input = Biomass_CHP_CCS.key, amount = df['USA_Num'][86], unit = "kilowatt hour", type = 'technosphere').save()

us_2050 = ee.new_activity(code = 'us_2050', name = "USA 2050", unit = "unit")

us_2050.new_exchange(input = Solar_PV_cen.key, amount = df['USA_Num'][87], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Solar_PV_decen.key, amount = df['USA_Num'][88], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = CSP.key, amount = df['USA_Num'][89], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Wind_onshore.key, amount = df['USA_Num'][90], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Wind_offshore.key, amount = df['USA_Num'][91], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Wave.key, amount = df['USA_Num'][92], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Hydro.key, amount = df['USA_Num'][93], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Other_renewables.key, amount = df['USA_Num'][94], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Nuclear.key, amount = df['USA_Num'][95], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Coal_ST.key, amount = df['USA_Num'][96], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Oil_ST.key, amount = df['USA_Num'][97], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Natural_gas_OC.key, amount = df['USA_Num'][98], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Biomass_ST.key, amount = df['USA_Num'][99], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = IGCC.key, amount = df['USA_Num'][100], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Oil_CC.key, amount = df['USA_Num'][101], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Natural_gas_CC.key, amount = df['USA_Num'][102], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Biomass_CC.key, amount = df['USA_Num'][103], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Coal_CCS.key, amount = df['USA_Num'][104], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Oil_CCS.key, amount = df['USA_Num'][105], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Natural_gas_CCS.key, amount = df['USA_Num'][106], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Biomass_CCS.key, amount = df['USA_Num'][107], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Coal_CHP.key, amount = df['USA_Num'][108], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Oil_CHP.key, amount = df['USA_Num'][109], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Natural_gas_CHP.key, amount = df['USA_Num'][110], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Biomass_CHP.key, amount = df['USA_Num'][111], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Coal_CHP_CCS.key, amount = df['USA_Num'][112], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Oil_CHP_CCS.key, amount = df['USA_Num'][113], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Natural_gas_CHP_CCS.key, amount = df['USA_Num'][114], unit = "kilowatt hour", type = 'technosphere').save()
us_2050.new_exchange(input = Biomass_CHP_CCS.key, amount = df['USA_Num'][115], unit = "kilowatt hour", type = 'technosphere').save()



