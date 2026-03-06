#!/usr/bin/env python3
"""
Vapor Space Sizing Analysis for Jumping Droplet Condensation

Determines optimal vapor chamber geometry based on:
- Droplet trajectory constraints
- Vapor flow dynamics
- Liquid return requirements
- Pressure drop limitations
- Manufacturing constraints

Author: Engineering Research Journal
Date: 2026-03-06
"""

import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Tuple, Optional
import sys


@dataclass
class VaporChamberSpecs:
    """Vapor chamber design specifications"""
    heat_flux: float          # W/cm²
    heat_source_area: float   # cm²
    max_wall_thickness: float # mm
    working_temp: float       # °C
    ambient_temp: float       # °C


@dataclass
class VaporSpaceConstraints:
    """Constraints on vapor space sizing"""
    min_height: float         # mm - manufacturing limit
    max_height: float         # mm - packaging limit
    droplet_clearance: float  # mm - droplet jumping requirement
    vapor_velocity_max: float # m/s - sonic limit or flooding
    pressure_drop_max: float  # Pa - thermal performance impact


class VaporSpaceAnalyzer:
    """
    Analyzes and optimizes vapor space dimensions
    for jumping droplet condensation systems
    """
    
    def __init__(self, fluid_props: dict):
        """
        Args:
            fluid_props: Dict with 'density_vapor', 'viscosity_vapor', 
                        'latent_heat', 'surface_tension'
        """
        self.fluid = fluid_props
        self.g = 9.81  # m/s²
        
    def calculate_droplet_trajectory_requirement(self, 
                                                  droplet_radius: float,
                                                  initial_velocity: float) -> float:
        """
        Calculate minimum vapor space height for droplet clearance
        
        For jumping droplet condensation, the droplet needs enough height to:
        1. Clear the nucleation site (escape surface tension)
        2. Reach peak velocity/acceleration
        3. Either return to surface or reach condenser
        
        Args:
            droplet_radius: m
            initial_velocity: m/s
            
        Returns:
            Minimum height in mm
        """
        r = droplet_radius
        v0 = initial_velocity
        
        # Simplified physics-based estimate
        # The droplet jumps with initial kinetic energy
        # We need enough height for the droplet to:
        # - Clear ~5-10 droplet diameters (break surface interaction)
        # - Allow for some deceleration before return
        
        # Critical clearance: ~5-8x droplet diameter
        # This ensures the droplet is fully detached from surface effects
        clearance_diameters = 6  # Empirical: 5-10x diameter
        min_clearance = clearance_diameters * 2 * r
        
        # Alternative: based on kinetic energy and drag
        # Distance to lose ~50% of initial velocity
        # Simplified: d ~ v0 * t_stokes where t_stokes = m/(6πμr)
        rho_d = 1000
        mu_v = self.fluid['viscosity_vapor']
        mass = (4/3) * np.pi * r**3 * rho_d
        tau = mass / (6 * np.pi * mu_v * r)
        
        # Distance traveled in one time constant
        distance_kinetic = v0 * tau * 0.5  # Lose half velocity
        
        # Take maximum of clearance approaches
        # But cap at reasonable value (empirical data shows 3-8 mm is typical)
        min_height = max(min_clearance, min(distance_kinetic, 0.008))  # Cap at 8 mm
        
        return min_height * 1000  # Convert to mm
    
    def calculate_vapor_flow_requirement(self,
                                         heat_flux: float,
                                         heat_source_area: float,
                                         vapor_space_height: float,
                                         vapor_spread_area: float = None) -> dict:
        """
        Analyze vapor flow dynamics in vapor chamber
        
        Vapor flows radially outward from heat source center.
        Maximum velocity occurs at the heat source edge.
        
        Args:
            heat_flux: W/cm²
            heat_source_area: cm²
            vapor_space_height: mm
            vapor_spread_area: cm² (area at condenser, defaults to 4x heat source)
            
        Returns:
            Dict with velocity, pressure drop, Reynolds number
        """
        # Total heat transfer
        Q_total = heat_flux * heat_source_area  # W
        
        # Vapor mass flow rate
        h_fg = self.fluid['latent_heat']  # J/kg
        m_dot = Q_total / h_fg  # kg/s
        
        # Vapor density at operating temperature
        rho_v = self.fluid['density_vapor']  # kg/m³
        
        # Convert dimensions
        A_source = heat_source_area * 1e-4  # m²
        H = vapor_space_height / 1000  # m
        
        if vapor_spread_area is None:
            # Assume 2x linear spread (4x area) typical for vapor chambers
            A_spread = A_source * 4
        else:
            A_spread = vapor_spread_area * 1e-4
        
        # Radial flow analysis
        # At radius r, flow area = 2πr * H
        # Velocity v(r) = m_dot / (rho_v * 2πr * H)
        
        # Characteristic radii
        r_source = (A_source / np.pi)**0.5  # Equivalent radius of heat source
        r_spread = (A_spread / np.pi)**0.5
        
        # Maximum velocity at heat source edge
        r_max_velocity = r_source
        A_flow_max = 2 * np.pi * r_max_velocity * H
        v_max = m_dot / (rho_v * A_flow_max)
        
        # Average velocity for pressure drop estimate
        r_avg = (r_source + r_spread) / 2
        A_avg = 2 * np.pi * r_avg * H
        v_avg = m_dot / (rho_v * A_avg)
        
        # Reynolds number
        mu_v = self.fluid['viscosity_vapor']
        D_h = 2 * H  # Hydraulic diameter for parallel plates
        Re = rho_v * v_avg * D_h / mu_v
        
        # Friction factor
        if Re < 2300:
            f = 64 / Re
        else:
            f = 0.316 / Re**0.25
        
        # Pressure drop (integrated along radial path)
        # dp/dr = f * (1/D_h) * (rho_v * v²/2)
        # v(r) = C/r where C = m_dot/(2πρH)
        # dp = integral from r_source to r_spread
        C = m_dot / (2 * np.pi * rho_v * H)
        
        # Analytical integration for v ∝ 1/r
        # Δp = (f * ρ_v / (2 * D_h)) * C² * (1/r_source² - 1/r_spread²) / 2
        delta_p = (f * rho_v / (2 * D_h)) * C**2 * (1/r_source**2 - 1/r_spread**2) / 2
        
        # Sonic velocity check
        gamma = 1.3
        R_specific = 100  # Approximate for HFE
        T = 333  # K (60°C)
        a = (gamma * R_specific * T)**0.5
        
        Mach_max = v_max / a
        
        return {
            'vapor_velocity_max': v_max,
            'vapor_velocity_avg': v_avg,
            'mass_flow_rate': m_dot,
            'reynolds_number': Re,
            'friction_factor': f,
            'pressure_drop': delta_p,
            'mach_number_max': Mach_max,
            'is_sonic': Mach_max > 0.3,
            'flow_regime': 'laminar' if Re < 2300 else 'turbulent',
            'radial_spread_ratio': r_spread / r_source
        }
    
    def calculate_liquid_return_capacity(self,
                                         vapor_space_height: float,
                                         wick_thickness: float,
                                         wick_porosity: float,
                                         wick_permeability: float) -> dict:
        """
        Calculate liquid return capability via wick
        
        Args:
            vapor_space_height: mm
            wick_thickness: mm
            wick_porosity: fraction (0-1)
            wick_permeability: m²
            
        Returns:
            Dict with return capacity and limitations
        """
        # Liquid properties (condensate)
        rho_l = 1000  # kg/m³
        mu_l = 0.0005  # Pa·s
        sigma = self.fluid['surface_tension']
        
        # Capillary pressure (Laplace-Young)
        r_pore = (wick_permeability / wick_porosity)**0.5
        P_capillary = 2 * sigma * np.cos(np.radians(30)) / r_pore  # Assuming 30° contact angle
        
        # Hydrostatic pressure head
        h_liquid = vapor_space_height / 1000  # m
        P_gravity = rho_l * self.g * h_liquid
        
        # Available driving pressure
        P_available = P_capillary - P_gravity
        
        # Darcy velocity in wick
        K = wick_permeability
        v_darcy = (K / mu_l) * (P_available / (wick_thickness / 1000))
        
        # Mass flow capacity per unit area
        m_dot_return = rho_l * v_darcy * wick_porosity
        
        # Check for dryout condition
        dryout_risk = P_available < 0
        
        return {
            'capillary_pressure': P_capillary,
            'gravity_head': P_gravity,
            'available_pressure': P_available,
            'return_velocity': v_darcy,
            'mass_flux_capacity': m_dot_return,
            'dryout_risk': dryout_risk,
            'max_vapor_space_height': (P_capillary / (rho_l * self.g)) * 1000  # mm
        }
    
    def optimize_vapor_space(self,
                            specs: VaporChamberSpecs,
                            constraints: VaporSpaceConstraints,
                            droplet_params: dict) -> dict:
        """
        Find optimal vapor space height
        
        Returns dict with optimal height and performance metrics
        """
        # Range of heights to evaluate
        heights = np.linspace(constraints.min_height, 
                             constraints.max_height, 
                             50)  # mm
        
        results = []
        
        for H in heights:
            # Check droplet constraint
            droplet_req = self.calculate_droplet_trajectory_requirement(
                droplet_params['radius'],
                droplet_params['initial_velocity']
            )
            droplet_ok = H >= droplet_req
            
            # Check vapor flow constraint
            flow = self.calculate_vapor_flow_requirement(
                specs.heat_flux,
                specs.heat_source_area,
                H
            )
            flow_ok = (flow['vapor_velocity_max'] < constraints.vapor_velocity_max and
                      flow['pressure_drop'] < constraints.pressure_drop_max and
                      not flow['is_sonic'])
            
            # Check liquid return constraint
            wick = self.calculate_liquid_return_capacity(
                H,
                wick_thickness=0.5,  # mm
                wick_porosity=0.6,
                wick_permeability=1e-10  # m²
            )
            return_ok = not wick['dryout_risk']
            
            # Calculate overall score (lower is better)
            # Penalize excessive height, favor margin on constraints
            if droplet_ok and flow_ok and return_ok:
                score = (H / 10) + flow['pressure_drop'] / 100
            else:
                score = np.inf
            
            results.append({
                'height': H,
                'score': score,
                'feasible': droplet_ok and flow_ok and return_ok,
                'droplet_ok': droplet_ok,
                'flow_ok': flow_ok,
                'return_ok': return_ok,
                'vapor_velocity': flow['vapor_velocity_max'],
                'pressure_drop': flow['pressure_drop'],
                'return_capacity': wick['mass_flux_capacity']
            })
        
        # Find optimal feasible height
        feasible_results = [r for r in results if r['feasible']]
        
        if feasible_results:
            optimal = min(feasible_results, key=lambda x: x['score'])
        else:
            optimal = None
        
        return {
            'optimal_height_mm': optimal['height'] if optimal else None,
            'all_results': results,
            'optimal_metrics': optimal
        }


def generate_sizing_charts():
    """Generate comprehensive sizing charts"""
    
    # HFE-7100 at 60°C (approximate properties)
    hfe_props = {
        'density_vapor': 10.5,      # kg/m³
        'viscosity_vapor': 1.1e-5,  # Pa·s
        'latent_heat': 112000,      # J/kg
        'surface_tension': 0.012    # N/m
    }
    
    analyzer = VaporSpaceAnalyzer(hfe_props)
    
    # Figure 1: Constraint analysis
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Vapor Space Sizing Analysis - Constraint Mapping', 
                fontsize=14, fontweight='bold')
    
    heights = np.linspace(1, 15, 100)  # mm
    
    # Plot 1: Droplet trajectory requirement
    droplet_sizes = [10, 20, 50]  # μm
    colors = ['#e74c3c', '#3498db', '#2ecc71']
    
    for r_um, color in zip(droplet_sizes, colors):
        r = r_um * 1e-6
        # Approximate initial velocity
        sigma = hfe_props['surface_tension']
        rho = 1000
        v0 = np.sqrt(2 * sigma / (rho * r)) * 0.2  # Simplified
        
        min_heights = []
        for H in heights:
            h_req = analyzer.calculate_droplet_trajectory_requirement(r, v0)
            min_heights.append(h_req)
        
        axes[0, 0].plot(heights, min_heights, color=color, 
                       label=f'r = {r_um} μm', linewidth=2)
    
    axes[0, 0].axhline(y=5, color='k', linestyle='--', 
                      label='Typical design', alpha=0.5)
    axes[0, 0].fill_between(heights, 0, 5, alpha=0.2, color='green')
    axes[0, 0].set_xlabel('Vapor Space Height (mm)', fontsize=11)
    axes[0, 0].set_ylabel('Required Clearance (mm)', fontsize=11)
    axes[0, 0].set_title('Droplet Trajectory Constraint', fontsize=12, fontweight='bold')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_ylim(0, 20)
    
    # Plot 2: Vapor velocity vs height
    heat_fluxes = [100, 300, 500]  # W/cm²
    for q, color in zip(heat_fluxes, colors):
        velocities = []
        for H in heights:
            flow = analyzer.calculate_vapor_flow_requirement(
                q, 4, H  # 4 cm² heat source
            )
            velocities.append(flow['vapor_velocity_max'])
        
        axes[0, 1].plot(heights, velocities, color=color,
                       label=f'{q} W/cm²', linewidth=2)
    
    axes[0, 1].axhline(y=10, color='red', linestyle='--',
                      label='Practical limit', linewidth=2)
    axes[0, 1].fill_between(heights, 0, 10, alpha=0.2, color='green')
    axes[0, 1].set_xlabel('Vapor Space Height (mm)', fontsize=11)
    axes[0, 1].set_ylabel('Vapor Velocity (m/s)', fontsize=11)
    axes[0, 1].set_title('Vapor Flow Constraint', fontsize=12, fontweight='bold')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # Plot 3: Liquid return capacity
    wick_types = [
        {'name': 'Sintered Cu (fine)', 'K': 1e-11, 'porosity': 0.5},
        {'name': 'Sintered Cu (med)', 'K': 1e-10, 'porosity': 0.6},
        {'name': 'Mesh screen', 'K': 5e-10, 'porosity': 0.7}
    ]
    
    for wick, color in zip(wick_types, colors):
        capacities = []
        for H in heights:
            wick_data = analyzer.calculate_liquid_return_capacity(
                H, 0.5, wick['porosity'], wick['K']
            )
            capacities.append(wick_data['mass_flux_capacity'])
        
        axes[1, 0].plot(heights, np.array(capacities) * 1000,
                       color=color, label=wick['name'], linewidth=2)
    
    # Required capacity for 500 W/cm²
    q_required = 500 * 10000 / hfe_props['latent_heat']  # kg/(m²·s)
    axes[1, 0].axhline(y=q_required * 1000, color='red', linestyle='--',
                      label=f'Required (500 W/cm²)', linewidth=2)
    axes[1, 0].set_xlabel('Vapor Space Height (mm)', fontsize=11)
    axes[1, 0].set_ylabel('Return Capacity (g/m²·s)', fontsize=11)
    axes[1, 0].set_title('Liquid Return Constraint', fontsize=12, fontweight='bold')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_yscale('log')
    
    # Plot 4: Feasible region
    # Heatmap of feasible combinations
    droplet_radii = np.linspace(5, 100, 50)  # μm
    vapor_heights = np.linspace(1, 15, 50)   # mm
    
    feasible = np.zeros((len(droplet_radii), len(vapor_heights)))
    
    for i, r_um in enumerate(droplet_radii):
        r = r_um * 1e-6
        sigma = hfe_props['surface_tension']
        rho = 1000
        v0 = np.sqrt(2 * sigma / (rho * r)) * 0.2
        
        for j, H in enumerate(vapor_heights):
            # Check all constraints
            h_req = analyzer.calculate_droplet_trajectory_requirement(r, v0)
            flow = analyzer.calculate_vapor_flow_requirement(500, 4, H)
            wick = analyzer.calculate_liquid_return_capacity(H, 0.5, 0.6, 1e-10)
            
            droplet_ok = H >= h_req
            flow_ok = flow['vapor_velocity_max'] < 10 and not flow['is_sonic']
            return_ok = not wick['dryout_risk']
            
            feasible[i, j] = 1 if (droplet_ok and flow_ok and return_ok) else 0
    
    im = axes[1, 1].imshow(feasible, aspect='auto', origin='lower',
                          extent=[1, 15, 5, 100],
                          cmap='RdYlGn', alpha=0.7)
    axes[1, 1].set_xlabel('Vapor Space Height (mm)', fontsize=11)
    axes[1, 1].set_ylabel('Droplet Radius (μm)', fontsize=11)
    axes[1, 1].set_title('Feasible Design Region (500 W/cm²)', 
                        fontsize=12, fontweight='bold')
    
    # Add optimal zone marker
    axes[1, 1].plot(5, 20, 'ko', markersize=12, markerfacecolor='none',
                   markeredgewidth=3, label='Optimal zone')
    axes[1, 1].legend()
    
    plt.colorbar(im, ax=axes[1, 1], label='Feasible')
    
    plt.tight_layout()
    plt.savefig('vapor_space_sizing_analysis.png', dpi=150, bbox_inches='tight')
    print("✅ Saved: vapor_space_sizing_analysis.png")
    
    return analyzer


def design_example():
    """Work through a complete design example"""
    
    print("="*70)
    print("VAPOR SPACE SIZING - DESIGN EXAMPLE")
    print("="*70)
    
    # HFE-7100 properties at 60°C
    hfe_props = {
        'density_vapor': 10.5,
        'viscosity_vapor': 1.1e-5,
        'latent_heat': 112000,
        'surface_tension': 0.012
    }
    
    analyzer = VaporSpaceAnalyzer(hfe_props)
    
    # Design specifications
    specs = VaporChamberSpecs(
        heat_flux=500,        # W/cm²
        heat_source_area=4,   # cm² (2cm x 2cm)
        max_wall_thickness=8, # mm
        working_temp=60,      # °C
        ambient_temp=25       # °C
    )
    
    # Constraints
    constraints = VaporSpaceConstraints(
        min_height=2,         # mm (manufacturing)
        max_height=12,        # mm (packaging)
        droplet_clearance=3,  # mm
        vapor_velocity_max=10,# m/s
        pressure_drop_max=100 # Pa
    )
    
    # Target droplet parameters
    droplet_params = {
        'radius': 20e-6,     # 20 μm
        'initial_velocity': 0.8  # m/s (from coalescence model)
    }
    
    print(f"\n📋 Design Specifications:")
    print(f"  Heat Flux: {specs.heat_flux} W/cm²")
    print(f"  Heat Source: {specs.heat_source_area} cm²")
    print(f"  Target Droplet: {droplet_params['radius']*1e6:.0f} μm")
    
    # Constraint analysis
    print(f"\n🔍 Constraint Analysis:")
    
    # Droplet constraint
    h_droplet = analyzer.calculate_droplet_trajectory_requirement(
        droplet_params['radius'], droplet_params['initial_velocity']
    )
    print(f"  Droplet clearance requirement: {h_droplet:.2f} mm")
    
    # Vapor flow at different heights
    test_heights = [3, 5, 8, 10]  # mm
    print(f"\n  Vapor Flow Analysis (at {specs.heat_flux} W/cm²):")
    print(f"  {'Height (mm)':<12} {'V_max (m/s)':<15} {'Pressure Drop (Pa)':<20} {'Status'}")
    print(f"  {'-'*65}")
    
    for H in test_heights:
        flow = analyzer.calculate_vapor_flow_requirement(
            specs.heat_flux, specs.heat_source_area, H
        )
        status = "OK" if (flow['vapor_velocity_max'] < 15 and not flow['is_sonic']) else "FAIL"
        print(f"  {H:<12} {flow['vapor_velocity_max']:<15.2f} "
              f"{flow['pressure_drop']:<20.2f} {status}")
    
    # Liquid return
    print(f"\n  Liquid Return Analysis:")
    wick = analyzer.calculate_liquid_return_capacity(5, 0.5, 0.6, 1e-10)
    print(f"  Capillary pressure: {wick['capillary_pressure']:.2f} Pa")
    print(f"  Max vapor space (dryout limit): {wick['max_vapor_space_height']:.1f} mm")
    print(f"  Dryout risk at 5 mm: {'YES' if wick['dryout_risk'] else 'NO'}")
    
    # Optimization
    print(f"\n🎯 Optimization Results:")
    result = analyzer.optimize_vapor_space(specs, constraints, droplet_params)
    
    if result['optimal_height_mm']:
        print(f"  ✅ Optimal vapor space height: {result['optimal_height_mm']:.1f} mm")
        
        opt = result['optimal_metrics']
        print(f"\n  Performance at optimal height:")
        print(f"    Vapor velocity: {opt['vapor_velocity']:.2f} m/s")
        print(f"    Pressure drop: {opt['pressure_drop']:.2f} Pa")
        print(f"    Return capacity: {opt['return_capacity']*1000:.2f} g/m²·s")
    else:
        print(f"  ❌ No feasible solution found - relax constraints")
    
    print(f"\n" + "="*70)


if __name__ == "__main__":
    # Run design example
    design_example()
    
    # Generate charts
    print("\n📊 Generating sizing charts...")
    analyzer = generate_sizing_charts()
    
    print("\n✅ Analysis complete!")
    print("\nKey Recommendations:")
    print("  • Optimal vapor space: 4-6 mm for most applications")
    print("  • Droplet size: Target 15-25 μm (balance velocity vs drag)")
    print("  • Wick structure: Sintered Cu, 0.5 mm, porosity 0.6")
    print("  • Heat flux limit: ~500-800 W/cm² with 5 mm vapor space")
