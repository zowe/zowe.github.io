---
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<style>
table, th, td {
  border: 1px solid black;
}

.faq-hide {
  display: none;
}
</style>

<section class="whitebackground">
  <h1 id="download" style="margin-bottom: 1.5rem">Table of Content</h1>
  <ul>
    <li><a href="#general-information" class="card-link">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
      General Information 
      </a></li>
      <li><a href="#coming-changes" class="card-link">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
      Coming changes (For Users)
      </a></li>
      <li><a href="#conformance-changes" class="card-link">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
      Changes to the Conformance Criteria
      </a></li>
      <li><a href="#office-hours" class="card-link">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
      Office Hours
      </a></li>
  </ul>

  <div>
    <h2 style="margin-bottom: 1.5rem; margin-top: 2%" id="general-information">General Information</h2>
    <!-- <p>The preview of the docs-site is available at: <a
        href="https://docs.zowe.org/v2.0.x/getting-started/overview">Docs-site</a></p>
    <p>Download the latest release at: <a href="download.html">Download</a></p> -->
    <p>If you want to learn more about what you can expect compatibility wise, the statement is <a
      href="download.html#compatibility-extensions">here</a></p>
  </div>

  <h2 id="coming-changes">Coming changes (For Users)</h2>

  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.slack_url }}">API Mediation Layer</a></h5>
      </div>
      <ul>
        <li>Remove support for the old path pattern</li>
        <li>Move to the Material UI from Mineral UI</li>
        <li>New change password as a part of the API Catalog</li>
        <li>Remove the support for different authentication schemas for different instances of service</li>
      </ul>
      </p>
    </div>
  </div>

  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.omp_calendar_url }}">CLI</a></h5>
      </div>
      <p class="card-text">Zowe CLI - End User Breaking Changes</p>
      <p>
      <ul>
        <li>`zowe config` no longer manages app settings (Imperative & CLI)</li>
        <li>`fail-on-error` default changed to true for `zowe plugins validate` (Imperative & CLI)</li>
        <li>Default Imperative and CLI log level changed from DEBUG to WARN (Imperative & CLI) - just potentially
          changes troubleshooting steps for providing info to support.</li>
      </ul>
      </p>
      <p class="card-text">Breaking Changes that could prevent a V1 plug-in (or SDK) from working in V2</p>
      <p>
      <ul>
        <li>CLI package should be removed as a plug-in peer dep (Imperative)</li>
        <li>AbstractRestClient.mDecode defaults to true - so any plugin with custom RestClient implementation that
          adds gzip decompression may break</li>
        <li>Any command with --dcd will not behave the way you expect it to (undocumented global option for Daemon
          Mode Current Directory - to be mentioned in updated conformance criteria)</li>
        <li>PluginManagementFacility.requirePluginModuleCallback - return value changed. <br />
          Context:<br />
          Application (and Plugin) developers requiring a module from a plugin’s relative path using the
          requirePluginModuleCallback function no longer need to provide the plugin name in a separate variable
          (this.pluginNmForUseInCallback = pluginName)<br />
          before binding the class (this.requirePluginModuleCallback.bind(this)).<br />
          Instead they can call this.requirePluginModuleCallback(pluginName)</li>          
      </ul>
      </p>
      <p>Common usage: ConfigurationLoader.load</p>
      <p><b>Before:</b><br />
        this.pluginNmForUseInCallback = pluginName<br />
        ConfigurationLoader.load(null,pkgJsonData,this.requirePluginModuleCallback.bind(this))<br /></p>
      <p><b>After:</b> pluginConfig =
        ConfigurationLoader.load(null,pkgJsonData,this.requirePluginModuleCallback(pluginName))</p>
      <p class="card-text">All changes below were marked for deprecation in the zowe-v1-lts release. These changes are
        also less likely to impact plug-ins.</p>
      <p>
      <ul>
        <li>AbstractRestClient.performRest -> AbstractRestClient.request </li>
        <li>AbstractSession.HTTP_PROTOCOL -> SessConstants.HTTP_Protocol </li>
        <li>AbstractSession.HTTPS_PROTOCOL -> SessConstants.HTTPS_Protocol </li>
        <li>AbstractSession.TYPE_NONE -> SessConstants.AUTH_TYPE_NONE </li>
        <li>AbstractSession.TYPE_BASIC -> SessConstants.AUTH_TYPE_BASIC </li>
        <li>AbstractSession.TYPE_BEARER -> SessConstants.AUTH_TYPE_BEARER</li>
        <li>AbstractSession.TYPE_TOKEN -> SessConstants.AUTH_TYPE_TOKEN </li>
        <li>ICliLoadProfile.ICliILoadProfile -> ICliLoadProfile.ICliLoadProfile </li>
        <li>IImperativeErrorParms.suppressReport -> removed </li>
        <li>IImperativeConfig.pluginBaseCliVersion -> removed </li>
        <li>CliUtils.promptForInput -> CliUtils.readPrompt </li>
        <li>CliUtils.promptWithTimeout -> CliUtils.readPrompt </li>
        <li>(zosmf) IZosfmMessages -> IZosmfMessages  </li>
        <li>(workflows) listWorkflows -> getWorkflows </li>
        <li>(workflows) getResourcesQuery -> getResourceQuery </li>
        <li>(workflows) archiveWorfklowByKey -> archiveWorkflowByKey </li>
        <li>(uss) createBasicSshSession -> createSshSessCfgFromArgs </li>
        <li>(uss) createBasicSshSessionFromArguments -> createSshSessCfgFromArgs </li>
        <li>(zosmf) createBasicZosmfSession -> createSessCfgFromArgs </li>
        <li>(zosmf) createBasicZosmfSessionFromArguments -> createSessCfgFromArgs </li>
        <li>(files) bufferToUSSFile -> bufferToUssFile </li>
        <li>(files) streamToUSSFile -> streamToUssFile</li>
        <li>(files) fileToUSSFile -> fileToUssFile </li>
      </ul>
      </p>
      <p class="card-text">Zowe CLI & Imperative - Plug-in Developer Breaking Changes (V2-V2 - these changes only
        impacted early adopters of `@next` as these are breaking changes made during the technical preview validation
        phase - thanks to the community for their feedback)</p>
      <p>
      <ul>
        <li>`tokenType` and `tokenValue` were combined into `authToken` and we later reverted this change (Imperative
          & CLI) </li>
        <li>Options in “zowe config” group renamed: `--user` -> `--user-config` and `--global` -> `--global-config`
        </li>
        <li>Zowe.schema.json format changed a few times (version 2, version 3)
          ConfigSchemas.loadProfileSchemas -> ConfigSchemas.loadSchema
          Config.set no longer coerces string values to other types unless parseString = true (potential SDK impact -
          not CLI Plug-in impact)</li>
      </ul>
      </p>
    </div>
  </div>

  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.slack_url }}">Explorers</a></h5>
      </div>
      <ul>
        <li>Describes the change & what will break</li>
        <li>Changes to settings keys - automated migration of settings when user opens Zowe Explorer v2: PR 1450
          (includes documentation) - Merged</li>
        <li>(optional) Tips on how to make the transition process easier</li>
        <li>Describes the change & what will break</li>
        <li>See doc items marked with "Early Access" here:
          https://github.com/zowe/vscode-extension-for-zowe/tree/next/docs</li>
        <li>(optional) Tips on how to make the transition process easier</li>
      </ul>
      </p>
    </div>
  </div>

  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.slack_url }}">Systems</a></h5>
      </div>
      <ul>
        <li>Zowe v2: Review usage of z/OS System resources</li>
        <li>Start building 'v2' Zowe</li>
        <li>Spike: propose v2 changes and discuss with community</li>
        <li>Define new FMID AZWE002 for Zowe v2</li>
      </ul>
      </p>
    </div>
  </div>

  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.slack_url }}">Web UI</a></h5>
      </div>
      <ul>
        <li>zpdt tune option such as to reduce process/thread count (like not using "cluster mode")
          desktop library removal: bootstrap... bootstrap infects root, making it challenging to use other style
          libraries. Can have apps bring their own bootstrap as a solution, but is breaking as a result.</li>
        <li>update all var names to be ZWE_ and ZWED and ZWES consistently</li>
        <li>rename or get rid of zowe_explorer_host</li>
        <li>expose more zss configuration as parameters in instance.yaml</li>
        <li>Consolidation of web explorer servers (node code rolled into app-server) to reduce process count...
          breaking due to change of URLs (bookmarks break) #97</li>
        <li>Making the explorer java servers optional, by making the web explorers utilize zosmf instead</li>
        <li>desktop library upgrades (angular 6->10?, corejs 2->3)... can break plugins, but could choose minor
          upgrades that are less likely to do so #704</li>
        <li>eliminate loopback routing in favor of internal routing #706 ~75% done</li>
        <li>zss 64 bit #703 ~90% done</li>
      </ul>
      </p>
    </div>
  </div>

<section class="bluebackground">

  <h2 id="conformance-changes">Changes to the Conformance Criteria (For Extenders) </h2>

  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.slack_url }}">API Mediation Layer</a></h5>
      </div>
      <p class="card-text">Change to Item number 8: For versioned and non-versioned APIs, service URLs must contain a
        service version before the service ID (all formats)
        The new Item 8 will now read: For versioned and non-versioned APIs, service URLs must contain a service ID in
        the first place in the path, before the service version (all formats) </p>
      <p>Clarification to Item number 6: The API ID must follow the same rules for Java packages. Example of the API
        ID: zowe.apiml.apicatalog. The new Item 6 will now read: Services must provide API ID to allow for Automated
        CLI Client Configuration.</p>
    </div>
  </div>

  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.omp_calendar_url }}">CLI</a></h5>
      </div>
      <p class="card-text"></p>
    </div>
  </div>

  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.slack_url }}">Explorers</a></h5>
      </div>        
      <p class="card-text"></p>
    </div>
  </div>

  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.slack_url }}">Systems</a></h5>
      </div>
    </div>
  </div>

  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.slack_url }}">Web UI</a></h5>
      </div>
    </div>
  </div>

</section>

<section class="whitebackground">
  <div id="office-hours">
    <h2 style="margin-bottom: 1.5rem; margin-top: 2%">Office Hours Recordings</h2>
    <table>
    <tr>
    <td><b>Date</b></td>
    <td><b>Topic</b></td>
    <td><b>Link to the meeting</b></td>
    <td><b>Link to the recording</b></td>
    </tr>
    <tr>
    <td>12/8</td>
    <td>Kickoff</td>
    <td>https://zoom.us/j/94312528890</td>
    <td></td>
    </tr>
    <tr>
    <td>12/15</td>
    <td>CLI</td>
    <td>https://zoom.us/j/94312528890</td>
    <td></td>
    </tr>
    <tr>
    <td>12/29</td>
    <td>API Mediation Layer</td>
    <td>https://zoom.us/j/94312528890</td>
    <td></td>
    </tr>    
    <tr>
    <td>1/12</td>
    <td>Explorers</td>
    <td>https://zoom.us/j/94312528890</td>
    <td></td>
    </tr>
    <tr>
    <td>1/26</td>
    <td>Web UI (App Framework)</td>
    <td>https://zoom.us/j/94312528890</td>
    <td></td>
    </tr>
    <tr>
    <td>2/9</td>
    <td>Systems / Install</td>
    <td>https://zoom.us/j/94312528890</td>
    <td></td>
    </tr>
    <tr>
    <td>2/23</td>
    <td>General Wrap-up</td>
    <td>https://zoom.us/j/94312528890</td>
    <td></td>
    </tr>
    </table>
  </div>

</section>
<section class="bluebackground">

  <script>
    function toggle(id) {
      var x = document.getElementById(id);
      if (x.className.indexOf("faq-hide") == -1) {
        x.className += " faq-hide";
      } else {
        x.className = x.className.replace(" faq-hide", "");
      }
    }
  </script>

  <div>
    <h2 style="margin-bottom: 1.5rem; margin-top: 2%">Frequently Asked Questions</h2>
    <button onclick="toggle('question-1')" class="w3-button w3-block w3-left-align">
    1. What is the “official” date of Zowe V2 LTS?</button>
    <div id="question-1" class="w3-container w3-hide">
      <p>&nbsp;&nbsp;&nbsp;a. The official date is TBD, the target is Feb 28, 2022; look for the official announcement at
      Zowe.orglanding page announcement banner</p>
    </div>
    <p>1. What is the “official” date of Zowe V2 LTS?</p>
    <p></p>
    <p>2. Where can I find the current (V1) and new (V2) LTS conformance criteria?</p>
    <p>&nbsp;&nbsp;&nbsp;a.The Zowe Squads have prepared XLS spreadsheets with conformance criteria for all Zowe
      extensionsincluding: CLI, APIs, App Framework, and Explorerfor VS Code. The spreadsheets clearly show the prior /
      V1 criteria alongside the new / V2 criteria. Please be aware, there are additions, deletions, and CHANGES to the
      criteria. In some cases the change issimply thata BEST PRACTICE has been deemed REQUIRED. Use the light-GREEN
      highlights to easily identify the changes.See the FOR EXTENDERSsection at Zowe.org/vNext.</p>
    <p>3.Will my V1 conformant extension automatically work with V2?</p>
    <p>&nbsp;&nbsp;&nbsp;a.NO. We recommend testing all V1 conformant extensions. See the COMPATIBILITYsection at
      Zowe.org/Vnext</p>
    <p>4.What if my extension does not work with Zowe V2?</p>
    <p>&nbsp;&nbsp;&nbsp;a.See the recommendations in the COMPATIBILITYsection at Zowe.org/Vnext</p>
    <p>5.How can I test my current plug-in and/or extension with Zowe V2?</p>
    <p>&nbsp;&nbsp;&nbsp;a.Obtain the pre-GA Zowe V2 release; for details see the pre-GA DOWNLOADsection at
      Zowe.org/Vnext</p>
    <p>6.Do I need to reapply for conformance?</p>
    <p>&nbsp;&nbsp;&nbsp;a.YES, we expect the Zowe V2 Conformance program to be available in early Feb 2022. We will
      announce when extenders my pre-apply in the LATEST ANNOUNCEMENTSsection at Zowe.org/Vnext</p>
    <p>7.What happens to my V1 conformance badge?</p>
    <p>&nbsp;&nbsp;&nbsp;a.All Zowe V1 conformance badges will remain at the Open Mainframe Project Interactive
      Landscape; we recommend documenting a Zowe compatibility matrixto ensure clients are aware of any/all
      compatibility issues between your V1 conformant apps and Zowe V2</p>
    <p>8.Will I be able to pre-apply for Zowe V2 conformance?</p>
    <p>&nbsp;&nbsp;&nbsp;a.Yes, We will announce when extenders my pre-apply in the LATEST ANNOUNCEMENTSsection at <a
        href="vNext.html">Zowe.org/Vnext</a></p>
    <p>9.When can I share this information with my customers?</p>
    <p>&nbsp;&nbsp;&nbsp;a.Anytime. Zowe is an Open Source project managed by a transparent, Open Source Community.</p>
    <p>10.How long willV1LTS be supported?</p>
    <p>&nbsp;&nbsp;&nbsp;a.The V1 LTS Maintenancetimeline runs through July 2024. See RELEASE TIMELINE at <a
        href="download.html">Zowe.org/download</a></p>
    <p>11.What if my extension does not qualify for V2 conformance?</p>
    <p>&nbsp;&nbsp;&nbsp;a.You have several options:</p>
    <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i.Notify your customer base and advise them to remain on Zowe V1 LTS until
      you are able to make the necessary modifications to satisfy all of the new requirements (Note: extenders can
      choose NOT to be “day-1” V2 conformant )</p>
    <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ii.Notify your customer base of V2 compatibility concerns (or lack thereof)
      and advise accordingly (e.g. extension operates but will not leverage V2 features etc.)</p>
    <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iii.Replace your extension with a V2 conformant extension and indicate it as
      such</p>
    <p>12.Where can I go for more information or get interactive help? (my question is not listed here)</p>
    <p>&nbsp;&nbsp;&nbsp;a.You have several options:</p>
    <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i.Attend one (or more) of the (7) bi-weekly Zowe V2 OFFICE HOURS meetings
      offered on Wednesdays at 12pm ET. Kickoff is scheduled for 12/8. Following (6) meetings are scheduled for: 12/15,
      12/29(?), 1/12, 1/26, 2/9, 2/23</p>
    <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ii.Interact with a Zowe Community Member via SLACK. Click on the COMMUNITYtab
      at Zowe.org, navigate to the SLACK box and click #zowe-onboarding</p>
    <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iii.Join a Zowe Squad call. Click on the COMMUNITYtab at zowe.org, navigate
      to the JOIN A SQUAD CALLsection on this page.Click on one of the calendar entries for Zoom meeting links</p>
    <p>13.Will the Zowe V2 Office Hours be recorded? (Howdo I find the recording?)</p>
    <p>a.Yes. Recordings can be provided on request. Click on the COMMUNITYtab at Zowe.org, navigate to the SLACK box
      and click #zowe-onboardingand request the recording.</p>
  </div>

  

</section>