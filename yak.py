import pyak as pk

# replace 00's with your location
location = pk.Location(40.423705, -86.921195)
testyakker = pk.Yakker(None, location, False)
yaklist = testyakker.get_yaks()
for yak in yaklist:
    yak.print_yak()