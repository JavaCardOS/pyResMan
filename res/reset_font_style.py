file_src = open('pyResManDialogBase.fbp', 'r')
src_lines = file_src.readlines()
file_src.close()

file_dest = open('pyResManDialogBase2.fbp', 'w')
for src_line in src_lines:
    if src_line.find('<property name="font"') == -1:
        file_dest.write(src_line)
file_dest.close()
