# chatgpt

This repo contains simple Python scripts.

## Scripts

- `hellow.py` – interactively prints a greeting.
- `financial_metrics.py` – calculates ROI and payback period.

### Usage
Run with all parameters on the command line or let the script prompt you for
missing values:

```bash
python3 financial_metrics.py <initial_investment> <annual_cash_flow> [years]
```

Example:

```bash
python3 financial_metrics.py 1000 300 5
```

This command prints the ROI after 5 years and the payback period. If you omit
the numeric arguments, the program will ask for them interactively.

For a simple greeting:

```bash
python3 hellow.py
```

The script prompts you for a word and prints `hellow <word>`.
