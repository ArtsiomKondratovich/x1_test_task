SELECT 
	client_number,
  SUM(CASE WHEN outcome = 'win' then 1 else 0 end) AS count_win,
  SUM(CASE WHEN outcome = 'lose' then 1 else 0 end) AS count_lose
FROM bid 
INNER JOIN event_value as win ON bid.play_id = win.play_id
WHERE bid.coefficient = win.value
GROUP BY client_number
