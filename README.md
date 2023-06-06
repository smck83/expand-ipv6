# expand-ipv6
FastAPI app that takes a IPv6 address in compressed notation and responds with the full, dot notation, as well as providing it in reverse (for RBL)


e.g. Send a GET request to
`http://localhost:8000/ipAddress/?ip6=2607:f8b0:4023:1004:0000:0000:0000:001b'

and receive the following response

````
{
  "ipv6": "2607:f8b0:4023:1004::1b",
  "exploded": "2607:f8b0:4023:1004:0000:0000:0000:001b",
  "reversed": "b100000000000000400132040b8f7062",
  "dotNotation": "b.1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.4.0.0.1.3.2.0.4.0.b.8.f.7.0.6.2",
  "error": [
    false
  ]
}
````
