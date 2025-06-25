# edc_crowd_risk_model
Predictive crowd density and turbulence risk modeling for EDC Las Vegas
# EDC Crowd Risk Modeling – Las Vegas 2025

### Author: Wyatt Brereton  
**Repository:** `edc_crowd_risk_model`

---

## Project Summary

This project simulates crowd movement, density, and turbulence risk during EDC Las Vegas 2025 using Python and real-world festival layouts. The goal is to predict high-risk zones and visualize crowd surges across a realistic time series of festival activity.

---

## Key Features

- Zone based crowd simulation across major stages (Kinetic Field, Circuit Grounds, Cosmic Meadow, Basspod)
- Oval masking to mimic the shape of the Las Vegas Motor Speedway
- Turbulence risk calculation based on scientifically validated density thresholds
- Crowd surge modeling (e.g., post-set flood from Circuit Grounds to Kinetic Field)
- Time-lapse heatmap simulation from T1–T6 (7 PM to 5 AM)
- Visual overlays on the official EDC 2023 festival map
- Exported PNGs for each time block and risk profile

---

## Files Included

| File | Description |
|------|-------------|
| `EDC_Crowd_TimeSeries.py` | Full Python simulation script |
| `/output/` folder | 12 exported PNG heatmaps (6 density, 6 risk) |
| `README.md` | This file |
| *(optional)* `crowd_data.csv` | Export-ready for Power BI |
| *(optional)* `EDC_Risk_Animation.gif` | Visual time-lapse |

---

## Power BI Dashboard

The Power BI file `EDC_Crowd_Risk_Model.pbix` includes:

- Interactive time-slicer from T1 to T6
- Card visual for max density zone
- Matrix summary of all zones with average risk scores
- Tooltips for zone-level deep dives
- Export-ready for operational briefings or stakeholder walkthroughs

You can open the `.pbix` file in Power BI Desktop. Use the slicer to explore how risk shifts across the night.

[Download EDC_Crowd_Risk_Model.pbix](https://github.com/Wbrereton/edc_crowd_risk_model/blob/main/EDC_Crowd_Risk_Model.pbix)

---

## Technical Stack

- NumPy for spatial modeling
- Matplotlib for heatmaps and vector plots
- Pillow (PIL) for image overlay
- Git/GitHub for version control

---

## Time Series Blocks

| Block | Time     | Description |
|-------|----------|-------------|
| T1    | 7:00 PM  | Entry surge begins |
| T2    | 9:00 PM  | Main stages fill |
| T3    | 11:00 PM | Peak congestion |
| T4    | 1:00 AM  | Surge from Circuit to Kinetic |
| T5    | 3:00 AM  | Fatigue and dispersal |
| T6    | 5:00 AM  | Final exits |

---

## Why This Project Matters

This simulation models real crowd behavior and offers predictive analytics for:
- Festival operations
- Emergency response planning
- Stage layout optimization
- Data consulting case studies

---

## Future Add-ons

- Power BI integration with time-slider visual
- Streamlit app or interactive dashboard
- AI-based crowd forecasting

---

## Repository

`https://github.com/Wbrereton/edc_crowd_risk_model`

---

## Author Bio

Wyatt Brereton is an aspiring data consultant focused on real-world simulation, predictive analytics, and operational optimization. This project blends my passion for data with event safety and crowd modeling.
