---
layout: post
title: "Layer-by-Layer Design: Bottom-Up Thermal Stack Analysis"
date: 2026-03-06 13:15:00 +0000
topic: "Thermal Systems"
tags: ["thermal management", "CTE mismatch", "failure analysis", "material selection", "reliability"]
summary: "Detailed bottom-up analysis of the 500 W/cm² thermal stack, examining materials, failure modes, CTE mismatch, and interface engineering for each layer from heat source to ambient."
references:
  - author: "Sloan et al."
    year: 2018
    title: "Thermal management of GaN HEMTs on diamond substrates"
    journal: "IEEE Transactions on Components, Packaging and Manufacturing Technology"
    volume: "8"
    issue: "7"
    pages: "1183-1191"
    
  - author: "Katz et al."
    year: 2020
    title: "Silver sintering die attach for wide bandgap semiconductors"
    journal: "Microelectronics Reliability"
    volume: "114"
    pages: "113804"
    
  - author: "Goodson et al."
    year: 2019
    title: "Thermal interfaces for high-power electronics: Challenges and opportunities"
    journal: "Annual Review of Heat Transfer"
    volume: "22"
    pages: "1-48"
---

## Bottom-Up Stack Analysis

Starting from the heat source and working upward, we analyze each layer's materials, failure modes, and critical interfaces.

---

## Layer 1: Heat Source (GaN/SiC Device)

### Material Options

| Technology | Substrate | k (W/m·K) | CTE (ppm/K) | Max T (°C) | Cost/cm² | Maturity |
|------------|-----------|-----------|-------------|------------|----------|----------|
| **GaN-on-Si** | Silicon | 150 | 2.6 | 150 | $ | High volume |
| **GaN-on-SiC** | SiC | 490 | 4.0 | 200 | $$ | Mature |
| **GaN-on-Diamond** | CVD Diamond | 1500 | 1.0 | 250 | $$$$ | Emerging |
| **SiC MOSFET** | SiC | 490 | 4.0 | 175 | $$$ | Mature |
| **GaN-on-QST** | Qromis substrate | 150 | 3.0 | 175 | $$ | Commercializing |

### Key Failure Modes

**1. Thermal Runaway**
- **Mechanism:** Positive feedback loop — temperature ↑ → on-resistance ↑ → power dissipation ↑ → temperature ↑↑
- **Trigger:** Inadequate heat removal, hotspot formation
- **Mitigation:** Active thermal monitoring, derating curves, junction temperature sensors

**2. Gate Degradation**
- **Mechanism:** Electrochemical reactions at high temperature/voltage
- **Threshold:** >150°C accelerates exponentially
- **Indicator:** Threshold voltage drift, gate leakage increase
- **Life model:** Arrhenius equation with Ea ~ 1.0-1.2 eV

**3. Electromigration**
- **Mechanism:** Metal atom migration in interconnects under high current density
- **Critical current:** ~1 MA/cm² for Al, ~5 MA/cm² for Cu
- **Mitigation:** Robust metallization, current spreading structures

### Interface to Layer 2 (Critical)

**CTE Mismatch Analysis:**

```
Device (GaN-on-SiC):  CTE = 4.0 ppm/K
TIM1 (AuSn solder):   CTE = 20 ppm/K  ← 16 ppm/K mismatch!
```

**Thermal cycling stress:**
```
Δσ = E × ΔCTE × ΔT
   = 30 GPa × 16×10⁻⁶ × 125K
   ≈ 60 MPa shear stress per cycle
```

With fatigue life ~10⁴-10⁵ cycles for typical solders, this is a **major reliability concern**.

---

## Layer 2: Die Attach / TIM 1

### Material Options

| Material | k (W/m·K) | CTE (ppm/K) | Process | Void Risk | Cycling Life | Cost/cm² |
|----------|-----------|-------------|---------|-----------|--------------|----------|
| **Au-20Sn** | 57 | 16 | Reflow 280°C | Low | 10³-10⁴ cycles | $20-50 |
| **Ag Sinter** | 250 | 19 | Press 250°C | Medium | 10⁴-10⁵ cycles | $10-30 |
| **Cu Sinter** | 300 | 17 | Press 300°C | High | 10⁴ cycles | $15-40 |
| **Thermal Grease** | 3-8 | N/A | Dispense | High (pump-out) | Poor | $0.50-2 |
| **Graphite Sheet** | 400 (in-plane) | -1 | Laminate | Low | 10⁵+ cycles | $5-15 |
| **Indium Foil** | 86 | 33 | Press | Low | Good (compliant) | $10-25 |

### CTE Mismatch Management

**Critical Interface: Device (4 ppm/K) → TIM1 → Diamond (1 ppm/K)**

The diamond interposer actually **reduces** CTE mismatch stress because:
- GaN/SiC CTE: 4.0 ppm/K
- Diamond CTE: 1.0 ppm/K  
- Net mismatch: 3.0 ppm/K (through TIM1)

**Without diamond** (direct to Cu): 4.0 vs 17.0 ppm/K = 13 ppm/K mismatch!

### Failure Modes

**1. Void Formation (Sintering)**
- **Cause:** Incomplete solvent burn-off, trapped air, poor pressure
- **Impact:** Local hot spots, current crowding
- **Detection:** Scanning acoustic microscopy (SAM), X-ray
- **Prevention:** Vacuum assist, staged temperature profile, pressure control

**2. Delamination**
- **Cause:** CTE mismatch stress, contamination, poor adhesion
- **Onset:** Typically after 500-2000 thermal cycles
- **Signature:** Acoustic voids at interface edges
- **Prevention:** Plasma cleaning, metallization optimization, compliant layers

**3. Pump-out (Greases)**
- **Mechanism:** Thermal cycling squeezes grease from interface
- **Rate:** ~10-30% area loss per 1000 cycles
- **Result:** Dry spots, catastrophic failure
- **Solution:** Use phase-change materials or solid bonding

### Recommended: Ag Sinter

**Why Ag sinter?**
- **Porosity:** 10-20% (compliant, stress relief)
- **High thermal conductivity:** 200-300 W/m·K
- **Good adhesion:** To most metallizations
- **Established process:** Automotive qualification (AEC-Q101)
- **Cost-effective:** Lower than AuSn for performance

**Process parameters:**
- Temperature: 200-250°C
- Pressure: 10-30 MPa
- Time: 10-30 minutes
- Atmosphere: N₂ or vacuum

---

## Layer 3: CVD Diamond Interposer

### Why Diamond?

| Property | Diamond | Copper | AlN | Benefit |
|----------|---------|--------|-----|---------|
| Thermal conductivity | 1000-2000 | 400 | 285 | 2.5-5× better spreading |
| CTE | 1.0 | 17 | 4.2 | Matches GaN, reduces stress |
| Electrical resistivity | >10¹⁶ | 10⁻⁸ | >10¹¹ | Electrical isolation |
| Young's modulus | 1050 GPa | 130 GPa | 330 GPa | Stiff, stable |
| Max temperature | 600°C | 200°C | 500°C | Wide operating range |

### Manufacturing Considerations

**CVD Diamond Growth:**
- **Method:** Microwave plasma CVD (MPCVD)
- **Rate:** ~1-3 μm/hour
- **Cost driver:** Deposition time (thickness³)
- **Typical thickness:** 0.5-2.0 mm for thermal management
- **Surface finish:** As-grown Ra ~1-5 μm, polished Ra <50 nm

**Metallization (Critical!):**
Diamond is chemically inert — adhesion is challenging.

| Metallization | Adhesion | Process | Reliability | Cost |
|--------------|----------|---------|-------------|------|
| Cr/Au | Good | Sputter | Good | $ |
| Ti/Pt/Au | Excellent | E-beam | Excellent | $$ |
| Ti/Cu/Ni/Au | Excellent | Electroless | Good | $$ |
| Direct Cu plating | Poor | Electroless | Poor | $ |

**Recommended:** Ti(50nm)/Pt(100nm)/Au(500nm) for critical applications

### Failure Modes

**1. Metallization Delamination**
- **Cause:** CTE mismatch between metal (17 ppm/K) and diamond (1 ppm/K)
- **Stress:** σ = E_metal × ΔCTE × ΔT ≈ 130 GPa × 16×10⁻⁶ × 125K ≈ 260 MPa
- **Solution:** Compliant interlayer (Pt), graded metallization

**2. Surface Roughness Issues**
- **Problem:** High Ra increases contact resistance
- **Target:** Ra < 100 nm for TIM interfaces
- **Method:** Mechanical polishing, laser polishing, chemical-mechanical polishing

**3. Graphitic Inclusions**
- **Cause:** Non-diamond carbon in growth
- **Impact:** Local thermal barriers, electrical shorts
- **Detection:** Raman spectroscopy, thermal imaging
- **Prevention:** Process optimization, quality screening

### CTE Mismatch: Layer 3 → Layer 4

```
Diamond (1 ppm/K) → TIM2 (15 ppm/K) → VC Wall (17 ppm/K)

Maximum mismatch: Diamond to VC wall = 16 ppm/K
Stress per cycle: ~200 MPa (high!)
```

**Critical:** TIM2 must be compliant to absorb this mismatch.

---

## Layer 4: TIM 2 (Diamond to Vapor Chamber)

### The Compliance Challenge

This interface sees the **largest CTE mismatch in the stack:**
- Diamond: 1 ppm/K  
- Copper VC wall: 17 ppm/K
- ΔCTE = 16 ppm/K (extreme!)

### Material Options

| Material | k (W/m·K) | Compliance | Max ΔT | Cycling Life | Key Advantage |
|----------|-----------|------------|--------|--------------|---------------|
| **Soft metal foil (In, Al)** | 80-237 | High (plastic deformation) | 100°C | 10⁵ cycles | Compliant, reworkable |
| **Graphite sheet** | 400 | High (anisotropic) | 150°C | 10⁶ cycles | Best conductivity |
| **Thermal grease** | 4-10 | Very high | 80°C | Poor | Conformal |
| **Phase change** | 3-8 | Medium | 100°C | 10⁴ cycles | Solid at use temp |
| **Gap filler pad** | 3-6 | High | 80°C | 10⁴ cycles | Easy assembly |
| **Liquid metal** | 40-80 | Very high | 100°C | Risk (pump-out) | Best wetting |

### Recommended: Graphite Sheet

**Why graphite?**
- **Anisotropic compliance:** Soft through-thickness, stiff in-plane
- **High conductivity:** 300-600 W/m·K in-plane
- **CTE:** -1 to +3 ppm/K (close to diamond!)
- **Proven:** Tesla, SpaceX use for similar applications

**Structure:**
```
[Diamond Interposer]
      ↓
[Graphite Sheet (200 μm)] — Through-thickness k ≈ 10 W/m·K
      ↓  
[VC Wall]
```

**Trade-off:** Low through-thickness conductivity requires thin sheets.

### Alternative: Indium Foil

**Benefits:**
- **Softest metal:** Yield strength ~3 MPa (vs 70 MPa for Cu)
- **Excellent wetting:** To most surfaces
- **Self-healing:** Cold welds under pressure

**Limitations:**
- **Cost:** Indium is expensive (~$200/kg)
- **Creep:** Can extrude from interface over time
- **Oxidation:** Requires protective coating

---

## Layer 5: Vapor Chamber Wall

### Material Options

| Material | k (W/m·K) | CTE (ppm/K) | Strength | Formability | Cost |
|----------|-----------|-------------|----------|-------------|------|
| **Copper (C110)** | 400 | 17 | Good | Excellent | $ |
| **Aluminum (6061)** | 205 | 23 | Moderate | Excellent | $ |
| **Cu-Mo-Cu (CMC)** | 180-220 | 6-9 | Excellent | Poor | $$ |
| **Al-SiC** | 170-200 | 6-8 | Good | Poor | $$ |
| **Cu-W** | 180-200 | 6-8 | Excellent | Poor | $$$ |

### Failure Modes

**1. Leaks (Hermeticity)**
- **Standard:** <1×10⁻⁹ mbar·L/s He leak rate
- **Common locations:** Weld seams, fill tube, corners
- **Detection:** Helium mass spectrometer leak testing
- **Prevention:** Electron beam welding, proper joint design

**2. Fatigue Cracking**
- **Cause:** Thermal cycling stress
- **Critical locations:** Thin wall sections, weld HAZ
- **Life:** 10⁴-10⁶ cycles depending on stress amplitude
- **Mitigation:** Wall thickness optimization, stress relief

**3. Corrosion**
- **Internal:** Working fluid compatibility
- **External:** Ambient environment (salt, humidity)
- **Prevention:** Passivation, protective coatings

### CTE Considerations

The VC wall sees stress from:
1. **Internal:** TIM2 mismatch (17 vs 1 ppm/K)
2. **External:** TIM3 to heat sink (17 vs 23 ppm/K for Al)

Cu-Mo-Cu (CMC) laminates reduce external mismatch but add cost.

---

## Summary: Critical Interfaces

| Interface | Mismatch (ppm/K) | Risk Level | Mitigation |
|-----------|------------------|------------|------------|
| Device → TIM1 | 16 (w/o diamond) | HIGH | Use diamond interposer |
| Device → TIM1 | 3 (w/ diamond) | LOW | Diamond reduces mismatch |
| TIM1 → Diamond | 15 (Ag sinter) | MEDIUM | Porous sinter compliance |
| Diamond → TIM2 | 16 | HIGH | Graphite sheet compliance |
| TIM2 → VC Wall | 0-16 | MEDIUM | Material selection |
| VC → Heat Sink | 6 (Cu→Al) | LOW | Standard interface |

### Key Design Rules

1. **Minimize CTE steps:** Large jumps (>10 ppm/K) require compliant interfaces
2. **Use diamond strategically:** Reduces device-side mismatch significantly
3. **Invest in TIM1:** Highest impact on thermal performance
4. **Plan for cycling:** All interfaces degrade; design for maintenance or over-specify
5. **Test early:** Thermal cycling qualification on sub-assemblies

---

*Next: Layer 6-10 analysis (wick structures, working fluid, condenser, fins)*