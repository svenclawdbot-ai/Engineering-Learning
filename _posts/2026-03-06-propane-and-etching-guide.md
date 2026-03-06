---
layout: post
title: "DIY Fabrication: Propane Systems and Chemical Etching"
date: 2026-03-06 13:35:00 +0000
topic: "Thermal Systems"
tags: ["DIY", "fabrication", "propane", "etching", "heat pipes", "micro-channels"]
summary: "Practical guide to safely managing propane fill systems and chemically etching copper for micro-channels and wick structures in DIY thermal management projects."
---

## DIY Propane System Management

### Why Propane for DIY?

**Advantages:**
- Boiling point: -42°C (works at atmospheric pressure)
- Easy to source (camping canisters)
- High latent heat: 426 kJ/kg
- Non-toxic (but flammable!)
- Cheap: ~$5-10 per fill

**Compared to water:**
- No pressure vessel needed at room temperature
- Easier to evacuate (air purges easier)
- Lower viscosity when operating

---

## Propane System Components

### Required Parts List

| Component | Specification | Cost | Source |
|-----------|--------------|------|--------|
| **Propane canister** | Camping gas (16oz/450g) | $5-8 | Hardware store |
| **Pressure regulator** | Adjustable 0-60 psi | $15-25 | Welding supply |
| **Fill valve** | Schrader or refrigeration valve | $3-5 | Amazon/eBay |
| **Copper tubing** | 1/4" OD refrigeration grade | $10 | Hardware store |
| **Vacuum pump** | 2-stage rotary vane (3 CFM) | $80-150 | Amazon/Harbor Freight |
| **Pressure gauge** | 0-100 psi liquid-filled | $15 | Amazon |
| **Pinch-off tool** | Refrigeration tube crimper | $20 | HVAC supply |
| **Safety relief valve** | 50-75 psi pop-off | $10 | McMaster-Carr |

**Total system cost:** ~$150-250

---

## Propane Fill Procedure (Step-by-Step)

### Step 1: System Preparation

**Evacuation setup:**
```
[Heat pipe/thermosyphon]
       ↑
   [Fill valve] ← [Vacuum pump]
       ↑
   [Pressure gauge]
       ↑
   [Propane regulator] ← [Canister]
```

**Tools needed:**
- Propane torch (for leak checking)
- Soapy water (dish soap + water)
- Safety glasses
- Gloves (insulated for cold)
- Fire extinguisher nearby

### Step 2: Leak Testing (Critical!)

**Before evacuation:**
1. Pressurize to 50 psi with nitrogen or air
2. Apply soapy water to all joints
3. Watch for bubbles (indicates leak)
4. Fix leaks by re-soldering or tightening
5. Repeat until no leaks

**Never proceed with propane if leaks exist!**

### Step 3: Evacuation

**Process:**
1. Connect vacuum pump to fill valve
2. Open valve, start pump
3. Pull vacuum to **<100 millitorr** (0.1 Torr)
4. This takes 10-30 minutes depending on pump
5. Close valve, turn off pump
6. Wait 10 minutes, check if pressure rises
   - If pressure rises >1 Torr: you have a leak
   - If stable: proceed to fill

**Why deep vacuum matters:**
- Non-condensable gases (air) destroy heat pipe performance
- Target: <0.1% non-condensable gas by volume

### Step 4: Propane Fill

**Calculation:**
```
Fill volume = 30-50% of total internal volume

Example: 10cm × 2cm × 0.5cm channel = 10 cm³
Propane liquid density: ~0.5 g/cm³
Fill mass: 5 cm³ × 0.5 g/cm³ = 2.5g propane

Small system (~10g propane total)
```

**Procedure:**
1. Connect propane canister to regulator
2. Set regulator to 20-30 psi
3. Chill heat pipe with ice (helps condensation)
4. Crack open fill valve slowly
5. Listen for liquid flow (hissing sound)
6. Fill for 10-20 seconds (small system)
7. Close valve

**Visual confirmation:**
- Cold spot forms at fill point
- Condensation on outside of pipe (normal)

### Step 5: Seal the System

**Option A: Pinch-off (Permanent)**
1. Use pinch-off tool on copper tube
2. Compress in 3 locations (triple seal)
3. Cut excess tube
4. Solder end shut

**Option B: Schrader valve (Serviceable)**
1. Install refrigeration Schrader valve
2. Can evacuate/refill multiple times
3. Slightly higher leak risk

**Option C: Compression fitting (R&D only)**
1. Use Swagelok or similar compression fitting
2. Easy to disassemble for inspection
3. Higher leak rate — not for long-term use

### Step 6: Final Testing

**Functional test:**
1. Apply heat to evaporator (hair dryer or hot plate)
2. Monitor temperatures along pipe
3. Should see:
   - Evaporator heats to ~40-50°C (propane boiling)
   - Condenser stays cooler (heat rejection)
   - Temperature difference 10-20°C

**Performance check:**
- Measure heat input (voltage × current)
- Measure temperature drop
- Calculate effective thermal resistance

---

## Safety Protocols

### ⚠️ Critical Safety Rules

**1. Ventilation**
- Work outdoors or in well-ventilated area
- Propane accumulates in low areas (heavier than air)
- No ignition sources within 10 feet

**2. Fire Protection**
- Fire extinguisher (Class B) within arm's reach
- No open flames during fill
- Ground all equipment (static discharge)

**3. Pressure Safety**
- **Never exceed 100 psi** (propane vapor pressure at 38°C is ~110 psi)
- Always install relief valve (set to 75 psi)
- Use pressure-rated components only

**4. Personal Protection**
- Safety glasses (propane can cause freeze burns)
- Insulated gloves (cold metal surfaces)
- Long sleeves and pants

### Emergency Procedures

**Propane leak detected:**
1. Shut off canister valve immediately
2. Do NOT operate electrical switches
3. Evacuate area
4. Allow to dissipate (propane is heavier than air)
5. Ventilate before resuming

**Fire:**
1. Shut off propane at source if safe to do so
2. Use Class B fire extinguisher
3. Evacuate if fire grows
4. Call emergency services

**Freeze burn:**
1. Flush with lukewarm water (NOT hot)
2. Seek medical attention if severe

---

## DIY Chemical Etching for Micro-Channels

### Why Etch Instead of Machine?

- **Cost:** Chemicals ~$20 vs CNC ~$200-500
- **Precision:** Can achieve 50-100 μm features
- **Surface area:** Creates micro-roughness (good for boiling)
- **Access:** No machine shop needed

---

## Method 1: Ferric Chloride Etching (Easiest)

### Materials

| Item | Specification | Cost | Source |
|------|--------------|------|--------|
| **Ferric chloride** | 42% solution, 500mL | $10-15 | Electronics store/Amazon |
| **Copper clad board** | FR4 or bare copper sheet | $5-10 | Electronics store |
| **Vinyl stickers** | Adhesive vinyl sheets | $5 | Craft store |
| **Laser printer** | Toner-based (not inkjet) | — | Home office |
| **Acetone** | For cleaning | $5 | Hardware store |
| **Gloves + eye protection** | Chemical resistant | $10 | Hardware store |

### Process Overview

```
1. Design channel pattern on computer
2. Print on vinyl sticker (laser printer)
3. Apply sticker to copper surface  
4. Etch in ferric chloride bath
5. Remove vinyl mask
6. Clean and finish
```

### Step-by-Step Procedure

**Step 1: Design Pattern**

Use CAD software (Fusion 360, Inkscape):
- Channel width: 200-500 μm (0.2-0.5mm)
- Channel depth: 100-300 μm
- Pitch (spacing): 400-1000 μm

**Pattern types:**
- Parallel straight channels (simplest)
- Radial channels (for circular evaporators)
- Grid pattern (high surface area)

**Step 2: Create Vinyl Mask**

**Toner transfer method:**
1. Print design on vinyl sticker paper
2. Cut to size
3. Apply to copper surface
4. Use credit card to remove bubbles
5. Ensure complete adhesion at edges

**Alternative: Photoresist (more precise)**
1. Coat copper with photoresist
2. Expose through transparency mask
3. Develop in sodium carbonate
4. More expensive (~$30), higher resolution

**Step 3: Etching Bath**

**Setup:**
- Plastic container (not metal!)
- Ferric chloride solution: 40-42% concentration
- Temperature: 30-50°C (warmer = faster)
- Agitation: Gentle stirring or air bubbler

**Process:**
1. Submerge masked copper in solution
2. Etch time: 20-60 minutes depending on depth
3. Etch rate: ~10-20 μm per hour at room temp
4. Check periodically (remove, rinse, inspect)

**Step 4: Stop + Clean**

1. Remove from etchant when desired depth reached
2. Rinse thoroughly in water
3. Remove vinyl mask (peel off)
4. Clean residue with acetone
5. Neutralize etchant (add baking soda until fizzing stops)

### Results

**Typical achievable:**
- Channel width: 200-500 μm
- Channel depth: 100-300 μm  
- Surface roughness: Ra ~1-5 μm

**Good for:**
- Micro-channel heat sinks
- Wick structures (if connected to reservoir)
- Surface enhancement (increased area)

---

## Method 2: Electroless Etching (Safer)

### Materials

| Item | Purpose | Cost |
|------|---------|------|
| **Copper sulfate** | Etchant | $10 |
| **Hydrogen peroxide (3%)** | Oxidizer | $3 |
| **Hydrochloric acid (muriatic)** | Activator | $8 |
| **Water** | Diluent | — |

### Solution Preparation

**Recipe (1 liter):**
```
- Copper sulfate: 100g
- HCl (conc): 50mL  
- H2O2 (3%): 100mL
- Water: 850mL
```

**Advantages over ferric chloride:**
- Less toxic (no heavy metals)
- Clear solution (can see progress)
- Reusable (add H2O2 to regenerate)

**Disadvantages:**
- Slower etch rate
- Still requires acid handling
- Less aggressive on copper

---

## Method 3: Electrochemical Etching (Most Control)

### Setup

**Components:**
- DC power supply (0-30V, 0-5A): $30
- Graphite or stainless steel cathode
- Copper workpiece (anode)
- Salt water electrolyte (NaCl, 5%)

**Circuit:**
```
[Power supply (+)] → [Copper workpiece]
                          ↓
                    [Salt water bath]
                          ↓
[Power supply (-)] → [Graphite cathode]
```

**Process:**
1. Apply 2-5V DC
2. Current density: 10-50 mA/cm²
3. Etch rate: ~5-15 μm/hour
4. Most controllable method

**Advantages:**
- Cleanest edges
- Adjustable rate
- No hazardous chemicals (just salt water)
- Can etch selectively with masking

---

## Creating Wick Structures

### Sintered Wick Alternative: Copper Foam

**Don't sinter at home** — requires hydrogen atmosphere and 800°C furnace.

**Use copper foam instead:**
- Source: ERG Aerospace, Amazon ("copper foam")
- Porosity: 90-95%
- Pore size: 100-500 μm
- Cost: $20-50 per sheet

**Attachment:**
- Silver solder (Harbor Freight propane torch)
- Thermal epoxy (for testing only)
- Press-fit into machined groove

### DIY Sintering (Advanced)

**If you have access to furnace:**
1. Pack Cu powder (10-50 μm) into mold
2. Heat in hydrogen atmosphere to 800-900°C
3. Hold for 1-2 hours
4. Cool slowly
5. Requires tube furnace + hydrogen safety

**Not recommended for home without proper equipment.**

---

## Micro-Channel Design Guidelines

### Dimensions for Different Applications

| Application | Channel Width | Depth | Pitch | Feature |
|-------------|--------------|-------|-------|---------|
| **Liquid cooling** | 200-500 μm | 200-400 μm | 400-800 μm | High flow, low ΔP |
| **Boiling enhancement** | 100-300 μm | 100-200 μm | 300-500 μm | Nucleation sites |
| **Vapor venting** | 500-1000 μm | 300-600 μm | 800-1500 μm | Low resistance |
| **Wick (capillary)** | 50-200 μm | 100-300 μm | 200-400 μm | Surface tension |

### Design Tips

**For thermosyphon evaporator:**
- Channels toward center (radial)
- Depth: 200-300 μm
- Include vapor escape channels (larger)
- Surface roughness: Ra > 2 μm (enhances boiling)

**For heat pipe wick:**
- Connected pore network
- Small pore size (50-150 μm)
- High porosity (>80%)

---

## Testing Etched Channels

### Visual Inspection
- Stereo microscope ($50-100)
- Measure depth with depth gauge
- Check for blocked channels

### Flow Testing
- Push colored water through with syringe
- Verify all channels flow
- Check for leaks

### Thermal Testing
- Mount heater on back side
- IR camera or thermocouples on front
- Measure temperature uniformity
- Good channels: uniform temperature
- Blocked channels: hot spots

---

## Safety for Chemical Etching

### Ferric Chloride
- **Skin/eye irritant**
- **Stains everything** (brown color)
- **Neutralize with baking soda** before disposal
- **Wear gloves and eye protection**

### Acids (HCl)
- **Corrosive** — causes burns
- **Fumes** — work in ventilated area
- **Never add water to acid** (always acid to water)

### Disposal
- Neutralize acid with baking soda (pH ~7)
- Dilute heavily with water
- Check local regulations
- Most municipal systems can handle small quantities

---

## Cost Summary: DIY Fabrication Setup

| Capability | Cost | Performance |
|------------|------|-------------|
| **Propane fill system** | $150-250 | Professional-grade fill |
| **Ferric chloride etching** | $30-50 | 200-500 μm features |
| **Electrochemical etching** | $60-80 | Cleanest, most control |
| **Microscope inspection** | $50-100 | Quality control |
| **Total fab setup** | **$300-500** | Capable of 300+ W/cm² prototypes |

---

## Recommended Starting Point

**Phase 1: Quick Test**
- Buy pre-made heat pipes ($3 each)
- Flatten in vice
- Test with CPU + water cooling
- **Cost:** $50, **Time:** 1 day

**Phase 2: Custom Channels**
- Ferric chloride etch copper plate
- 200 μm channels for evaporator
- Solder to heat pipes
- **Cost:** +$30, **Time:** 1 weekend

**Phase 3: Propane System**
- Build fill station
- Fill custom thermosyphon
- Characterize performance
- **Cost:** +$150, **Time:** 2-3 weekends

---

*Start with pre-made heat pipes to prove concept, then iterate toward custom fabrication.*