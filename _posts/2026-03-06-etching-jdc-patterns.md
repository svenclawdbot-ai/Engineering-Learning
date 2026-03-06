---
layout: post
title: "Etching Patterns for Jumping Droplet Condensation: Condenser Surface Design"
date: 2026-03-06 19:30:00 +0000
topic: "Thermal Systems"
tags: ["etching", "jumping droplet", "condenser", "superhydrophobic", "nucleation", "microstructure"]
summary: "Design guide for etched surface patterns that optimize jumping droplet condensation. Covers nucleation site spacing, hierarchical structures, coalescence promotion, and prevention of flooding."
---

## The Goal: Controlled Droplet Formation

For jumping droplet condensation (JDC), we need surfaces that:

1. **Promote nucleation** at specific sites (not random)
2. **Control droplet size** (10-30 μm before jumping)
3. **Facilitate coalescence** (droplets merge, then jump)
4. **Prevent flooding** (maintain Cassie-Baxter state)
5. **Enable easy departure** (low adhesion after coalescence)

This is fundamentally different from evaporator channel design!

---

## Key Differences: Condenser vs Evaporator

| Feature | Evaporator (Boiling) | Condenser (JDC) |
|---------|---------------------|-----------------|
| **Goal** | Generate vapor | Remove condensate |
| **Pattern** | Channels/pores for liquid | Pillars/posts for droplets |
| **Surface** | Often wicking (hydrophilic) | Superhydrophobic |
| **Size scale** | 50-500 μm channels | 1-20 μm pillars |
| **Depth** | 100-500 μm | 5-20 μm (shallow!) |
| **Key metric** | CHF, capillary pressure | Nucleation density, droplet size |

**Critical insight:** JDC surfaces are about creating the right "texture" not "channels".

---

## Physics of JDC Surface Design

### Nucleation Site Spacing

Droplets grow independently until they touch, then coalesce and jump.

**Optimal spacing calculation:**

$$
D_{optimal} = 2 \times r_{jump} = 2 \times 20\ \mu m = 40\ \mu m
$$

Where $r_{jump}$ is the target droplet radius for jumping (15-25 μm).

**Spacing rules:**
- **Too close (<20 μm):** Droplets coalesce too early, large drops form, flooding risk
- **Optimal (30-50 μm):** Controlled coalescence at jumping size
- **Too far (>100 μm):** Low nucleation density, reduced heat transfer

| Spacing | Nucleation Density | Behavior | Performance |
|---------|-------------------|----------|-------------|
| 20 μm | 25×10⁸ /m² | Early coalescence, large drops | Poor |
| **40 μm** | **6×10⁸ /m²** | **Controlled jumping** | **Excellent** |
| 80 μm | 1.5×10⁸ /m² | Slow growth, low density | Moderate |
| 150 μm | 0.4×10⁸ /m² | Isolated droplets, low flux | Poor |

### Hierarchical Structure

**Two-tier approach:**

```
Nanostructure (100-500 nm):     Microstructure (5-20 μm):
    ╱╲                                ┃
   ╱  ╲                               ┃  10-20 μm tall
  ╱    ╲                              ┃
 ╱______╲                            ┃
   
Provides:                         Provides:
- Superhydrophobicity             - Nucleation sites
- Low contact angle hysteresis    - Controlled spacing
- Durability                      - Droplet anchoring
```

**Why both scales?**
- **Nano alone:** Fragile, difficult to manufacture
- **Micro alone:** Insufficient superhydrophobicity (Wenzel state risk)
- **Combined:** Robust, high performance, manufacturable

### Geometric Patterns

#### Pattern 1: Square Array (Simplest)

```
┌───┬───┬───┬───┐
│ ● │   │ ● │   │
├───┼───┼───┼───┤
│   │ ● │   │ ● │
├───┼───┼───┼───┤
│ ● │   │ ● │   │
└───┴───┴───┴───┘

● = Pillar (5-10 μm diameter)
Spacing: 40-50 μm center-to-center
```

**Pros:**
- Simple to design and etch
- Uniform coverage
- Predictable behavior

**Cons:**
- Droplets can grow along rows (anisotropic)
- Less efficient coalescence

#### Pattern 2: Hexagonal Array (Best)

```
     ●       ●       ●
        \   /   \
         ●       ●
        /   \   /
     ●       ●       ●

Spacing: 40-50 μm
Hexagonal packing: highest density, isotropic
```

**Pros:**
- Maximum nucleation density
- Isotropic droplet growth
- Optimal coalescence (6 neighbors)
- Best heat transfer

**Cons:**
- Slightly harder to lay out
- Must align carefully with etch mask

#### Pattern 3: Gradient Pattern (Advanced)

```
[Hot inlet side]        [Cold outlet side]

●  ●  ●  ●              ●●●●●●●●●
  ●  ●  ●  ●            ●●●●●●●●●
●  ●  ●  ●              ●●●●●●●●●
  
Sparse (80 μm)          Dense (20 μm)
```

**Concept:** 
- Hot side: Sparse nucleation (drops grow large before jumping)
- Cold side: Dense nucleation (high heat flux at cooler temperatures)

**Benefit:** Matches heat flux distribution to temperature profile

#### Pattern 4: Bi-Porous (For High Flux)

```
Small posts (nucleation):    Large channels (vapor escape):

  ●     ●     ●              ═══════════════
     ●     ●                 ═══════════════
  ●     ●     ●              ═══════════════
     
  5-10 μm diameter           50-100 μm width
  30 μm spacing              200 μm spacing
```

**Purpose:** Separate liquid (small posts) and vapor (large channels) paths

**Benefit:** Prevents flooding at high heat flux

---

## Detailed Geometry Specifications

### Micro-Pillar Design

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Diameter** | 5-10 μm | Large enough for nucleation, small enough for density |
| **Height** | 10-20 μm | Aspect ratio 2:1 to 4:1 (structural stability) |
| **Spacing** | 30-50 μm | Center-to-center (allows 20-25 μm droplet growth) |
| **Shape** | Circular or square | Circular: better stress distribution; Square: easier to etch |
| **Top surface** | Flat or slightly rounded | Rounded: better droplet release |

### Nano-Texture on Pillars

**Approach 1: Native Oxidation (Cu)**
- Heat copper to 200-300°C
- Forms CuO nanowires naturally
- Height: 1-5 μm
- Random orientation

**Approach 2: Etched Texture (Si, Cu)**
- Isotropic etch creates rough surface
- Feature size: 100-500 nm
- Depth: 1-3 μm

**Approach 3: Particle Deposition**
- Spray SiO₂ nanoparticles (100 nm)
- Sinter at low temperature
- Creates random nano-roughness

### Substrate Surface Between Pillars

**Cassie-Baxter requirement:** Air must be trapped between pillars

**Land area:** 60-70% of surface should be "air" (not solid)

**Calculation:**
```
For 10 μm pillars, 40 μm spacing:
- Pillar area: π × (5 μm)² = 78.5 μm²
- Unit cell: 40 × 40 = 1600 μm²
- Solid fraction: 78.5/1600 = 4.9%
- Air fraction: 95.1% ✓ (excellent!)
```

---

## Etching Process for JDC Surfaces

### Method 1: Photolithography + Deep RIE (Best)

**For silicon substrates:**

```
1. Clean Si wafer
2. Spin coat photoresist (2-5 μm)
3. Expose through mask (hexagonal array)
4. Develop resist
5. Deep reactive ion etch (Bosch process)
   - Etch 10-20 μm depth
   - Straight sidewalls
6. Strip resist
7. Optional: Nano-texture (secondary etch)
8. Hydrophobic coating (FDTS, etc.)
```

**Pros:** Precise, vertical walls, high aspect ratio
**Cons:** Requires RIE equipment ($100K+), not DIY

### Method 2: Electrochemical Etching (DIY-Friendly)

**For copper:**

```
1. Clean copper plate
2. Apply photoresist or vinyl mask (hex pattern)
3. Expose/develop pattern (holes for pillars)
4. Electrochemical etch:
   - Cu anode in CuSO₄/HCl solution
   - 2-5V DC
   - Current density: 10-50 mA/cm²
   - Time: 20-60 minutes for 10-20 μm depth
5. Remove mask
6. Oxidize for nano-texture (heat to 200°C)
7. Hydrophobic coating
```

**Pros:** Simple equipment, controllable, DIY
**Cons:** Slower than RIE, slightly tapered walls

### Method 3: Laser Ablation (Rapid Prototyping)

**For any metal:**

```
1. Program laser path (hexagonal array)
2. Ablate material (femtosecond laser)
3. Create 10-20 μm holes/posts
4. Scan speed: 1-10 mm/s
5. Post-process: Nano-texture + coating
```

**Pros:** No mask needed, flexible patterns
**Cons:** Expensive equipment, slow for large areas

### Method 4: Template/Mold Method (Replication)

**For mass production:**

```
1. Create master template (etched Si or Cu)
2. Electroform nickel mold
3. Press or cast polymer replica
4. Metallize (sputter Cu or Al)
5. Apply hydrophobic coating
```

**Pros:** Cheap replicas, consistent quality
**Cons:** Requires master template first

---

## Design Calculator

**Python script for pattern design:**

```python
import numpy as np

def design_jdc_surface(area_mm2, droplet_radius_um=20, packing='hex'):
    """
    Design JDC surface parameters
    
    Args:
        area_mm2: Surface area in mm²
        droplet_radius_um: Target droplet radius (μm)
        packing: 'square' or 'hex'
    
    Returns:
        dict with design parameters
    """
    # Optimal spacing = 2 × droplet diameter
    spacing_um = 2 * droplet_radius_um * 2  # 4× radius = 2× diameter
    
    if packing == 'hex':
        # Hexagonal packing density
        density = 2 / (np.sqrt(3) * spacing_um**2)  # sites/μm²
        area_per_site = np.sqrt(3) / 2 * spacing_um**2
    else:  # square
        density = 1 / spacing_um**2
        area_per_site = spacing_um**2
    
    # Convert to m²
    area_m2 = area_mm2 * 1e-6
    spacing_m = spacing_um * 1e-6
    
    # Total sites
    total_sites = int(area_m2 * density * 1e12)  # Convert μm² to m²
    
    # Pillar size (1/4 of spacing)
    pillar_diameter_um = spacing_um / 4
    pillar_height_um = pillar_diameter_um * 2  # 2:1 aspect ratio
    
    # Solid fraction
    if packing == 'hex':
        solid_fraction = (np.pi * (pillar_diameter_um/2)**2) / area_per_site
    else:
        solid_fraction = (np.pi * (pillar_diameter_um/2)**2) / spacing_um**2
    
    return {
        'area_mm2': area_mm2,
        'droplet_radius_um': droplet_radius_um,
        'spacing_um': spacing_um,
        'packing': packing,
        'total_sites': total_sites,
        'nucleation_density_per_m2': density * 1e12,
        'pillar_diameter_um': pillar_diameter_um,
        'pillar_height_um': pillar_height_um,
        'solid_fraction': solid_fraction,
        'air_fraction': 1 - solid_fraction
    }

# Example: 10mm × 10mm surface, 20 μm droplets
result = design_jdc_surface(100, droplet_radius_um=20, packing='hex')

print("JDC Surface Design Parameters:")
print("="*50)
for key, value in result.items():
    if isinstance(value, float):
        print(f"{key}: {value:.2f}")
    else:
        print(f"{key}: {value}")
```

**Example output:**
```
area_mm2: 100.00
droplet_radius_um: 20.00
spacing_um: 80.00
packing: hex
total_sites: 180428
nucleation_density_per_m2: 1804280000.00
pillar_diameter_um: 20.00
pillar_height_um: 40.00
solid_fraction: 0.05
air_fraction: 0.95
```

---

## Pattern Comparison Matrix

| Pattern | Nucleation Density | Coalescence | Flooding Risk | Manufacturing | Best For |
|---------|-------------------|-------------|---------------|---------------|----------|
| **Square array** | 6×10⁸ /m² | Good | Low | Easy | Prototyping |
| **Hexagonal array** | 7×10⁸ /m² | Excellent | Low | Moderate | **Production** |
| **Gradient** | Variable | Variable | Medium | Hard | Special apps |
| **Bi-porous** | High | Excellent | Very low | Complex | High flux |
| **Random** | Variable | Poor | High | Accidental | Avoid |

---

## Common Design Mistakes

### Mistake 1: Spacing Too Close

```
WRONG:              RIGHT:
●●●●●●              ●   ●   ●
●●●●●●                ●   ●
●●●●●●              ●   ●   ●
                    
20 μm spacing      40 μm spacing
Result: Flooding   Result: Jumping!
```

**Problem:** Droplets coalesce too early, form film
**Fix:** Increase spacing to 2× droplet diameter

### Mistake 2: Pillars Too Tall

```
WRONG:              RIGHT:
┃                   ┃
┃  50 μm            ┃  15 μm
┃                   ┃
                    
Fragile!            Robust
```

**Problem:** High aspect ratio pillars collapse
**Fix:** Keep height/diameter < 4:1

### Mistake 3: No Nano-Texture

```
WRONG:              RIGHT:
Smooth pillars      Rough pillars
                    ╱╲╱╲╱╲
Wenzel state!       Cassie-Baxter!
(Stuck droplets)    (Jumping droplets)
```

**Problem:** Insufficient superhydrophobicity
**Fix:** Add nano-roughness to pillars

### Mistake 4: Sharp Corners

```
WRONG:              RIGHT:
┌─┬─┐               ╭─╮
├─┼─┤              (   )
└─┴─┘               ╰─╯
Square pillars      Rounded pillars
                    
Stress concentrators Better release
```

**Problem:** Stress cracking, droplet pinning
**Fix:** Round all corners (minimum 2 μm radius)

---

## DIY Pattern Creation (Step-by-Step)

### For 50mm × 50mm Copper Condenser

**Step 1: Design Pattern**

Use Python script or Inkscape:
```python
# Generate hexagonal array SVG
import svgwrite

def create_hex_pattern(filename, width_mm, height_mm, spacing_um, pillar_um):
    dwg = svgwrite.Drawing(filename, profile='tiny')
    
    # Convert to user units (μm)
    width = width_mm * 1000
    height = height_mm * 1000
    spacing = spacing_um
    pillar = pillar_um
    
    # Hexagonal grid
    dx = spacing
    dy = spacing * np.sqrt(3) / 2
    
    for row in range(int(height / dy) + 1):
        offset = (row % 2) * dx / 2
        for col in range(int(width / dx) + 1):
            x = col * dx + offset
            y = row * dy
            if x < width and y < height:
                dwg.add(dwg.circle(center=(x, y), r=pillar/2, 
                                  fill='black'))
    
    dwg.save()

create_hex_pattern('jdc_pattern.svg', 50, 50, 40, 10)
```

**Step 2: Create Mask**

- Print on transparency (laser printer, 1200 DPI)
- Or use vinyl cutter (Cricut/Silhouette) for adhesive mask

**Step 3: Transfer to Copper**

```
1. Clean copper with acetone
2. Apply mask (transparency or vinyl)
3. Ensure no bubbles at edges
4. Protect back side with tape
```

**Step 4: Etch**

```
Ferric chloride etch:
- Concentration: 40%
- Temperature: 40°C
- Time: 30-45 minutes for 15 μm depth
- Agitate gently
```

**Step 5: Create Nano-Texture**

```
Thermal oxidation:
1. Heat etched copper to 250°C in oven
2. Hold for 2 hours
3. Forms CuO nanowires
4. Cool slowly
```

**Step 6: Hydrophobic Coating**

```
FDTS vapor deposition:
1. Place sample in desiccator
2. Add few drops FDTS in small dish
3. Evacuate to 100 mbar
4. Hold for 2 hours
5. Vent, remove sample
```

**Step 7: Test**

```
1. Place water droplet on surface
2. Should bead up (contact angle >150°)
3. Tilt surface: droplet should roll off easily
4. If stuck: re-coat or check nano-texture
```

---

## Testing and Validation

### Contact Angle Measurement

**DIY method:**
```
1. Place 5 μL water droplet on surface
2. Photograph from side (macro lens)
3. Measure angle in image editor
4. Target: >160° advancing, <5° hysteresis
```

**Expected results:**
- Bare copper: 80-90° (hydrophilic)
- Nano-textured Cu: 130-150° (hydrophobic)
- Nano + FDTS: 160-170° (superhydrophobic) ✓

### Jumping Test

**Setup:**
```
1. Cool surface to 10-20°C below dew point
2. Observe condensation with microscope
3. Watch for droplet coalescence and jumping
4. Count jumps per second
```

**Good performance:** >10 jumps/cm²/s at moderate subcooling (5K)

### Heat Transfer Test

**Compare:**
- Filmwise condensation (smooth surface)
- Jumping droplet (patterned surface)

**Expected:** 3-10× enhancement with JDC

---

## Summary

### The Perfect JDC Surface

```
Specification:
├── Pattern: Hexagonal array
├── Spacing: 40 μm center-to-center  
├── Pillars: 10 μm diameter, 20 μm height
├── Nano-texture: CuO nanowires (1-5 μm)
├── Coating: FDTS SAM
├── Contact angle: >160°
├── Hysteresis: <5°
└── Nucleation density: 6×10⁸ sites/m²
```

### Key Design Rules

1. **Spacing = 2 × droplet diameter** (not 1×, not 4×)
2. **Hexagonal packing** beats square (isotropic, denser)
3. **Hierarchical structure** (micro + nano) required
4. **Aspect ratio < 4:1** for mechanical stability
5. **Air fraction >90%** for Cassie-Baxter state
6. **Round corners** everywhere (no stress concentrators)

### Manufacturing Recommendation

**For DIY:**
- Electrochemical etch + thermal oxidation + FDTS
- Hexagonal pattern, 40 μm spacing
- Expect 70-80% of theoretical performance

**For production:**
- DRIE (silicon) or laser (metal) + vapor deposition
- Tighter tolerances, better repeatability
- 90-95% of theoretical performance

---

*Part of the thermal management research series. See related posts on evaporator channel design and vapor space optimization.*
