# ECG Data Compression using Singular Value Decomposition (SVD)

**Course:** UE25MA242A – Mathematical Foundation for AI & Data Science (MFAD 2026)  
**Mini Project – Experiential Learning Level 2 (Orange Problem)**

## Team Members
*   Vishesh M - PES1UG25AM451
*   Vishnu Marangat Sankaran - PES1UG25AM452
*   Yuvaraj Karam - PES1UG25AM458
*   Vihaan Vishwanath Siddini - PES1UG25AM448

## Project Objective
This project demonstrates the practical application of linear algebra in the medical data science domain. We use **Singular Value Decomposition (SVD)** to compress high-dimensional physiological time-series data (ECG readings). By factorizing the data matrix and retaining only the dominant singular values, we isolate the critical QRS waveform structures from baseline noise, drastically reducing data size while preserving diagnostic fidelity.

## Mathematical Concepts Applied
1. **Matrix Representation:** Converting 141-column tabular time-series data into an $m \times n$ mathematical matrix.
2. **Singular Value Decomposition ($A = U \Sigma V^T$):** Decomposing the dataset to extract orthogonal matrices and singular values.
3. **Basis Formation and Truncation:** Slicing matrices to retain only the top $k$ components (dominant signals).
4. **Signal Reconstruction:** Utilizing matrix multiplication (dot products) to rebuild the compressed signal.
5. **Error Calculation:** Using Mean Squared Error (MSE) to quantify data loss mathematically.

## Setup Instructions
To run this project locally, ensure you have Python 3 installed on your system. 

1. **Clone the repository:**
   ```bash
   git clone <your-repo-link>
   cd <your-repo-folder>
   ```

2. **Install required dependencies:**
   The project requires standard data science libraries. Install them using pip:
   ```bash
   pip install pandas numpy matplotlib scikit-learn
   ```

3. **Add the Dataset:**
   Ensure the `ecg.csv` file (containing the numerical voltage readings without text headers) is placed in the same root directory as `main.py`.

## How to Run the Project
Execute the main Python script from your terminal:
```bash
python main.py
```

## Expected Output (Deliverables)
Upon successful execution, the program will output:
1. **Terminal Metrics:** The original matrix shape, the calculated Data Compression Ratio, and the Mean Squared Error (MSE) comparing the original vs. reconstructed signal.
2. **Visual Demo:** A Matplotlib graph comparing the original noisy ECG wave against the newly compressed SVD wave side-by-side. 
