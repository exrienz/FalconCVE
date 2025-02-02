# Falcon CrowdStrike CVE Checker

## Overview

This script utilizes the Falcon CrowdStrike API to determine whether a specific CVE is affecting your environment. It checks for vulnerabilities associated with the provided CVE ID and informs you if your system is vulnerable or not.

## Prerequisites

Before using this script, ensure that you have the following:

- Python installed (version 3.6 or higher)
- CrowdStrike API credentials (Client ID and Secret)
- Access to the Falcon CrowdStrike API

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/exrienz/Falcon-CrowdStrike-CVE-Checker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Falcon-CrowdStrike-CVE-Checker
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script from the command line, providing the CVE ID as an argument:

```bash
python3 falconcve.py CVE-XXXX-XXXXX
```

Replace CVE-XXXX-XXXXX with the desired CVE ID.

The script will output whether your system is vulnerable or not based on the CrowdStrike API response.

