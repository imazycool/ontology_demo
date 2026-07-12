
# ==================================================
# ENTITY_METADATA
# ==================================================
GET_ENTITY_NAMES = """
    SELECT DISTINCT entity_name FROM entity_metadata
    WHERE entity_name IS NOT NULL ORDER BY entity_name;
    """


GET_ENTITY = """
    SELECT
        entity_name,
        description,
        business_domain,
        entity_category,
        physical_table,
        entity_type,
        business_owner
    FROM entity_metadata
    WHERE entity_name = %s
    AND is_active = 1;
    """
    
    


# ==================================================
# ATTRIBUTE_METADATA
# ==================================================






# ==================================================
# METRIC_METADATA
# ==================================================
GET_ENTITY_METRICS = """
    SELECT
        display_name
    FROM metric_metadata
    WHERE entity_name = %s
    AND is_active = TRUE
    ORDER BY display_order;
    """




# ==================================================
# ATTRIBUTE_METADATA
# ==================================================
GET_METRIC_DEFINITION = """
    SELECT
        metric_name,
        formula,
        source_table
    FROM metric_definitions
    WHERE metric_name = %s;
    """


GET_ATTRIBUTE = """
    SELECT
        attribute_name,
        physical_attribute,
        data_type,
        is_dimension,
        is_measure,
        is_filterable
    FROM attribute_metadata
    WHERE entity_name = %s
    AND attribute_name = %s;
    """


GET_ENTITY_DIMENSIONS = """
    SELECT
        attribute_name
    FROM attribute_metadata
    WHERE entity_name = %s
    AND is_dimension = 1
    ORDER BY attribute_name;
    """


# ==================================================
# METRIC_DEFINITION 
# ==================================================

GET_METRIC_DEFINITION = """
    SELECT
        metric_name,
        formula,
        source_table
    FROM metric_definitions
    WHERE metric_name = %s;
    """


# ==================================================
# _METADATA
# ==================================================