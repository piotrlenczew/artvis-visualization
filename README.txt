
World Art Exhibitions (1902-1916) Interactive Visualization

General Information
- Project Title: World Art Exhibitions (1902-1916) 
   Github link: https://github.com/piotrlenczew/artvis-visualization
   Interactive Visualization: https://piotrlenczew.github.io/artvis-visualization/
- Authors: Piotr Lenczewski, Pablo Pardo, Jorge Bailez
- Date: January 16, 2025

Libraries and Tools Used
1. Frontend:
   - Vega v5.30.0 (License: BSD-3-Clause)
   - Vega-Lite v5.20.1 (License: BSD-3-Clause)
   - Vega-Embed v6.26.0 (License: BSD-3-Clause)

2. Data Files:
   - visualization.json:
     - Interactive Map: Uses geographical data from `world-110m.json` (Vega Datasets).
     - Exhibition Data: Loaded from the local CSV file `exhibitions_with_countries.csv` (derived from dataset https://exhibitions.univie.ac.at/).
     - Country id to name map: Additional file containing data to join above datasets.

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
2. Run 'python -m http.server 8000' command to create local server (needed due to CORS blocking local file access).
3. Open 'http://localhost:8000/index.html' in your browser.

Command Line Parameters
This project does not use command-line parameters, as it is designed to run in a web environment.

Configuration and Dependencies
- Configuration Files:
  - visualization.json: Contains specifications for Vega.
  - exhibitions_with_countries.csv: Input data for art exhibitions.
- Additional Notes:
  - World map (world-110m.json) is fetched directly from the Vega datasets found here: https://vega.github.io/vega-datasets.
