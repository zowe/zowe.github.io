---
---
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<section class="whitebackground" style="padding-top:1%">
<h1 id="download">Download Zowe</h1>
<div class="card">
  <div class="card-body">
  <p class="card-text">
    Zowe has both server and client components, which you can install independently. Download the latest installer to install Zowe on the z/OS server, on your computer, or both. Start your journey with Zowe today!
  </p>
  <p class="card-text">
    Want to build Zowe on your own? Access <a href="{{ site.github_repo_url }}">Zowe GitHub repositories</a> to download the source code.
  </p>
  </div>
</div>
<p> </p>
{% if site.data.releases[0].cli_version and site.data.releases[0].cli_plugins_version and site.data.releases[0].zos_version and site.data.releases[0].smpe_version and site.data.releases[0].node_sdk_version and site.data.releases[0].python_sdk_version %}
<div class="card-deck">
<div class="card bg-light border-light mb-3">
  <h4 class="card-header">Server-side component installer</h4>
    <div class="card-body">
    <p class="card-text">Install Zowe z/OS components from the <b>convenience build</b> or the <b>SMP/E build</b> depending on your need.</p>
    <p class="card-text">You can also optionally use the Docker build technical preview to run a subset of the Zowe server-side components outside z/OS. Download and learn more about the build in the technical preview section.</p>
        <div class="row">
          <div class="card-body">
            <h5 class="card-title">Convenience build</h5>
            <p class="card-text">PAX archive format installed on the z/OS server</p>
            <p><a class="btn btn-primary" href="{{ site.zos_download_url }}{{ site.data.releases[0].zos_version }}">Zowe {{ site.data.releases[0].zos_version }} z/OS Convenience build</a></p>
          <div>
            <a href="{{ site.zos_component_install_doc_url }}" class="card-link">
            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
            Read installation docs
            </a>
          </div>
          </div>
          <div class="card-body">
            <h5 class="card-title">SMP/E build</h5>
            <p class="card-text">SMP/E format installed on the z/OS server</p>
            <p class="card-text">Download the base FMID AZWE001 (based on v1.9.0) first and then apply the PTFs to get the latest version. </p>
            <p><a class="btn btn-primary" href="{{ site.smpe_download_url }}{{ site.zowe_fmid_oss_version }}">Zowe 1.9.0 FMID {{ site.zowe_fmid }}</a></p>
            <p><a class="btn btn-primary" href="{{ site.smpe_download_url }}{{ site.data.releases[0].smpe_version }}">Zowe {{ site.data.releases[0].zos_version }} {{ site.data.releases[0].smpe_sysmod }} {{ site.data.releases[0].smpe_numbers }}</a></p>
            <div>
              <a href="{{ site.zos_component_install_doc_url }}" class="card-link">
              <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
              Read installation docs
              </a>
            </div>
          </div>
       </div>
    </div>
  </div>
<div class="card bg-light border-light mb-3">
  <h4 class="card-header">Client-side component installer</h4>
    <div class="card-body">
    <p class="card-text">Install <b>Zowe CLI</b> or <b>Zowe Explorer</b>, a Visual Studio Code extension powered by Zowe CLI.</p>
      <div class="row">
        <div class="card-body">
          <h5 class="card-title">Zowe CLI</h5>
          <p class="card-text">Install Zowe CLI from the local package or from an npm registry if your computer is connected to the Internet.</p>
          <p class="card-text">Download the Zowe CLI core package and optionally download the plug-ins (CICS, Db2, IMS, MQ, z/OS FTP, and so on) to gain more capabilities.</p>
          <p><a class="btn btn-primary" href="{{ site.cli_download_url }}{{ site.data.releases[0].cli_version }}">Zowe {{ site.data.releases[0].cli_version }} CLI Core</a></p>
          <p><a class="btn btn-primary" href="{{ site.cli_plugins_download_url }}{{ site.data.releases[0].cli_plugins_version }}">Zowe {{ site.data.releases[0].cli_plugins_version }} CLI Plug-ins</a></p>
          <div>
            <a href="{{ site.zowe_cli_install_doc_url }}" class="card-link">
            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
            Read installation docs
            </a>
          </div>
        </div>        
        <div class="card-body">
          <h5 class="card-title">Zowe Client SDKs</h5>
          <p class="card-text">Download the Zowe Software Development Kits (SDKs) for use in development and automation.</p>
          <p><a class="btn btn-primary" href="{{ site.zowe_node_sdk_download_url }}{{ site.data.releases[0].node_sdk_version }}">Zowe {{ site.data.releases[0].node_sdk_version }} Node.js Client SDK</a></p>
          <p><a class="btn btn-primary" href="{{ site.zowe_python_sdk_download_url }}{{ site.data.releases[0].python_sdk_version }}">Zowe {{ site.data.releases[0].python_sdk_version }} Python Client SDK</a></p>
          <div>
            <a href="{{ site.zowe_sdk_install_doc_url }}" class="card-link">
            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
            Read installation docs
            </a>
          </div>
        </div>
        <div class="card-body">
          <h5 class="card-title">Zowe Explorer</h5>
          <p class="card-text">Installed directly to VSCode within the GUI</p>
          <p><a class="btn btn-primary" href="{{ site.vscode_marketplace_url }}">Visual Studio Code Marketplace</a></p>
          <div>
            <a href="{{ site.zowe_explorer_install_doc_url }}" class="card-link">
            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
            Read installation docs
            </a>
          </div>
       </div>
     </div>
   </div>
</div>
</div>
{% else %}
  <p>
    <a class="button" href="{{ site.zos_download_url }}{{ site.data.releases[0].version }}">Zowe {{ site.data.releases[0].version }} z/OS Convenience build</a>
    <a class="button" href="{{ site.cli_download_url }}{{ site.data.releases[0].version }}">Zowe {{ site.data.releases[0].version }} CLI</a>
  </p>
{% endif %}
<p> </p>

<h2>Zowe Technical Preview</h2>
<p>
Test the latest Zowe features and provide feedback. Technical previews are <b>for testing only</b> and not ready for production.</p>
<p>Explore the upcoming production-ready release below and provide feedback to the community on the documentation, user experience, and desired features that can be implemented in future releases. Any feedback that you can provide is highly appreciated. Let us know via Slack or GitHub!
</p>
<div class="card-deck">
  <div class="card bg-light border-light mb-3">
  <h4 class="card-header">Zowe Docker build</h4>
    <div class="card-body">
    <p class="card-text">The Zowe Docker build enables you to run a subset of the Zowe server-side components outside z/OS. The Docker build runs in combination with the convenience or S MP/E build. Learn more about the relationship of the builds in the docs.</p>
    <p class="card-text">You can download the build directly via the tarball, or as a cloud download from Docker Hub. Separate downloads exist for z/Linux ("s390x") and other Linux ("amd64" for intel & amd systems).</p>
        <div class="row">
          <div class="card-body">
            <h5 class="card-title">Direct download</h5>
            <p><a class="btn btn-primary" href="{{ site.docker_download_url }}{{ site.data.releases[0].zos_version }}/server-bundle.amd64-{{ site.data.releases[0].zos_version }}.tar">Zowe {{ site.data.releases[0].zos_version }} amd64 tarball</a></p> 
            <p><a class="btn btn-primary" href="{{ site.docker_download_url }}{{ site.data.releases[0].zos_version }}/server-bundle.s390x-{{ site.data.releases[0].zos_version }}.tar">Zowe {{ site.data.releases[0].zos_version }} s390x tarball</a></p> 
          </div>
          <div class="card-body">
            <h5 class="card-title">Cloud download</h5>
            <p><a class="btn btn-primary" href="{{ site.zowe_dockerhub_download_url }}">Zowe v1.x LTS Docker Hub</a></p>
            <div>
              <a href="{{ site.docker_install_doc_url }}" class="card-link">
              <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
              Read installation docs
              </a>
            </div>
         </div>
      </div>   
    </div>
  </div>
</div>


<h1>Previous Releases</h1>
<p>
Download previous releases of Zowe by version number.
</p>
<p>
Zowe version 1.0.0 through 1.8.0 are only available as rollup convenience builds. Zowe version 1.9.0 is the beginning of the Active Long-Term Support (LTS) release and it provides an SMP/E build with an FMID of AZWE001. The SMP/E build is the same content as the Zowe 1.9.0 convenience build. Updates in subsequent releases are made available as co-requisite PTFs as well as in convenience builds. Also, starting in 1.9.0, Zowe CLI core and plug-in packages are distributed separately.
</p>
{% for release in site.data.releases %}
  {% if forloop.first %}
  <table class="table table-hover table-sm">
  {% endif %}
  {% unless forloop.first %}
    <tr>
      <td>Zowe {{release.version}} ({{release.release_date}})</td>
    {% if release.zos_version %}
      <td><a href="{{site.zos_download_url}}{{release.zos_version}}">z/OS Convenience build</a></td>
    {% else %}
      <td><a href="{{site.zos_download_url}}{{release.version}}">z/OS Convenience build</a></td>
    {% endif %}
    {% if release.smpe_version and release.smpe_sysmod %}
      <td><a href="{{site.smpe_download_url}}{{release.smpe_version}}">SMP/E {{release.smpe_sysmod}} {{release.smpe_numbers}}</a></td>
    {% else %}
      <td></td>
    {% endif %}
    {% if release.cli_version and release.cli_plugins_version %}
      <td><a href="{{site.cli_download_url}}{{release.cli_version}}">CLI Core</a></td>
    {% else %}
      {% if release.cli_version %}
        <td><a href="{{site.cli_download_url}}{{release.cli_version}}">CLI</a></td>
      {% else %}
        <td><a href="{{site.cli_download_url}}{{release.version}}">CLI</a></td>
      {% endif %}
    {% endif %}
    {% if release.cli_plugins_version %}
      <td><a href="{{site.cli_plugins_download_url}}{{release.cli_plugins_version}}">CLI Plug-ins</a></td>
    {% else %}
      <td></td>
    {% endif %}
      <td><a href="{{ site.docs_site_url }}/{{release.documentation}}/getting-started/summaryofchanges.html">Release Notes</a></td>
      <td><a href="{{ site.docs_site_url }}/{{release.documentation}}">Documentation</a></td>
    </tr>
  {% endunless %}
  {% if forloop.last %}
  </table>
  <p class="text-muted">All builds prior to Zowe v1.0.0 are no longer available.</p>
  {% endif %}
{% endfor %}
</section>

<section class="bluebackground">
<h1>Release Timeline</h1>
<p><img src="assets/img/zowe-lts.png" width="950" /></p>
<p><b>Version timeframe, Current, Active LTS, Maintenance</b></p>
<ul>
<li>New Zowe versions will enter <b>current</b> release status for six to nine months to allow consumers of Zowe to test, provide feedback, and adjust to any changes.</li>
<li>After current release phase, Zowe will move to <b>Active LTS</b> status and will be deemed ready by the community for general use. <b>Active LTS</b> will have additional releases with both fixes and enhancements.</li>
<li>Following a period of <b>Active LTS</b>, the Zowe version will enter <b>Maintenance</b> for fixes only.</li>
<li>The combination of <b>Active LTS</b> and <b>Maintenance LTS</b> release is designated as <b>"long-term support”</b>, which provides two guarantees:
  <ul>
    <li>Critical defects will be fixed. The criteria for what constitutes a critical defect is covered in <a href="{{ site.lts_url }}">Release Process</a>.</li>
    <li>Extenders who achieve Zowe conformance for the long-term support version will not need to modify their product for it to remain functional when the Zowe community provides distributions within the release or  modification level boundary within the same version.</li>
  </ul>
</li>
<li>The length of <b>Active LTS</b> may vary but the total time period of <b>Active LTS</b> + <b>Maintenance LTS</b> will be at least 24 months.</li>
<li>Production applications should only use <b>Active LTS</b> or <b>Maintenance LTS</b> releases due to the contract with extender products remaining functional and the community’s commitment to fix critical defects.</li>
</ul>
<a class="button" href="{{ site.lts_url }}">Learn more</a>
</section>

<section class="whitebackground">
<h1>Nightly Builds</h1>
<p>Visit the Zowe Artifactory <a class="white" href="{{ site.nightly_build_url }}">nightly build folder</a> to find the most recent build.</p>
<p>Please note:
  <ul>
    <li>Nightly builds are made available to allow preview and early distribution of in-progress work items which may be functionally incomplete and unstable. The coverage and successful execution of tests has not been guaranteed and the builds should be treated accordingly.</li>
    <li>The latest build status is available from <a class="white" href="{{ site.zowe_build_slack_url }}">#zowe-build Slack channel</a>.</li>
    <li>A nightly build will be removed about 30 days after release.</li>
  </ul>
</p>
</section>


