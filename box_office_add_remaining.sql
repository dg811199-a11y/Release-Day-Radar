USE release_day_radar;

-- Adds the last 3 films. Run ONCE (box_office should currently have 5 rows).
SELECT COUNT(*) AS rows_before FROM box_office;

INSERT INTO box_office (movie_id, day1_net_cr, opening_weekend_net_cr, source, status, note)
SELECT movie_id, 61.85, 162.85, 'Sacnilk (all languages)', 'provisional', 'Thu-Sat 61.85+46.00+55.00; BH 75 cr is Hindi-dubbed only'
FROM movies WHERE movie_name = 'Kantara Chapter 1';

INSERT INTO box_office (movie_id, day1_net_cr, opening_weekend_net_cr, source, status, note)
SELECT movie_id, 63.75, 100.70, 'Sacnilk (day-wise)', 'final', 'Thu-Sat 63.75+18.45+18.50; excludes 21 cr Wed premiere'
FROM movies WHERE movie_name = 'They Call Him OG';

INSERT INTO box_office (movie_id, day1_net_cr, opening_weekend_net_cr, source, status, note)
SELECT movie_id, 2.70, 14.30, 'Sacnilk (all languages)', 'final', 'Thu-Sat 2.70+4.00+7.60'
FROM movies WHERE movie_name = 'Lokah Chapter 1: Chandra';

SELECT COUNT(*) AS rows_after FROM box_office;

-- Query 6: engagement, sentiment and box office together (JOIN + GROUP BY)
SELECT m.movie_name, m.language, y.views, y.engagement_rate,
       ROUND(100 * SUM(s.sentiment_label = 'Positive') / COUNT(*), 1) AS positive_pct,
       b.opening_weekend_net_cr
FROM movies m
JOIN youtube_stats y ON m.movie_id = y.movie_id
JOIN youtube_comments c ON m.movie_id = c.movie_id
JOIN comment_sentiment s ON c.comment_id = s.comment_id
JOIN box_office b ON m.movie_id = b.movie_id
GROUP BY m.movie_name, m.language, y.views, y.engagement_rate, b.opening_weekend_net_cr
ORDER BY b.opening_weekend_net_cr DESC;
