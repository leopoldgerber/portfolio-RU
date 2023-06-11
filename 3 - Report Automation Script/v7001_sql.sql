SELECT 
    t_all.full_instrument
    , abs(SUM(t_all.amount)) AS sum_amount
    , ROUND((SUM(volume_minus) + SUM(volume_plus))/100, 2) AS volume
    , t_all.currency
    , t_all.group_of_the_login_of_the_instrument
    , t_all.size_of_the_contract
  FROM
  (SELECT
    t1.full_instrument
     , t1.instrument
     , t1.group_of_the_login_of_the_instrument
     , sum(t1.volume_sum) AS volume_sum
     , sum(t1.volume_minus) AS volume_minus
     , sum(t1.volume_plus) AS volume_plus
     , t1.sell_position
     , t1.buy_position
     , t1.size_of_the_contract
     , sum(t1.volume_minus_sell_position) AS volume_minus_sell_position
     , sum(t1.volume_plus_buy_position) AS volume_plus_buy_position
     , sum(t1.amount) AS amount
     , t1.currency
  FROM  
    (SELECT
        SUBSTRING_INDEX(SUBSTRING_INDEX(t_1.instrument,'.',1), '_', 1) AS full_instrument
        , t_1.instrument
        , ss.group_of_the_login_of_the_instrument
        , t_1.VOLUME AS volume_sum 
        , if(t_1.option_1 = 1, -t_1.volume, 0) AS volume_minus
        , if(t_1.option_1 = 0, t_1.volume, 0) AS volume_plus
        , t0.sell_position
        , t0.buy_position
        , cs.size_of_the_contract
        , (if(t_1.option_1 = 1, -t_1.volume, 0) * cs.size_of_the_contract * if(ss.group_of_the_login_of_the_instrument = 1 , 1, t_1.price_on_buy)) / if(ss.group_of_the_login_of_the_instrument = 4,20,if(ss.group_of_the_login_of_the_instrument IS NULL, 20, 100)) AS volume_minus_sell_position
        , (if(t_1.option_1 = 0, t_1.volume, 0) * cs.size_of_the_contract * if(ss.group_of_the_login_of_the_instrument = 1, 1, t_1.price_on_buy)) / if(ss.group_of_the_login_of_the_instrument = 4,20,if(ss.group_of_the_login_of_the_instrument IS NULL, 20, 100)) AS volume_plus_buy_position
        , ((if(t_1.option_1 = 1, -t_1.volume, 0) * cs.size_of_the_contract * if(ss.group_of_the_login_of_the_instrument = 1, 1, t_1.price_on_buy)) / if(ss.group_of_the_login_of_the_instrument = 4,20,if(ss.group_of_the_login_of_the_instrument IS NULL, 20, 100))
          + (if(t_1.option_1 = 0, t_1.volume, 0) * cs.size_of_the_contract * if(ss.group_of_the_login_of_the_instrument = 1, 1, t_1.price_on_buy)) / if(ss.group_of_the_login_of_the_instrument = 4,20,if(ss.group_of_the_login_of_the_instrument IS NULL, 20, 100))) / 100 AS amount
        , cs.currency
      FROM
        BASE_1.MT4_USERS_VIEW AS us
        LEFT JOIN BASE_1.TABLE_2 AS t_1 ON us.login = t_1.login
        LEFT JOIN CONFIG.sprecification_instruments AS ss ON ss.instrument = t_1.instrument
        LEFT JOIN (
            SELECT
              cnt.instrument
              , cnt.date_time AS last_date_cnt
              , cnt.buy_position
              , cnt.sell_position
            FROM
              BASE_1.collected_new_tasks AS cnt
              INNER JOIN (
              SELECT 
                cnt.instrument
                , max(cnt.date_time) AS max_date
              FROM 
                BASE_1.collected_new_tasks AS cnt
              WHERE 1=1 AND 
                cnt.buy_position != 0
                AND cnt.sell_position != 0
              group_of_the_login BY
                cnt.instrument
              ) AS t0 ON cnt.instrument = t0.instrument AND t0.max_date = cnt.date_time
              ) AS t0 ON t0.instrument = t_1.instrument
        LEFT JOIN(
            SELECT
              cs.instrument
              , cs.slice_date
              , cs.size_of_the_contract
              , cs.currency
            FROM 
              CONFIG.configuration_instrument AS cs
              INNER JOIN (
              SELECT 
                cs.instrument
                , max(cs.slice_date) AS max_date
              FROM 
                CONFIG.configuration_instrument AS cs
              group_of_the_login BY
                cs.instrument) AS t0 ON cs.instrument = t0.instrument AND cs.slice_date = t0.max_date
            group_of_the_login BY 
              cs.instrument 
            ) AS cs ON cs.instrument = t_1.instrument
      WHERE 1=1 AND
      
        t_1.option_1 IN (0,1)
        AND (t_1.CLOSE_TIME BETWEEN (SELECT
                          DATE_ADD(rs.end_date, INTERVAL -rs.time_zone_difference HOUR)
                        FROM
                          (
                            SELECT
                              rs.id AS id
                            FROM
                              BASE_1.settings AS rs
                          ) AS last_report
                          LEFT JOIN BASE_1.settings AS rs ON last_report.id = rs.id
                          ORDER BY 
                            rs.id DESC
                  LIMIT
                    1,1) AND NOW())
          AND t_1.OPEN_TIME <= (SELECT
                          DATE_ADD(rs.end_date, INTERVAL -rs.time_zone_difference HOUR)
                        FROM
                          (
                            SELECT
                              rs.id AS id
                            FROM
                              BASE_1.settings AS rs
                          ) AS last_report
                          LEFT JOIN BASE_1.settings AS rs ON last_report.id = rs.id
                          ORDER BY 
                            rs.id DESC
                  LIMIT
                    1,1)
        
      group_of_the_login BY
        t_1.ticket
     ) AS t1
  group_of_the_login BY
    t1.instrument 

  UNION ALL

 SELECT
....;