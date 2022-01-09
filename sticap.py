from solidff import *
import solid

stick_width, stick_corner_radius, stick_length, stick_thick = 2, 0.5, 1.7, 0.5
bowl_base_thick, bowl_outer_r, bowl_inner_r, bowl_corner_r = 3, 6, 8.5, 1/2
tip_r, tip_h = 1.4, 1

stick_base = s(stick_width, True).o(delta=-stick_corner_radius).o(r=stick_corner_radius)
stick = stick_base.o(r=stick_thick).e(stick_length + stick_thick) - stick_base.e(stick_length).z(-0.001)

outer = c(r=bowl_outer_r).y(bowl_outer_r + bowl_corner_r)
inner = c(r=bowl_inner_r).y(bowl_inner_r + bowl_base_thick - bowl_corner_r)
cut_tip_r, cut_tip_h = tip_r - bowl_corner_r, tip_h - bowl_corner_r
tip = poly(points=[(2*cut_tip_r, -cut_tip_h), (0, cut_tip_h), (-2*cut_tip_r, -cut_tip_h)]).y(bowl_base_thick)
bowl_section = (outer - inner + tip).o(r=bowl_corner_r) * s(100)
bowl = solid.rotate_extrude(segments=60)(bowl_section).z(stick_length)

(bowl + stick).dump_this()
