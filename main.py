import winsound, keyboard, time

try:

	import pystyle

except ModuleNotFoundError:

	print('Ugh, you really don\'t have  pystyle installed ?')

	time.sleep(2)

	__import__('os').system('pip install pystyle')

	__import__('os').system('pause')

	__import__('os').system('py main.py')

pystyle.Anime.Fade(pystyle.Center.Center('''
                         !*:            !!        
                      :%&§§#:          %§§&!      
                    :$#§§§§/:       :: !&§§/%     
                  !@/§§§§§§/:      @/#%  $§§§$    
               :*&§§§§§§§§§/:      %§§§@  %§§§%   
  :***********%#§§§§§§§§§§§/: !@@!  */§§@  $§§/!  
  @§§§§§§§§§§§§§§§§§§§§§§§§/: $§§§*  *§§§* :#§§&  
  &§§§§§§§§§§§§§§§§§§§§§§§§/:  $§§/!  @§§#: %§§/! 
  &§§§§§§§§§§§§§§§§§§§§§§§§/:   #§§@  *§§§! :/§§% 
  &§§§§§§§§§§§§§§§§§§§§§§§§/:   $§§#  :/§§* :#§§$ 
  &§§§§§§§§§§§§§§§§§§§§§§§§/:   @§§&  !/§§* :/§§% 
  &§§§§§§§§§§§§§§§§§§§§§§§§/:  !/§§%  %§§/: !§§§* 
  &§§§§§§§§§§§§§§§§§§§§§§§§/: !#§§&: :#§§@  $§§/: 
  *&&&&&&&&&&&/§§§§§§§§§§§§/: $§§&:  @§§/: !/§§%  
              :%#§§§§§§§§§§/: :!!  :@§§/* :#§§&:  
                 *&§§§§§§§§/:      &§§#! :&§§#:   
                   !$/§§§§§/:      *$$: !#§§#!    
                     :%#§§§/:          %§§§@:     
                       :*&#$           *&&%       '''), pystyle.Colors.black_to_white, pystyle.Colorate.Horizontal, enter=True)


print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_red, pystyle.Center.XCenter("""
 ___      ___     ______  ___________  __    __    _______   _______   
|"  \    /"  |   /    " \("     _   ")/" |  | "\  /"     "| /"      \ 
 \   \  //   |  // ____  \)__/  \\__/(:  (__)  :)(: ______)|:        |
 /\\  \/.    | /  /    ) :)  \\_ /    \/      \/  \/    |  |_____/   )
|: \.        |(: (____/ //   |.  |    //  __  \\  // ___)_  //      / 
|.  \    /:  | \        /    \:  |   (:  (  )  :)(:      "||:  __   \ 
|___|\__/|___|  \"_____/      \__|    \__|  |__/  \_______)|__|  \___)
                                                                       

             1.One beep					 	              2.Piano
""")))

Choice = int(pystyle.Write.Input("Choice > ", pystyle.Colors.blue_to_green))
if Choice == 1:

	winsound.Beep(int(pystyle.Write.Input("Fréquence > ", pystyle.Colors.green_to_blue)), int(pystyle.Write.Input("Temps (secondes) > ", pystyle.Colors.blue_to_green))*1000)

elif Choice == 2:

	while True:

		if keyboard.is_pressed('a'):

			winsound.Beep(261, 500)
		
		elif keyboard.is_pressed('z'):

			winsound.Beep(293, 500)

		elif keyboard.is_pressed('e'):

			winsound.Beep(329, 500)
		
		elif keyboard.is_pressed('r'):

			winsound.Beep(349, 500)
		
		elif keyboard.is_pressed('t'):

			winsound.Beep(392, 500)
		
		elif keyboard.is_pressed('y'):

			winsound.Beep(440, 500)

		elif keyboard.is_pressed('u'):

			winsound.Beep(493, 500)

		elif keyboard.is_pressed('i'):

			winsound.Beep(523, 500)
