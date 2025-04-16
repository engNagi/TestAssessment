# Testing Challenge Repository

## Overview
This repository is designed for a testing challenge focused on image classification. For the purpose of this challenge we have created a mocked model that will randomly indicate if an image is a "dog" or a "cat", and then it will send it to a mocked service and print the result in the console." 

### Repository Structure
```
├── data/
│   ├── images/              # Sample images for testing
│   ├── labels/              # Corresponding labels for the images
├── src/
│   ├── model/
│   │   ├── mocked_model.py   # Mocked model implementation
│   │   └── __init__.py      # Initialization for the model package
│   ├── services/
│   │   ├── mock_service.py  # Simulated service interaction
│   ├── utils/
│   │   ├── data_validator.py # Functions to validate data integrity
│   │   ├── helpers.py       # General utility functions
├── tests/                   # Contains all test cases
├── requirements.txt         # Python dependencies
├── pytest.ini               # Pytest configuration
└── README.md                # Documentation
```

---

## Installation

### Prerequisites
Ensure you have Python 3.8+ installed. Use a virtual environment to manage dependencies.

### Steps
1. **Fork the repository:**
   ```bash
   git fork <repository-url>
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
or
   ```bash
   pip3 install -r requirements.txt
   ```

4. **How to run the project:**
```bash
python3 -m src.services.mock_service  
```

You will get something like this in the terminal:
```bash
{'status': 'success', 'data': {'label': 'dog', 'confidence': 0.92}}
```

4. **Verify the setup:**
   Run the following command to ensure everything works:
   ```bash
   pytest
   ```
You should get the following:
   ```bash

   ```
---

## Tasks

Notes: Use Pytest, or `unittest`.

**Task-1:**
Under the tests/ folder, you will find four empty files:
   test_data_validation.py, test_model.py, unit_testing.py and test_service.py

    - Develop data testing based from `data/images/` folder, and allocate the testing in the test_data_validation.py
    - Develop testing for the mocked model within `test_model.py` 
    - Develop integration testing in the `test_service.py` 
    - Develop unit testing on any of the files and include in `unit_testing.py`

**Task-2:**
   - Review the random and unrelated unit testing done in `tests/unit_tests` and do code review on it. And then insert your code review on UNITTESTREVIEW.md file

**Task-3:**
   - Configure CI/CD pipeline for one of the testing files. 

**Task-4:**
   - Update the README.md file or create a new one named `HOW_TO_RUN_TESTS.md` on how to run the tests. 


**Deliverables:**
   - A private GitLab Repository with Task-1, Task-2, Task-3, and Task-4
   - Share the private GitLab repo with @karlamieses

---

## Notes
- The `data/` directory contains sample images and corresponding labels.
- The `src/` directory provides reusable modules for model, services, and utilities.
- The `tests/` directory includes test cases written using `pytest`.

Feel free to extend the repository by adding more tests or enhancing existing functionality!
