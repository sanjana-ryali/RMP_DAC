# AIR CONTACTOR

ac_construction = ee.new_activity(code = 'ac_construction', name = "Air Contactor Construction", unit = "unit")

Concrete = [act for act in ee if 'market for concrete, normal' == act['name'] and 'RoW' == act['location']][0]
Low_alloyed_steel = [act for act in ee if 'market for steel, low-alloyed' == act['name'] and 'GLO' == act['location']][0]
Stainless_steel = [act for act in ee if 'steel production, chromium steel 18/8, hot rolled' == act['name'] and 'RoW' == act['location']][0]
Polyeruthane = [act for act in ee if 'market for polyurethane, flexible foam' == act['name'] and 'RoW' == act['location']][0]
Glass_fiber = [act for act in ee if 'market for glass fibre' == act['name'] and 'GLO' == act['location']][0]
Polypropylene = [act for act in ee if 'market for polypropylene, granulate' == act['name'] and 'GLO' == act['location']][0]
Polyvinyl = [act for act in ee if 'market for polyvinylchloride, bulk polymerised' == act['name'] and 'GLO' == act['location']][0]

ac_construction.new_exchange(input = Concrete.key, amount = 0.0067, unit = "cubic meter",type = 'technosphere').save()
ac_construction.new_exchange(input = Low_alloyed_steel.key, amount = 0.27, unit = "kilogram",type = 'technosphere').save()
ac_construction.new_exchange(input = Stainless_steel.key, amount = 0.0017, unit = "kilogram",type = 'technosphere').save()
ac_construction.new_exchange(input = Polyeruthane.key, amount = 0.0005, unit = "kilogram",type = 'technosphere').save()
ac_construction.new_exchange(input = Glass_fiber.key, amount = 0.0038, unit = "kilogram",type = 'technosphere').save()
ac_construction.new_exchange(input = Polypropylene.key, amount = 0.0008, unit = "kilogram",type = 'technosphere').save()
ac_construction.new_exchange(input = Polyvinyl.key, amount = 0.76, unit = "kilogram",type = 'technosphere').save()

# PELLET REACTOR

pellet_reactor_construction = ee.new_activity(code = 'pellet_reactor_construction', name = "Pellet Reactor Construction", unit = "unit")

Concrete_pr = [act for act in ee if 'market for concrete, normal' == act['name'] and 'RoW' == act['location']][0]
Stainless_steel_pr = [act for act in ee if 'steel production, chromium steel 18/8, hot rolled' == act['name'] and 'RoW' == act['location']][0]

pellet_reactor_construction.new_exchange(input = Concrete_pr.key, amount = 0.0033, unit = "cubic meter",type = 'technosphere').save()
pellet_reactor_construction.new_exchange(input = Stainless_steel_pr.key, amount = 0.023, unit = "kilogram",type = 'technosphere').save()

# CALCINER

calciner_construction = ee.new_activity(code = 'calciner_construction', name = "Calciner Construction", unit = "unit")

Concrete_c = [act for act in ee if 'market for concrete, normal' == act['name'] and 'RoW' == act['location']][0]
Low_alloyed_steel_c = [act for act in ee if 'market for steel, low-alloyed' == act['name'] and 'GLO' == act['location']][0]
Refractory_brick_c = [act for act in ee if 'market for refractory, basic, packed' == act['name'] and 'GLO' == act['location']][0]

calciner_construction.new_exchange(input = Concrete_c.key, amount = 0.0021, unit = "cubic meter",type = 'technosphere').save()
calciner_construction.new_exchange(input = Low_alloyed_steel_c.key, amount = 0.059, unit = "kilogram",type = 'technosphere').save()
calciner_construction.new_exchange(input = Refractory_brick_c.key, amount = 0.12, unit = "kilogram",type = 'technosphere').save()

# OTHER EQUIPMENT

other_equipment = ee.new_activity(code = 'other_equipment', name = "Other Equipment", unit = "unit")

Concrete_oe = [act for act in ee if 'market for concrete, normal' == act['name'] and 'RoW' == act['location']][0]
Aluminium_oe = [act for act in ee if 'market for aluminium, wrought alloy' == act['name'] and 'GLO' == act['location']][0]
Low_alloyed_steel_oe = [act for act in ee if 'market for steel, low-alloyed' == act['name'] and 'GLO' == act['location']][0]
Stainless_steel_oe = [act for act in ee if 'steel production, chromium steel 18/8, hot rolled' == act['name'] and 'RoW' == act['location']][0]
Carbon_steel_oe = [act for act in ee if 'market for steel, unalloyed' == act['name'] and 'GLO' == act['location']][0]

other_equipment.new_exchange(input = Concrete_oe.key, amount = 0.0037, unit = "cubic meter",type = 'technosphere').save()
other_equipment.new_exchange(input = Aluminium_oe.key, amount = 0.0025, unit = "kilogram",type = 'technosphere').save()
other_equipment.new_exchange(input = Low_alloyed_steel_oe.key, amount = 0.048, unit = "kilogram",type = 'technosphere').save()
other_equipment.new_exchange(input = Stainless_steel_oe.key, amount = 0.033, unit = "kilogram",type = 'technosphere').save()
other_equipment.new_exchange(input = Carbon_steel_oe.key, amount = 0.27, unit = "kilogram",type = 'technosphere').save()

# DAC OPERATION: WATER

dac_operation_water = ee.new_activity(code = 'dac_operation_water', name = "DAC Operation Water", unit = "kilogram")

Water = [act for act in ee if 'market for tap water' == act['name'] and 'RoW' == act['location']][0]

dac_operation_water.new_exchange(input = Water.key, amount = 3437, unit = "kilogram",type = 'technosphere').save()

# DAC OPERATION: HEAT

dac_operation_heat = ee.new_activity(code = 'dac_operation_heat', name = "DAC Operation Heat", unit = "MJ")

Natural_gas = [act for act in ee if 'heat production, natural gas, at industrial furnace >100kW' == act['name'] and 'RoW' == act['location']][0]

dac_operation_heat.new_exchange(input = Natural_gas.key, amount = 6280, unit = "MJ",type = 'technosphere').save()

# DAC OPERATION: MATERIAL

dac_operation_material = ee.new_activity(code = 'dac_operation_material', name = "DAC Operation Material", unit = "kg")

Potassium_hydroxide = [act for act in ee if 'market for potassium hydroxide' == act['name'] and 'GLO' == act['location']][0]
Calcium_carbonate = [act for act in ee if 'market for limestone, crushed, for mill' == act['name'] and 'RoW' == act['location']][0]

dac_operation_material.new_exchange(input = Potassium_hydroxide.key, amount = 4.0, unit = "kilogram",type = 'technosphere').save()
dac_operation_material.new_exchange(input = Calcium_carbonate.key, amount = 3.5, unit = "kilogram",type = 'technosphere').save()

# DAC END-OF-LIFE

dac_eol = ee.new_activity(code = 'dac_eol', name = "DAC End of life", unit = "unit")

Concrete_eol = [act for act in ee if 'treatment of waste concrete, inert material landfill' == act['name'] and 'RoW' == act['location']][0]
Steel_eol = [act for act in ee if 'treatment of waste reinforcement steel, recycling' == act['name'] and 'RoW' == act['location']][0]
Glass_fiber_eol = [act for act in ee if 'treatment of waste plastic, mixture, municipal incineration' == act['name'] and 'RoW' == act['location']][0]
Polyvinyl_chloride_eol = [act for act in ee if 'treatment of waste polyvinylchloride, municipal incineration' == act['name'] and 'RoW' == act['location']][0]
Polypropylene_eol = [act for act in ee if 'treatment of waste polypropylene, municipal incineration' == act['name'] and 'RoW' == act['location']][0]
Polyeruthane_eol = [act for act in ee if 'treatment of waste polyurethane, municipal incineration' == act['name'] and 'RoW' == act['location']][0]
Refractory_brick_eol = [act for act in ee if 'treatment of waste brick, collection for final disposal' == act['name'] and 'RoW' == act['location']][0]
Aluminium_eol = [act for act in ee if 'treatment of aluminium scrap, post-consumer, prepared for recycling, at remelter' == act['name'] and 'RoW' == act['location']][0]
Potassium_hydroxide_eol = [act for act in ee if 'treatment of spent solvent mixture, hazardous waste incineration' == act['name'] and 'RoW' == act['location']][0]
Calcium_carbonate_eol = [act for act in ee if 'treatment of limestone residue, inert material landfill' == act['name'] and 'RoW' == act['location']][0]

dac_eol.new_exchange(input = Concrete_eol.key, amount = 38, unit = "kilogram",type = 'technosphere').save()
dac_eol.new_exchange(input = Steel_eol.key, amount = 0.6, unit = "kilogram",type = 'technosphere').save()
dac_eol.new_exchange(input = Glass_fiber_eol.key, amount = 0.0038, unit = "kilogram",type = 'technosphere').save()
dac_eol.new_exchange(input = Polyvinyl_chloride_eol.key, amount = 0.76, unit = "kilogram",type = 'technosphere').save()
dac_eol.new_exchange(input = Polypropylene_eol.key, amount = 0.0008, unit = "kilogram",type = 'technosphere').save()
dac_eol.new_exchange(input = Polyeruthane_eol.key, amount = 0.0005, unit = "kilogram",type = 'technosphere').save()
dac_eol.new_exchange(input = Refractory_brick_eol.key, amount = 0.12, unit = "kilogram",type = 'technosphere').save()
dac_eol.new_exchange(input = Aluminium_eol.key, amount = 0.0023, unit = "kilogram",type = 'technosphere').save()
dac_eol.new_exchange(input = Potassium_hydroxide_eol.key, amount = 4.0, unit = "kilogram",type = 'technosphere').save()
dac_eol.new_exchange(input = Calcium_carbonate_eol.key, amount = 3.5, unit = "kilogram",type = 'technosphere').save()

