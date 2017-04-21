physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
physics_mean = sum(physics_scores) / len(physics_scores)
history_mean = sum(history_scores) / len(history_scores)
physics_mean_squares = [ (element - physics_mean)**2 for element in physics_scores];
history_mean_squares = [ (element - history_mean)**2 for element in history_scores];
physics_std = (sum(physics_mean_squares) / len(physics_scores))**(1/2)
history_std = (sum(history_mean_squares) / len(history_scores))**(1/2)
z_physics = [(element - physics_mean) / physics_std for element in physics_scores];
z_history = [(element - history_mean) / history_std for element in history_scores];
coefficient = 0;
for i in range(0, len(physics_scores)):
    coefficient += z_physics[i] * z_history[i];
coefficient = coefficient / (len(physics_scores) - 1);
print(coefficient)
