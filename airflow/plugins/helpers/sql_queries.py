class SqlQueries:
    create_table_queries = (""" 

    -- Recreate Staging Tables to ensure freshness 
    DROP TABLE IF EXISTS public.staging_restaurants;
    DROP TABLE IF EXISTS public.staging_payment_providers;
    DROP TABLE IF EXISTS public.staging_parking;
    DROP TABLE IF EXISTS public.staging_cuisine;
    DROP TABLE IF EXISTS public.staging_hours;
    DROP TABLE IF EXISTS public.staging_ratings;
    DROP TABLE IF EXISTS public.staging_user_cuisine;
    DROP TABLE IF EXISTS public.staging_user_payment;
    DROP TABLE IF EXISTS public.staging_user_profile;

    CREATE TABLE IF NOT EXISTS public.staging_restaurants(
        placeID                         INT IDENTITY(1,1) PRIMARY KEY ENCODE ZSTD,
        latitude                        FLOAT DEFAULT 0.0 ENCODE ZSTD,
        longitude                       FLOAT DEFAULT 0.0 ENCODE ZSTD,
        the_geom_meter                  VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        name                            VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        address                         VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        city                            VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        state                           VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        country                         VARCHAR(100) DEFAULT 'Mexico' ENCODE ZSTD,
        alcohol                         VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        smoking_area                    VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        dress_code                      VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        accessibility                   VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        price                           VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        ambience                        VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        area                            VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        other_services                  VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD       
    );

    CREATE TABLE IF NOT EXISTS public.staging_payment_providers(
        placeID                         INT IDENTITY(1,1) PRIMARY KEY ENCODE ZSTD,
        Rpayment                        VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD  

    );

    CREATE TABLE IF NOT EXISTS public.staging_parking(

        placeID                         INT IDENTITY(1,1) PRIMARY KEY ENCODE ZSTD,
        parking_lot                     VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD 

    );

    CREATE TABLE IF NOT EXISTS public.staging_cuisine(

        placeID                         INT IDENTITY(1,1) PRIMARY KEY ENCODE ZSTD,
        Rcuisine                        VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD 

    );

    CREATE TABLE IF NOT EXISTS public.staging_hours(
        placeID                        INT IDENTITY(1,1) PRIMARY KEY ENCODE ZSTD,
        hours                          VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        days                           VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD

    );

    CREATE TABLE IF NOT EXISTS public.staging_reviews(
        id                            INT IDENTITY(1,1) PRIMARY KEY ENCODE ZSTD, -- Surrogate key
        userID                        INT ENCODE ZSTD,
        placeID                       INT ENCODE ZSTD,
        place_review                  INT ENCODE ZSTD,
        food_review                   INT ENCODE ZSTD,
        service_review                INT ENCODE ZSTD,

    )DISTSTYLE ALL
    SORTKEY();

    CREATE TABLE IF NOT EXISTS public.staging_user_cuisine(
        userID                       INT IDENTITY(1,1) PRIMARY KEY ENCODE ZSTD,
        Rcuisine                     VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD
    );

    CREATE TABLE IF NOT EXISTS public.staging_user_payment(
        userID                       INT IDENTITY(1,1) PRIMARY KEY ENCODE ZSTD,
        Upayment                     VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD 
    )DISTSTYLE ALL
    SORTKEY();

    CREATE TABLE IF NOT EXISTS public.staging_user_profile(
        userID                      INT IDENTITY(1,1) PRIMARY KEY ENCODE ZSTD,
        latitude                    FLOAT DEFAULT 0.0 ENCODE ZSTD,
        longitude                   FLOAT DEFAULT 0.0 ENCODE ZSTD,
        smoker                      VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        drink_level                 VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        dress_preference            VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        ambience                    VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        transport                   VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        marital_status              VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        hijos                       VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        birth_year                  INT ENCODE ZSTD,
        interest                    VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        personality                 VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        religion                    VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        activity                    VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        color                       VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        weight                      INT ENCODE ZSTD,
        budget                      VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,
        height                      FLOAT DEFAULT 0.0 ENCODE ZSTD,
    )DISTSTYLE ALL
    SORTKEY();


    ---Create fact table if required 
    CREATE TABLE IF NOT EXISTS public_fact_reviews(
        id                         INT IDENTITY(1,1) PRIMARY KEY ENCODE ZSTD, -- Surrogate key
        --Dimension tables ids 
        restaurant_id               INT ENCODE ZSTD,
        user_id                     INT ENCODE ZSTD,

        -- dimensions
        );

    CREATE TABLE IF NOT EXISTS public.user(
        userID                      INT IDENTITY(1,1) PRIMARY KEY ENCODE ZSTD,
        userRcuisine                VARCHAR(100) DEFAULT 'Unknown' ENCODE ZSTD,

    );











    
    
    
    
    
    
    """)