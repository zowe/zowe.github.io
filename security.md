<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->
<!-- # Zowe Security Policy-->

<!-- <div style="display:none" hidden>(Zowe-SSDP-SDLC ID: ZSSD-LP:RV)</div> -->

<div class="row" style="padding: 4% 7% 5% 7%">
<div class="col-md-12">
<h1>Zowe Security Policy</h1>

<p>This Security Policy governs how Zowe handles vulnerabilities identification, mitigation and disclosure.</p>

<p>Our policy is based on the <a href="https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure">Coordinated Vulnerability Disclosure (CVD) Policy</a>
which is also adopted by many other organizations, <a href="https://www.cisa.gov/coordinated-vulnerability-disclosure-process">CISA</a> and <a href="https://www.etsi.org/standards/coordinated-vulnerability-disclosure">ETSI</a> among them.
Zowe adapts the following 5 CVD topics to declare complete set of policy requirements for Respond to Vulnerabilities:</p>

<ul>
  <li><a href="#security-issues-identification">Security issues identification</a> <!-- <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM)</span> --></li>
  <li><a href="#analysis-and-assessment">Security issues analysis and assessment</a></li>
  <li><a href="#security-issues-mitigation">Security issues mitigation</a></li>
  <li><a href="#security-issues-disclosure">Security issues disclosure</a> <!-- <span style="display:none">(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-VDR)</span> --></li>
  <li><a href="#solution-publishing">Solution publishing</a></li>
</ul>

<p>The topics listed above contain sets of applicable requirements. Where appropriate the fulfilment of these requirements may be governed by internal processes and guidance.
In such cases, a detailed description of the corresponding processes and guidance is provided in separate documents.</p>

<pre><code>NOTE: Wherever appropriate, the policy requirements are mapped to the NIST SSDF Respond to Vulnerabilities (RV) Best practices - see [https://csrc.nist.gov/publications/detail/sp/800-218/final](https://csrc.nist.gov/publications/detail/sp/800-218/final)
      and/or to the Open Source Security Foundation (OpenSSF) Best Practices] - see [https://openssf.org/](https://openssf.org/) (former Core Infrastructure Iniitative) - see [https://www.coreinfrastructure.org/](https://www.coreinfrastructure.org/).
      The mappings are part of this document but are provided as comments and those are not rendered in the markdown viewer. 
</code></pre>

<p>The individual requirements may be a responsibility of a single participant or the responsibilities could be shared between multiple cooperating participants.</p>

<p>The main participants in the CVD related processes are:</p>

<ul>
  <li>The Zowe Security Workgroup</li>
  <li>The Zowe squads</li>
  <li>External researchers and reporters</li>
</ul>

<h1>Zowe Response to Vulnerability Policy</h1>

<h2 id="security-issues-identification">Security issues identification</h2>

<!-- <span style="display:none" hidden>(Zowe-SSDP-SDLC - #ID: ZSSD-LP:RV-ICV)</span> -->

<h3>Code review and tests</h3>

<!--
<div style="display: none;">(Zowe-SSDP-SDLC: C7. Test Executable Code - #ID: ZSSD-LP:PW-TEC)</div>
<span style="display:none">(Zowe-SSDP-SDLC - #ID: ZSSD-LP:RV-ICV-CRT)</span>
-->

<ul>
  <li>The security architecture of all Zowe projects is reviewed by the Security Workgroup.</li>
  <li>The squads perform internal security code review of newly implemented features and other security related code changes.</li>
  <li>The code reviews are performed by squad members other than the individuals who created the code.</li>
  <li>The squads continuously perform security testing for security issues in their projects' code and configuration.</li>
  <li>Before each major release, the Security Workgroup conducts full penetration testing.</li>
</ul>

<h3>Vulnerability monitoring</h3>

<!-- Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM -->

<p>The Security Workgroup continuously monitors well-known sources of information about discovered or otherwise severe security issues. Some sources a listed below:</p>

<ul>
  <li><a href="https://nvd.nist.gov/vuln">NIST National Vulnerability Database</a></li>
  <li><a href="https://cve.mitre.org/">MITRE CVE List</a></li>
  <li><a href="https://security.snyk.io/">Snyk Vulnerability DB</a></li>
  <li><a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">CISA Exploited Vulnerabilities Catalog</a></li>
</ul>

<p>Any issues found to have impact on Zowe projects, are further <a href="#analysis-and-assessment">analyzed</a> without unnecessary delay.</p>

<p>Information about any identified issues is propagated by the Security Workgroup to the squads for <a href="#security-issues-mitigation">mitigation</a>.</p>

<h3>Security issues reporting</h3>

<!-- Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ICV-PVM -->

<p>Zowe encourages the community, users and security researchers to perform testing and report vulnerabilities.</p>

<p>Please direct all security issues to &lt;code&gt;zowe-security@lists.openmainframeproject.org&lt;/code&gt;.</p>

<p>To help Zowe developers understand and resolve the issues, please provide accurate details.</p>

<h4>Security report template</h4>

<p>Please fill in as much as you can of the following template fields:</p>

<pre><code>  - General
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
</code></pre>

<p>Additional hints and recommendations:</p>

<pre><code>    - While testing or replicating the vulnerability take notes, snapshots, collect log files.
    - Start with a summary.
    - Detail the narrative.
    - Follow the form.
    - Proofread.
    - Avoid emotional language.
    - Avoid abbreviations and conjunctions.
    - Be prompt.
</code></pre>

<h4>What happens after security report is received by the Security Workgroup</h4>

<ul>
  <li>After your report is received, a member of the Security Workgroup replies to acknowledge receipt of the report.</li>
  <li>The reporter may be contacted for clarification.</li>
  <li>Without unnecessary delay the report is <a href="#analysis-and-assessment">analyzed</a>.</li>

</ul>

<p><!-- <strong>IMPORTANT:</strong>  Please do not file a public issue <a href="#Security-issues-disclosure">disclosing vulnerabilities</a> as this may be misused by violent attackers. -->
Note 1: We encourage the reporters to work with the Security Workgroup team to resolve the issue before going publicly with it.</p>

<pre><code>Note 2: Security vulnerabilities identified through own testing or reported by community members, and which don't yet have assigned a CVE, are reported by the Zowe Security Workgroup to a CVE Numbering Authorityu (CNA).     
</code></pre>

<h2 id="analysis-and-assessment">Analysis and assessment</h2>

<!--
(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV)
(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV-AEV)
(NIST-SSF: #REF: SSDF:RV.2.1)
-->

<ul>
  <li>Reported issues are analyzed within the security workgroup.</li>
  <li>The issues' analyzes outcome is determined by the risk severity measured by the combination of vulnerability exploitability and its impact.</li>
</ul>

<p>The severity can be one of the:</p>

<ul>
  <li><p>Critical (C) - An event that, if it occurred, would cause program failure (inability to achieve minimum acceptable requirements).</p>
<pre><code>Critical issues are fixed as early as possible and not later than 30 days after the issue acknowledgment
</code></pre></li>
  <li><p>High (H) - An event that, if it occurred, would cause major cost and schedule increases. Secondary requirements may not be achieved.</p>
<pre><code>High issues are fixed within next minor/patch release within 30 days of the issue acknowledgment. 
</code></pre></li>
  <li><p>Medium (M) - An event that, if it occurred, would cause moderate cost and schedule increases, but important requirements would still be met.</p>
<pre><code>Medium issues are fixed within 90 days, basically with the next regular release of the project.
</code></pre></li>
  <li><p>Low (L) - An event that, if it occurred, would cause only a small cost and schedule increase. Requirements would still be achieved.</p>
<pre><code>Low issues are fixed when the squad decides to fix but not later than 180 days from issue acknowledgment.
</code></pre></li>
</ul>

<h2 id="security-issues-mitigation">Security issues mitigation</h2>

<p>After the issue is sufficiently documented, the Security Workgroup coordinates the issue <a href="#security-issues-mitigation">mitigation</a>.
<!--
(Zowe-SSDP-SDLC #ID: ZSSD-LP:RV-ARV)
(NIST-SSF #REF: SSF-A.4.2-B)
--></p>

<p>The Zowe squads strive to fix the relevant security issues according to their assessed priority within a predefined timeframe. [vulnerabilities_critical_fixed policy]</p>

<!--
(NIST-SSF #REF: SSF-A.4.1-B)
-->

<h2 id="security-issues-disclosure">Security issues disclosure</h2>

<ul>
  <li><p>Zowe discloses fixed vulnerabilities in a timely manner giving the users sufficient time to plan their upgrades.</p></li>
  <li><p>We however don't disclose the vulnerabilities fixed in the latest release as we respect the need for at least 45 days to decide when and how will the users upgrade.</p></li>
  <li><p>When a new release is published, the project list the vulnerabilities fixed in the previous release.</p>
<pre><code>For example when we'd release Zowe v2.3 we'd publish the list of vulnerabilities that were fixed in the version 2.2 .
The issues that were fixed would be published in the [Zowe security reports](https://github.com/zowe/security-reports/blob/master/security-vulnerabilities.md) repository listing.
</code></pre></li>
</ul>

<h2 id="solution-publishing">Solution publishing</h2>

<h3>Security advisory</h3>

<ul>
  <li>The project's squad discloses a vulnerability by first creating a draft security advisory in the project repository in GitHub.</li>
  <li>For critical priority vulnerability, security patches are created as soon as the issue is fixed in code and configuration.</li>
  <li>The security fixes become an integral part of the latest Zowe distribution.</li>
</ul>

<pre><code>Note: <a href="https://docs.github.com/en/code-security/repository-security-advisories/about-github-security-advisories-for-repositories#about-github-security-advisories">GitHub Security Advisories</a> allow the squad to privately discuss and fix a security vulnerability in their project.
</code></pre>

<ul>
  <li>After collaborating on a fix, the project maintainers publish the security advisory to a project specific place.</li>
</ul>

<pre><code>Note: Projects hosted in GitHub take advantage of the GH features providing special security advisory dedicated pages.   
      See: <a href="https://docs.github.com/en/code-security/repository-security-advisories/creating-a-repository-security-advisory">https://docs.github.com/en/code-security/repository-security-advisories/creating-a-repository-security-advisory</a>
</code></pre>

<h3>Security updates</h3>

<p>Security notifications are distributed by the following methods.</p>

<ul>
  <li>Publishing project specific advisories in the corresponding project GitHub repository Security page.</li>
</ul>

<pre><code>For example you can find the API Mediation Layer related security advisories here: <a href="https://github.com/zowe/api-layer/security/advisories">https://github.com/zowe/api-layer/security/advisories</a>
</code></pre>

<ul>
  <li>Notification to Zowe users who explicitly requested receiving security alerts and advisories by subscribing to:
  <ul>
    <li><code>zowe-user@lists.openmainframeproject.org</code></li>
    <li><code>zowe-dev@lists.openmainframeproject.org</code></li>
  </ul>
  </li>
</ul>

<h2>Additional sources:</h2>

<ul>
  <li><a href="https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html">https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html</a></li>
  <li><a href="https://bestpractices.coreinfrastructure.org/en">https://bestpractices.coreinfrastructure.org/en</a></li>
  <li><a href="https://openssf.org/">https://openssf.org/</a></li>
  <li><a href="https://github.com/coreinfrastructure/best-practices-badge">https://github.com/coreinfrastructure/best-practices-badge</a></li>
  <li><a href="https://www.apache.org/security/">https://www.apache.org/security/</a></li>
</ul>

</div>
</div>
