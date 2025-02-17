# Dagster Crypto Notification Pipeline
This project aims to provide insights on cryptocurrency using [Dagster](https://docs.dagster.io/) orchestration to collect and transform data from APIs. Notifications about data insights can then be sent via messaging service to the user.

## API(s) Utilized

- [Crypto Compare](https://cryptocompare.com) - data source for information on cryptocurrencies (i.e., price, volume, percentage change)
> Note: This is a free API up to 11,000 calls per month.

## Getting Started
Follow these instructions to experiment with the project yourself.
### Clone the Repo
Copy the repo locally.

```git clone https://github.com/jharring17/dagster_crypto_pipeline.git <folder_path>```

### Create a Virtual Env
Enter the folder when the project was cloned.

```cd <path_to_project_folder>```

Create a virtual env to manage dependencies.

```python -m venv <virtual_env_name>```

Activate the virtual env.

```source <virtual_env_name>/bin/activate```

Install the dependencies listed within the repo.

```pip install -r requirements.txt```

To check all packages successfully installed, list them.

```pip list```

### Create a .env File
In the project root directory, create a .env file.

```touch .env```

Enter the API credentials within the file.

```VAR_NAME="value"```

### To Run Dagster UI
Execute the following command within the project.

```dagster dev```

The UI will now be accessible at [localhost](localhost:3000).