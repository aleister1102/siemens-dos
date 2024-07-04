# Siemens S7-1200 PLC - Denial of Service

## Setup

- Siemens TIA Portal Installation Guide: https://controlbyte.tech/blog/siemens-tia-portal-installation-and-troubleshooting/
- Download TIA Portal and PLC SIM: https://support.industry.siemens.com/cs/document/109784440/simatic-step-7-incl-safety-s7-plcsim-and-wincc-v17-trial-download?dti=0&lc=en-VN
- Automation License Manager: https://support.industry.siemens.com/cs/document/114358/handling-programs-for-authorization-or-licensing-of-simatic-products-(alm-authors)?dti=0&lc=en-VN

## Protocols

- ISO transport arrives on top of the TCP (TSAP): https://datatracker.ietf.org/doc/html/rfc983
- ISO over TCP: 
    - TPKT: https://datatracker.ietf.org/doc/html/rfc1006, https://wiki.wireshark.org/TPKT
    - COTP: https://datatracker.ietf.org/doc/html/rfc905/, https://wiki.wireshark.org/COTP
- S7 Plus: 
    - https://blog.viettelcybersecurity.com/security-wall-of-s7commplus-part-1/
    - https://blog.viettelcybersecurity.com/security-wall-of-s7commplus-3/
- S7: 
    - General structure: http://gmiru.com/article/s7comm/
    - Job and ACK messages: http://gmiru.com/article/s7comm-part2/
    - Constants: 
        - http://gmiru.com/resources/s7proto/constants.txt
        - https://dokuwiki.hampel-soft.com/kb/production/s7-communication/constants

## Firmware

- MC7: https://www.pnfsoftware.com/blog/reversing-simatic-s7-plc-programs/

## Libraries

- Snap 7: https://snap7.sourceforge.net/
- PLC4x: https://plc4x.apache.org/
- S7.Net: https://github.com/S7NetPlus/s7netplus

## Attacks
- Rouge 7:
    - https://www.youtube.com/watch?v=dHxsctLBUEI
    - https://i.blackhat.com/USA-19/Thursday/us-19-Bitan-Rogue7-Rogue-Engineering-Station-Attacks-On-S7-Simatic-PLCs-wp.pdf