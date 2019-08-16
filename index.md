<p style="padding-left:7%;padding-top:2%;padding-bottom:2%"><strong>Please note: this website is under-construction. Please visit https://zowe.org and check the most recent news of Zowe.</strong></p>

<div class="announcementsection">
<h1>Announcements</h1>
<strong>Zowe {{ site.releases[0].version }} is now available. See <a href="{{ site.releases[0].release_notes }}">What's New</a>.<br></strong>
</div>

<section class="whitebackground" style="padding-top:1%">

<h1 id="what-is-zowe">What is Zowe?</h1>

<div class="section1col1">
<p>
Zowe is an open source project created to host technologies that benefit the Z platform from all members of the Z community (Integrated Software Vendors, System Integrators and z/OS consumers). Zowe, like Mac OS or Windows, comes with a set of APIs and OS capabilities that applications build on and also includes some applications out of the box.
</p>
  
<p>
Zowe offers modern interfaces to interact with z/OS and allows you to work with z/OS in a way that is similar to what you experience on cloud platforms today. You can use these interfaces as delivered or through plug-ins and extensions that are created by clients or third-party vendors.
</p>

<p>Zowe consists of the following main components.</p>

<p><b>Zowe Application Framework:</b> A web user interface (UI) that provides a virtual desktop containing a number of apps allowing access to z/OS function.  Base Zowe includes apps for traditional access such as a 3270 terminal and a VT Terminal, as well as an editor and explorers for working with JES, MVS Data Sets and Unix System Services.</p>

<p><b>API Mediation Layer:</b> Provides a gateway that acts as a reverse proxy for z/OS services, together with a catalog of REST APIs and a dynamic discovery capability. Base Zowe provides core services for working with MVS Data Sets, JES, as well as working with z/OSMF REST APIs. The API Mediation Layer also provides a framework for Single Sign On (SSO). </p>

<p><b>Zowe CLI:</b> Provides a command-line interface that lets you interact with the mainframe remotely and use common tools such as Integrated Development Environments (IDEs), shell commands, bash scripts, and build tools for mainframe development. It provides a set of utilities and services for application developers that want to become efficient in supporting and building z/OS applications quickly. The CLI provides a core set of commands for working with data sets, USS, JES, as well as issuing TSO and console commands.</p>
</div>

<div class="videocol">
<object style="width:100%;height:330px;width:100%; float: none; clear: both; margin: 2px auto;" data="{{ site.latest_video_embed }}">
</object>
</div>

</section>

<section class="bluebackground">

<h1 id="documentation">Try Zowe now</h1>
<p>
Try Zowe today at no charge, and with no installation required. Your no-charge trial is available in two hours for three days. Register and get started today. 
</p>
<button><a href="{{ site.ibm_ztrial_url }}">Request a trial</a></button>
<p>* By proceeding to the trial, you will be leaving the Zowe.org website.</p>

</section>

<section class="whitebackground">

<h1 id="download">Download</h1>
<p>
The easiest way to get started with Zowe is by downloading the convenience build. You can also go to the GitHub repository to build Zowe on your own.
</p>
<button><a href="{{ site.releases[0].zos_download_url }}">Zowe z/OS Components</a></button>
<button><a href="{{ site.releases[0].cli_download_url }}">Zowe Command Line Interface</a></button>
<button><a href="{{ site.github_repo_url }}">Zowe GitHub repository</a></button>
<details>
<summary>Past Releases</summary>
<table>
{% for release in site.releases %}
  {% unless forloop.first %}
  <tr>
    <td>Zowe {{release.version}} ({{release.release_date}})</td>
    <td><a href="{{release.zos_download_url }}">Zowe z/OS Components</a></td>
    <td><a href="{{release.cli_download_url }}">Zowe Command Line Interface</a></td>
    <td><a href="{{release.release_notes}}">Release Notes</a></td>
    <td><a href="{{release.documentation}}">Documentation</a></td>
  </tr>
  {% endunless %}
{% endfor %}
</table>
</details>
<p>
* Please note the Zowe binaries are made available to you by Zowe Binary Projects a Series of LF Projects, LLC, and not by The Linux Foundation or the Open Mainframe Project.
</p>
</section>

<section class="bluebackground">

<h1 id="documentation">Documentation</h1>
<p>
Check out quick start guides, user guides, developer guides, references, tutorials, and more.
</p>
<button><a href="{{ site.docs_site_url }}">Read the docs</a></button>

</section>

<section class="whitebackground">

<h1 id="community">Community</h1>
<p>
Zowe is more than a framework - it's a worldwide community of developers, vendors, and users building and extending Zowe. Discover how you can connect, learn, and contribute to it's future.
</p>
<button><a href="{{ site.community_site_url }}">Learn more</a></button>
