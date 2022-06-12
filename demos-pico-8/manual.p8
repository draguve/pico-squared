print("hello world")
rectfill(80,80,120,100,12)
circfill(70,90,20,14)
for i=1,4 do print(i) end


x = 64  y = 64
function _update()
  if (btn(0)) then x=x-1 end
  if (btn(1)) then x=x+1 end
  if (btn(2)) then y=y-1 end
  if (btn(3)) then y=y+1 end
end
 
function _draw()
  cls(5)
  circfill(x,y,7,14)
end

-- use two dashes like this to write a comment
--[[ multi-line
comments ]]

num = 12/100
s = "this is a string"
b = false
t = {1,2,3}	

?0x11        -- 17
?0x11.4000   -- 17.25

?tostr(-32768,true)      -- 0x8000.0000
?tostr(32767.99999,true) -- 0x7fff.ffff

if not b then
  print("b is false")
else
  print("b is not false")
end

if x == 0 then
  print("x is 0")
elseif x < 0 then
  print("x is negative")
else
  print("x is positive")
end

if (4 == 4) then print("equal") end
if (4 ~= 3) then print("not equal") end
if (4 <= 4) then print("less than or equal") end
if (4 > 3) then print("more than") end

for x=1,5 do
  print(x)
end
-- prints 1,2,3,4,5

x = 1
while(x <= 5) do
  print(x)
  x = x + 1
end

for x=1,10,3 do print(x) end   -- 1,4,7,10

for x=5,1,-2 do print(x) end  -- 5,3,1

y=0
function plusone(x)
  local y = x+1
  return y
end
print(plusone(2)) -- 3
print(y)          -- 0

a={} -- create an empty table
a[1] = "blah"
a[2] = 42
a["foo"] = {1,2,3}

a = {11,12,13,14}
print(a[2]) -- 12

a = {[0]=10,11,12,13,14}
 
print(#a)   -- 4
add(a, 15)
print(#a)   -- 5

player = {}
player.x = 2 -- is equivalent to player["x"]
player.y = 3

if (not b) i=1 j=2

if not b then i=1 j=2 end

a += 2   -- equivalent to: a = a + 2

print(1 != 2) -- true
print("foo" == "foo") -- true (string are interned)

function _init()
  -- always start on white
  col = 7
end
 
function _update()
  -- press x for a random colour
  if (btnp(5)) col = 8 + rnd(8)
end
 
function _draw()
  cls(1)
  circfill(64,64,32,col)
end

::_::
cls()
for i=1,100 do
  a=i/50 - t()
  x=64+cos(a)*i
  y=64+sin(a)*i
  circfill(x,y,1,8+(i/4)%8)
end
flip()goto _

for y=0,127 do
  for x=0,127 do
    pset(x, y, x*y/8)
  end
end

while (true) do
  x, y = rnd(128), rnd(128)
  dx, dy = rnd(4)-2, rnd(4)-2
  pset(x, y, pget(dx+x, dy+y))
end

fset(2, 1 | 2 | 8)   -- sets bits 0,1 and 3
fset(2, 4, true)     -- sets bit 4
print(fget(2))       -- 27 (1 | 2 | 8 | 16)

?"hi"

?"the quick brown fox\0"

w = print("hoge", 0, -20) -- returns 16
pal({[12]=9, [14]=8})
pal({1,1,5,5,5,6,7,13,6,7,7,6,13,6,7,1}, 1)
palt(8, true) -- red pixels not drawn in subsequent sprite/tline draw calls
palt(0b1100000000000000)
fillp(0b0011010101101000)
circfill(64,64,20, 0x4e) -- brown and pink
-- checkboard with transparent squares
fillp(0b0011001111001100.1)

for i=0,15 do pal(i, i+i*16, 2) end  --  all other colours map to themselves
pal(12, 0x87, 2)                     --  remap colour 12 in the secondary palette
 
fillp(0b0011001111001100.01)         --  checkerboard palette, applied to sprites
spr(1, 64,64)                        --  draw the sprite

fillp(0b0011001111001100.001)
pal(12, 0x87, 2)
circfill(64,64,20,12)                -- red and white checkerboard circle

pal(3,12)
circfill(64,64,20,3)

tbl[#tbl + 1] = val

foo={}        -- create empty table
add(foo, 11)
add(foo, 22)
print(foo[2]) -- 22

a={1,10,2,11,3,12}
for item in all(a) do
  if (item < 10) then del(a, item) end
end
foreach(a, print) -- 10,11,12
print(a[3])       -- 12

t = {["hello"]=3, [10]="blah"}
t.blue = 5;
for k,v in pairs(t) do
  print("k: "..k.."  v:"..v)
end

poke(0x5f5c, delay) -- set the initial delay before repeating. 255 means never repeat.
poke(0x5f5d, delay) -- set the repeating delay.

sfx(3)    --  play sfx 3
sfx(3,2)  --  play sfx 3 on channel 2
sfx(3,-2) --  stop sfx 3 from playing on any channel
sfx(-1,2) --  stop whatever is playing on channel 2
sfx(-2,2) --  release looping on channel 2
sfx(-1)   --  stop all sounds on all channels
sfx(-2)   --  release looping on all channels

music(0, 1000)

map(0, 0, 20, 20, 4, 2)
map(0, 0, 0, 0, 128, 64)
camera(pl.x - 64, pl.y - 64)
map()
poke(0x5f38, 8)
poke(0x5f39, 4)
tline(...)
poke(0x5f3a, offset_x)
poke(0x5f3b, offset_y)

x = @addr  -- peek(addr)
y = %addr  -- peek2(addr)
z = $addr  -- peek4(addr)

function _draw()
  cls()
  circ(64, 64, 20, 7)
  x = 64 + cos(t()) * 20
  y = 64 + sin(t()) * 20
  line(64, 64, x, y)
end

p8cos = cos function cos(angle) return p8cos(angle/(3.1415*2)) end
p8sin = sin function sin(angle) return -p8sin(angle/(3.1415*2)) end

x=20 y=30
function _update()
  if (btn(0)) x-=2
  if (btn(1)) x+=2
  if (btn(2)) y-=2
  if (btn(3)) y+=2
end
 
function _draw()
  cls()
  circfill(x,y,2,14)
  circfill(64,64,2,7)
   
  a=atan2(x-64, y-64)
  print("angle: "..a)
  line(64,64,
    64+cos(a)*10,
    64+sin(a)*10,7)
end

function _draw()
  cls()
  srand(33)
  for i=1,100 do
    pset(rnd(128),rnd(128),7)
  end
end

x = 0b1010
y = 0b0110

band(x, y) -- both bits are set
bor(x, y)  -- either bit is set
bxor(x, y) -- either bit is set, but not both of them
bnot(x)    -- each bit is not set
shl(x, n)  -- shift left n bits (zeros come in from the right)
shr(x, n)  -- arithmetic right shift (the left-most bit state is duplicated)
lshr(x, n) -- logical right shift (zeros comes in from the left)
rotl(x, n) -- rotate all bits in x left by n places
rotr(x, n) -- rotate all bits in x right by n places

menuitem(1, "restart puzzle",
  function() reset_puzzle() sfx(10) end
)

menuitem(1, "foo",
  function(b) if (b&1 > 0) then printh("left was pressed") end end
)

s = "the quick"
s = 'brown fox';
s = [[
  jumps over
  multiple lines
]]
print(#s)
print("three "..4) --> "three 4"
print(2+"3")   --> 5

tostr(17)       -- "17"
tostr(17,0x1)   -- "0x0011.0000"
tostr(17,0x3)   -- "0x00110000"
tostr(17,0x2)   -- "1114112"

tonum("17.5")  -- 17.5
tonum(17.5)    -- 17.5
tonum("hoge")  -- no return value

tonum("ff",       0x1)  -- 255
tonum("1114112",  0x2)  -- 17
tonum("1234abcd", 0x3)  -- 0x1234.abcd

chr(64)                    -- "@"
chr(104,101,108,108,111)   -- "@"

ord("@")         -- 64
ord("123",2)     -- 50 (the second character: "2")
ord("123",2,3)   -- 50,51,52

s = "the quick brown fox"
print(sub(s,5,9))   --> "quick"
print(sub(s,5))     --> "quick brown fox"
print(sub(s,5,_))   --> "q"

split("1,2,3")               -- {1,2,3}
split("one:two:3",":",false) -- {"one","two","3"}
split("1,,2,")               -- {1,"",2,""}

print(type(3))
print(type("3"))

cstore(0,0,0x2000, "sprite sheet.p8")
-- later, restore the saved data:
reload(0,0,0x2000, "sprite sheet.p8")

cartdata("zep_dark_forest")
dset(0, score)

t = 0
function _draw()
 cls(5)
 for i=0,7 do
  val = 0
  if (t % 2 < 1) val = 255
  poke(0x5f80 + i, val)
  circfill(20+i*12,64,4,val/11)
 end
 t += 0.1
end

val = 42          -- value to send
dat = 16 clk = 15 -- data and clock pins depend on device
poke(0x4300,0)    -- data to send (single bytes: 0 or 0xff)
poke(0x4301,0xff)
for b=0,7 do
  -- send the bit (high first)
  serial(dat, band(val, shl(1,7-b))>0 and 0x4301 or 0x4300, 1)
  -- cycle the clock
  serial(clk, 0x4301)
  serial(0xff, 5) -- delay 5
  serial(clk, 0x4300)
  serial(0xff, 5) -- delay 5
end

vec2d={
 __add=function(a,b)
  return {x=(a.x+b.x), y=(a.y+b.y)}
 end
}
 
v1={x=2,y=9} setmetatable(v1, vec2d)
v2={x=1,y=5} setmetatable(v2, vec2d)
v3 = v1+v2
print(v3.x..","..v3.y) -- 3,14

function preprint(pre, s, ...)
  local s2 = pre..tostr(s)
  print(s2, ...) -- pass the remaining arguments on to print()
end

function foo(...)
  local args={...} -- becomes a table of arguments
  foreach(args, print)
  ?select("#",...)    -- alternative way to count the number of arguments
  foo2(select(3,...)) -- pass arguments from 3 onwards to foo2()
end

function hey()
  print("doing something")
  yield()
  print("doing the next thing")
  yield()
  print("finished")
end
 
c = cocreate(hey)
for i=1,3 do coresume(c) end

x = (11%4)-2
y = (11/4)-8