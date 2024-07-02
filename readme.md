# Siemens S7 DoS on port 102

## Setup

- Siemens TIA Portal Installation Guide: https://controlbyte.tech/blog/siemens-tia-portal-installation-and-troubleshooting/
- Download TIA Portal: https://support.industry.siemens.com/cs/document/109772803/simatic-step-7-incl-safety-and-wincc-v16-trial-download?dti=0&lc=en-VN

## Protocols

- S7: 
    - General structure: http://gmiru.com/article/s7comm/
    - Job and ACK messages: http://gmiru.com/article/s7comm-part2/
    - Constants: http://gmiru.com/resources/s7proto/constants.txt
    - https://wiki.wireshark.org/S7comm
- ISO over TCP: 
    - TPKT: https://datatracker.ietf.org/doc/html/rfc1006, https://wiki.wireshark.org/TPKT
    - COTP: https://datatracker.ietf.org/doc/html/rfc905/, https://wiki.wireshark.org/COTP
- ISO transport arrives on top of the TCP (TSAP): https://datatracker.ietf.org/doc/html/rfc983

Additional:
- S7 Plus (with encryption): https://blog.viettelcybersecurity.com/security-wall-of-s7commplus-part-1/

## Libraries

- Snap 7: https://snap7.sourceforge.net/
- PLC4x: https://plc4x.apache.org/
