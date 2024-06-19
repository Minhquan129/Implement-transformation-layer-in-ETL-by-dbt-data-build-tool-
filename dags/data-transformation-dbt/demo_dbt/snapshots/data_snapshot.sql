{% snapshot speed_model_snapshot %}

{{
    config( 
      target_schema='public',
      unique_key='index',
      strategy='timestamp',
      updated_at='updated_at',
    )
}}

select * from {{ ref('speed_model') }}

{% endsnapshot %}
