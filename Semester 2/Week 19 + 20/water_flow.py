
EARTH_ACCELERATION_OF_GRAVITY=9.80665
WATER_DENSITY=998.2
WATER_DYNAMIC_VISCOSITY=0.0010016

def water_column_height(tower_height, tank_height):
    t = tower_height
    w = tank_height
    height = t+(3*w)/4
    return height

def pressure_gain_from_water_height(height):
    h = height
    pressure = (WATER_DENSITY*EARTH_ACCELERATION_OF_GRAVITY*h)/1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    f = friction_factor
    l = pipe_length
    v = fluid_velocity
    d = pipe_diameter
    pressure_loss = (-f*l*WATER_DENSITY*(v**2))/(2000*d)
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    v = fluid_velocity
    n = quantity_fittings
    pressure_loss_fittings = (-0.04*WATER_DENSITY*(v**2)*n)/2000
    return pressure_loss_fittings

def reynolds_number(hydraulic_diameter, fluid_velocity):
    d = hydraulic_diameter
    v = fluid_velocity
    reynolds_number = (WATER_DENSITY*d*v)/WATER_DYNAMIC_VISCOSITY
    return reynolds_number

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    R = reynolds_number
    D = larger_diameter
    d = smaller_diameter
    v = fluid_velocity
    k = (0.1+(50/R))*(((D/d)**4)-1)
    lost_pressure = ((-k*WATER_DENSITY*(v**2))/2000)
    return lost_pressure

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()