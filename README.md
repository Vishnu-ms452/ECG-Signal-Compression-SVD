# ECG Data Compression using SVD

Compressing and denoising ECG heartbeat signals with a truncated Singular Value Decomposition (SVD).

**Course:** UE25MA242A – Mathematical Foundation for AI & Data Science

**Team:**
- Vishesh M (PES1UG25AM451)
- Vishnu Marangat Sankaran (PES1UG25AM452)
- Vihaan Vishwanath Siddini (PES1UG25AM448)
- Yuvaraj Karam (PES1UG25AM458)

---

## Overview

Continuous ECG monitoring produces large amounts of high-dimensional time-series data, and raw signals are costly to store and transmit. They are also affected by baseline wander and high-frequency noise.

This project represents the ECG dataset as a matrix (rows = heartbeats, columns = time-step voltage samples) and applies SVD to keep only the dominant waveform patterns. Large singular values capture the main heartbeat structure (such as the QRS complex), while the small trailing components mostly contain noise.

## Method

1. **Load data:** read `ecg.csv` with Pandas and convert it to a NumPy matrix `A`.
2. **Decompose:** compute the SVD, `A = UΣVᵀ`.
3. **Truncate:** keep the top `k` singular values to form `Uₖ`, `Σₖ` and `Vₖᵀ`.
4. **Reconstruct:** `Aₖ = UₖΣₖVₖᵀ` using matrix multiplication.
5. **Evaluate:** compute the mean squared error (MSE) and the compression ratio, then plot the original signal against the reconstruction.

## Requirements

- Python 3.8+
- pandas
- numpy
- matplotlib
- scikit-learn

Install them with:

```bash
pip install pandas numpy matplotlib scikit-learn
```

## Usage

1. Place your dataset as `ecg.csv` in the same folder as the script. The file should have no header row, with each row being one heartbeat and each column one time step.
2. Run the script:

```bash
python main.py
```

3. To change the number of retained components, edit this line in the script:

```python
k = 5   # try 2, 5, 10, ...
```

## Output

The script prints:

- the original matrix shape
- the **compression ratio**, calculated as `original size / (size of Uₖ + Σₖ + Vₖᵀ)`
- the **mean squared error** between the original and reconstructed matrices

It also shows a plot of the first heartbeat (row 0): the original noisy ECG in light red and the SVD-compressed version in dark red.

## Results (k = 5)

| Metric | Value |
|---|---|
| Signal columns | 141 |
| Retained components (k) | 5 |
| Compression ratio | ~4.2× |
| MSE | ~0.001 |

The reconstruction keeps the QRS complex while smoothing jagged inter-beat noise.

> **Note:** These are project-reported results from this demonstration, not general or clinical validation.

## Future Work

- Test across more ECG records and different values of `k`.
- Evaluate the compressed signals as inputs to predictive models such as CNNs, and compare task performance before and after compression.

## File Structure

```
.
├── main.py     # SVD compression script
├── ecg.csv     # ECG dataset (not included, add your own)
└── README.md
```
````

- **Script name:** I assumed `main.py`, so change it if yours is named differently.
- **Dataset:** Add a line about where `ecg.csv` came from if you want to credit it.
- **Results table:** The numbers come from your slides, since I haven't run the code.
