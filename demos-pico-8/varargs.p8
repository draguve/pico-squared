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

function test1(arg,...)
	local dict = {...}
	x,y,z = ...
	print(tostring(dict))
	print(tostring(x))
	print(tostring(y))
	print(tostring(z))
end

test1("a","b","c","f")

function test2(arg,...)
	local dict = {...}
	x,y,z = ...,10
	print(tostring(dict))
	print(tostring(x))
	print(tostring(y))
	print(tostring(z))
end

test2("a","b","c","f")

function test3(arg,...)
	local dict = {...}
	x,y,z = 10,...
	print(tostring(dict))
	print(tostring(x))
	print(tostring(y))
	print(tostring(z))
end

test3("a","b","c","f")
test3("a","b")

print("---------5--------")

function test4(...)
	local dict = {...}
	print(tostring(dict))
end

function test5(...)
	test4(...)
end

test5("a","b")

print("---------6--------")

function test6(...)
	test4("12",...)
end

test6("a","b")

print("---------7--------")

-- does not emit working code here

function check1(a)
	print(a)
end

function test7(...)
	check1(...)
end

test7("a","b")

print("---------8--------")

function check2(a,b,c)
	print(a)
	print(b)
	print(c)
end

function test8(...)
	check2(...)
end

test8("a","b")

print("---------9--------")

function check3(a,b,c)
	print(a)
	print(b)
	print(c)
end

function test9(...)
	check3("x",...,"z")
end

test9("a","b")

--[[
crashes
function test10()
	check(...)
end 

test10() 
--]]

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
