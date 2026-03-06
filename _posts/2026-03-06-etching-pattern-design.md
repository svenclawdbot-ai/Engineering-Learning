---
layout: post
title: "Etching Pattern Design: Micro-Channel Geometries for Thermal Management"
date: 2026-03-06 13:40:00 +0000
topic: "Thermal Systems"
tags: ["etching", "micro-channels", "wick design", "boiling enhancement", "CFD", "pattern design"]
summary: "Comprehensive guide to designing etched micro-channel patterns for evaporators, wicks, and condensers. Covers geometric parameters, flow dynamics, boiling enhancement, and practical design rules for DIY fabrication."
---

## Introduction to Micro-Channel Pattern Design

The geometry of etched channels directly impacts:
- **Heat transfer coefficient** (nucleation sites, surface area)
- **Pressure drop** (pumping power, flow distribution)
- **Critical heat flux** (CHF — dryout prevention)
- **Manufacturability** (etch time, aspect ratios)

This guide covers optimal patterns for different applications in DIY thermal management.

---

## 1. Fundamental Design Parameters

### Key Geometric Variables

| Parameter | Symbol | Typical Range | Impact |
|-----------|--------|---------------|--------|
| **Channel width** | $w_c$ | 50-1000 μm | Flow resistance, nucleation |
| **Channel depth** | $h_c$ | 50-500 μm | Heat transfer, pressure drop |
| **Rib width** | $w_r$ | 50-500 μm | Structural integrity |
| **Aspect ratio** | $AR = h_c/w_c$ | 0.5-4 | Manufacturability |
| **Hydraulic diameter** | $D_h = 4A/P$ | 50-800 μm | Flow regime |

### Hydraulic Diameter Calculation

For rectangular channels:

$$
D_h = \frac{4wh}{2(w+h)} = \frac{2wh}{w+h}
$$

**Example:**
- Channel: 200 μm wide × 300 μm deep
- $D_h = 2×200×300/(200+300) = 240$ μm

### Flow Regime Determination

**Reynolds number:**

$$
Re = \frac{\rho v D_h}{\mu}
$$

| Flow Regime | Re Range | Characteristics |
|-------------|----------|-----------------|
| **Laminar** | < 2300 | Smooth, predictable |
| **Transitional** | 2300-4000 | Unsteady |
| **Turbulent** | > 4000 | Enhanced mixing |

**For micro-channels:** Typically laminar (Re < 1000)

---

## 2. Pattern Types by Application

### 2.1 Parallel Straight Channels

**Best for:** Liquid cooling, low pressure drop

```
← Inlet
╔═══════════════════════════════════════╗
║  ═══  ═══  ═══  ═══  ═══  ═══  ═══  ║
║  ═══  ═══  ═══  ═══  ═══  ═══  ═══  ║
║  ═══  ═══  ═══  ═══  ═══  ═══  ═══  ║
║  ═══  ═══  ═══  ═══  ═══  ═══  ═══  ║
╚═══════════════════════════════════════╝
→ Outlet
```

**Design Rules:**
- Width: 200-500 μm
- Depth: 200-400 μm  
- Rib width: 100-200 μm (structural)
- Aspect ratio: 1-2

**Advantages:**
- Simple to design and fabricate
- Predictable flow distribution
- Low pressure drop

**Disadvantages:**
- Limited surface enhancement
- Poor for boiling (vapor blocks flow)
- Flow maldistribution if inlet/outlet not designed

**Pressure drop estimate:**
```
ΔP/L = 32μv/D_h² (laminar)

Example:
- Water, v = 0.5 m/s, D_h = 300 μm
- ΔP/L ≈ 0.1 bar/m
```

---

### 2.2 Radial Channels

**Best for:** Thermosyphon evaporators, axisymmetric heat sources

```
         Outlet
           ↑
    ╭─────────────╮
   ╱   ╱│╲   ╱│╲   ╲
  │   ╱ │ ╲ ╱ │ ╲   │
  │  ╱  │  ╳  │  ╲  │
  │ ╱   │ ╱ ╲ │   ╲ │  ← Center heat input
  │╱    │╱   ╲│    ╲│
   ╲    │     │    ╱
    ╰─────────────╯
```

**Design Rules:**
- Channels widen toward periphery (area expansion)
- Width gradient: 100 μm (center) → 500 μm (edge)
- Depth: Constant 200-300 μm
- Number of channels: 8-16 (depends on diameter)

**Advantages:**
- Natural flow path for vapor (outward)
- Good for pool boiling
- Accommodates circular heat sources

**Disadvantages:**
- Complex to model (2D flow)
- Flow distribution depends on orientation (gravity)
- Requires large diameter (min 20mm effective)

**Critical consideration:** Vapor must have escape path. Include larger vapor channels between liquid channels.

---

### 2.3 Grid/Interconnected Network

**Best for:** Wick structures, boiling enhancement, thermal spreading

```
╔════╦════╦════╦════╦════╗
║    ║    ║    ║    ║    ║
╠════╬════╬════╬════╬════╣
║    ║    ║    ║    ║    ║
╠════╬════╬════╬════╬════╣
║    ║    ║    ║    ║    ║
╠════╬════╬════╬════╬════╣
║    ║    ║    ║    ║    ║
╚════╩════╩════╩════╩════╝
```

**Design Rules:**
- Cell size: 200-1000 μm
- Channel width: 50-200 μm (narrow for wicking)
- Depth: 100-300 μm
- Open ends for fluid supply

**Advantages:**
- Excellent capillary action (wicking)
- Redundant flow paths (fault tolerant)
- High surface area for boiling

**Disadvantages:**
- Highest pressure drop
- Complex flow modeling
- Manufacturing: intersections are stress concentrators

**For wick structures:**
- Smaller channels (50-100 μm) for capillary pressure
- Connected to liquid reservoir
- Vapor escapes through larger channels above

---

### 2.4 Pin Fin Arrays

**Best for:** Boiling enhancement, compact heat exchangers

```
    ○   ○   ○   ○   ○
  ○   ○   ○   ○   ○   ○
    ○   ○   ○   ○   ○
  ○   ○   ○   ○   ○   ○
    ○   ○   ○   ○   ○
```

**Design Rules:**
- Pin diameter: 100-500 μm
- Pitch: 200-1000 μm (2-4× diameter)
- Height: 200-600 μm
- Staggered arrangement (better mixing)

**Advantages:**
- Maximum surface area
- Excellent for nucleate boiling
- Tortuous flow enhances mixing
- Structural robustness

**Disadvantages:**
- Highest pressure drop
- Difficult to etch uniformly
- Risk of pin collapse if too tall

**Etching consideration:** Undercutting can cause pin collapse. Limit aspect ratio (height/diameter) < 3.

---

### 2.5 Bi-Porous Structures

**Best for:** High heat flux boiling (separate liquid/vapor paths)

```
Liquid Channels          Vapor Channels
 (small pores)           (large pores)

   ≋≋≋≋≋≋≋≋≋≋≋≋≋≋       ◯  ◯  ◯  ◯  ◯
   ≋≋≋≋≋≋≋≋≋≋≋≋≋≋       ◯  ◯  ◯  ◯  ◯
   ≋≋≋≋≋≋≋≋≋≋≋≋≋≋       ◯  ◯  ◯  ◯  ◯
   ≋≋≋≋≋≋≋≋≋≋≋≋≋≋       ◯  ◯  ◯  ◯  ◯
   ≋≋≋≋≋≋≋≋≋≋≋≋≋≋       ◯  ◯  ◯  ◯  ◯
```

**Design Rules:**
- Small pores: 50-150 μm (capillary)
- Large pores: 300-800 μm (vapor escape)
- Ratio: 2-4 small per 1 large
- Interconnected at base

**Mechanism:**
1. Liquid feeds through small channels
2. Boiling occurs at heated surface
3. Vapor escapes through large channels
4. Prevents vapor blocking (enhances CHF)

**Advantages:**
- Separate liquid/vapor paths
- Highest CHF performance
- Self-regulating

**Disadvantages:**
- Complex to design
- Critical pore size distribution
- Challenging to fabricate

---

### 2.6 Re-Entrant Cavities

**Best for:** Boiling nucleation enhancement

```
Cross-section view:

Normal channel:        Re-entrant cavity:
    │                       ╭──╮
    │                       │  │
    │                       ╰──╯
    │                          │
```

**Design:**
- Cavity mouth: 20-100 μm
- Cavity depth: 50-200 μm
- Array spacing: 100-500 μm

**Mechanism:**
- Trapped vapor/seed bubbles
- Reduces superheat for nucleation
- Promotes early boiling onset

**Fabrication:**
- Difficult with standard etching
- Requires side-wall passivation
- Alternative: laser drilling + etching

---

## 3. Application-Specific Designs

### 3.1 Thermosyphon Evaporator

**Requirements:**
- Pool boiling (gravity return)
- Vapor escape paths
- Nucleation enhancement

**Recommended pattern:**
```
         [Vapor outlet]
              ↑
    ╭───────────────────╮
   ╱  ════  ◯  ════  ◯  ╲   ← Vapor channels (large)
  │   ════  ◯  ════  ◯   │
  │   ════  ◯  ════  ◯   │
  │   ════  ◯  ════  ◯   │  ← Liquid channels (radial)
  │   ════  ◯  ════  ◯   │
   ╲  ════  ◯  ════  ◯  ╱
    ╰───────────────────╯
              ↓
         [Liquid pool]
```

**Parameters:**
- Liquid channels: 200 μm wide, 300 μm deep
- Vapor channels: 500 μm wide, 400 μm deep
- Radial layout (center heat input)
- Area ratio: 70% liquid, 30% vapor

### 3.2 Heat Pipe Wick

**Requirements:**
- Capillary pressure for liquid return
- Small pore size
- Connected network

**Recommended pattern:** Grid with gradient
```
Evaporator          Transport           Condenser
 (small pores)      (medium)            (large pores)

≋≋≋≋≋≋≋≋≋≋≋≋ → ≋≋≋≋≋≋≋≋≋≋ → ≋≋≋≋≋≋≋≋≋≋
≋≋≋≋≋≋≋≋≋≋≋≋ → ≋≋≋≋≋≋≋≋≋≋ → ≋≋≋≋≋≋≋≋≋≋
≋≋≋≋≋≋≋≋≋≋≋≋ → ≋≋≋≋≋≋≋≋≋≋ → ≋≋≋≋≋≋≋≋≋≋

≋ = 50-100 μm      ≋ = 100-200 μm     ≋ = 200-400 μm
```

**Gradient reasoning:**
- Evaporator: Small pores → high capillary pressure
- Condenser: Large pores → low flow resistance
- Compromise in transport section

### 3.3 Jumping Droplet Condenser

**Requirements:**
- Superhydrophobic surface
- Droplet removal
- Minimal liquid retention

**Pattern:** Minimal texture (smooth with nano-features)
```
Actually: DON'T etch deep channels

Instead:
- Smooth condenser surface (Ra < 100 nm)
- Nanowires or pillars (5-20 μm tall, 100-500 nm diameter)
- Spacing: 1-5 μm
- Coating: Hydrophobic (FDTS, etc.)
```

**Key:** The "texture" is nanoscale — etched micro-channels would trap liquid.

---

## 4. Design Calculations

### 4.1 Pressure Drop in Micro-Channels

**Laminar flow (most micro-channels):**

For rectangular channels, friction factor:

$$
f \cdot Re = 96 \left(1 - 1.3553\alpha + 1.9467\alpha^2 - 1.7012\alpha^3 + 0.9564\alpha^4 - 0.2537\alpha^5\right)
$$

Where $\alpha = h/w$ (height/width, \u003c 1)

**Simplified (approximate):**
```
f ≈ 64/Re (circular approximation)
ΔP = f × (L/D_h) × (ρv²/2)
```

**Example calculation:**
- Channel: 200×300 μm, L = 20 mm
- Water at 0.5 m/s, 25°C
- D_h = 240 μm
- Re = 120 (laminar)
- f = 64/120 = 0.53
- ΔP = 0.53 × (0.02/0.00024) × (1000×0.5²/2) = 11,000 Pa = 0.11 bar

### 4.2 Capillary Pressure (for Wick Design)

**Laplace pressure:**

$$
\Delta P_{cap} = \frac{2\sigma \cos\theta}{r}
$$

Where:
- σ = surface tension (0.072 N/m for water)
- θ = contact angle (0° for wetting)
- r = pore radius

**Example:**
- 100 μm channel (r = 50 μm = 5×10⁻⁵ m)
- ΔP_cap = 2 × 0.072 × 1 / (5×10⁻⁵) = **2880 Pa**

**Can overcome:** ~30 mm water head

### 4.3 Surface Area Enhancement

**Flat plate:** $A_0 = L × W$

**With channels:** $A_{total} = A_0 × (1 + 2h/(w+s))$

Where:
- h = channel depth
- w = channel width
- s = rib width (land)

**Example:**
- Channels: 200 μm wide × 300 μm deep
- Rib: 200 μm
- Enhancement: 1 + 2×300/(200+200) = **2.5× surface area**

---

## 5. Fabrication Constraints

### 5.1 Etching Limitations

**Minimum feature size:** ~50 μm (limited by mask resolution)

**Maximum aspect ratio:** ~3:1 (depth:width)
- Higher AR → undercutting, non-uniform etch
- Solution: Multiple etch cycles with mask refresh

**Etch uniformity:** ±10-20% typical
- Deeper etches less uniform
- Agitation helps
- Temperature control critical

### 5.2 Design Rules for DIY Etching

| Parameter | Conservative | Aggressive |
|-----------|--------------|------------|
| Minimum width | 100 μm | 50 μm |
| Minimum rib | 100 μm | 50 μm |
| Max aspect ratio | 2:1 | 4:1 |
| Feature spacing | 2× width | 1× width |
| Corner radius | 50 μm | 25 μm |

**Etch time estimation:**
```
Time = Desired depth / Etch rate

Ferric chloride @ 40°C: ~15 μm/hour
Electrochemical: ~10 μm/hour
Deep etch (500 μm): 30-50 hours!
```

### 5.3 Mask Design Tips

**Positive vs negative mask:**
- **Positive:** Channels = exposed copper (etch away)
- **Negative:** Channels = masked (keep copper)
- Use **positive** for most designs

**Compensation for undercutting:**
- Etch spreads laterally ~30-50% of depth
- Make channels narrower in design by ~20%

**Corner rounding:**
- Sharp corners = stress concentrators
- Add 25-50 μm radius to all corners

---

## 6. Optimization Workflows

### 6.1 For Maximum Heat Transfer

1. Maximize surface area → grid or pin fins
2. Minimize hydraulic diameter → more nucleation sites
3. Include vapor escape paths → bi-porous design
4. Limit pressure drop → optimize L/D_h ratio

**Trade-off:** Surface area ↑ = Pressure drop ↑↑

### 6.2 For Minimum Pressure Drop

1. Large hydraulic diameter → parallel straight channels
2. Short length → compact design
3. Smooth walls → minimize roughness
4. Gradual expansions/contractions

### 6.3 For CHF Enhancement

1. Bi-porous structure (separate liquid/vapor paths)
2. Re-entrant cavities (nucleation sites)
3. Surface roughness (Ra = 1-10 μm)
4. Adequate wick thickness (capillary limit)

---

## 7. Example Design Files

### 7.1 Simple Parallel Channels (SVG)

```svg
<svg width="100mm" height="20mm" viewBox="0 0 100 20">
  <!-- 10 channels, 200μm wide, 200μm spacing -->
  <rect x="0" y="0" width="0.2" height="20" fill="black"/>
  <rect x="4" y="0" width="0.2" height="20" fill="black"/>
  <rect x="8" y="0" width="0.2" height="20" fill="black"/>
  <rect x="12" y="0" width="0.2" height="20" fill="black"/>
  <rect x="16" y="0" width="0.2" height="20" fill="black"/>
  <rect x="20" y="0" width="0.2" height="20" fill="black"/>
  <rect x="24" y="0" width="0.2" height="20" fill="black"/>
  <rect x="28" y="0" width="0.2" height="20" fill="black"/>
  <rect x="32" y="0" width="0.2" height="20" fill="black"/>
  <rect x="36" y="0" width="0.2" height="20" fill="black"/>
</svg>
```

### 7.2 Design Software

**Free options:**
- **Inkscape:** Vector graphics → print masks
- **Fusion 360:** CAD → export SVG
- **KiCad:** PCB design → etching patterns
- **Python + Matplotlib:** Parametric generation

**Parametric Python example:**
```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_grid_channels(nx, ny, width, pitch, length):
    fig, ax = plt.subplots()
    
    for i in range(nx):
        for j in range(ny):
            x = i * pitch
            y = j * pitch
            rect = patches.Rectangle((x, y), width, length, 
                                      linewidth=1, edgecolor='black', 
                                      facecolor='black')
            ax.add_patch(rect)
    
    ax.set_xlim(0, nx*pitch)
    ax.set_ylim(0, ny*pitch)
    ax.set_aspect('equal')
    plt.savefig('grid_pattern.svg')
    
generate_grid_channels(20, 20, 0.1, 0.5, 20)  # 100μm channels, 500μm pitch
```

---

## 8. Testing and Validation

### 8.1 Visual Inspection

**Check for:**
- Channel width uniformity (±10% tolerance)
- Depth consistency (cross-section samples)
- No blocked channels
- Clean mask removal

**Tools:**
- USB microscope ($30-50)
- Caliper depth gauge
- Cross-section: Cut, polish, photograph

### 8.2 Flow Testing

**Procedure:**
1. Block one end of channels
2. Fill with colored water
3. Check for uniform fill
4. Apply pressure, measure flow rate
5. Compare to theoretical (Poiseuille flow)

**Red flags:**
- Partial filling = blocked channels
- Asymmetric flow = uneven etching
- Low flow = insufficient depth

### 8.3 Thermal Testing

**Setup:**
- Mount heater on back side
- Thermocouples or IR camera on front
- Insulate sides (1D heat flow)

**Metrics:**
- Temperature uniformity
- Heat transfer coefficient
- Pressure drop vs flow rate

---

## 9. Common Design Mistakes

| Mistake | Consequence | Solution |
|---------|-------------|----------|
| **Channels too narrow** | Excessive pressure drop | Minimum 100 μm for DIY |
| **Aspect ratio too high** | Collapse, non-uniform etch | Keep AR < 3 |
| **No vapor escape** | CHF limitation, dryout | Bi-porous design |
| **Sharp corners** | Stress cracks | Add radii >25 μm |
| **Inadequate inlet/outlet** | Flow maldistribution | Plenum design |
| **Ignoring gravity** | Pool boiling fails | Thermosyphon orientation |

---

## 10. Quick Reference Charts

### Channel Sizing by Application

| Application | Width (μm) | Depth (μm) | Pitch (μm) | Pattern |
|-------------|------------|------------|------------|---------|
| **Liquid cooling (water)** | 300-500 | 300-500 | 600-1000 | Parallel |
| **Liquid cooling (dielectric)** | 200-400 | 200-400 | 400-800 | Parallel |
| **Boiling enhancement** | 100-300 | 150-300 | 400-600 | Grid/Pins |
| **Wick (capillary)** | 50-150 | 100-200 | 200-400 | Grid |
| **Vapor venting** | 500-1000 | 300-600 | 800-1500 | Radial |
| **Thermosyphon** | 200-400 | 300-500 | 600-1000 | Radial |

### Expected Performance

| Pattern | Enhancement | Pressure Drop | CHF | Fabrication |
|---------|-------------|---------------|-----|-------------|
| Smooth | 1× | Low | Low | Trivial |
| Parallel | 1.5-2× | Low | Medium | Easy |
| Grid | 2.5-4× | Medium | High | Medium |
| Pin fins | 3-5× | High | Very high | Hard |
| Bi-porous | 4-7× | Medium | Very high | Very hard |

---

*Start with parallel channels for first prototype. Iterate based on testing.*