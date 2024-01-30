pico-8 cartridge // http://www.pico-8.com
version 41
__lua__
player_pos = {20, 60}

function get_pos()
    print("12")
end

function move_player(newx, newy)
  player_pos = {newx, newy}
end

function draguve(x)
	if(x==0) then
		print("test_a")
		return
	end
	print("test")
	return 0
end

function distance(x1, y1, x2, y2)
  return sqrt((x2 - x1)^2 + (y2 - y1)^2)
end

function circumference(r)
  -- a local variable
  local pi = 3.14
  return 2 * pi * r
end
--[[
anonymousfunctions(function()
  print(x)
end)

foreach(x, function(v) print(v^2) end)
]]--
__gfx__
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00700700005550000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00077000005550000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00077000005550000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00700700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
__map__
0000000000000000010000000100010100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
0000000000000000010000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
0000010101010100010000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
0000000000010100010000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
0000000000000100000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
0000000000000100010000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
0000000000000100010000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
__sfx__
000100000000000000000000000000000250502505025050240502405024050240502505025050250502505025050250500000000000000000000000000000000000000000000000000000000000000000000000
0010000000000000000000000000291502a1502b1502b1502c1502c1502d1502d1502e1502e1502e1502f1502f1502f1502f1502e1502d1500000000000000000000000000000000000000000000000000000000
__music__
00 41424344
00 41424344
07 41424344

