# Madhava-Leibniz Series for Calculating Pi

"""
This script implements the Madhava-Leibniz series for calculating the value of pi.

The Madhava-Leibniz series is defined as:

    π = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...)

This implementation includes:
1. A basic version of the series.
2. An optimized version that avoids power calculations.
3. Analysis of convergence with different numbers of terms.
4. Detailed documentation of series behavior and characteristics.
"""

def madhava_leibniz(terms):
    """Calculate pi using the Madhava-Leibniz series with the specified number of terms."""
    pi_over_4 = 0.0
    for n in range(terms):
        pi_over_4 += ((-1)**n) / (2 * n + 1)
    return pi_over_4 * 4


def optimized_madhava(terms):
    """Calculate pi using an optimized version of the Madhava-Leibniz series."""
    pi_over_4 = 0.0
    sign = 1
    denominator = 1
    for n in range(terms):
        pi_over_4 += sign / denominator
        sign *= -1  # Alternate the sign
        denominator += 2  # Increase denominator by 2
    return pi_over_4 * 4


def analyze_convergence(max_terms):
    """Analyze convergence of the series by calculating pi for a range of terms."""
    results = []
    for terms in range(1, max_terms + 1):
        results.append((terms, madhava_leibniz(terms)))
    return results


if __name__ == '__main__':
    max_terms = 100  # Change this value to analyze more terms
    print(f'Madhava-Leibniz Series Results (up to {max_terms} terms):')
    for terms, pi_val in analyze_convergence(max_terms):
        print(f'Terms: {terms}, Estimated Value of Pi: {pi_val}')  
