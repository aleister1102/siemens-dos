# RFC 1006 (TPKT)

Ref: https://datatracker.ietf.org/doc/html/rfc1006

## Introduction

ARPA Internet protocol suite and the ISO protocol suite are both layered systems.

A layer is defined by one definition: a protocol definition, which describes the rules which each service-peer uses when communicating with other service-peers. The service-provider (the layer) uses the protocol and services from the layer below to offer the its service to the layer above.

## Model

The ISO transport service definition describes the services offered by the TS-provider (transport service) and the interfaces used to access those services.

```txt
+-----------+                                       +-----------+
|  TS-user  |                                       |  TS-user  |
+-----------+                                       +-----------+
    |                                                     |
    | TSAP interface                       TSAP interface |
    |  [ISO8072]                                          |
    |                                                     |
+----------+   ISO Transport Services on the TCP     +----------+
|  client  |-----------------------------------------|  server  |
+----------+              (this memo)                +----------+
    |                                                     |
    | TCP interface                         TCP interface |
    |  [RFC793]                                           |
    |                                                     |
```

Where:
- TS-peer: a process which implements the protocol described by this memo
- TS-user: a process talking using the services of a TS-peer
- TS-provider: the black-box entity implementing the protocol described by this memo
