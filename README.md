# expand-ipv6
FastAPI app that takes a IPv4 or IPv6(compressed & exploded) address and responds with the full, dot notation, as well as providing it in reverse (for RBL)


e.g. Send a GET request with IPv6 address:
`http://localhost:8000/ipAddress/?ip=2001:4860:4000::`

and receive the following response

````
{
  "sourceIP": "2001:4860:4000::",
  "exploded": "2001:4860:4000:0000:0000:0000:0000:0000",
  "ipv": 6,
  "dotNotation": "2.0.0.1.4.8.6.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0",
  "reversedDotNotation": "0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.4.0.6.8.4.1.0.0.2",
  "error": [
    false
  ]
}
````

This is particularly useful when dealing with IPv6 addresses with SPF records, where they need to be parsed in dot notation, and often reversed.


e.g. Send a GET request with IPv4 address:
`http://localhost:8000/ipAddress/?ip=192.0.2.1`

and receive the following response

````
{
  "sourceIP": "192.0.2.1",
  "ipv": 4,
  "dotNotation": "192.0.2.1",
  "reversedDotNotation": "1.2.0.291",
  "error": [
    false
  ]
}
````

Try it out in docker:
`docker run -it -p 8000:8000 smck83/expand-ipv6`
