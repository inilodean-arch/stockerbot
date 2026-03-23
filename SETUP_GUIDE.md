# Setup Guide for Stockerbot

## Prerequisites
Before getting started, make sure you have the following installed:
- **Python 3.7 or higher**: You can download Python from [python.org](https://www.python.org/downloads/).
- **pip**: This should come installed with Python, but you can verify by running `pip --version` in your terminal.

## Step 1: Clone the Repository
Open your terminal and run:
```bash
git clone https://github.com/inilodean-arch/stockerbot.git
cd stockerbot
```

## Step 2: Install Required Packages
Inside the `stockerbot` directory, run the following command to install the necessary Python packages:
```bash
pip install -r requirements.txt
```

## Step 3: Set Up API Keys
1. Sign up for the necessary services to obtain your API keys (e.g., stock market APIs).
2. Create a `.env` file in the root of the project directory.
3. Add your keys in the following format:
   ```bash
   API_KEY1=your_api_key_here
   API_KEY2=your_api_key_here
   ```

## Step 4: Run the Application Locally
With everything set up, you can run the application using:
```bash
python main.py
``` 

Make sure to consult the application's documentation for any specific options or configurations.

## Troubleshooting
If you encounter any issues, ensure that all dependencies are correctly installed, and the API keys are set up correctly in the `.env` file.
