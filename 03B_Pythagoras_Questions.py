# Component 3B: Provide 3 different scenarios for the Pythagoras questions

import random

questions = ["In a right angle triangle ABC, the hypotenuse AB has a\nlength of {}, while another side AC has "
             "a length of {}.\n\nWork out the length of BC using Pythagoras Theorem", "In an isosceles triangle ABC, "
             "sides AB and AC have the same length. A\nline perpendicular to BC is drawn from point A, touching line BC "
             "at a\npoint, D. Line AD has a length of {}, and Line BC has a length of {}.\n\nWork out the length of AC "
             "using Pythagoras Theorem", "In a right angle triangle XYZ, line XZ is the hypotenuse, XY\nhas a length of "
             "{}, and another side YZ has a length of {}.\n\nWork out the length of XZ using Pythagoras Theorem", "In an "
             "isosceles right triangle TUV, side TU is\nthe hypotenuse, and has a length of {}.\n\nFind the length of side "
             "VU using Pythagoras Theorem"]

question_number = random.randint(0, 3)
print(questions[question_number])
