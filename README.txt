
World Art Exhibitions (1905-1915) Interactive Visualization

General Information
- Project Title: World Art Exhibitions (1905-1915) Interactive Visualization
- Authors: Piotr Lenczewski, Pablo Pardo, Jorge Bailez
- Date: January 16, 2025

Libraries and Tools Used
1. Frontend:
   - Vega v5.30.0 (License: BSD-3-Clause)
   - Vega-Lite v5.20.1 (License: BSD-3-Clause)
   - Vega-Embed v6.26.0 (License: BSD-3-Clause)

2. Data Files:
   - interactive_world_map.json:
     - Interactive Map: Uses geographical data from `world-110m.json` (Vega Datasets).
     - Exhibition Data: Loaded from the local CSV file `exhibitions_with_countries.csv`.

Development Environment
- Text Editor or IDE: Vega Editor
- Web Browser: Compatible with any modern browser (Chrome, Firefox, Edge).

Executable Files
- The main application file is index.html, which should be opened in a web browser to view the interactive map.

How to Run the Program
1. Ensure all the necessary files are in the same folder:
   - index.html
   - interactive_world_map.json
   - exhibitions_with_countries.csv
2. Open the index.html file in a compatible browser.

Command Line Parameters
This project does not use command-line parameters, as it is designed to run in a web environment.

Configuration and Dependencies
- Configuration Files:
  - interactive_world_map.json: Contains specifications for Vega.
  - exhibitions_with_countries.csv: Input data for art exhibitions (must be in the same directory as `index.html`).
- Additional Notes:
  - World map (world-110m.json) is fetched directly from the Vega datasets found here: https://vega.github.io/vega-datasets.
