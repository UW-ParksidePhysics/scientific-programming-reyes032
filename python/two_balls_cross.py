import vpython as vp

initial_position = vp.vector(-1., 0., 0.)
initial_velocity = vp.vector(1., 0., 0.)
initial_position_2 = vp.vector(1., 0., 0)
initial_velocity_2 = vp.vector(1, 0, 0)
ball = vp.sphere(pos=initial_position, radius=0.1, color=vp.color.red, make_trail=True, trail_type='points')
ball_2 = vp.sphere(pos=initial_position_2, radius=0.1, color=vp.color.yellow, make_trail=True, trail_type='points')
animation_time_step = 0.1  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.05
stop_time = 10.

time = 0.
while time < stop_time:
    vp.rate(rate_of_animation)
    x = initial_position.x + initial_velocity.x * time
    y = initial_position.y + initial_velocity.y * time
    z = initial_position.z + initial_velocity.z * time
    ball.pos = vp.vector(x, y, z)
    x = initial_position_2.x + initial_velocity_2.x * time
    y = initial_position_2.y + initial_velocity_2.y * time
    z = initial_position_2.z + initial_velocity_2.z * time
    ball.pos = vp.vector(x, y, z)
    time += time_step
