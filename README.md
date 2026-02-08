# 🏎️ Dynamic Systems Analysis

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![LaTeX](https://img.shields.io/badge/typeset-LaTeX-green.svg)
![Python](https://img.shields.io/badge/simulation-Python-yellow.svg)

A comprehensive technical investigation into the behavior, modeling, and frequency-domain characteristics of **Linear Time-Invariant (LTI)** systems. This project bridges the gap between theoretical calculus and mechanical engineering applications through a detailed analysis of a **Quarter-Car Suspension Model**.

## 📑 Project Overview
This repository contains a 7-page technical booklet (written in LaTeX) and supporting Python scripts that explore second-order dynamic systems. Key topics include:
* **Laplace Transform Theory:** Derivations of transfer functions and stability criteria.
* **Quarter-Car Case Study:** Numerical analysis of a luxury sedan's suspension parameters.
* **Frequency Analysis:** Investigation of resonance phenomena and damping ratios ($\zeta$).
* **Active Control:** Conceptual framework for PID feedback integration.

## 🧮 Mathematical Model
The system is governed by the second-order differential equation:
$$m\ddot{x} + c\dot{x} + kx = F(t)$$



[Image of a mass-spring-damper system diagram]


Converted to the $s$-domain, the transfer function $H(s)$ is:
$$H(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$



## 🚀 Getting Started

### Prerequisites
To compile the booklet and run the simulations, you will need:
* **LaTeX Distribution:** (TeX Live or MiKTeX)
* **Python 3.x:** with `numpy`, `matplotlib`, and `scipy`

### Compilation Instructions
To generate the PDF booklet with correct citations and table of contents, run the following sequence in your terminal:
1. `pdflatex main.tex`
2. `bibtex main`
3. `pdflatex main.tex`
4. `pdflatex main.tex`

### Running the Simulation
Execute the Python script located in Appendix A to visualize the suspension response:
```bash
python simulation_script.py

```

## 📈 Key Results

* **Damping Ratio ():** 0.35 (Underdamped).
* **Natural Frequency ():** 7.89 rad/s.
* **Settling Time ():** ~1.45s (2% criterion).
* **Resonance Peak:** Analysis shows significant cabin amplification at  rad/s.

## 🛠️ Repository Structure

* `main.tex`: The primary LaTeX source code.
* `references.bib`: Bibliography database for engineering citations.
* `simulation.py`: Python script for LTI system response.
* `Dynamic_Systems_Analysis.pdf`: The final generated report.

## 📄 License

This project is licensed under the MIT License.
