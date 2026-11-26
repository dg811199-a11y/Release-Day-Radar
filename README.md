# Release Day Radar 🎬

### Did online buzz predict opening weekends for 8 Indian films?

**Team:** Cursors  
**Team Members:**
- Dhanush Gowda C – 1RV23CV018
- Naresh S S – 1RV22CV066

## 1. Project Overview

Release Day Radar is a data analysis project that investigates whether online audience engagement and sentiment around film trailers can predict opening-weekend box-office collections.

The project focuses on 8 Indian films released in 2025, covering Hindi and regional-language cinema.

The main objective is to help a film distributor make better decisions about adding screens, reducing screens or spending more on promotion within 72 hours of a film's release.

## 2. Research Question

Does YouTube trailer engagement and audience sentiment predict opening-weekend India net collections for recent Hindi and regional films?

## 3. Films Covered

1. Chhaava – Hindi
2. Saiyaara – Hindi
3. Housefull 5 – Hindi
4. Dhurandhar – Hindi
5. Kantara Chapter 1 – Kannada
6. Coolie – Tamil
7. They Call Him OG – Telugu
8. Lokah Chapter 1: Chandra – Malayalam

## 4. Data Sources

| Data Source | Data Collected | Format |
|---|---|---|
| YouTube Data API v3 | Trailer views, likes and comment counts | JSON |
| YouTube trailer comments | 800 comments, 100 per film | Text |
| Bollywood Hungama and Sacnilk | Day-1 and opening-weekend box-office figures | HTML tables |
| IMDb 50K labelled reviews | Supplementary text-analysis dataset | JSON Lines |

## 5. Tools and Technologies

- Python
- Google Colab
- Pandas
- VADER Sentiment Analysis
- MySQL
- SQL
- Apache PySpark
- Microsoft Excel
- Matplotlib

## 6. Project Methodology

1. **Data Collection:** Collected YouTube trailer statistics and comments using the YouTube Data API and gathered box-office figures from public tracking websites.
2. **Data Cleaning:** Used Python and pandas for data cleaning, type conversion, text preprocessing and engagement-rate calculation.
3. **Sentiment Analysis:** Applied VADER to classify YouTube comments into positive, neutral and negative sentiment.
4. **Database Development:** Loaded the processed data into a MySQL database named `release_day_radar`.
5. **SQL Analysis:** Created relational tables and executed SQL queries using JOIN, GROUP BY and aggregations.
6. **Big Data Processing:** Used PySpark to process the supplementary IMDb dataset containing 50,000 labelled reviews.
7. **Visualisation:** Created charts to study the relationship between online engagement, sentiment and box-office performance.

## 7. Database Structure

The MySQL database contains five tables:

- `movies`
- `youtube_stats`
- `youtube_comments`
- `comment_sentiment`
- `box_office`

The database uses movie IDs and relational keys to connect the datasets.

## 8. Key Findings

- YouTube engagement and comment sentiment did not show statistically significant relationships with opening-weekend collections in this sample.
- Day-1 collection showed a strong relationship with opening-weekend collection (Pearson correlation r = 0.84).
- High engagement does not necessarily indicate positive audience approval.
- The findings suggest that Friday-night Day-1 collection is a more useful decision signal than trailer views alone.

## 9. Project Recommendation

Film distributors should use Day-1 box-office performance as the primary signal for screen-allocation decisions. YouTube engagement can be used as a secondary indicator, while sentiment should be considered to understand audience response.

Future analysis should collect daily trailer statistics from the trailer-launch date and include more films.

## 10. Repository Contents

This repository contains the project report, presentation, Jupyter notebook, Python scripts, SQL scripts, datasets, Excel documentation and visualisations.

## 11. Team Contribution

| Member | USN | Contribution |
|---|---|---:|
| Dhanush Gowda C | 1RV23CV018 | 50% |
| Naresh S S | 1RV22CV066 | 50% |

## 12. Limitations

- The analysis covers only eight films.
- YouTube statistics are cumulative snapshots collected on 26 November 2026.
- Comments were relevance-sorted rather than randomly sampled.
- VADER may misclassify regional-language and mixed-language comments.
- Box-office figures are estimates from public tracking sources.
- Correlation does not establish causation.

## 13. Conclusion

Release Day Radar demonstrates how data from multiple sources and formats can be combined to support film-distribution decisions. The analysis found no reliable predictive relationship between online trailer buzz and opening-weekend collections in the selected sample, highlighting the importance of data quality, timing and careful interpretation.

---

**Project:** Data and Storytelling – Case Study A  
**Team:** Cursors
