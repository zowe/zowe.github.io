---
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<section class="whitebackground" style="float: none;">
  <h1 id="download" style="margin-bottom: 2rem">Zowe Security</h1>

<div style="padding-top: 3%">
    <h3 style="margin-bottom: 1.5rem">Zowe security policy</h3>
    <p>Coming soon...</p>
</div>

<div style="padding-top: 3%">
    <h3 style="margin-bottom: 1.5rem">Report security issues</h3>
    <p>Please direct all security issues to <code>zowe-security@lists.openmainframeproject.org</code>. A member of the security team will reply to acknowledge receipt of the vulnerability and coordinate remediation with the affected project.</p>
</div>

<div style="padding-top: 3%">
    <h3 style="margin-bottom: 1.5rem">Disclosure policy</h3>
    <p>Coming soon...</p>
   <div style="padding-top: 3%">
    <h4 style="margin-bottom: 1.5rem">Comments on this policy</h4>
    <p>If you have suggestions on how this process could be improved, please file an issue to discuss.</p>
   </div>
</div>

<div style="padding-top: 3%">
    <h3 style="margin-bottom: 1.5rem">Receive security updates</h3>
    <p>Security notifications will be distributed via the following methods.</p>
    <ul>
    <li><code>zowe-user@lists.openmainframeproject.org</code></li>
    <li><code>zowe-dev@lists.openmainframeproject.org</code></li>
    </ul>
</div>

</section>
---
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<section class="whitebackground" style="float: none;">
  <h1 id="download" style="margin-bottom: 2rem">Zowe Security</h1>

<div style="padding-top: 3%">
    <h3 style="margin-bottom: 1.5rem">Zowe Respond to Vulnerabilities <div style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV)</div> security policy</h3>
    This Zowe Respond to Vulnerabilities Security Policy consists of the following interrelated topics/sub-policies:
    <ul>
        <li><a href="#IDENTIFY">Security issues identification <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM)</span></a></li>
        <li><a href="#DISCLOSE">Security issues disclosure <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-VDR)</span></a></li>
        <li><a href="#REMEDIATE">Security issues remediation </a></li>
        <li><a href="#ADVISE">Solution publication</a></li>
    </ul>
</div>

<div>
The individual sub-policies contain sets of interrelated applicable requirements on how the Zowe project and organization treat 
security vulnerabilities and issues. The requirements are governed by internal processes and guidance for the users and other reporters.
</div>

<div style="padding-top: 3%">
    <a id="IDENTIFY"/><h2>Security issues identification</h2>
    <ul>    
        <li> 
            <h3 style="margin-bottom: 1.5rem"> Code Review and Tests</h3>
            <p> 
                <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-CRT)</span>
                The Zowe product teams must/will continuously perform security testing of their products' code and configuration for security issues. 
                Irregularly but at least before each major release a full penetration testing must be performed.
            </p>
        </li>
        <li> 
            <h3 style="margin-bottom: 1.5rem">Vulnerability sources Monitoring</h3>
            <p> 
                <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM)</span>
                <div>The Zowe product teams must/will continuously monitor well know sources of information about freshly discovered or otherwise severe security issues.</div>
                <br/>
                <div>Any issues found to be potentially impacting the respective products, must be booked and further analyzed without unnecessary delay.</div>
            </p>
        </li>
        <li> 
            <h3 style="margin-bottom: 1.5rem">Security issues reporting</h3>
            <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM)</span>
            <p>
                Please direct all security issues to <code>zowe-security@lists.openmainframeproject.org</code>. 
                <br/>
                After your report is received, a member of the security team will reply to acknowledge receipt of the vulnerability.
                <br/>
                Without unnecessary delay the report will be analyzed and you may be contacted for clarification.
                <br/>
                After the issue is sufficiently documented, our security team will coordinate remediation with the affected project.
                <br/>
                Please do not file a public issue disclosing potential vulnerabilities as this may be misused by violent attackers. 
            </p>
        </li>
        <li> 
            <h3 style="margin-bottom: 1.5rem"> Issues assessment and evidence</h3>
            <p> 
                <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV)</span>
                <span style="display:none"> (Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV-AEV)</span>
                <span style="display:none"> (NIST-SSF: #REF: SSDF:RV.2.1)</span>
                <div>Any issues found during testing and reviewing the code, must be assessed and for severity, exploitability and impact on the respective components and the whole Zowe system.</div>
                <br/>
                <div>The assessment results reports will be collected and stored for evidence and measurement of the product security state and hardening.</div>
            </p>
        </li>
    </ul> 
</div>

<div style="padding-top: 3%">
    <a id="DISCLOSE"/><h2>Security issues disclosure</h2>
    <h3 style="margin-bottom: 1.5rem">Disclosure policy</h3>
    <p>Zowe adopts a variant/modification (in case we modify it) of the <a href="https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure">Coordinated Vulnerability Disclosure Policy</a></p>
    ALTERNATIVELY:
    <p>The Zowe Vulnerability Disclosure Policy is (based on / a modification of) the <a href="">Responsible or Coordinated Vulnerability Disclosure (CVD) Policy</a></p>
    <br/>
    The project maintainers would disclose a confirmed vulnerability in the code by first by creating a draft security advisory in the package's repository in GitHub/other CMS.
    GitHub Security Advisories allow repository maintainers to privately discuss and fix a security vulnerability in a project.
    <br/>See https://docs.github.com/en/code-security/repository-security-advisories/creating-a-repository-security-advisory
    <br/>
    After collaborating on a fix, repository maintainers can publish the security advisory to publicly disclose the security vulnerability to the project's community.
   <div></div>
</div>

<div style="padding-top: 3%">
    <a id="REMEDIATE"/><h2>Security issues remediation</h2>
    <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV)</span>
    <span style="display:none">(NIST-SSF #REF: SSF-A.4.2-B)</span>
    <div>Projects SHOULD fix all critical vulnerabilities rapidly after they are reported. [vulnerabilities_critical_fixed]</div>
    <br/>
    <span style="display:none">(NIST-SSF #REF: SSF-A.4.1-B)</span>
    <div>There MUST be no un-patched vulnerabilities of medium or higher severity that have been publicly known for more than 60 days. [vulnerabilities_fixed_60_days]</div>
</div>

<div style="padding-top: 3%">
    <a id="ADVISE"/><h2>Solution advisory publishing</h2>
    <h3 style="margin-bottom: 1.5rem">Receive security updates</h3> 
    By publishing security advisories, repository maintainers make it easier for their community to update package dependencies and research the impact of the security vulnerabilities. 
    For more information, see "About GitHub Security Advisories for repositories."
    <p>Security notifications will be distributed via the following methods.</p>
    <ul>
    <li><code>zowe-user@lists.openmainframeproject.org</code></li>
    <li><code>zowe-dev@lists.openmainframeproject.org</code></li>
    </ul>
</div>

</section>
