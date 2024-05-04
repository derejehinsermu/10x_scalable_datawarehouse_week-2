
-- models/my_transformations.sql
{{ config(materialized='table') }}

SELECT
    track_id,
    vehicle_type,
    AVG(speed) AS average_speed,
    MAX(speed) AS max_speed,
    MIN(speed) AS min_speed
FROM
    {{ ref('my_transformion') }}
GROUP BY
    track_id, vehicle_type


