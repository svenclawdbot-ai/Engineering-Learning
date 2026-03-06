---
layout: post
title: "NCG Management in Phase-Change Thermal Systems"
date: 2026-03-06 19:30:00 +0000
topic: "Thermal Systems"
tags: ["NCG", "non-condensable gas", "phase change", "thermal management", "vacuum", "degassing"]
summary: "Comprehensive guide to non-condensable gas (NCG) management in vapor chambers and heat pipes. Covers detection, prevention, removal strategies, and operational protocols for maintaining performance."
---

## The NCG Problem

Non-condensable gases (NCG) are the #1 performance killer in phase-change thermal systems. Even 1% NCG can reduce heat transfer by 50%.

### What is NCG?

Any gas that doesn't condense at operating temperatures:
- **Air** (N₂, O₂) — most common
- **Water vapor** — if system operated below dew point
- **Dissolved gases** — from manufacturing, materials
- **Decomposition products** — fluid breakdown over time

### Why NCG Destroys Performance

```
Without NCG:
[Hot vapor] → [Condenser wall] → [Liquid film] → [Cool surface]
        ↓              ↓
   Latent heat    Conductive heat transfer

With NCG:
[Hot vapor] → [NCG boundary layer] → [Condenser wall]
        ↓              ↓
   Blocked!       Must diffuse through stagnant gas
```

**The NCG blanket:**
- Accumulates near condenser (coolest point)
- Creates diffusion barrier
- Reduces effective condenser area
- Increases thermal resistance exponentially

---

## Quantifying NCG Impact

### Theoretical Model

NCG creates a partial pressure barrier:

$$
P_{total} = P_{vapor} + P_{NCG}
$$

At the condenser wall:
- Vapor partial pressure drops to saturation pressure at wall temperature
- NCG partial pressure increases
- Diffusion layer thickness: $\delta \propto \frac{1}{\sqrt{Re}}$

### Performance Degradation

| NCG Concentration | Heat Transfer Reduction | Effective Condenser Area |
|-------------------|------------------------|-------------------------|
| 0.1% | 10-15% | 90% |
| 0.5% | 30-40% | 60% |
| **1.0%** | **50-60%** | **40%** |
| 5.0% | 80-90% | 10% |
| 10%+ | >95% failure | <5% |

**Critical threshold:** 0.5-1.0% NCG for most systems

### Temperature Signature

NCG accumulation shows characteristic temperature profile:

```
Temperature along condenser:

Without NCG:        With NCG:
T ────────┐        T ────────┐
          │                  │      ┌── NCG front
          │        T_sat ────┼──────┘
          │                  │
T_wall ───┘        T_wall ───┘
    ↓                  ↓
[Uniform]            [Step change at NCG boundary]
```

The "NCG front" is visible as a sharp temperature drop where NCG blocks condensation.

---

## Sources of NCG

### Manufacturing Sources

| Source | Typical Amount | Prevention |
|--------|---------------|------------|
| Incomplete evacuation | 0.1-1% | Better vacuum pump, longer pump time |
| Trapped air in wick | 0.05-0.5% | Pre-fill with working fluid, vacuum impregnation |
| Outgassing from materials | 0.01-0.1% | Material baking, proper cleaning |
| Leaks during seal | 0.1-2% | Pressure testing, proper welding |
| Dissolved gases in fluid | 0.01-0.05% | Pre-degassing of fluid |

### Operational Sources

| Source | Mechanism | Rate |
|--------|-----------|------|
| **Permeation through walls** | Air diffuses through metal/plastic | 10⁻⁹-10⁻⁶ mbar·L/s |
| **Leaks at seals/joints** | Imperfect hermeticity | Variable |
| **Fluid decomposition** | Thermal/chemical breakdown | Temperature dependent |
| **Corrosion reactions** | Metal + fluid products | Material dependent |

### Fluid-Specific Decomposition

| Fluid | Decomposition Temp | Products | NCG Generation Rate |
|-------|-------------------|----------|-------------------|
| Water | >150°C | H₂, O₂ | Slow |
| Methanol | >80°C | CO, CO₂, H₂ | Moderate |
| Ammonia | >100°C | N₂, H₂ | Low |
| HFE-7100 | >150°C | CF₄, HF | Very low |
| Propane | >200°C | C₂H₄, CH₄ | Low |

---

## Detection Methods

### Method 1: Temperature Monitoring (Passive)

**Setup:** Thermocouples along condenser length

**Signature of NCG:**
- Sudden temperature drop at NCG front
- Steady-state temperature higher than design
- Poor temperature uniformity

**Advantages:**
- Simple, no additional hardware
- Real-time monitoring
- Can localize NCG accumulation

**Disadvantages:**
- Only detects significant NCG (>0.5%)
- Can't distinguish from other failures (dryout)
- Requires baseline data

**DIY Implementation:**
```python
# Simple NCG detection algorithm
if (T_condenser - T_wall) > 10K and flow_rate_normal:
    # Large ΔT suggests NCG blocking
    ncg_alert = True
```

### Method 2: Pressure Monitoring (Active)

**Setup:** Pressure transducer + temperature sensor

**Principle:**
- Measure total pressure (P_total)
- Calculate expected vapor pressure from temperature (P_sat)
- NCG partial pressure: P_NCG = P_total - P_sat

**Accuracy:** ±0.1% NCG with good sensors

**DIY Implementation:**
- Pressure sensor: MPX5700 ($10)
- Temperature: K-type thermocouple
- Arduino for logging

### Method 3: Gas Chromatography (Laboratory)

**Setup:** Sample port + GC analyzer

**Principle:** Separate and quantify gas components

**Accuracy:** ±0.01% NCG

**Limitations:**
- Requires sampling (system disruption)
- Expensive equipment ($5000+)
- Not for continuous monitoring

### Method 4: Acoustic/Electrical Methods (Advanced)

**Ultrasonic sensing:**
- NCG changes acoustic impedance
- Can detect bubbles/gas pockets
- Research stage for heat pipes

**Electrical conductivity:**
- NCG affects dielectric properties
- Indirect measurement
- Limited application

---

## Prevention Strategies

### Strategy 1: Proper Evacuation

**Vacuum Requirements:**

| Application | Target Pressure | Pump Type | Time Required |
|-------------|----------------|-----------|---------------|
| DIY/Lab | 10⁻² mbar | Rotary vane | 30-60 min |
| Industrial | 10⁻³ mbar | Two-stage rotary | 1-2 hours |
| **High-performance** | **10⁻⁴ mbar** | **Turbo/diffusion** | **2-4 hours** |
| Aerospace | 10⁻⁵ mbar | Ion pump | 4-8 hours |

**DIY Evacuation Protocol:**

```
1. Connect vacuum pump to fill valve
2. Pump down to <10 mbar (rough vacuum)
3. Heat system gently (40-50°C) to drive off volatiles
4. Continue pumping to <1 mbar
5. Cool to room temperature
6. Final pump to <0.1 mbar
7. Close valve, isolate system
8. Monitor pressure rise over 24 hours
   - <1 mbar rise = acceptable
   - >10 mbar rise = leak or outgassing
```

### Strategy 2: Materials Selection

**Low-Outgassing Materials:**

| Material | Outgassing Rate | Suitable For |
|----------|----------------|--------------|
| OFHC copper | Very low | High-performance |
| 316L stainless | Low | Industrial |
| Aluminum (6061) | Moderate | Consumer |
| Brass | Moderate | Avoid with water |
| Plastics | High | Avoid in vapor path |

**Surface Treatment:**
- Electropolishing: Reduces surface area, less adsorption
- Gold plating: Barrier layer
- Baking: 200°C for 4 hours before assembly

### Strategy 3: Working Fluid Purity

**Pre-treatment:**
- Distillation for water
- Degassing by freeze-pump-thaw cycles
- Chemical purification for organics

**DIY Degassing (Water):**
```
1. Freeze working fluid in container
2. Pump vacuum on headspace
3. Thaw slowly (trapped gas bubbles escape)
4. Repeat 3-5 cycles
5. Transfer to system under vacuum
```

### Strategy 4: Hermetic Sealing

**Seal Types:**

| Method | Leak Rate | Permanent? | DIY-Friendly? |
|--------|-----------|------------|---------------|
| **Pinch-off (copper tube)** | 10⁻⁹ mbar·L/s | Yes | Moderate |
| **Electron beam weld** | 10⁻¹⁰ mbar·L/s | Yes | No |
| **Solder seal** | 10⁻⁸ mbar·L/s | No | Yes |
| **Compression fitting** | 10⁻⁶ mbar·L/s | No | Yes |
| **Valve (Schrader)** | 10⁻⁷ mbar·L/s | No | Yes |

**DIY Best Practice:**
- Pinch-off for final seal
- Schrader valve for service access
- Pressure test before final seal

---

## Removal Strategies

### Passive Removal (No Hardware)

**1. Thermal Cycling**
- Heat system above normal operating temperature
- NCG expands, moves to condenser
- Cool quickly, NCG trapped in liquid
- Repeat 5-10 cycles

**Effectiveness:** Removes 20-50% of mobile NCG

**2. Cold Trap Method**
- Cool condenser end to very low temperature
- Working fluid condenses completely
- NCG concentrates at cold point
- Vent concentrated NCG

**Effectiveness:** Good for initial startup, limited for continuous operation

### Active Removal (Hardware Required)

**1. Gas Vent (Passive Valve)**

```
[Heat Pipe] ←── [Vent Valve] ←── [Cold Trap]
                     ↑
                [To atmosphere or recovery]
```

**Principle:** Permeable membrane or pressure-activated valve releases NCG while retaining working fluid

**Types:**
- Hydrophobic membrane (PTFE): Allows gas, blocks liquid
- Pressure relief valve: Opens at ΔP threshold
- Getter pump: Chemical absorption of gases

**DIY Implementation:**
- Small membrane module (~$20)
- Replaceable getter cartridge
- Manual or automatic venting

**2. Active Pumping System**

```
[System] ←── [Valve] ←── [Vacuum Pump]
              ↓
         [Pressure sensor]
```

**Operation:**
- Periodic pumping cycles (daily/weekly)
- Continuous monitoring
- Automated when NCG detected

**Effectiveness:** Can maintain <0.1% NCG indefinitely

**Cost:** $100-500 for DIY setup

**3. Liquid Nitrogen Cold Trap**

For laboratory/prototype systems:
- Condense all working fluid at one end
- NCG concentrates at warm end
- Pump out NCG with vacuum pump
- Remove cold trap, system restarts

**Effectiveness:** Removes 90%+ of NCG

**Frequency:** Monthly for research systems

---

## Operational Protocols

### Startup Protocol

```
1. Verify vacuum seal integrity (pressure check)
2. Gradual heat input (avoid thermal shock)
3. Monitor temperatures for NCG signature
4. If NCG detected, activate removal system
5. Continue startup once temperatures stabilize
```

### Normal Operation

```
1. Continuous temperature monitoring
2. Weekly pressure checks (if accessible)
3. Monthly visual inspection (if transparent)
4. Log any performance degradation
```

### Maintenance Schedule

| Interval | Action | Indicator of Need |
|----------|--------|-------------------|
| Daily | Temperature log | ΔT > 5K from baseline |
| Weekly | Pressure check | P > 2× baseline |
| Monthly | NCG purge | Performance drop >10% |
| Annually | Seal integrity test | Any pressure rise |
| 5 years | Complete refurbishment | Performance <70% |

---

## Design for NCG Tolerance

### Redundant Condenser Area

**Strategy:** Over-size condenser by 50-100%

**Benefit:** When NCG blocks 30% of area, still have sufficient capacity

**Trade-off:** Larger, heavier, more expensive

### Graded Condenser Design

```
Temperature gradient along condenser:

[Hot end]        [Gradual cooling]        [Cold end]
     │                   │                      │
   60°C ──────────────→ 40°C ──────────────→ 20°C
     │                   │                      │
     └─ NCG accumulates here, away from hot zone ─┘
```

**Benefit:** NCG pushed to cold end, hot zone remains active

### Multiple Vapor Chambers

Parallel redundant systems:
- If one degrades due to NCG, others compensate
- Individual units can be serviced
- Higher overall reliability

---

## DIY NCG Management System

### Components ($100-150 total)

| Component | Purpose | Cost |
|-----------|---------|------|
| Vacuum gauge | Monitor pressure | $30 |
| Mini vacuum pump | Active removal | $50 |
| Solenoid valve | Automated venting | $15 |
| Cold trap (optional) | Concentrate NCG | $20 |
| Controller (Arduino) | Automation | $10 |

### Simple Automated System

```
IF pressure > threshold AND temperature_gradient > normal:
    OPEN vent valve
    RUN vacuum pump for 30 seconds
    CLOSE valve
    LOG event
    
IF performance degradation > 20%:
    ALERT user
    SCHEDULE maintenance
```

### Manual Alternative

1. Monthly: Connect hand pump to vent valve
2. Pump for 2-3 minutes
3. Close valve
4. Log pressure before/after

---

## Summary: Best Practices

### For New Systems

1. **Proper evacuation:** <10⁻² mbar minimum
2. **Clean materials:** Low outgassing, baked
3. **Pure fluid:** Pre-degassed
4. **Hermetic seal:** Pinch-off or EB weld
5. **Initial test:** 24-hour pressure stability

### For Operating Systems

1. **Monitor continuously:** Temperature/pressure
2. **Act early:** At 0.5% performance drop
3. **Periodic purging:** Monthly for critical systems
4. **Log everything:** Trends predict failures
5. **Plan refurbishment:** Every 5-10 years

### For DIY Prototypes

1. **Accept some NCG:** 1-2% is manageable for learning
2. **Use getters:** Replaceable cartridges
3. **Design for access:** Service ports
4. **Test seals rigorously:** Before final fill
5. **Document baseline:** Performance when new

---

## Key Equations

**NCG partial pressure:**

$$
P_{NCG} = P_{total} - P_{sat}(T_{wall})
$$

**NCG concentration (ideal gas):**

$$
X_{NCG} = \frac{P_{NCG}}{P_{total}} = \frac{P_{NCG}}{P_{vapor} + P_{NCG}}
$$

**Diffusion-limited heat transfer:**

$$
q_{eff} = q_0 \cdot e^{-\alpha \cdot X_{NCG}}
$$

Where α ≈ 3-5 for typical systems

---

## References

1. Chi, "Heat Pipe Theory and Practice" (recovery from NCG)
2. Peterson, "An Introduction to Heat Pipes" (outgassing)
3. JPL Technical Reports (spacecraft NCG management)
4. ASHRAE Handbook (refrigeration system purging)

---

*Part of the thermal management research series. See related posts on vapor chamber design and jumping droplet condensation.*
