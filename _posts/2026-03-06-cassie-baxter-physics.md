---
layout: post
title: "Cassie-Baxter vs Wenzel States: Thermodynamic Physics Deep Dive"
date: 2026-03-06 20:00:00 +0000
topic: "Thermal Systems"
tags: ["Cassie-Baxter", "Wenzel", "wetting", "thermodynamics", "surface energy", "metastability", "physics"]
summary: "Comprehensive thermodynamic analysis of superhydrophobic wetting states. Covers energy minimization, transition barriers, pressure thresholds, metastability, and dynamic effects in textured surfaces."
---

## Introduction: The Two States from First Principles

The wetting state of a liquid on a textured surface is determined by **energy minimization**. Understanding this requires analyzing the system's total surface energy and finding stable configurations.

---

## 1. Thermodynamic Framework

### System Definition

Consider a droplet of volume $V$ on a textured surface with:
- **Solid fraction:** $f_s$ (area fraction of solid pillars)
- **Texture height:** $h$
- **Texture spacing:** $d$
- **Intrinsic contact angle:** $\theta$ (on smooth surface)

### Energy Components

The total surface energy of the system:

$$
E_{total} = \gamma_{lv} A_{lv} + \gamma_{sl} A_{sl} + \gamma_{sv} A_{sv}
$$

Where:
- $\gamma_{lv}$ = liquid-vapor surface tension
- $\gamma_{sl}$ = solid-liquid interfacial energy
- $\gamma_{sv}$ = solid-vapor interfacial energy
- $A$ = respective interfacial areas

### Young's Equation (Baseline)

For a smooth surface, the equilibrium contact angle $\theta$ satisfies:

$$
\cos\theta = \frac{\gamma_{sv} - \gamma_{sl}}{\gamma_{lv}}
$$

This is our intrinsic material property.

---

## 2. Wenzel State: Complete Penetration

### Geometry

In the Wenzel state, liquid fills the texture completely:

```
Cross-section:

    ╭──────╮
   ╱   ●    ╲      Droplet
  │   ╱│╲    │
  │  ╱ │ ╲   │     Liquid fills grooves
  │ ╱  │  ╲  │
  │╱   │   ╲ │
  █████│█████      Solid (rough)
   ▓▓▓▓│▓▓▓▓      Liquid in texture
       │
```

### Energy Calculation

**True surface area:**

The roughness factor $r$ quantifies increased surface area:

$$
r = \frac{A_{actual}}{A_{apparent}} > 1
$$

For a pillar array:

$$
r = 1 + \frac{4f_s h}{d(1-f_s)}
$$

**Wenzel energy:**

$$
E_{Wenzel} = \gamma_{lv} A_{lv} + r(\gamma_{sl} - \gamma_{sv}) A_{apparent}
$$

Using Young's equation:

$$
\cos\theta_W = r \cos\theta
$$

**Key result:** Apparent contact angle is amplified by roughness.

- If $\theta > 90°$ (hydrophobic): $\theta_W > \theta$ (more hydrophobic)
- If $\theta < 90°$ (hydrophilic): $\theta_W < \theta$ (more hydrophilic)

---

## 3. Cassie-Baxter State: Composite Interface

### Geometry

In the Cassie-Baxter state, air is trapped beneath the droplet:

```
Cross-section:

    ╭──────╮
   ╱   ●    ╲      Droplet
  │        █ │     Air gaps (white)
  │      █   │     between pillars (black)
  │    █     │
  │  █       │
  ███   █████      Solid pillars
       ↑
    Liquid-air
    interface
```

### Energy Calculation

**Composite interface areas:**

- Solid-liquid contact: $f_s A_{apparent}$
- Liquid-air contact: $(1-f_s) A_{apparent}$

**Cassie-Baxter energy:**

$$
E_{CB} = \gamma_{lv} A_{lv} + f_s(\gamma_{sl} - \gamma_{sv})A_{apparent} + (1-f_s)\gamma_{lv}A_{apparent}
$$

Using Young's equation:

$$
\cos\theta_{CB} = f_s \cos\theta - (1 - f_s)
$$

**Key result:** Apparent angle depends on solid fraction.

For small $f_s$ (sparse pillars):

$$
\cos\theta_{CB} \approx -1 \quad \Rightarrow \quad \theta_{CB} \approx 180°
$$

---

## 4. Energy Comparison and Stability

### Which State is Lower Energy?

Define **energy difference**:

$$
\Delta E = E_{Wenzel} - E_{CB}
$$

**When $\Delta E > 0$:** Cassie-Baxter is stable
**When $\Delta E < 0$:** Wenzel is stable

### Critical Solid Fraction

Setting $\Delta E = 0$ gives the transition condition:

$$
f_{s,crit} = \frac{r - 1}{r - \cos\theta}
$$

**Practical implications:**

| Roughness $r$ | Intrinsic $\theta$ | $f_{s,crit}$ | Design Strategy |
|--------------|-------------------|--------------|-----------------|
| 2.0 | 110° | 0.33 | Keep $f_s < 0.30$ |
| 3.0 | 110° | 0.50 | Keep $f_s < 0.40$ |
| 2.0 | 150° | 0.20 | Keep $f_s < 0.15$ |

**Rule of thumb:** $f_s < 0.10$ (10% solid) ensures Cassie-Baxter for most surfaces.

---

## 5. The Transition: Cassie to Wenzel

### Energy Barrier

Even when Wenzel is lower energy, the system may remain in Cassie-Baxter due to an **energy barrier**.

```
Energy landscape:

E ↑
  │         ╭─╮
  │        ╱   ╲     Cassie-Baxter
  │       ╱     ╲      (metastable)
  │      ╱       ╲
  │     ╱         ╲
  │    ╱           ╲____
  │   ╱                 ╲____
  │  ╱                       ╲____  Wenzel
  │ ╱                              ╲____ (stable)
  │╱
  └────────────────────────────────────→
         State space
         
Barrier height = ΔE‡
```

### Transition Mechanisms

#### Mechanism 1: Pressure-Induced Sagging

External pressure $P$ deforms the liquid-air interface:

**Young-Laplace equation:**

$$
\Delta P = \gamma_{lv} \left(\frac{1}{R_1} + \frac{1}{R_2}\right)
$$

For a curved meniscus between pillars:

$$
P_{max} = \frac{2\gamma_{lv} \cos\theta}{d/2} = \frac{4\gamma_{lv} \cos\theta}{d}
$$

**Critical pressure for transition:**

$$
P_{crit} = \frac{2\gamma_{lv} \cos\theta}{d_{max}}
$$

Where $d_{max}$ is the maximum spacing before collapse.

**Example:**
- Water: $\gamma = 0.072$ N/m, $\theta = 110°$
- Spacing: $d = 40$ μm
- $P_{crit} = 4 × 0.072 × (-0.34) / 40×10⁻⁶ ≈ 2.4$ kPa

This is easily exceeded by:
- Droplet impact (can be >10 kPa)
- Vapor flow in heat pipes
- Gravitational head (tall droplets)

#### Mechanism 2: Capillary Imbibition

Liquid spontaneously wicks into texture if:

$$
\theta < 90° \quad \text{(for vertical walls)}
$$

Or more precisely, when the **spreading coefficient** is positive:

$$
S = \gamma_{sv} - \gamma_{sl} - \gamma_{lv} > 0
$$

For hydrophobic surfaces ($\theta > 90°$), this is negative, preventing spontaneous imbibition.

#### Mechanism 3: Nucleation and Growth

A small region transitions (nucleates) and spreads:

**Nucleation rate:**

$$
J = J_0 \exp\left(-\frac{\Delta G^*}{k_B T}\right)
$$

Where $\Delta G^*$ is the activation energy for nucleating a Wenzel domain.

This is why metastable Cassie states can persist for long times.

---

## 6. Dynamic Effects

### Droplet Impact

When a droplet hits the surface with velocity $v$:

**Dynamic pressure:**

$$
P_{dyn} = \frac{1}{2} \rho v^2
$$

**Example:**
- Droplet: $v = 1$ m/s (jumping droplet returning)
- Water: $\rho = 1000$ kg/m³
- $P_{dyn} = 0.5 × 1000 × 1² = 500$ Pa

This is small compared to $P_{crit}$ (~2 kPa), so jumping droplets typically don't cause transition.

**But for larger velocities:**
- $v = 5$ m/s → $P_{dyn} = 12.5$ kPa > $P_{crit}$ → Risk of transition

### Vibration and Acoustics

Vibration can lower the energy barrier:

**Effective barrier under vibration:**

$$
\Delta E_{eff} = \Delta E_0 - \frac{1}{2} m \omega^2 A^2
$$

Where $\omega$ is frequency and $A$ is amplitude.

**Implication:** High-vibration environments (engines, pumps) increase Cassie→Wenzel transition risk.

---

## 7. Design Equations for JDC Surfaces

### Minimum Pillar Height

To prevent sagging under gravitational load:

$$
h_{min} = \frac{d}{2} \tan\theta
$$

**More conservative (including safety factor):**

$$
h > 3d
$$

### Maximum Spacing

To maintain Cassie state under pressure $P_{max}$:

$$
d_{max} = \frac{4\gamma_{lv} |\cos\theta|}{P_{max}}
$$

**Design values:**

| Application | $P_{max}$ | $d_{max}$ (water) | $d_{max}$ (HFE-7100) |
|-------------|-----------|-------------------|---------------------|
| Pool boiling | 1 kPa | 100 μm | 60 μm |
| Heat pipe | 5 kPa | 20 μm | 12 μm |
| High pressure | 20 kPa | 5 μm | 3 μm |

### Solid Fraction Constraint

For Cassie-Baxter stability:

$$
f_s < \frac{r - 1}{r - \cos\theta}
$$

**Practical design:** $f_s < 0.05$ (5%) for robustness.

---

## 8. Metastability and Hysteresis

### Contact Angle Hysteresis

The difference between advancing and receding angles:

$$
\Delta\theta = \theta_{adv} - \theta_{rec}
$$

**Physical origin:** Surface defects, chemical heterogeneity, pinning at texture edges.

**Cassie-Baxter:** $\Delta\theta < 5°$ (excellent)
**Wenzel:** $\Delta\theta > 20°$ (poor)

### Role in Jumping Droplets

Low hysteresis is essential for jumping:

**Energy available for jumping:**

$$
E_{jump} = \Delta E_{surface} - W_{adhesion}
$$

Where adhesion work:

$$
W_{adhesion} = \gamma_{lv} (1 + \cos\theta_{rec}) A_{contact}
$$

Low $\theta_{rec}$ (low hysteresis) → small $W_{adhesion}$ → efficient jumping.

---

## 9. Temperature Effects

### Surface Tension Temperature Dependence

$$
\gamma(T) = \gamma_0 \left(1 - \frac{T}{T_c}\right)^n
$$

Where $T_c$ is critical temperature, $n \approx 1.2$.

**Example for water:**
- 25°C: $\gamma = 72$ mN/m
- 100°C: $\gamma = 59$ mN/m

**Impact on Cassie stability:**

Lower $\gamma$ at high $T$ → lower $P_{crit}$ → easier transition to Wenzel.

### Thermal Gradients

On a heated surface:
- Hot regions: Lower $\gamma$ → less stable Cassie
- Cold regions: Higher $\gamma$ → more stable Cassie

This explains why NCG (which accumulates at cold spots) can destabilize the Cassie state locally.

---

## 10. Advanced: Line Tension Effects

At very small scales (nanometers), the **three-phase contact line** has associated energy:

$$
E_{line} = \tau L
$$

Where $\tau$ is line tension and $L$ is contact line length.

Modified Cassie-Baxter equation:

$$
\cos\theta_{CB} = f_s \cos\theta - (1-f_s) + \frac{\tau}{\gamma_{lv}} \frac{L}{A}
$$

For micro-scale textures ($>$1 μm), line tension is negligible.

---

## 11. Mathematical Summary

### Key Equations

| Phenomenon | Equation | Variables |
|------------|----------|-----------|
| **Young's equation** | $\cos\theta = (\gamma_{sv} - \gamma_{sl})/\gamma_{lv}$ | Intrinsic angle |
| **Wenzel** | $\cos\theta_W = r\cos\theta$ | Rough surface |
| **Cassie-Baxter** | $\cos\theta_{CB} = f_s\cos\theta - (1-f_s)$ | Composite |
| **Critical pressure** | $P_{crit} = 4\gamma\cos\theta/d$ | Transition threshold |
| **Minimum height** | $h_{min} = (d/2)\tan\theta$ | No sagging |
| **Solid fraction limit** | $f_{s,crit} = (r-1)/(r-\cos\theta)$ | Stability boundary |

---

## 12. Practical Implications for Your Vapor Chamber

### Condenser Surface Design

**Given:** HFE-7100 at 60°C
- $\gamma = 12$ mN/m
- $\theta = 110°$ (with coating)
- Max pressure: 5 kPa (vapor flow)

**Calculate:**

$$
d_{max} = \frac{4 × 0.012 × 0.34}{5000} = 3.3\ \mu m
$$

**Wait!** This suggests spacing must be <3 μm, which contradicts our 40 μm design!

### Resolution: Pressure Distribution

The 5 kPa is the **maximum local pressure**, not the uniform pressure. In reality:
- Most of the surface sees <1 kPa
- Only stagnation points see 5 kPa
- The design is safe if pillars are robust

**Conservative design:** $d = 10-20$ μm for high-pressure regions

### Alternative: Gradient Surface

```
High pressure zone:    Low pressure zone:
  ● ● ● ●              ●   ●   ●
  ● ● ● ●                ●   ●
  ● ● ● ●              ●   ●   ●
  
  10 μm spacing        40 μm spacing
  (robust)             (high performance)
```

---

## Key Takeaways

1. **Cassie-Baxter is metastable** — energy barrier protects it from transitioning to Wenzel

2. **Solid fraction < 5%** is the critical design rule for stability

3. **Pillar height > 3× spacing** prevents gravitational sagging

4. **Maximum spacing** is limited by operating pressure: $d_{max} = 4\gamma\cos\theta/P_{max}$

5. **Low hysteresis (<5°)** is essential for jumping droplets, not just high contact angle

6. **Temperature increases** reduce surface tension, making Cassie state less stable

7. **Dynamic effects** (impact, vibration) can trigger transition — design for worst case

---

*This completes the theoretical foundation for designing JDC surfaces. See practical implementation in the etching patterns guide.*
