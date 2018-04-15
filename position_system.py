from filter import IrregularDoubleExponentialFilter
from parameters import camera_y_offset, move_dist_smoothing_factors, heading_smoothing_factors
from position import Position, ZERO_POS


class PositionSystem:
    
    def __init__(self):
        self._move_dist_filter = IrregularDoubleExponentialFilter(*move_dist_smoothing_factors)
        self._heading_filter = IrregularDoubleExponentialFilter(*heading_smoothing_factors)
        self.last_ball_loc = ZERO_POS
    
    def calc_ball_movement(self, dist_to_ball, angle_to_ball, vehicle_xy_theta,
                           time_elapsed):
        # calculate xy dif from vehicle
        rel_ball_pos = ZERO_POS.pos_from_dist_angle(dist_to_ball, angle_to_ball)
        rel_ball_pos = rel_ball_pos.pos_from_xy_dif(
            Position(0, camera_y_offset))
        
        # rotate rel xy offset then add to vehicle_pos to find the ball's
        # absolute position
        vehicle_pos, vehicle_theta = vehicle_xy_theta
        abs_ball_pos = vehicle_pos.pos_from_xy_angle_dif(rel_ball_pos,
                                                         vehicle_theta)
        
        # find dist and angle of ball from ball's last position
        ball_move_dist, ball_heading = \
            self.last_ball_loc.relative_dist_angle_to(abs_ball_pos)
        self.last_ball_loc = abs_ball_pos
        
        ball_move_dist = self._move_dist_filter.filter(ball_move_dist)
        ball_heading = self._heading_filter.filter(ball_heading)
        
        # find the relative position of the vehicle from the ball's pov
        rel_pos_from_ball_pov = ZERO_POS.pos_from_dist_angle(dist_to_ball,
                                                             angle_to_ball -
                                                             ball_heading)
        
        ball_speed = ball_move_dist/time_elapsed
        return rel_pos_from_ball_pov, ball_heading, ball_speed
