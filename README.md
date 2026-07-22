# SW2627_Python_University
 
## Setup
 
1. Clone the repository
   git clone https://github.com/team/customer-analytics.git
   cd customer-analytics
 
2. Create and activate a virtual environment
   python3 -m venv venv
   source venv/bin/activate    # Windows: venv\Scripts\activate
 
3. Install dependencies
   pip install -r requirements.txt
 
4. Configure environment variables
   Copy .env.example to .env and fill in your database credentials
 
## Project Structure
 
data/raw/       Source data - never modified
data/processed/ Cleaned data ready for analysis
notebooks/      Jupyter exploration and reporting notebooks
scripts/        Repeatable Python scripts
output/         Generated reports and figures
 
## Running the Analysis
 
python scripts/clean_data.py          # Produces data/processed/
python scripts/run_segmentation.py    # Produces output/
jupyter notebook notebooks/           # Open interactive notebooks