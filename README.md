# Distribution-Model-GUI
Organic Contaminants Distribution Model
This repository contains a program designed to predict the distribution of organic contaminants in different environmental compartments (air, water, soil, etc.). The model utilizes basic properties of the contaminants to estimate their distribution, helping users make informed decisions about remediation and detection.

Table of Contents
Introduction
Background
Solution Method
Program Design and Implementation
Conclusion
References
Introduction
With the increasing presence of organic products in the environment, understanding their distribution is crucial for effective detection and remediation. This model predicts the distribution of organic contaminants in water, air, and soil based on their properties, aiding in better environmental management strategies.

Background
Organic contaminants possess varying physical and chemical properties that influence their environmental fate. By utilizing properties like vapor pressure, solubility, and molar weight, along with distribution factors (e.g., air/water partitioning factor), this model predicts their behavior.

Common pollutants like benzene, chlorobenzene, DDT, DEHP, PCB, and aniline, with differing molecular weights and properties, exhibit varied behaviors in the environment.

Solution Method
The model uses dictionaries to store contaminant data (e.g., name, vapor pressure, solubility, molecular weight, distribution factors) and user-provided environmental data (e.g., volumes of air, water, soil, sediment, organisms). The program calculates the distribution results using these inputs and visualizes them through pie charts.

Program Design and Implementation
Input Values: Users provide environmental data via a GUI entry and select default chemicals from pull-down menus.
Display Information: The selected chemical's properties are displayed in a text area.
Calculation: The program calculates the chemical's distribution in different environmental compartments.
Visualization: Results are presented as pie charts in a pop-up window.
Conclusion
Summary
This program offers a simple environmental model to help users understand the distribution of organic contaminants. Users input volume data, select chemicals, and view distribution results via pie charts in a user-friendly GUI.

Lessons Learned
Utilized dictionaries for efficient data storage.
Enhanced GUI with text display functions and pie chart visualizations.
Added default values to prevent potential bugs.
Future Work
To expand this project, automatic value retrieval from online databases could be implemented, allowing users to input compound names and receive distribution results for a wider range of organic compounds.

References
Gschwend, Philip M., Dieter M. Imboden, and Ren P. Schwarzenbach. Environmental Organic Chemistry. New York: John Wiley & Sons, Incorporated, 2016.
Feel free to contribute to this project by submitting issues or pull requests.

How to Run
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/organic-contaminants-distribution-model.git
Navigate to the project directory:
bash
Copy code
cd organic-contaminants-distribution-model
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the program:
bash
Copy code
python main.py
