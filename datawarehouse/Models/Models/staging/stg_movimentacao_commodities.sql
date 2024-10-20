-- models/staging/stg_movimentacao_commodities.sql

with source as (
    select
        date,
        symbol,
        action,
        quantity
    from 
        {{ source('dbsales', 'movimentacao_commodities') }}
),

renamed as (
    select
        cast(date as date) as data,
        symbol as símbolo,
        action as acao,
        quantity as quantidade
    from source
)

select
    data,
    símbolo,
    acao,
    quantidade
from renamed