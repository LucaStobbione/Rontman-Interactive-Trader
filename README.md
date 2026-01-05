# Rotman Interactive Trader – Dynamic Order Arrival (LT3)

This project is a **partial automation trading script** developed for the **Rotman Interactive Trader (RIT)** simulator, specifically for the **Dynamic Order Arrival (LT3) case**.

**Case Description**:  
[Dynamic Order Arrival Case Brief (LT3)](https://rotmanfrtl.github.io/RIT%20-%20Case%20Brief%20-%20LT3%20-%20Dynamic%20Order%20Arrival.pdf)

**Rotman Interactive Trader Platform**:  
https://rotmaninteractive.trading/

---

## Objective of the Project

The goal of this project is to **automate the evaluation and execution of tender offers** in the LT3 Dynamic Order Arrival case, where third-party participants periodically submit **buy or sell tenders** on two stocks.

The script is designed to:
- React **in real time**
- Evaluate **market liquidity and pricing**
- Automatically accept **profitable tenders**
- Leave **position liquidation to the trader**, due to platform constraints

This mirrors a realistic trading setup where **decision-making is automated**, but **execution and risk management still require human intervention**.

---

## How the Code Works

### Case Timing Management
- The script starts **5 seconds after the case begins**
- It stops **5 seconds before the case ends**
- This ensures stability and avoids edge-case execution issues

---

### Real-Time Monitoring (1-second frequency)

Every second, the program:
1. **Checks for incoming tender offers**  
   - Buy or sell offers from third parties on either stock

2. **Evaluates market conditions**
   - Reads the current **order book**
   - Checks whether there is **sufficient liquidity**
   - Verifies that prices in the book are:
     - **Better than or equal to the tender price**, depending on the side

3. **Decision Logic**
   - If both **liquidity and price conditions** are satisfied  
   → the tender is **automatically accepted** on the RIT platform  
   - Otherwise, the tender is ignored

---

### Position Liquidation (Manual)

After a tender is accepted:
- The resulting position **must be liquidated manually** on the RIT platform
- Full automation of liquidation was **not possible**, as:
  - Rotman Interactive Trader does **not allow programmatic trade execution** for market orders

This design choice reflects real-world constraints where **API limitations** require hybrid human–algorithm workflows.

---

## Limitations & Improvements

**Current limitations**
- No automated liquidation due to platform restrictions

---

## 🛠 Technologies Used

- **Python**

---

## Final Notes

This project demonstrates:
- Practical understanding of **market microstructure**
- Ability to **translate trading logic into code**
- Awareness of **execution constraints and operational risk**

It is intentionally simple, robust, and designed to operate **under real-time pressure**, consistent with trading environments.

