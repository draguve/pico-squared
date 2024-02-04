pico-8 cartridge // http://www.pico-8.com
version 41
__lua__
function tostring(any)
    if type(any)=="function" then 
        return "function" 
    end
    if any==nil then 
        return "nil" 
    end
    if type(any)=="string" then
        return any
    end
    if type(any)=="boolean" then
        if any then return "true" end
        return "false"
    end
    if type(any)=="table" then
        local str = "{ "
        for k,v in pairs(any) do
            str=str..tostring(k).."->"..tostring(v).." "
        end
        return str.."}"
    end
    if type(any)=="number" then
        return ""..any
    end
    return "unkown" -- should never show
end

function test(arg,...)
	local dict = {...}
	x,y,z = ...
	print(tostring(dict))
	print(tostring(x))
	print(tostring(y))
	print(tostring(z))
end

test("a","b","c","f")

function test(arg,...)
	local dict = {...}
	x,y,z = ...,10
	print(tostring(dict))
	print(tostring(x))
	print(tostring(y))
	print(tostring(z))
end

test("a","b","c","f")

function test(arg,...)
	local dict = {...}
	x,y,z = 10,...
	print(tostring(dict))
	print(tostring(x))
	print(tostring(y))
	print(tostring(z))
end

function test(arg,...)
	local dict = {...}
	x,y,z = 10,...
	print(tostring(dict))
	print(tostring(x))
	print(tostring(y))
	print(tostring(z))
end

test("a","b","c","f")
test("a","b")

--does not work
--function test(arg,...)
--	print(tostring(...[1]))
--end

__gfx__
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00700700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00077000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00077000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00700700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
