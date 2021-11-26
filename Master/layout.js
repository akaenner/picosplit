var layout = `
// Do not modify the content above this line

keyboard
tap_timeout=0.15
long_tap_timeout=0.4

layout
name=US macOS

layer
name=Base
 1 : tap=Codes[ Q ]     		: long_tap=Shift
 2 : tap=Codes[ W ]     		: long_tap=Shift
 3 : tap=Codes[ E ]     		: long_tap=Shift
 4 : tap=Codes[ R ]     		: long_tap=Shift
 5 : tap=Codes[ T ]     		: long_tap=Shift
 6 : tap=Codes[ A ]     		: long_tap=Shift 	: hold=Codes[ LEFT_GUI ]
 7 : tap=Codes[ S ]     		: long_tap=Shift 	: hold=Codes[ LEFT_ALT ]
 8 : tap=Codes[ D ]     		: long_tap=Shift 	: hold=Codes[ LEFT_CONTROL ]
 9 : tap=Codes[ F ]     		: long_tap=Shift 	: hold=Codes[ LEFT_SHIFT ]
10 : tap=Codes[ G ]     		: long_tap=Shift
11 : tap=Codes[ Z ]     		: long_tap=Shift
12 : tap=Codes[ X ]     		: long_tap=Shift 	: hold=Codes[ RIGHT_ALT ] 
13 : tap=Codes[ C ]     		: long_tap=Shift 
14 : tap=Codes[ V ] 			: long_tap=Shift 
15 : tap=Codes[ B ] 			: long_tap=Shift 
17 : tap=ChangeLayer( Special )
18 : tap=Codes[ ESCAPE ]  							: hold=ChangeLayer( Umlaut )  
19 : tap=Codes[ SPACE ] 							: hold=ChangeLayer( Navigation ) 
20 : tap=Codes[ TAB ] 								
21 : tap=Codes[ Y ] 			: long_tap=Shift
22 : tap=Codes[ U ] 			: long_tap=Shift
23 : tap=Codes[ I ] 			: long_tap=Shift  
24 : tap=Codes[ O ] 			: long_tap=Shift
25 : tap=Codes[ P ] 			: long_tap=Shift 
26 : tap=Codes[ H ] 			: long_tap=Shift
27 : tap=Codes[ J ] 			: long_tap=Shift 	: hold=Codes[ LEFT_SHIFT ]
28 : tap=Codes[ K ] 			: long_tap=Shift 	: hold=Codes[ LEFT_CONTROL ]  
29 : tap=Codes[ L ] 			: long_tap=Shift 	: hold=Codes[ LEFT_ALT ]  
30 : tap=Codes[ QUOTE ] 		: long_tap=Shift 	: hold=Codes[ LEFT_GUI ]
31 : tap=Codes[ N ] 			: long_tap=Shift
32 : tap=Codes[ M ] 			: long_tap=Shift  
33 : tap=Codes[ COMMA ] 		: long_tap=Shift
34 : tap=Codes[ PERIOD ] 		: long_tap=Shift 	: hold=Codes[ RIGHT_ALT ]  
35 : tap=Codes[ FORWARD_SLASH ] : long_tap=Shift
36 : tap=Codes[ ENTER ] 							: hold=ChangeLayer( Symbols )
37 : tap=Codes[ BACKSPACE ] 						: hold=ChangeLayer( Numeric )
38 : tap=Codes[ DELETE ] 							: hold=ChangeLayer( Umlaut ) 
40 : tap=ChangeLayer( Function )
       
layer
name=Media
	
layer
name=Navigation
22 : tap=Codes[ LEFT_GUI, Z ]
23 : tap=Codes[ LEFT_GUI, X ]
24 : tap=Codes[ LEFT_GUI, C ]
25 : tap=Codes[ LEFT_GUI, V ]
26 : tap=Codes[ CAPS_LOCK ] 
27 : tap=Codes[ LEFT_ARROW ]
28 : tap=Codes[ DOWN_ARROW ] 
29 : tap=Codes[ UP_ARROW ]
30 : tap=Codes[ RIGHT_ARROW ]
31 : tap=Codes[ INSERT ] 
32 : tap=Codes[ HOME ]
33 : tap=Codes[ PAGE_UP ] 
34 : tap=Codes[ PAGE_DOWN ]
35 : tap=Codes[ END ]
36 : tap=Codes[ ENTER ]
37 : tap=Codes[ BACKSPACE ]
38 : tap=Codes[ DELETE ]

layer
name=Symbols
 1 : tap=Codes[ LEFT_SHIFT, LEFT_BRACKET ]
 2 : tap=Codes[ LEFT_SHIFT, SEVEN ]
 3 : tap=Codes[ LEFT_SHIFT, EIGHT ]
 4 : tap=Codes[ LEFT_SHIFT, NINE ]
 5 : tap=Codes[ LEFT_SHIFT, RIGHT_BRACKET ]
 6 : tap=Codes[ LEFT_SHIFT, SEMICOLON ]
 7 : tap=Codes[ LEFT_SHIFT, FOUR ]
 8 : tap=Codes[ LEFT_SHIFT, FIVE ]
 9 : tap=Codes[ LEFT_SHIFT, SIX ]
10 : tap=Codes[ LEFT_SHIFT, EQUALS ]
11 : tap=Codes[ LEFT_SHIFT, GRAVE_ACCENT ]
12 : tap=Codes[ LEFT_SHIFT, ONE ]
13 : tap=Codes[ LEFT_SHIFT, TWO ]
14 : tap=Codes[ LEFT_SHIFT, THREE ]
15 : tap=Codes[ LEFT_SHIFT, BACKSLASH ]
18 : tap=Codes[ LEFT_SHIFT, NINE ]
19 : tap=Codes[ LEFT_SHIFT, ZERO ]
20 : tap=Codes[ LEFT_SHIFT, MINUS ]

layer
name=Numeric
 1 : tap=Codes[ LEFT_BRACKET ] 	: long_tap=Shift
 2 : tap=Codes[ SEVEN ]    		: long_tap=Shift
 3 : tap=Codes[ EIGHT ] 		: long_tap=Shift
 4 : tap=Codes[ NINE ] 			: long_tap=Shift
 5 : tap=Codes[ RIGHT_BRACKET ] : long_tap=Shift
 6 : tap=Codes[ SEMICOLON ] 	: long_tap=Shift
 7 : tap=Codes[ FOUR ] 			: long_tap=Shift
 8 : tap=Codes[ FIVE ] 			: long_tap=Shift
 9 : tap=Codes[ SIX ] 			: long_tap=Shift
10 : tap=Codes[ EQUALS ]		: long_tap=Shift
11 : tap=Codes[ GRAVE_ACCENT ] 	: long_tap=Shift
12 : tap=Codes[ ONE ] 			: long_tap=Shift
13 : tap=Codes[ TWO ] 			: long_tap=Shift
14 : tap=Codes[ THREE ] 		: long_tap=Shift
15 : tap=Codes[ BACKSLASH ] 	: long_tap=Shift
18 : tap=Codes[ PERIOD ]
19 : tap=Codes[ ZERO ]
20 : tap=Codes[ MINUS ]
        
layer
name=Function
 1 : tap=Codes[ F12 ]
 2 : tap=Codes[ F7 ]
 3 : tap=Codes[ F8 ]
 4 : tap=Codes[ F9 ]
 5 : tap=Codes[ PRINT_SCREEN ]
 6 : tap=Codes[ F11 ]
 7 : tap=Codes[ F4 ]
 8 : tap=Codes[ F5 ]
 9 : tap=Codes[ F6 ]
10 : tap=Codes[ SCROLL_LOCK ] 
11 : tap=Codes[ F10 ] 
12 : tap=Codes[ F1 ] 
13 : tap=Codes[ F2 ] 
14 : tap=Codes[ F3 ] 
15 : tap=Codes[ PAUSE ]
18 : tap=ResetKeyboard
        
layer
name=Special
18 : tap=ResetKeyboard
                
layer
name=Umlaut
 6 : tap=Sequence[Codes[ LEFT_ALT, U ]; Codes[ A ]] : long_tap=Sequence[Codes[ LEFT_ALT, U ]; Codes[ LEFT_SHIFT, A ]] : hold=Codes[ LEFT_GUI ]
 7 : tap=Codes[ LEFT_ALT, S ] : hold=Codes[ LEFT_ALT ]
22 : tap=Sequence[Codes[ LEFT_ALT, U ]; Codes[ U ]] : long_tap=Sequence[Codes[ LEFT_ALT, U ]; Codes[ LEFT_SHIFT, U ]] : hold=Codes[ LEFT_GUI ]
24 : tap=Sequence[Codes[ LEFT_ALT, U ]; Codes[ O ]] : long_tap=Sequence[Codes[ LEFT_ALT, U ]; Codes[ LEFT_SHIFT, O ]] : hold=Codes[ LEFT_GUI ]

// Do not modify the content below this line 
`
        
