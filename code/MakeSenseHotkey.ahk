#SingleInstance, Force

XButton2::
MouseGetPos, X, Y
MouseClick, Left, 1074, 1022
MouseMove, X, Y
return

XButton1::
MouseGetPos, X, Y
MouseClick, Left, 848, 1021
MouseMove, X, Y
return


Left::
MouseGetPos, X, Y
Loop 100
	MouseClick, Left, 848, 1021
MouseMove, X, Y
return

Right::
MouseGetPos, X, Y
Loop 100
	MouseClick, Left, 1074, 1022
MouseMove, X, Y
return