# Component 3B: Provide 3 different scenarios for the Pythagoras questions

questions = ["In a right angle triangle ABC, the hypotenuse AB has a\nlength of {}, while another side AC has "
             "a length of {}.\n\nWork out the length of BC using Pythagoras Theorem", "In an isosceles triangle ABC, "
             "sides AB and AC have the same length. A\nline perpendicular to BC is drawn from point A, touching line B"
             "C at a\npoint, D. Line AD has a length of {}, and Line BC has a length of {}.\n\nWork out the length of "
             "AC using Pythagoras Theorem", "In a right angle triangle XYZ, line XZ is the hypotenuse, XY\nhas a lengt"
             "h of {}, and another side YZ has a length of {}.\n\nWork out the length of XZ using Pythagoras Theorem",
             "In an isosceles right triangle TUV, side TU is\nthe hypotenuse, and has a length of {}.\n\nFind the leng"
             "th of side VU using Pythagoras Theorem"]

for i in range(0, 4):
    print(questions[i])
