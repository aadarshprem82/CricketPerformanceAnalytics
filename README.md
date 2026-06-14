# Cricket Performance Analytics
A data engineering project built with PySpark to analyze T20 cricket match and ball-by-ball datasets.

# Architecture

CSV Files -> PySpark DataFrames -> CSV outputs
                |- Batting Analytics
                |- Bowling Analytics
                |- Team Analytics
                |- Venue Analytics
                |- MVP Rankings

# How to run
Install dependencies:
```bash
pip install -r requirements.txt
```

Place datasets:
```text
|- matches.csv
|- deliveries.csv
```

Run Application:
```bash
python src/main.py
```

or

```bash
spark-submit src/main.py
```

---
# Generated Outputs

```text
output/
    |- top_batsmen/
    |- orange_cap/
    |- top_bowlers/
    |- purple_cap/
    |- team_win_percentage/
    |- venue_analysis/
        |- average_score/
        |- powerplay_analysis/
    |- mvp_rankings/
```
---

# Author
Aadarsh Prem