import requests
import subprocess
import logging
import tempfile
import os

# List of raw GitHub URLs to your scripts
GITHUB_SCRIPTS = [
    #"https://raw.githubusercontent.com/MariaKlap/RI/main/EMAnews2.py",
    #"https://raw.githubusercontent.com/MariaKlap/RI/main/ECnews11.py",
    #"https://raw.githubusercontent.com/MariaKlap/RI/main/ICR.py",
    #"https://raw.githubusercontent.com/MariaKlap/RI/main/ICHnews.py",
    #"https://raw.githubusercontent.com/MariaKlap/RI/main/IS1.py",
    #"https://raw.githubusercontent.com/MariaKlap/RI/main/SWISS5.py",
    #"https://raw.githubusercontent.com/MariaKlap/RI/main/AT.py",
    #"https://raw.githubusercontent.com/MariaKlap/RI/main/GMP.py",
    #"https://raw.githubusercontent.com/MariaKlap/RI/main/EC-Updates.py",
    #"https://raw.githubusercontent.com/MariaKlap/RI/main/EC-Medical.py",
    #"https://raw.githubusercontent.com/MariaKlap/RI/main/FDAnews.py",
    #"https://raw.githubusercontent.com/MariaKlap/RI/main/RQAnews4.py",
    #"https://raw.githubusercontent.com/MariaKlap/RI/main/Topra.py",
    #"https://raw.githubusercontent.com/MariaKlap/RI/main/raps-2.py",
    #"https://raw.githubusercontent.com/MariaKlap/RI/main/WHOnews.py",
    "https://raw.githubusercontent.com/MariaKlap/RI/main/CBGnewsfinal5win.py",
    "https://raw.githubusercontent.com/MariaKlap/RI/main/HMA6news.py"
    
    
    # Add more script URLs here
]

# Set up logging
log_file = os.path.join(os.getcwd(), "batch_run_log.txt")
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def download_and_run_script(url):
    try:
        logging.info(f"📥 Downloading script: {url}")
        response = requests.get(url)
        response.raise_for_status()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp_file:
            temp_file.write(response.content)
            temp_file_path = temp_file.name

        logging.info(f"🚀 Running script: {url}")
        subprocess.run(["python", temp_file_path], check=True)
        logging.info(f"✅ Completed: {url}")
        
        os.remove(temp_file_path)
    except requests.RequestException as e:
        logging.error(f"❌ Download failed for {url}: {e}")
    except subprocess.CalledProcessError as e:
        logging.error(f"❌ Execution failed for {url}: {e}")

def main():
    logging.info("=== Batch GitHub Execution Started ===")
    for url in GITHUB_SCRIPTS:
        download_and_run_script(url)
    logging.info("=== Batch GitHub Execution Completed ===")
    print("✅ All scripts from GitHub have been executed. Check 'batch_run_log.txt' for details.")

if __name__ == "__main__":
    main()
