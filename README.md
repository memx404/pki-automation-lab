# PKI Automation Tool
**Course:** Skills Development III - DevOps Laboratory 1  
**Date:** December 2025

## Project Overview
This project demonstrates the automation of a Public Key Infrastructure (PKI) simulation tool using GitHub Actions. It focuses on integrating security-related tools into a Continuous Integration (CI) pipeline.

## Files
* `pki_tool.py`: Simulates key generation (Public/Private).
* `test_pki_tool.py`: Unit test to verify tool output.
* `.github/workflows/pki-ci.yml`: Automation script for GitHub Actions.

## CI/CD Status
The project is configured with GitHub Actions. On every push, the `PKI CI Pipeline` automatically runs the test suite to ensure code integrity.

## How to Run Locally
1. Clone the repo: `git clone <your-repo-url>`
2. Run the tool: `python pki_tool.py`
3. Run the tests: `python test_pki_tool.py`