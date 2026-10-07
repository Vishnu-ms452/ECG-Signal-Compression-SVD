import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

def main():
    # 1. Matrix Representation of Data
    print("Loading dataset...")
    # Make sure ecg.csv is in the same folder as this script
    df = pd.read_csv('ecg.csv', header=None)
    ecg_matrix = df.to_numpy()
    print(f"Original Matrix Shape: {ecg_matrix.shape}")

    # 2. Singular Value Decomposition (SVD) Core
    print("Executing Singular Value Decomposition...")
    U, S, Vt = np.linalg.svd(ecg_matrix, full_matrices=False)

    # 3. Truncation and Basis Formation
    # k is the number of singular values we keep. 
    # Try changing this to 2, 5, or 10 during your demo!
    k = 5 
    U_k = U[:, :k]
    S_k = np.diag(S[:k])
    Vt_k = Vt[:k, :]

    # 4. Final Reduced Model & Reconstruction
    print(f"Reconstructing compressed signal with top {k} singular values...")
    compressed_ecg_matrix = np.dot(U_k, np.dot(S_k, Vt_k))

    # --- Analytics & Validation ---
    mse = mean_squared_error(ecg_matrix, compressed_ecg_matrix)
    
    # Calculate compression ratio
    original_size = ecg_matrix.size
    compressed_size = U_k.size + S[:k].size + Vt_k.size
    compression_ratio = original_size / compressed_size

    print("\n--- Project Results ---")
    print(f"Compression Ratio: {compression_ratio:.2f}x")
    print(f"Mean Squared Error: {mse:.5f}")

    # --- Visual Demo Output ---
    # Plotting the very first patient's ECG record (Row 0)
    plt.figure(figsize=(10, 5))
    plt.plot(ecg_matrix[0], label='Original Noisy ECG', color='lightcoral', alpha=0.8)
    plt.plot(compressed_ecg_matrix[0], label=f'SVD Compressed (k={k})', color='darkred', linewidth=2)
    plt.title(f"ECG Data Compression using SVD (Components Kept: {k})")
    plt.xlabel("Time Steps (Data Points)")
    plt.ylabel("Voltage Amplitude")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()