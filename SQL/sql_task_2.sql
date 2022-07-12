SELECT 
	(CASE 
    	WHEN home_team > away_team
        THEN CONCAT(away_team, '-', home_team)
        ELSE CONCAT(home_team, '-', away_team)
	END) AS game,
	COUNT(*) AS game_count 
FROM event_entity
GROUP BY game
ORDER BY game_count ASC
