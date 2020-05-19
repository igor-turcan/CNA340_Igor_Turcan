eightteen = 200
twentysix = 150
sixtyfive = 120
age = int( input( 'Enter your age: \n' ) )
nights = int( input( 'Enter nights: \n' ) )

if age < 18:
    print( 'You are too young to rent a room.' )
if age > 17:
    if age > 17 and age < 25 or age == 18:
        print( 'Your nightly rate is: ${:.2f}'.format( eightteen ) )
        print( 'Your total cost is: ${:.2f}'.format( eightteen * nights ) )
    if age > 26 and age < 64 or age == 25 or age == 64:
        print( 'Your nightly rate is: ${:.2f}'.format( twentysix ) )
        print( 'Your total cost is: ${:.2f}'.format( twentysix * nights ) )
    if age > 64:
        print( 'Your nightly rate is: ${:.2f}'.format( sixtyfive ) )
        print( 'Your total cost is: ${:.2f}'.format( sixtyfive * nights ) )
