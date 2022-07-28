<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->
<!-- # Zowe Security Policy-->

<div class="row" style="padding: 5%">

# Respond to Vulnerabilities Policy
<!--<div style="display:none" hidden>(Zowe-SSDP-SDLC ID: ZSSD-LP:RV)</div>-->

This Security Policy governs how Zowe handles vulnerabilities identification, mitigation and disclosure.

Our policy is based on the <a href="https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure">Coordinated Vulnerability Disclosure (CVD) Policy</a>
which is also adopted by many other organizations, <a href="https://www.cisa.gov/coordinated-vulnerability-disclosure-process">CISA</a> and <a href="https://www.etsi.org/standards/coordinated-vulnerability-disclosure">ETSI</a> among them. 
Zowe adapts the following 5 CVD topics to declare complete set of policy requirements for Respond to Vulnerabilities:
* [Security issues identification](#security-issues-identification) <!-- <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM)</span> -->
* [Security issues analysis and assessment](#analysis-and-assessment)
* [Security issues mitigation](#security-issues-mitigation)
* [Security issues disclosure](#security-issues-disclosure) <!-- <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-VDR)</span> -->
* [Solution publishing](#solution-publishing)

The topics listed above contain sets of applicable requirements. Where appropriate the fulfilment of these requirements may be governed by internal processes and guidance. 
In such cases, a detailed description of the corresponding processes and guidance is provided in separate documents.

    NOTE: Wherever appropriate, the policy requirements are mapped to the NIST SSDF Respond to Vulnerabilities (RV) Best practices - see https://csrc.nist.gov/publications/detail/sp/800-218/final 
          and/or to the Open Source Security Foundation (OpenSSF) Best Practices] - see https://openssf.org/ (former Core Infrastructure Iniitative) - see https://www.coreinfrastructure.org/.
          The mappings are part of this document but are provided as comments and those are not rendered in the markdown viewer. 

The individual requirements may be a responsibility of a single participant or the responsibilities could be shared between multiple cooperating participants.

The main participants in the CVD related processes are:
* The Zowe Security Workgroup
* The Zowe squads 
* External researchers and reporters
 
# Zowe Response to Vulnerability Policy
## Security issues identification
<!-- <span style="display:none" hidden>(Zowe-SSDP-SDLC - #ID: ZSSD-LP:RV-ICV)</span> -->

### Code review and tests
<!--
<div style="display: none;">(Zowe-SSDP-SDLC: C7. Test Executable Code - #ID: ZSSD-LP:PW-TEC)</div>
<span style="display:none">(Zowe-SSDP-SDLC - #ID: ZSSD-LP:RV-ICV-CRT)</span>
-->

* The security architecture of all Zowe projects is reviewed by the Security Workgroup.
* The squads perform internal security code review of newly implemented features and other security related code changes.
* The code reviews are performed by squad members other than the individuals who created the code.
* The squads continuously perform security testing for security issues in their projects' code and configuration.
* A full penetration testing is performed by the Security Workgroup before each major release.

### Vulnerability monitoring</h3>
<!-- Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM -->

The Security Workgroup continuously monitors well-known sources of information about discovered or otherwise severe security issues. Some sources a listed below:
  * [NIST National Vulnerability Database](https://nvd.nist.gov/vuln)
  * [MITRE CVE List](https://cve.mitre.org/)
  * [Snyk Vulnerability DB](https://security.snyk.io/)
  * [CISA Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
   
   
Any issues found to have impact on Zowe projects, are further [analyzed](#analysis-and-assessment) without unnecessary delay.

Information about any identified issues is propagated by the Security Workgroup to the squads for [mitigation](#security-issues-mitigation).  
    
### Security issues reporting
<!-- Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM -->

Zowe encourages the community, users and security researchers to perform testing and report vulnerabilities.  

Please direct all security issues to <code>zowe-security@lists.openmainframeproject.org</code>.

To help Zowe developers understand and resolve the issues, please provide accurate details. 

#### Security report template

Please fill in as much as you can of the following template fields:
````
  - General
    - Date discovered
    - Severity
    - Impact
      
  - Reporter information  
    - Full name 
    - Contact - preferably e-mail
    - Organization (optional)
    
  - Environment
    - Operating platform: Win (32/64), Linux (flavor), MacOS (pre-M1 / M1)
    - Hosted (optional):  (y,n,N/A) - (Eclipse Che, Theia, CRW, ...)
    - z/OS (optional) 
      - Version
      - Security manager 
      - Related products names and versions
    - Zowe
      - Version
      - Sub-component/s name and version
  
  - Issue description   
    - Short (one liner) summary
    - Detailed information - pre-conditions, access rights,   
    - Steps to reproduce
````

Additional hints and recommendations:
````
    - While testing or replicating the vulnerability take notes, snapshots, collect log files.
    - Start with a summary.
    - Detail the narrative.
    - Follow the form.
    - Proofread.
    - Avoid emotional language.
    - Avoid abbreviations and conjunctions.
    - Be prompt.
````

#### What happens after security report is received by the Security Workgroup 
* After your report is received, a member of the Security Workgroup replies to acknowledge receipt of the report. 
* The reporter may be contacted for clarification.
* Without unnecessary delay the report is [analyzed](#analysis-and-assessment).

<!-- **IMPORTANT:**  Please do not file a public issue [disclosing vulnerabilities](#Security-issues-disclosure) as this may be misused by violent attackers. -->
    Note 1: We encourage the reporters to work with the Security Workgroup team to resolve the issue before going publicly with it.

    Note 2: Security vulnerabilities identified through own testing or reported by community members, and which don't yet have assigned a CVE, are reported by the Zowe Security Workgroup to a CVE Numbering Authorityu (CNA).     

## Analysis and assessment 
<!--
    (Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV)
    (Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV-AEV)
    (NIST-SSF: #REF: SSDF:RV.2.1)
-->

* Reported issues are analyzed within the security workgroup.
* The issues' analyzes outcome is determined by the risk severity measured by the combination of vulnerability exploitability and its impact. 

The severity can be one of the:
  * Critical (C) - An event that, if it occurred, would cause program failure (inability to achieve minimum acceptable requirements).
  
        Critical issues are fixed as early as possible and not later than 30 days after the issue acknowledgment

  * High (H) - An event that, if it occurred, would cause major cost and schedule increases. Secondary requirements may not be achieved.
  
        High issues are fixed within next minor/patch release within 30 days of the issue acknowledgment. 

  * Medium (M) - An event that, if it occurred, would cause moderate cost and schedule increases, but important requirements would still be met.
    
        Medium issues are fixed within 90 days, basically with the next regular release of the project.

  * Low (L) - An event that, if it occurred, would cause only a small cost and schedule increase. Requirements would still be achieved.   

        Low issues are fixed when the squad decides to fix but not later than 180 days from issue acknowledgment.
 
## Security issues mitigation

 After the issue is sufficiently documented, the Security Workgroup coordinates the issue [mitigation](#security-issues-mitigation).
<!--
    (Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV)
    (NIST-SSF #REF: SSF-A.4.2-B)
-->

The Zowe squads strive to fix the relevant security issues according to their assessed priority within a predefined timeframe. [vulnerabilities_critical_fixed policy]

<!-- 
    (NIST-SSF #REF: SSF-A.4.1-B)
-->

## Security issues disclosure

* Zowe discloses fixed vulnerabilities in a timely manner giving the users sufficient time to plan their upgrades. 
* We however don't disclose the vulnerabilities fixed in the latest release as we respect the need for at least 45 days to decide when and how will the users upgrade. 
* When a new release is published, the project list the vulnerabilities fixed in the previous release.
    
      For example when we'd release Zowe v2.3 we'd publish the list of vulnerabilities that were fixed in the version 2.2 .
      The issues that were fixed would be published in the [Zowe security reports](https://github.com/zowe/security-reports/blob/master/security-vulnerabilities.md) repository listing.

## Solution publishing
### Security advisory
* The project's squad discloses a vulnerability by first creating a draft security advisory in the project repository in GitHub.
* For critical priority vulnerability, security patches are created as soon as the issue is fixed in code and configuration.
* The security fixes become an integral part of the latest Zowe distribution.


    Note: <a href="https://docs.github.com/en/code-security/repository-security-advisories/about-github-security-advisories-for-repositories#about-github-security-advisories">GitHub Security Advisories</a> allow the squad to privately discuss and fix a security vulnerability in their project.
* After collaborating on a fix, the project maintainers publish the security advisory to a project specific place.
        

    Note: Projects hosted in GitHub take advantage of the GH features providing special security advisory dedicated pages.   
          See: https://docs.github.com/en/code-security/repository-security-advisories/creating-a-repository-security-advisory

### Security updates
Security notifications are distributed by the following methods.

* Publishing project specific advisories in the corresponding project GitHub repository Security page.


    For example you can find the API Mediation Layer related security advisories here: https://github.com/zowe/api-layer/security/advisories

* Notification to Zowe users who explicitly requested receiving security alerts and advisories by subscribing to:
  * <code>zowe-user@lists.openmainframeproject.org</code>
  * <code>zowe-dev@lists.openmainframeproject.org</code>

## Additional sources:
  - https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html
  - https://bestpractices.coreinfrastructure.org/en
  - https://openssf.org/
  - https://github.com/coreinfrastructure/best-practices-badge
  - https://www.apache.org/security/

</div>