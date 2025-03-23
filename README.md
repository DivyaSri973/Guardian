# Guardian - Workplace Harassment Detection Slack App

## Overview

Guardian is a Slack app designed to detect and flag potential workplace harassment within Slack channels. It uses a pre-trained Natural Language Processing (NLP) model to analyze messages and identify offensive content. The app aims to create a safer and more respectful work environment by providing real-time feedback and alerts.

## Codebase Structure
  todo
  
## Setup and Installation

Follow these steps to set up and run Guardian locally:

### Prerequisites

- **Python 3.7+**: Ensure you have Python 3.7 or a later version installed on your system.
- **Conda (Recommended)**: It is recommended to use Conda to create a virtual environment and manage dependencies. You can download and install Conda from [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
- **Slack App**: You will need to create a Slack app and obtain the necessary API tokens and signing secret. Follow the instructions in the Slack API documentation to set up your app.

### Installation Steps

#### 1. Clone the Repository

Clone the Guardian repository to your local machine:

```bash
git clone https://github.com/DivyaSri973/Guardian.git
cd Guardian
```

#### 2. Create a Virtual Environment (Recommended)

Using Conda:

```bash
conda create -n guardian_env python=3.9
conda activate guardian_env
```

Using venv:

```bash
python3 -m venv guardian_env
source guardian_env/bin/activate  # On Windows, use: guardian_env\Scripts\activate
```

#### 3. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

#### 4. Set Up Environment Variables

You need to set the following environment variables:

- `SLACK_BOT_TOKEN`: Your Slack bot token (xoxb-...).
- `SLACK_SIGNING_SECRET`: Your Slack signing secret.

You can set these variables in your terminal or in a `.env` file.

For example, using a `.env` file:

1. Create a `.env` file in the root directory of the project.
2. Add the following lines, replacing the values with your actual tokens:

    ```bash
    SLACK_BOT_TOKEN=xoxb-your-bot-token
    SLACK_SIGNING_SECRET=your-signing-secret
    ```

3. If using a `.env` file, install `python-dotenv`:

    ```bash
    pip install python-dotenv
    ```

4. Load the variables in your `app.py` file:

    ```python
    from dotenv import load_dotenv
    import os

    load_dotenv()

    SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
    SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")
    ```

#### 5. Download the Model

Download the model and tokenizer from this Google Drive link:
[Download Model](https://drive.google.com/drive/folders/1YCdlOuN_9EUy9kF6j1KKLM3UPi9fJc6R?usp=drive_link)

Place the downloaded files in the `model_tokenizer/` folder.

#### 6. Run the Application

Run the Slack app using the following command:

```bash
python app.py
```

The app should now be running and listening for events from your Slack workspace.

## Usage

1. **Invite the App to a Channel**:

    Invite your Slack app to the channels you want it to monitor.

2. **Real-time Message Analysis**:

    The app will analyze messages in real-time and flag potentially offensive content.

3. **Review and Adjust**:

    Review the flagged messages and adjust the app's settings or model as needed to improve accuracy.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

