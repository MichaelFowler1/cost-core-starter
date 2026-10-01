# cost-core starter

[![examples](https://github.com/MichaelFowler1/cost-core-starter/actions/workflows/examples.yml/badge.svg)](https://github.com/MichaelFowler1/cost-core-starter/actions/workflows/examples.yml)

Example workbooks for [cost-core](https://github.com/MichaelFowler1/cost-risk-toolkit),
ready to run. Clone it, install one package, and you'll have a cost risk
analysis, an EVM forecast, a schedule check, a JCL, an analysis of
alternatives and a portfolio choice, each as an Excel report and a
PowerPoint briefing.

## Quick start

```bash
git clone https://github.com/MichaelFowler1/cost-core-starter
cd cost-core-starter
pip install -r requirements.txt
python run_all.py
```

The install takes a few minutes the first time (it brings in numpy, scipy,
matplotlib and friends). After that the cost risk example takes about 15
seconds and all six about a minute and a half. Then open
`results/cost-risk/report.xlsx`, or run just one: `python run_all.py cost-risk`.

No git? Click **Code**, then **Download ZIP**, unzip it and run the last two
lines in that folder.

## What's here

| File | What it is | What you get |
| --- | --- | --- |
| `examples/estimate.xlsx` | A ground station upgrade: eight WBS elements with low, most likely and high, three risks, correlations | How likely the estimate is to overrun, the cost at 50/70/80/90% confidence, what drives the risk |
| `examples/cer.xlsx` | Twelve past radar programs, cost against weight and power, and two new radars to price | The CER fitted three ways (OLS, MUPE, ZMPE), what each driver does to cost, and each new radar's estimate with a range |
| `examples/phase.xlsx` | Five estimate lines across RDT&E, procurement and O&M, with a spending profile each and an invented 2% index | The budget by fiscal year and appropriation, in then-year dollars, and what inflation adds |
| `examples/evm.xlsx` | Monthly earned value for three control accounts | CPI, SPI, warning signs and a forecast at completion with a range |
| `examples/schedule.xml` | A small Microsoft Project schedule saved as XML | The DCMA 14-point check |
| `examples/jcl.xlsx` | A spacecraft from design to launch, with durations, costs and risks | The joint cost and schedule confidence of the plan |
| `examples/aoa.xlsx` | Three ways to replace a sensor, and keeping it, costed over their life | Which is cheapest, how often, which are dominated, and whether each pays for itself against keeping the current system |
| `examples/portfolio.xlsx` | Candidate programs, funding options and a budget by year | The best set to fund, and the chance each year goes over |

Every workbook has an Instructions sheet saying what goes in each column.
Every number in them is invented.

## Now with your own numbers

Copy an example into a folder called `mine`, edit it in Excel, and point the
command at it:

```bash
mkdir mine
copy examples\estimate.xlsx mine\estimate.xlsx        # Windows (cp on Mac and Linux)
ce-core cost-risk --data mine/estimate.xlsx --out mine/results
```

`mine/` and `results/` are in `.gitignore`, so git never picks them up.
**Keep real program, contractor and sponsor data off GitHub**, including
forks of this repository. Everything cost-core does runs on your own
machine; nothing is sent anywhere.

`ce-core` on its own lists everything it can do, and `ce-core <command>
--help` explains each option. If `ce-core` isn't found after installing,
`python -m cost_core` does the same.

## Found a problem?

[Open an issue on cost-core](https://github.com/MichaelFowler1/cost-risk-toolkit/issues/new/choose),
with invented numbers only.

## Licence

The example files and `run_all.py` here are under the MIT No Attribution
licence ([LICENSE](LICENSE)): copy them, change them, build on them, no
strings. cost-core itself, which `pip install` brings in, has its own licence:
free for noncommercial and government work, contractors included. See
[its License section](https://github.com/MichaelFowler1/cost-risk-toolkit#license).
