USE release_day_radar;

SELECT m.movie_name,
       m.language,
       y.views
FROM youtube_stats y
JOIN movies m ON y.movie_id = m.movie_id
ORDER BY y.views DESC;
SELECT m.movie_name,
       m.language,
       y.views,
       y.likes,
       y.comments,
       y.engagement_rate
FROM youtube_stats y
JOIN movies m ON y.movie_id = m.movie_id
ORDER BY y.engagement_rate DESC;
SELECT m.movie_name,
       SUM(CASE WHEN c.release_period = 'Pre-release' THEN 1 ELSE 0 END) AS pre_release_comments,
       SUM(CASE WHEN c.release_period = 'Post-release' THEN 1 ELSE 0 END) AS post_release_comments,
       COUNT(*) AS total_comments
FROM youtube_comments c
JOIN movies m ON c.movie_id = m.movie_id
GROUP BY m.movie_name
ORDER BY m.movie_name;
USE release_day_radar;

SELECT m.movie_name,
       SUM(s.sentiment_label = 'Positive') AS positive_comments,
       SUM(s.sentiment_label = 'Neutral')  AS neutral_comments,
       SUM(s.sentiment_label = 'Negative') AS negative_comments,
       ROUND(100 * SUM(s.sentiment_label = 'Positive') / COUNT(*), 1) AS positive_pct,
       ROUND(100 * SUM(s.sentiment_label = 'Negative') / COUNT(*), 1) AS negative_pct
FROM comment_sentiment s
JOIN youtube_comments c ON s.comment_id = c.comment_id
JOIN movies m ON c.movie_id = m.movie_id
GROUP BY m.movie_name
ORDER BY positive_pct DESC;
WITH stats AS (
    SELECT m.language,
           COUNT(*) AS movies,
           ROUND(AVG(y.views), 0) AS avg_views,
           ROUND(AVG(y.engagement_rate), 4) AS avg_engagement_rate
    FROM movies m
    JOIN youtube_stats y ON m.movie_id = y.movie_id
    GROUP BY m.language
),
sent AS (
    SELECT m.language,
           ROUND(100 * SUM(s.sentiment_label = 'Positive') / COUNT(*), 1) AS positive_pct,
           ROUND(100 * SUM(s.sentiment_label = 'Negative') / COUNT(*), 1) AS negative_pct
    FROM movies m
    JOIN youtube_comments c ON m.movie_id = c.movie_id
    JOIN comment_sentiment s ON c.comment_id = s.comment_id
    GROUP BY m.language
)
SELECT st.language, st.movies, st.avg_views, st.avg_engagement_rate,
       se.positive_pct, se.negative_pct
FROM stats st
JOIN sent se ON st.language = se.language
ORDER BY st.avg_engagement_rate DESC;
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