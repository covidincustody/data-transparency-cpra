# Background
This program scores the transparency of sheriff's departments in California based on the COVID-19 data provided in response to our California Public Records Act (CPRA) requests. Please note that this does NOT score sheriff's departments' transparency pertaining to the COVID-19 data collection effort lead by the Board of State and Community Corrections (BSCC). For this scoring and corresponding visualizations, please see the covidincustody/data-transparency-bscc repository. 

The first component scores transparency based on the COVID-19 data reported by all of the sheriff's departments in California that has been cleaned, processed and aggregated. Access here: https://docs.google.com/spreadsheets/d/1q9zoEN_nI_oBAxO8k_9kd5612gCaMHSfViU-1WKVSKY/edit#gid=0. Details on the CPRA requests for information on COVID-19 cases, vaccinations, deaths and compliance with public health orders can be found here: https://drive.google.com/drive/folders/1VQr_BHHzCEwUH93qSXlsF3V2k1r6wAxi. 

The second component generates visualizations of the transparency scores by data category - COVID-19 cases, vaccinations, etc. 

# Instructions
Download repository and modify the ```run.py``` file to reflect the appropriate read and write paths. 

The read path will be the local version the county jail dataset referenced above: https://docs.google.com/spreadsheets/d/1q9zoEN_nI_oBAxO8k_9kd5612gCaMHSfViU-1WKVSKY/edit#gid=0 (ensure that the local file contains no banners and that the first row contains the column headers). The write path will be a local path specified by the user where the transparency scores will be written in Excel format.

For simplest execution, use the Anaconda Environment (https://www.anaconda.com/products/distribution) which has the necessary modules or packages pre-installed. Navigate to either data-transparency-cpra/transparency-scores or data-transparency-cpra/visualizations and execute program as ``python run.py`` in the Anaconda terminal. Alternatively, a user can execute the modified ```run.py``` file in any Python IDE (Spyder, PyCharm, etc.) launched through the Anaconda Environment.

Please contact info@covidincustody.org with any questions or concerns.
