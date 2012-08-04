--http://springrts.com/wiki/Modinfo.lua
local modinfo = {
	name = "Warcraft 3",
	shortname = "W3",
	game = "W3",
	shortgame = "W3",
	description = "Warcraft 3 for the Spring Engine",
	url = "https://github.com/CamShaft/w3spring",
	version = "0.1", --when zipping .sdz for releasing make this a full integer like 1,2,3
	modtype = 1,
	depend = {
		"cursors.sdz",
	}
}
return modinfo