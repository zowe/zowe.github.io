<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->
<!-- # Zowe Security Policy-->

# Zowe Respond to Vulnerabilities Policy
<!--<div style="display:none" hidden>(Zowe-SSDP-SDLC ID: ZSSD-LP:RV)</div>-->

The Zowe Respond to Vulnerability Policy governs how Zowe handles vulnerabilities identification, mitigation and disclosure.

Our policy is based on the <a href="https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure">Coordinated Vulnerability Disclosure (CVD) Policy</a>
which is also adopted by many other organizations, <a href="https://www.cisa.gov/coordinated-vulnerability-disclosure-process">CISA</a> and <a href="https://www.etsi.org/standards/coordinated-vulnerability-disclosure">ETSI</a> among them. 
Zowe adapts the following 5 CVD topics used to declare complete set of requirements:
* [Security issues identification](#Security-issues-identification) <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM)</span>
* [Security issues analysis and assessment](#Security-issues-analysis-and-assessment)
* [Security issues mitigation](#Security-issues-mitigation)
* [Security issues disclosure](#Security-issues-disclosure) <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-VDR)</span>
* [Solution publishing](#Solution-publishing)

The topics listed above contain sets of applicable requirements. Where appropriate the fulfilment of these requirements may be governed by internal processes and guidance. 
In such cases, a detailed description of the corresponding processes and guidance will be provided in separate documents.

The main participants in the CVD are:
* Zowe Security Workgroup
* Zowe squads 
* External researchers and reporters
 
Each requirement listed under the individual topics may be a responsibility of a single participant 
or the responsibility may be split between multiple participants as described below.    

    NOTE: Wherever appropriate the policy requirements are mapped to the <a href="https://csrc.nist.gov/publications/detail/sp/800-218/final">NIST SSDF</a> Respond to Vulnerabilities (RV) Best practices 
          and/or to the [Open Source Security Foundation (OpenSSF) Best Practices](https://openssf.org/)(former [Core Infrastructure Iniitative (CII)](https://www.coreinfrastructure.org/)).
          The mappings are part of this document but are provided as comments and those are not rendered in the markdown viewer. 

## Security issues identification
<!--<span style="display:none" hidden>(Zowe-SSDP-SDLC - #ID: ZSSD-LP:RV-ICV)</span>-->

### Code review and tests
<!--
<div style="display: none;">(Zowe-SSDP-SDLC: C7. Test Executable Code - #ID: ZSSD-LP:PW-TEC)</div>
<span style="display:none">(Zowe-SSDP-SDLC - #ID: ZSSD-LP:RV-ICV-CRT)</span>
-->
* The architecture of any Zowe component's security features designed by the Zowe squads must be reviewed by the Zowe Security Workgroup.
* The Zowe squads must perform internal security code review of newly implemented features and other security related code changes.
* Code review must be performed by other squad members than the ones who created the code.
* The Zowe squads must continuously perform security testing of their components' code and configuration for security issues.
* Irregularly but at least before each major release a full penetration testing must be performed by the Zowe Security Workgroup.

### Potential vulnerability sources monitoring</h3>
<!-- <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM)</span> -->

* The Zowe Security Workgroup must continuously monitor well know sources of information about freshly discovered or otherwise severe security issues. Some sources a listed below:
  * [NIST National Vulnerability Database](https://nvd.nist.gov/vuln)
  * [MITRE CVE List](https://cve.mitre.org/)
  * [Snyk Vulnerability DB](https://security.snyk.io/)
  * [CISA Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
* Any issues found to potentially have impact on Zowe components, must be further [analyzed](#Security-Issues-Analysis-And-Assessment) without unnecessary delay.
* Information about any identified issues found to be of high severity and/or impact must be propagated by the Zowe Security Workgroup to all Zowe squads.  
    
### Security issues reporting
<!-- <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM)</span> -->

Zowe encourages the community, users and other security researchers to perform security testing and report potential vulnerabilities of the Zowe components.  

<!-- <span style="display: none;">#TODO: Alternatively use Zowe report form if we have one</span> -->
<!-- <span style="display: none;">#TODO: Publish the reporting process on the project web-site: Open SSF: FLOSS Best Practices Criteria  - Vulnerability report process</span> -->

Please direct all security issues to <code>zowe-security@lists.openmainframeproject.org</code>.

To help Zowe developers understand and resolve the issues in most efficient way, please provide sufficient and accurate details about the issue and the approach to reproduce it. 

#### Security report template

Please fill in as much as you can of the following template fields:
````
  - General
    - Date discovered
    - Severiity
    - Impact
      
  - Reporter information  
    - Full name 
    - Contact - preferably e-mail
    - Customer ID (optional)
    
  - Product related
    - Operating environment 
      - z/OS version
      - Security manager
    - Product name and version
    - Zowe version
    - Vulnerable sub-component name and version

  - Issue description   
    - Short (one liner) summary
    - Detailed information - pre-conditions, access rights,   
    - Steps to reproduce
````

Additional hints and recommendations:
````
    - While testing or hunting the vulnerability take notes, snapshots, collect log files.
    - Start with a summary.
    - Detail the narrative.
    - Follow the form.
    - Proofread.
    - Avoid emotional language.
    - Avoid abbreviations and conjunctions.
    - Be prompt.
````

**IMPORTANT:**  Please do not file a public issue [disclosing vulnerabilities](#Security-issues-disclosure) as this may be misused by violent attackers.

<!--
<div style="display: none;">
* References:
  * https://owasp.org/www-community/vulnerabilities/Vulnerability_template
  * https://ossf.github.io/osv-schema/
  * https://github.com/CVEProject/cve-schema
  * https://security.googleblog.com/2021/06/announcing-unified-vulnerability-schema.html
</div>
-->

#### What happens after security report is received by Zowe Security Workgroup 
* After your report is received, a member of the security team will reply to acknowledge receipt of the report.
* Without unnecessary delay the report will be [analyzed](Security-issues-analysis-and_assessment) and you may be contacted for clarification.
* After the issue is sufficiently documented, our security team will coordinate [mitigation](#Security-issues-mitigation) with the affected squad.

## Security issues analysis and assessment 
<!--
    <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV)</span>
    <span style="display:none"> (Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV-AEV)</span>
    <span style="display:none"> (NIST-SSF: #REF: SSDF:RV.2.1)</span>
-->

* Any issue reported or reported by external reporters or identified by internal testing or code review, must be analyzed/assessed/triaged within the security workgroup.<br/> 
* The issues' assessment outcome is the value of the risk severity measured by the combination of exploitability and impact of the issue on the respective components and the whole Zowe system. The exploitability must be carefully investigated taking into account the component specific usage of the vulnerable code. The severity can be one of the: 

    * Critical (C) - An event that, if it occurred, would cause program failure (inability to achieve minimum acceptable requirements).
    * Serious (S) - An event that, if it occurred, would cause major cost and schedule increases. Secondary requirements may not be achieved.
    * Moderate (Mo) - An event that, if it occurred, would cause moderate cost and schedule increases, but important requirements would still be met.
    * Minor (Mi) - An event that, if it occurred, would cause only a small cost and schedule increase. Requirements would still be achieved.
    * Negligible (N) - An event that, if it occurred, would have no effect on program.
  
* The priority with which the issues will be fixed is based on the combination of the above factors (exploitability and impact) and falls in one of the following categories:
  
    * Critical: must be fixed as early as possible
    * High: must be fixed within next minor/patch release as latest. 
      Alternatively, There MUST be no un-patched vulnerabilities of High severity that have been publicly known for more than 60 days. [vulnerabilities_fixed_60_days policy]
    * Medium: fixed when the squad decides to fix 
    * Low: fixed when the squad decides to fix

* An assessment reports will be created and stored for evidence and measurement of the component security state and hardening.

## Security issues mitigation
<!--
    <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV)</span>
    <span style="display:none">(NIST-SSF #REF: SSF-A.4.2-B)</span>
-->

Zowe squads must fix the relevant security issues according to their assessed priority and its defined timeframe. [vulnerabilities_critical_fixed policy]

<!-- 
    <span style="display:none">(NIST-SSF #REF: SSF-A.4.1-B)</span> 
-->

## Security issues disclosure

* Zowe discloses fixed vulnerabilities in a timely manner giving the users sufficient time to plan their upgrades. 
* Zowe however won't disclose the vulnerabilities fixed in the latest release as we respect the need for at least 45 days to decide when and how will the users upgrade Zowe. 
* When a new release of Zowe is published, we will list the vulnerabilities fixed in the previous release.
    
      For example when we release Zowe 2.3 we will publish the list of vulnerabilities that were fixed in the 2.2 versions of Zowe.
          The issues that were fixed will be published in out [Zowe security reports](https://github.com/zowe/security-reports/blob/master/security-vulnerabilities.md) repository listing.

## Solution publishing
### Security advisory
* For critical priority vulnerability, security patches must be created as soon as the issue is fixed in code and configuration.
* The security fixes will also become an integral part of the nearest next Zowe distribution.
* The component's squad(repository maintainers) will disclose a confirmed vulnerability by first creating a draft security advisory in the component repository in GitHub/other CMS that is used by the squad.


    Note: GitHub Security Advisories allow repository maintainers to privately discuss and fix a security vulnerability in a project.
* After collaborating on a fix, component squad(repository maintainers) can publish the security advisory to publicly disclose the security vulnerability advisory in a project specific place.
        

    Note: Projects hosted in GitHub will take advantage of the GH features providing special security advisory dedicated pages.   
          See: https://docs.github.com/en/code-security/repository-security-advisories/creating-a-repository-security-advisory

### Security updates 
Security notifications will be distributed via the following methods.

* Publishing component specific advisories in the corresponding component GitHub repository Security page.
 
  
    For example you can find the Zowe API Mediation Layer related security advisories here: https://github.com/zowe/api-layer/security/advisories   
* <code>zowe-user@lists.openmainframeproject.org</code>
* <code>zowe-dev@lists.openmainframeproject.org</code>


-----------------------------------
## Additional sources:
  - https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html
  - https://bestpractices.coreinfrastructure.org/en
  - https://openssf.org/
  - https://github.com/coreinfrastructure/best-practices-badge
  - https://www.apache.org/security/
