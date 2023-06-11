DROP TABLE IF EXISTS BD_1.GL_strong;

CREATE TABLE BD_1.GL_strong (
        `client_login` INT
        , `ticket_number` INT
        , `instrument` VARCHAR(15)
        , `volume` INT
        , `comment` TEXT
    );

CREATE INDEX idx_cl_client_login ON BD_1.GL_strong(ticket_number);

SET
    @start_date = (SELECT
							DATE_ADD(rs.start_date, INTERVAL -rs.time_zone_difference HOUR)
						FROM
							(SELECT
						   	rs.id AS id
							FROM
						   	BD_2.settings_of_report AS rs
							) AS last_report
							LEFT JOIN BD_2.settings_of_report AS rs ON last_report.id = rs.id
						ORDER BY 
							rs.id DESC
						LIMIT
							1,1),
	@end_date = (SELECT
                  DATE_ADD(rs.end_date, INTERVAL -rs.time_zone_difference HOUR)
                FROM
                  (
                    SELECT
                      rs.id AS id
                    FROM
                      BD_2.settings_of_report AS rs
                  ) AS last_report
                  LEFT JOIN BD_2.settings_of_report AS rs ON last_report.id = rs.id
                  ORDER BY 
                  	rs.id DESC
						LIMIT
							1,1);

INSERT INTO BD_1.GL_strong

SELECT
	tr.client_login
	, tr.ticket_number
	, tr.instrument
	, tr.volume
	, tr.`comment`
FROM
	BD_2.MT4_TRADES AS tr
WHERE
	tr.cmd IN (0, 1)
	AND tr.client_login > 1500
	AND tr.CLOSE_TIME >= @start_date
	AND tr.CLOSE_TIME <= @end_date
	AND tr.`comment` REGEXP 'from|to '

UNION DISTINCT

SELECT
	tr.client_login
	, tr.ticket_number
	, tr.instrument
	, tr.volume
	, tr.`comment`
FROM
	BD_2.MT4_TRADES AS tr
WHERE
	tr.cmd IN (0, 1)
	AND tr.client_login > 112500
	AND tr.OPEN_TIME >= @start_date
	AND tr.OPEN_TIME <= @end_date
	AND tr.`comment` REGEXP 'from|to ';