


CREATE OR REPLACE TABLE CAPSTONE.STATE_DATA_CENTER.CALIFORNIA_FLAT (
    LOCATION                        VARCHAR(16777216),
    ENERGY                          VARCHAR,
    AREA                            VARCHAR,
    ESTABLISHED                     VARCHAR,
    DOWNLOADS                       VARCHAR,
    -- CAPACITY columns
    FULLY_BUILT_OUT_POWER           VARCHAR,
    FULLY_BUILT_OUT_WHITESPACE      VARCHAR,
    TOTAL_BUILDING_SIZE             VARCHAR,
    -- SERVICES columns
    FULL_CABINETS                   VARCHAR,
    PARTIAL_CABINETS                VARCHAR,
    SHARED_RACKSPACE                VARCHAR,
    CAGES                           VARCHAR,
    SUITES                          VARCHAR,
    BUILD_TO_SUIT                   VARCHAR,
    FOOTPRINTS                      VARCHAR,
    REMOTE_HANDS                    VARCHAR,
    -- POWER columns
    MAX_POWER_AREA                  VARCHAR,
    UPS_REDUNDANCY                  VARCHAR,
    COOLING_REDUNDANCY              VARCHAR,
    STANDBY_POWER_REDUNDANCY         VARCHAR,
    -- COMPLIANCE columns
    TIER_DESIGN                     VARCHAR,
    DSS_PCI_CERTIFIED               VARCHAR,
    ISO27001_CERTIFIED              VARCHAR,
    HIPAA                           VARCHAR,
    SOC_2_TYPE_II_CERTIFIED         VARCHAR,
    SOC_3_TYPE2_CERTIFIED           VARCHAR,
    NIST_800_53                     VARCHAR,
    -- SECURITY columns
    CCTV_SURVEILLANCE               VARCHAR,
    BIOMETRIC_ACCESS_CONTROL        VARCHAR,
    CARD_ACCESS_CONTROL             VARCHAR,
    ONSITE_SECURITY_STAFF           VARCHAR,
    ONSITE_TECHNICAL_STAFF          VARCHAR,
    -- BUILDING columns
    YEAR_OPERATIONAL                VARCHAR,
    ROOF_ACCESS                     VARCHAR,
    BUILDING_FLOORS                 VARCHAR,
    MAX_FLOOR_LOAD                  VARCHAR,
    -- AMENITIES columns
    MEET_ME_ROOM_MMR                VARCHAR,
    -- STATISTICS columns
    INTERNET_EXCHANGE_POINTS        VARCHAR,
    PEERING_NETWORKS                VARCHAR,
    NETWORK_PROVIDERS               VARCHAR,
    TENANTS_OFFERING_COLOCATION     VARCHAR,
    CHILD_DATA_CENTER_LISTINGS      VARCHAR
);





INSERT INTO CAPSTONE.STATE_DATA_CENTER.CALIFORNIA_FLAT
(
    LOCATION,
    ENERGY,
    AREA,
    ESTABLISHED,
    DOWNLOADS,
    FULLY_BUILT_OUT_POWER,
    FULLY_BUILT_OUT_WHITESPACE,
    TOTAL_BUILDING_SIZE,
    FULL_CABINETS,
    PARTIAL_CABINETS,
    SHARED_RACKSPACE,
    CAGES,
    SUITES,
    BUILD_TO_SUIT,
    FOOTPRINTS,
    REMOTE_HANDS,
    MAX_POWER_AREA,
    UPS_REDUNDANCY,
    COOLING_REDUNDANCY,
    STANDBY_POWER_REDUNDANCY,
    TIER_DESIGN,
    DSS_PCI_CERTIFIED,
    ISO27001_CERTIFIED,
    HIPAA,
    SOC_2_TYPE_II_CERTIFIED,
    SOC_3_TYPE2_CERTIFIED,
    NIST_800_53,
    CCTV_SURVEILLANCE,
    BIOMETRIC_ACCESS_CONTROL,
    CARD_ACCESS_CONTROL,
    ONSITE_SECURITY_STAFF,
    ONSITE_TECHNICAL_STAFF,
    YEAR_OPERATIONAL,
    ROOF_ACCESS,
    BUILDING_FLOORS,
    MAX_FLOOR_LOAD,
    MEET_ME_ROOM_MMR,
    INTERNET_EXCHANGE_POINTS,
    PEERING_NETWORKS,
    NETWORK_PROVIDERS,
    TENANTS_OFFERING_COLOCATION,
    CHILD_DATA_CENTER_LISTINGS
)
SELECT 
    LOCATION,
    ENERGY,
    AREA,
    ESTABLISHED,
    DOWNLOADS,
    PARSE_JSON(CAPACITY):"Fully Built-Out Power"::VARCHAR,
    PARSE_JSON(CAPACITY):"Fully Built-Out Whitespace"::VARCHAR,
    PARSE_JSON(CAPACITY):"Total Building Size"::VARCHAR,
    PARSE_JSON(SERVICES):"Full Cabinets"::VARCHAR,
    PARSE_JSON(SERVICES):"Partial Cabinets"::VARCHAR,
    PARSE_JSON(SERVICES):"Shared Rackspace"::VARCHAR,
    PARSE_JSON(SERVICES):"Cages"::VARCHAR,
    PARSE_JSON(SERVICES):"Suites"::VARCHAR,
    PARSE_JSON(SERVICES):"Build-to-Suit"::VARCHAR,
    PARSE_JSON(SERVICES):"Footprints"::VARCHAR,
    PARSE_JSON(SERVICES):"Remote Hands"::VARCHAR,
    PARSE_JSON(POWER):"Max power/area"::VARCHAR,
    PARSE_JSON(POWER):"UPS Redundancy"::VARCHAR,
    PARSE_JSON(POWER):"Cooling Redundancy"::VARCHAR,
    PARSE_JSON(POWER):"Standby Power Redundancy"::VARCHAR,
    PARSE_JSON(COMPLIANCE):"Tier Design"::VARCHAR,
    PARSE_JSON(COMPLIANCE):"DSS PCI Certified"::VARCHAR,
    PARSE_JSON(COMPLIANCE):"ISO27001 Certified"::VARCHAR,
    PARSE_JSON(COMPLIANCE):"HIPAA"::VARCHAR,
    PARSE_JSON(COMPLIANCE):"SOC 2 Type II Certified"::VARCHAR,
    PARSE_JSON(COMPLIANCE):"SOC 3 Type 2 Certified"::VARCHAR,
    PARSE_JSON(COMPLIANCE):"NIST 800-53"::VARCHAR,
    PARSE_JSON(SECURITY):"CCTV surveillance"::VARCHAR,
    PARSE_JSON(SECURITY):"Biometric Access Control"::VARCHAR,
    PARSE_JSON(SECURITY):"Card Access Control"::VARCHAR,
    PARSE_JSON(SECURITY):"Onsite Security Staff"::VARCHAR,
    PARSE_JSON(SECURITY):"Onsite Technical Staff"::VARCHAR,
    PARSE_JSON(BUILDING):"Year Operational"::VARCHAR,
    PARSE_JSON(BUILDING):"Roof Access"::VARCHAR,
    PARSE_JSON(BUILDING):"Building Floors"::VARCHAR,
    PARSE_JSON(BUILDING):"Max Floor Load"::VARCHAR,
    PARSE_JSON(AMENITIES):"Meet-Me-Room (MMR)"::VARCHAR,
    PARSE_JSON(STATISTICS):"Internet Exchange Points"::VARCHAR,
    PARSE_JSON(STATISTICS):"Peering networks"::VARCHAR,
    PARSE_JSON(STATISTICS):"Network providers"::VARCHAR,
    PARSE_JSON(STATISTICS):"Tenants offering colocation"::VARCHAR,
    PARSE_JSON(STATISTICS):"Child-Data Center listings"::VARCHAR
FROM CAPSTONE.STATE_DATA_CENTER.CALIFORNIA;


