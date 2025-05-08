import requests
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://hepciabashymueejiwml.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "your-default-key")


headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

def read_and_index_docs(docs_dir='./docs'):
    """
    Read name price and add to supabase
    """

    
    for filename in os.listdir(docs_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(docs_dir, filename)
            try:
                with open(file_path , 'r', encoding='utf-8') as file:
                    content = file.read()
                lines = content.split('\n')
                title = lines[0]  # Get the first line as the title
                name = title.split(':')[1].strip()  # Extract name from the title
                price = lines[2].split(':')[1].strip()  # Extract price from the second line
                price = price.replace('฿', '').replace(',', '')  # Clean the price string
                price = float(price)  # Convert to float    

                # Prepare the data for indexing
                data = {
                    "name": name,
                    "amount": 99,
                    "price": price,
                }            
                response = requests.post(
                            f"{SUPABASE_URL}/rest/v1/products",  # "users" is the table name
                            headers=headers,
                            json=data
                        )
                if response.status_code == 201:
                    logger.info(f"Successfully indexed {name} with price {price}")
            except Exception as e:
                logger.error(f"Error processing {name}: {str(e)}")
                

if __name__ == "__main__":
    read_and_index_docs()
