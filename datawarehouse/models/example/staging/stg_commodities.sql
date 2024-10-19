-- Importa dados da fonte
with source as (
    select
        "Date",
        "Close",
        symbol
    from 
        {{ source('dbsales', 'commodities') }}
),
-- Renomeia colunas
renamed as (
    select
        cast("Date" as date) as data,
        "Close" as valor_fechamento,
        symbol as símbolo 
    from 
        source 
)

select * from renamed
