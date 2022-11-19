-- HEAD --

description = [[
This is a simple script example that determines if a port is open.
]]

author = "Jon Salhus"
-- RULE --

portrule = function(host, port)
	return port.protocol == "tcp"
		and port.state == "open"
end
-- ACTION --

action = function(host, port)
	return "This port is open!"
end
