---
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<section class="whitebackground" style="float: none;">

#Zowe Respond to Vulnerabilities security policy
<span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV)</span>

This Zowe Respond to Vulnerabilities Security Policy consists of the following interrelated topics/sub-policies:

  - <a href="#IDENTIFY">Security issues identification <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM)</span></a>
  - <a href="#REMEDIATE">Security issues remediation </a>
  - <a href="#DISCLOSE">Security issues disclosure <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-VDR)</span></a>
  - <a href="#ADVISE">Solution publication</a>


The individual sub-policies contain sets of interrelated applicable requirements on how the Zowe project and organization treat 
security vulnerabilities and issues. 

The requirements are governed by internal processes and guidance for the users and other reporters.

##Security issues identification
<span style="display:none">(Zowe-SSDP-SDLC - #ID: ZSSD-LP:RV-ICV)</span>

###Code Review and Tests
<span style="display:none">(Zowe-SSDP-SDLC: C7. Test Executable Code - #ID: ZSSD-LP:PW-TEC)</span>
<span style="display:none">(Zowe-SSDP-SDLC - #ID: ZSSD-LP:RV-ICV-CRT)</span>

The Zowe product teams must/will continuously perform security testing of their products' code and configuration for security issues.

Irregularly but at least before each major release a full penetration testing must be performed.

###Potential vulnerability sources Monitoring</h3>
<span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM)</span>

The Zowe product teams must/will continuously monitor well know sources of information about freshly discovered or otherwise severe security issues.

Some sources a listed below:
  - <a href="https://nvd.nist.gov/vuln">NIST National Vulnerability Database</a>
  - <a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">CISA Exploited Vulnerabilities Catalog</a>
    
    /#TODO: Add other

Any issues found to be potentially impacting the respective products, must be further analyzed without unnecessary delay.
    
###Security issues reporting
<span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM)</span>

Zowe encourages the community users to perform security testing and report potential vulnerabilities as described bellow.  

Please direct all security issues to <code>zowe-security@lists.openmainframeproject.org</code>.

    #TODO: Alternatively use Zowe report form if we have one 

After your report is received, a member of the security team will reply to acknowledge receipt of the report.

Without unnecessary delay the report will be analyzed and you may be contacted for clarification.

After the issue is sufficiently documented, our security team will coordinate remediation with the affected project.

Please do not file a public issue disclosing potential vulnerabilities as this may be misused by violent attackers. 

###Issues assessment and evidence
<span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV)</span>
<span style="display:none"> (Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV-AEV)</span>
<span style="display:none"> (NIST-SSF: #REF: SSDF:RV.2.1)</span>

Issues found during testing and reviewing the code, must be assessed for severity, exploitability and impact on the respective components and the whole Zowe system.

The assessment results reports will be collected and stored for evidence and measurement of the product security state and hardening.
The issues collected through testing, monitoring and user reports are discussed within the security workgroup and fixed based on the severity:
  - **Critical:** fixed as early as possible
  - **High:** fixed within next minor/patch release
  - **Medium and Low:** fixed when the squad decides to fix


##Security issues remediation
<span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV)</span>
<span style="display:none">(NIST-SSF #REF: SSF-A.4.2-B)</span>

Projects MUST/SHOULD fix all Critical vulnerabilities rapidly after they are reported. [vulnerabilities_critical_fixed]
<span style="display:none">(NIST-SSF #REF: SSF-A.4.1-B)</span>

There MUST be no un-patched vulnerabilities of High severity that have been publicly known for more than 60 days. [vulnerabilities_fixed_60_days]

#Security issues disclosure
##Disclosure policy
The Zowe Vulnerability Disclosure Policy is (based on / a modification of) the <a href="">Responsible or Coordinated Vulnerability Disclosure (CVD) Policy</a>

The project maintainers would disclose a confirmed vulnerability by first creating a draft security advisory in the package's repository in GitHub/other CMS.
GitHub Security Advisories allow repository maintainers to privately discuss and fix a security vulnerability in a project.

See https://docs.github.com/en/code-security/repository-security-advisories/creating-a-repository-security-advisory

After collaborating on a fix, repository maintainers can publish the security advisory to publicly disclose the security vulnerability to the project's community.

Zowe discloses the vulnerabilities in a timely manner but giving the user time to upgrade. The fixed vulnerabilities
will be available on the [zowe security page](https://www.zowe.org/security.html). Zowe won't disclose the
vulnerabilities fixed in the latest release as we respect the need for at least 45 days to decide when and how will
the users upgrade Zowe.

When the new release of Zowe is public we will publish the vulnerabilities fixed in the previous release. For example
when we release Zowe 2.3 we will publish the list of vulnerabilities that were fixed in the 2.2 versions of Zowe

##Solution advisory publishing
###Receive security updates 
By publishing security advisories, repository maintainers make it easier for their community to update package dependencies and research the impact of the security vulnerabilities. 
For more information, see "About GitHub Security Advisories for repositories."
Security notifications will be distributed via the following methods.

  - Publishing component specific advisories in the corresponding component GitHub repository Security page.
    For example you can find the Zowe API Mediation Layer related security advisories here: https://github.com/zowe/api-layer/security/advisories   
  - <code>zowe-user@lists.openmainframeproject.org</code>
  - <code>zowe-dev@lists.openmainframeproject.org</code>

</section>
-----------------------------------
-----------------------------------
Additional sources:
  - https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure
  - https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html
