'''
*********************************************************************************
*
*
THE FEATURES CONCERNED BY THE ORDINAL ENCODING
*
*
*********************************************************************************
'''
X_ord_columns = [
    'MSZoning',        # Identifies the general zoning classification of the sale
    'Condition1',      # Proximity to various conditions
    'Heating',         # Type of heating
    'Street',          # Type of road access to property
    'CentralAir',      # Central air conditioning
    'Foundation',      # Type of foundation
    'ExterQual',       # Evaluates the quality of the material on the exterior
    'ExterCond',       # Evaluates the present condition of the material on the exterior
    'BsmtQual',        # Evaluates the height of the basement
    'BsmtCond',        # Evaluates the general condition of the basement
    'BsmtExposure',    # Refers to walkout or garden level walls
    'BsmtFinType1',    # Rating of basement finished area
    'KitchenQual',     # Kitchen quality
    'FireplaceQu',     # Fireplace quality
    'HeatingQC',       # Heating quality and condition
    'Utilities',       # Type of utilities available
    'PoolQC',          # Pool quality
    'GarageQual',      # Garage quality
    'GarageCond',      # Garage condition
    'Fence',           # Fence quality
    'PavedDrive',      # Paved driveway
    'LandContour',     # Flatness of the property
    'LandSlope',       # Slope of the property
    'BsmtFinType2',    # Rating of basement finished area (if multiple types)
    'GarageFinish',    # Interior finish of the garage
    'LotShape',        # General shape of property
    'Functional',      # Home functionality
]
'''
*********************************************************************************
*
*
SORT THE CONTENT OF THE FEATURES BY ORDER OF IMPORTANCE (LEAST TO MOST)
*
*
*********************************************************************************
'''
# ========================================================
# Identifies the general zoning classification of the sale 
# ========================================================
MSZoning_cat = [
    'NA',
    "I",         # Industrial – typically least desirable for residential homes
    "C (all)",   # Commercial – not ideal for detached homes, more noise/traffic
    "A",   # Agriculture – large lots, but limited infrastructure
    "FV",  # Floating Village Residential – niche market, could be undervalued or overvalued depending on location
    "RH",  # Residential High Density – more affordable, smaller lots or multifamily
    "RM",  # Residential Medium Density – balanced, decent price
    "RP",  # Residential Low Density Park – usually more premium zoning
    "RL"   # Residential Low Density – often highest value for suburban homes
]
# ========================================================
# Proximity to various conditions 
# ========================================================
Condition1_cat = [
    'NA',
    "RRAe",  # Adjacent to East-West Railroad
    "RRAn",  # Adjacent to North-South Railroad
    "RRNe",  # Within 200' of East-West Railroad
    "RRNn",  # Within 200' of North-South Railroad
    "Artery",# Adjacent to arterial street
    "Feedr", # Adjacent to feeder street
    "Norm",  # Normal
    "PosN",  # Near positive off-site feature
    "PosA"   # Adjacent to positive off-site feature
]
# ========================================================
# Type of heating 
# ========================================================
Heating_cat = [
    'NA',
    "Grav",   # Gravity furnace (older, less efficient)
    "Floor",  # Floor Furnace
    "Wall",   # Wall furnace
    "OthW",   # Hot water or steam heat other than gas
    "GasW",   # Gas hot water or steam heat
    "GasA"    # Gas forced warm air furnace (most common, generally preferred)
]
# ========================================================
# Type of road access to property 
# ========================================================
Street_cat = [
    'NA',
    "Grvl",  # Gravel – less desirable, can affect property accessibility and maintenance costs
    "Pave"   # Paved – more desirable, associated with better infrastructure and higher property values
]
# ========================================================
# Central air conditioning
# ========================================================
CentralAir_cat = [
    'NA',
    "N",  # No central air – generally less desirable, especially in hot climates
    "Y"   # Yes central air – more desirable, adds comfort and value to the home
]
# ========================================================
# Type of foundation
# ========================================================
Foundation_cat = [
    'NA',
    "Wood",     # Least durable, susceptible to moisture/insects
    "Stone",    # Older, less common, may need more maintenance
    "BrkTil",   # Brick & Tile, older method
    "CBlock",   # Cinder Block, common but can crack over time
    "Slab",     # Slab, efficient but less access to utilities
    "PConc"     # Poured Concrete, most modern and preferred
]
# =====================================================
# Evaluates the quality of the material on the exterior 
# =====================================================
ExterQual_cat = [
    "NA",  # For missing values
    "Po",       # Poor
    "Fa",       # Fair
    "TA",       # Typical/Average
    "Gd",       # Good
    "Ex"        # Excellent
]
# ===============================================================
# Evaluates the present condition of the material on the exterior 
# ===============================================================
ExterCond_cat = [
    "NA",  # for missing values
    "Po",       # Poor – serious issues, may need repairs
    "Fa",       # Fair – visible wear, some impact on value
    "TA",       # Typical/Average – acceptable condition
    "Gd",       # Good – well maintained
    "Ex"        # Excellent – like-new or recently updated
]
# ===============================================================
# Evaluates the height of the basement 
# ===============================================================
BsmtQual_cat = [
    "NA",       # No basement – lower value than even a low ceiling
    "Po",       # <70 inches – unusable or crawl space
    "Fa",       # 70–79 inches – tight, but usable
    "TA",       # 80–89 inches – standard height, acceptable
    "Gd",       # 90–99 inches – spacious
    "Ex"        # 100+ inches – best possible
]
# ===============================================================
# Evaluates the general condition of the basement 
# ===============================================================
BsmtCond_cat = [
    "NA",       # No basement – less utility, lower value
    "Po",       # Severe damage/wetness
    "Fa",       # Moderate issues – dampness, cracks
    "TA",       # Typical/some dampness – acceptable
    "Gd",       # Good condition
    "Ex"        # Excellent – dry and solid
]
# ===============================================================
# Refers to walkout or garden level walls 
# ===============================================================
BsmtExposure_cat = [
    "NA",  # No basement – lowest value for exposure potential
    "No",  # No exposure – completely underground
    "Mn",  # Minimum – small windows or partial view
    "Av",  # Average – decent lighting & partial walkout
    "Gd"   # Good – full walkout, lots of light
]
# ===============================================================
# Rating of basement finished area 
# ===============================================================
BsmtFinType1_cat = [
    "NA",    # No Basement – no added living space
    "Unf",   # Unfinished – unusable as living area
    "LwQ",   # Low Quality finished – limited appeal
    "Rec",   # Recreational area – some value, not a true living space
    "BLQ",   # Below Average Living Quarters – livable, but basic
    "ALQ",   # Average Living Quarters – usable and fairly comfortable
    "GLQ"    # Good Living Quarters – fully finished and high quality
]
# ===============================================================
# Kitchen quality 
# ===============================================================
KitchenQual_cat = [
    "NA",  # for missing or imputed values
    "Po",       # Poor – outdated, low-end materials
    "Fa",       # Fair – older or lower quality appliances/layout
    "TA",       # Typical – standard, functional kitchen
    "Gd",       # Good – some upgrades, decent materials
    "Ex"        # Excellent – high-end appliances, finishes, layout
]
# ===============================================================
# Fireplace quality 
# ===============================================================
FireplaceQu_cat = [
    "NA",   # No Fireplace – no added value for this feature
    "Po",   # Poor - Ben Franklin Stove, not considered a real fireplace
    "Fa",   # Fair - Basement fireplace, minimal appeal
    "TA",   # Average - Prefabricated or basement fireplace, functional
    "Gd",   # Good - Masonry fireplace in a prominent location
    "Ex"    # Excellent - High-quality masonry fireplace, a feature
]
# ===============================================================
# Heating quality and condition 
# ===============================================================
HeatingQC_cat = [
    'NA',
    "Po",  # Poor
    "Fa",  # Fair
    "TA",  # Average/Typical
    "Gd",  # Good
    "Ex"   # Excellent
]
# ===============================================================
# Type of utilities available 
# ===============================================================
Utilities_cat = [
    'NA',
    "ELO",     # Electricity only – least desirable
    "NoSeWa",  # Electricity and Gas
    "NoSewr",  # Electricity, Gas, and Water (no sewer)
    "AllPub"   # All public Utilities – most desirable
]
# ===============================================================
# Pool quality
# ===============================================================
PoolQC_cat = [
    "NA",  # No Pool – lowest value
    "Fa",  # Fair
    "TA",  # Typical/Average
    "Gd",  # Good
    "Ex"   # Excellent
]
# ===============================================================
# Garage quality
# ===============================================================
GarageQual_cat = [
    "NA",  # No Garage – typically less desirable than even a low-quality garage
    "Po",  # Poor
    "Fa",  # Fair
    "TA",  # Typical/Average
    "Gd",  # Good
    "Ex"   # Excellent
]
# ===============================================================
# Garage condition
# ===============================================================
GarageCond_cat = [
    "NA",  # No Garage – typically considered the least desirable
    "Po",  # Poor – significant issues, least desirable condition
    "Fa",  # Fair – moderate issues
    "TA",  # Typical/Average – acceptable condition
    "Gd",  # Good – well-maintained
    "Ex"   # Excellent – pristine, like new
]
# ===============================================================
# Fence quality
# ===============================================================
Fence_cat = [
    "NA",     # No Fence – no fence, least desirable
    "MnWw",   # Minimum Wood/Wire – basic, minimal privacy
    "MnPrv",  # Minimum Privacy – not much privacy provided
    "GdWo",   # Good Wood – decent quality, common material
    "GdPrv"   # Good Privacy – highest quality, maximum privacy
]
# ===============================================================
# Paved driveway
# ===============================================================
PavedDrive_cat = [
    'NA',
    "N",  # Dirt/Gravel – least desirable
    "P",  # Partial Pavement – somewhat desirable
    "Y"   # Paved – most desirable
]
# ===============================================================
# Flatness of the property
# ===============================================================
LandContour_cat = [
    'NA',
    "Lvl",  # Near Flat/Level
    "Bnk",  # Banked - Quick and significant rise from street grade to building
    "HLS",  # Hillside - Significant slope from side to side
    "Low"   # Depression
]
# ===============================================================
# Slope of property
# ===============================================================
LandSlope_cat = [
    'NA',
    "Gtl",  # Gentle slope
    "Mod",  # Moderate Slope
    "Sev"   # Severe Slope
]
# ===============================================================
# Rating of basement finished area (if multiple types)
# ===============================================================
BsmtFinType2_cat = [
    "NA",    # No Basement
    "Unf",   # Unfinished
    "LwQ",   # Low Quality
    "Rec",   # Average Rec Room
    "BLQ",   # Below Average Living Quarters
    "ALQ",   # Average Living Quarters
    "GLQ"    # Good Living Quarters
]
# ===============================================================
# Interior finish of the garage
# ===============================================================
GarageFinish_cat = [
    "NA",    # No Garage
    "Unf",   # Unfinished
    "RFn",   # Rough Finished
    "Fin"    # Finished
]
# ===============================================================
# General shape of property
# ===============================================================
LotShape_cat = [
    'NA',
    "Reg",  # Regular
    "IR1",  # Slightly irregular
    "IR2",  # Moderately Irregular
    "IR3"   # Irregular
]
# ===================================================================
# Home functionality (Assume typical unless deductions are warranted)
# ===================================================================
Functional_cat = [
    'NA',
    "Typ",  # Typical Functionality
    "Min1", # Minor Deductions 1
    "Min2", # Minor Deductions 2
    "Mod",  # Moderate Deductions
    "Maj1", # Major Deductions 1
    "Maj2", # Major Deductions 2
    "Sev",  # Severely Damaged
    "Sal"   # Salvage only
]
'''
*********************************************************************************
*
*
PUT THE ORDINAL FEATURES INTO A LIST OF CATEGORIES (LIST OF LISTS)
*
*
*********************************************************************************
'''
categories = [
    MSZoning_cat,      # Identifies the general zoning classification of the sale
    Condition1_cat,    # Proximity to various conditions
    Heating_cat,       # Type of heating
    Street_cat,        # Type of road access to property
    CentralAir_cat,    # Central air conditioning
    Foundation_cat,    # Type of foundation
    ExterQual_cat,     # Evaluates the quality of the material on the exterior
    ExterCond_cat,     # Evaluates the present condition of the material on the exterior
    BsmtQual_cat,      # Evaluates the height of the basement
    BsmtCond_cat,      # Evaluates the general condition of the basement
    BsmtExposure_cat,  # Refers to walkout or garden level walls
    BsmtFinType1_cat,  # Rating of basement finished area
    KitchenQual_cat,   # Kitchen quality
    FireplaceQu_cat,   # Fireplace quality
    HeatingQC_cat,     # Heating quality and condition
    Utilities_cat,     # Type of utilities available
    PoolQC_cat,        # Pool quality
    GarageQual_cat,    # Garage quality
    GarageCond_cat,    # Garage condition
    Fence_cat,         # Fence quality
    PavedDrive_cat,    # Paved driveway
    LandContour_cat,   # Flatness of the property
    LandSlope_cat,     # Slope of the property
    BsmtFinType2_cat,  # Rating of basement finished area (if multiple types)
    GarageFinish_cat,  # Interior finish of the garage
    LotShape_cat,      # General shape of property
    Functional_cat     # Home functionality
]