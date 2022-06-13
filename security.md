<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->
<!-- # Zowe Security Policy-->

# Zowe Respond to Vulnerabilities Policy
<!--<div style="display:none" hidden>(Zowe-SSDP-SDLC ID: ZSSD-LP:RV)</div>-->

This Respond to Vulnerability Policy governs how Zowe handles vulnerabilities identification, mitigation and disclosure.

Our policy is based on the <a href="https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure">Coordinated Vulnerability Disclosure (CVD) Policy</a>
which is also adopted by many other organizations, <a href="https://www.cisa.gov/coordinated-vulnerability-disclosure-process">CISA</a> and <a href="https://www.etsi.org/standards/coordinated-vulnerability-disclosure">ETSI</a> among them. 
Zowe adapts the following 5 CVD topics used to declare complete set of requirements:
* [Security issues identification](#Security-issues-identification) <!-- <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM)</span> -->
* [Security issues analysis and assessment](#Security-issues-analysis-and-assessment)
* [Security issues mitigation](#Security-issues-mitigation)
* [Security issues disclosure](#Security-issues-disclosure) <!-- <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-VDR)</span> -->
* [Solution publishing](#Solution-publishing)

The topics listed above contain sets of applicable requirements. Where appropriate the fulfilment of these requirements may be governed by internal processes and guidance. 
In such cases, a detailed description of the corresponding processes and guidance is provided in separate documents.

The main participants in the CVD related processes are:
* Zowe Security Workgroup
* Zowe squads 
* External researchers and reporters
 
Each requirement listed under the individual topics may be a responsibility of a single participant 
or the responsibilities could be split between multiple participants as described where appropriate.    

    NOTE: Wherever appropriate the policy requirements are mapped to the NIST SSDF Respond to Vulnerabilities (RV) Best practices - see https://csrc.nist.gov/publications/detail/sp/800-218/final 
          and/or to the Open Source Security Foundation (OpenSSF) Best Practices] - see https://openssf.org/ (former Core Infrastructure Iniitative) - see https://www.coreinfrastructure.org/.
          The mappings are part of this document but are provided as comments and those are not rendered in the markdown viewer. 

## Security issues identification
<!-- <span style="display:none" hidden>(Zowe-SSDP-SDLC - #ID: ZSSD-LP:RV-ICV)</span> -->

### Code review and tests
<!--
<div style="display: none;">(Zowe-SSDP-SDLC: C7. Test Executable Code - #ID: ZSSD-LP:PW-TEC)</div>
<span style="display:none">(Zowe-SSDP-SDLC - #ID: ZSSD-LP:RV-ICV-CRT)</span>
-->

* The security architecture of all Zowe components is reviewed by the Security Workgroup.
* The squads perform internal security code review of newly implemented features and other security related code changes.
* The code reviews are performed by squad members other than the individuals who created the code.
* The squads continuously perform security testing of their components' code and configuration for security issues.
* A full penetration testing is performed by the Security Workgroup before each major release.

### Vulnerability monitoring</h3>
<!-- <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM)</span> -->

* The Security Workgroup continuously monitors well known sources of information about discovered or otherwise severe security issues. Some sources a listed below:
  * [NIST National Vulnerability Database](https://nvd.nist.gov/vuln)
  * [MITRE CVE List](https://cve.mitre.org/)
  * [Snyk Vulnerability DB](https://security.snyk.io/)
  * [CISA Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
* Any issues found to have impact on Zowe components, are further [analyzed](#Security-Issues-Analysis-And-Assessment) without unnecessary delay.
* Information about any identified issues is propagated by the Security Workgroup to all squads.  
    
### Security issues reporting
<!-- <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM)</span> -->

Zowe encourages the community, users and security researchers to perform testing and report vulnerabilities.  

<!-- <span style="display: none;">#TODO: Publish the reporting process on the project web-site: Open SSF: FLOSS Best Practices Criteria  - Vulnerability report process</span> -->

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

#### What happens after security report is received by Zowe Security Workgroup 
* After your report is received, a member of the Zowe Security Workgroup replies to acknowledge receipt of the report.
* Without unnecessary delay the report is [analyzed](Security-issues-analysis-and_assessment). Please expect to be contacted for clarification.
* After the issue is sufficiently documented, the Zowe security team coordinates the issue [mitigation](#Security-issues-mitigation).

<!-- **IMPORTANT:**  Please do not file a public issue [disclosing vulnerabilities](#Security-issues-disclosure) as this may be misused by violent attackers. -->
We encourage the community to work with the Security Workgroup team to resolve the issue before going publicly with it.

## Analysis and assessment 
<!--
    <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV)</span>
    <span style="display:none"> (Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV-AEV)</span>
    <span style="display:none"> (NIST-SSF: #REF: SSDF:RV.2.1)</span>
-->

* Reported issues are analyzed within the security workgroup.<br/> 
* The issues' analyzes outcome is determined by the risk severity measured by the combination of exploitability and impact. 

The severity can be one of the: 
  
    #  TODO: Synch and merge the Prio and Severity into one topic 
 
    * Critical (C) - An event that, if it occurred, would cause program failure (inability to achieve minimum acceptable requirements).
    * Serious (S) - An event that, if it occurred, would cause major cost and schedule increases. Secondary requirements may not be achieved.
    * Moderate (Mo) - An event that, if it occurred, would cause moderate cost and schedule increases, but important requirements would still be met.
    * Minor (Mi) - An event that, if it occurred, would cause only a small cost and schedule increase. Requirements would still be achieved.
    * Negligible (N) - An event that, if it occurred, would have no effect on program.
  
* 
* The priority with which the issues are fixed is based on the combination of the vulnerability exploitability and impact. 
    The priority falls into one of the following categories:
  
    * Critical: fixed as early as possible
    * High: fixed within next minor/patch release as latest. 
      Alternatively, There are no un-patched vulnerabilities of High severity that have been publicly known for more than 60 days. [vulnerabilities_fixed_60_days policy]
    * Medium: fixed when the squad decides to fix 
    * Low: fixed when the squad decides to fix

* #TODO: reformulate or remove if doesn't sound appropriate: An assessment reports are created and stored for evidence and measurement of the component security state and hardening.

## Security issues mitigation
<!--
    <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV)</span>
    <span style="display:none">(NIST-SSF #REF: SSF-A.4.2-B)</span>
-->

Zowe squads strive to fix the relevant security issues according to their assessed priority within a predefined timeframe. [vulnerabilities_critical_fixed policy]

<!-- 
    <span style="display:none">(NIST-SSF #REF: SSF-A.4.1-B)</span> 
-->

## Security issues disclosure

* Zowe discloses fixed vulnerabilities in a timely manner giving the users sufficient time to plan their upgrades. 
* Zowe however won't disclose the vulnerabilities fixed in the latest release as we respect the need for at least 45 days to decide when and how will the users upgrade Zowe. 
* When a new release of Zowe is published, we list the vulnerabilities fixed in the previous release.
    
      For example when we'd release Zowe 2.3 we'd publish the list of vulnerabilities that were fixed in the 2.2 versions of Zowe.
          The issues that were fixed would be published in the [Zowe security reports](https://github.com/zowe/security-reports/blob/master/security-vulnerabilities.md) repository listing.

## Solution publishing
### Security advisory
* For critical priority vulnerability, security patches are created as soon as the issue is fixed in code and configuration.
* The security fixes become an integral part of the nearest next Zowe distribution.
* The component's squad(project maintainers) disclose a confirmed vulnerability by first creating a draft security advisory in the component repository in GitHub or other CMS that is used by the project.


    Note: GitHub Security Advisories allow repository maintainers to privately discuss and fix a security vulnerability in a project.
* After collaborating on a fix, the project maintainers publishes the security advisory to a project specific place.
        

    Note: Projects hosted in GitHub take advantage of the GH features providing special security advisory dedicated pages.   
          See: https://docs.github.com/en/code-security/repository-security-advisories/creating-a-repository-security-advisory

### Security updates 
Security notifications are distributed via the following methods.

* Publishing component specific advisories in the corresponding component GitHub repository Security page.


    For example you can find the Zowe API Mediation Layer related security advisories here: https://github.com/zowe/api-layer/security/advisories   
* Notification to Zowe users who explicitly signed in for receiving security alerts and advisories. 
       
          #TODO: Subscribe to the mailing lists or apply using  form to apply???
  * <code>zowe-user@lists.openmainframeproject.org</code>
  * <code>zowe-dev@lists.openmainframeproject.org</code>

-----------------------------------
## Additional sources:
  - https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html
  - https://bestpractices.coreinfrastructure.org/en
  - https://openssf.org/
  - https://github.com/coreinfrastructure/best-practices-badge
  - https://www.apache.org/security/
