---
redirect_from:
  - "/home"
  - "/home/"
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<script>
  fetch(`https://www.api.metrics.zowe.org/cli`)
    .then((response) => response.json())
    .then((data) => {
      document.querySelector('#cli-downloads').innerHTML = data.downloads;
    });
  fetch(`https://www.api.metrics.zowe.org/explorer`)
    .then((response) => response.json())
    .then((data) => {
      document.querySelector('#explorer-downloads').innerHTML = data.downloads;
    });
  fetch(`https://www.api.metrics.zowe.org/server`)
    .then((response) => response.json())
    .then((data) => {
      document.querySelector('#server-downloads').innerHTML = data.downloads;
    });
  fetch(`https://www.api.metrics.zowe.org/omp`)
    .then((response) => response.json())
    .then((data) => {
      document.querySelector('#slack-members').innerHTML = data.slackParticipants;
    });
  fetch(`https://www.api.metrics.zowe.org/omp`)
    .then((response) => response.json())
    .then((data) => {
      document.querySelector('#github-contributors').innerHTML = data.githubSubmittors;
    });
  fetch(`https://www.api.metrics.zowe.org/conformants`)
    .then((response) => response.json())
    .then((data) => {
      document.querySelector('#conformant-product-value').innerHTML = data.products;
    });
</script>

<div class="announcementsection">
  <h1>Announcements</h1>
  <!-- <p>
    <strong>New Build: </strong>Zowe {{ site.data.releases[0].version }} is now available. Install it from <a href="/download">here</a>, and check out the Release notes <a href="{{ site.docs_site_url }}/{{site.data.releases[0].documentation}}/getting-started/summaryofchanges.html">here</a>.
  </p>
  <p>
    <strong>Upcoming Events: </strong>Join the Quaterly Webinar to learn about the present and future of Zowe - find out more here
  </p>
  <p>
    <strong>New Features: </strong>
  </p> -->
  <strong>Zowe {{ site.data.releases[0].version }} is now available. You can download the installers and PTFs ({{ site.data.releases[0].smpe_numbers }}) for this release from the <a href="/download">Download</a> page. To learn what's new in this release, see the <a href="{{ site.docs_site_url }}/{{site.data.releases[0].documentation}}/getting-started/summaryofchanges.html">Release notes</a>.<br></strong>
  {% if site.data.announcements %}
    {% for announcement in site.data.announcements %}
    <hr class="w-100" style="margin-top: 0.5rem; margin-bottom: 0.5rem; border-top: 1px solid rgb(0 0 0 / 20%)">
    <strong>{{ announcement.announcement }}
      {% if announcement.link %}
        <a href="{{ announcement.link }}">Learn More</a>
      {% endif %}
      <br>
    </strong>
    {% endfor %}
  {% endif %}
</div>

<div style="text-align: center; padding: 3%; background-image: url('assets/img/bg2.png'); background-repeat: no-repeat; background-size: cover; color: white !important"> 
  <h1 id="conformance" style="margin-bottom: 2%">Open, Simple, Familiar</h1>
  <h4 style="">Combining the past and the present to build the future of mainframe</h4>
</div>

<div class="row" style="padding: 5%">
  <div class="col-12 col-md-8">
    <p>Zowe is an integrated and extensible open source framework for z/OS. Zowe, like Mac OS or Windows, comes with a set of APIs and OS capabilities that applications build on and also includes some applications out of the box. 
    </p>
    <br>
    <p>Zowe offers modern interfaces to interact with z/OS and allows you to work with z/OS in a way that is similar to what you experience on cloud platforms today. You can use these interfaces as delivered or through plug-ins and extensions that are created by clients or third-party vendors. 
    </p>
    <p>Zowe is composed of several components, each improving the learning ability, accessibility, and possibility of mainframe development.</p>
    <div class="d-flex flex-column">
      <a href="#app-framework-intro" class="card-link" style="margin-left: 1.25rem">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
      Zowe Application Framework
      </a>
      <a href="#apiml-intro" class="card-link">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
      Zowe API Mediation Layer
      </a>
      <a href="#cli-intro" class="card-link">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
      Zowe CLI
      </a>
      <a href="#zowe-explorer-intro" class="card-link">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
      Zowe Explorer
      </a>
      <a href="#zowe-client-sdk-intro" class="card-link">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
      Zowe Client SDKs - under development
      </a>
      <a href="#zowe-mobile-intro" class="card-link">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
      Zowe Mobile - Incubator
      </a>
      <a href="#zebra-intro" class="card-link">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
      ZEBRA (Zowe Embedded Browser for RMF/SMF and APIs) - Incubator
      </a>
    </div>
  </div>
  <div class="col-12 col-md-4 zowe-video">
    <iframe title="Introduction to Zowe" src="{{ site. latest_video_embed }}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="width: -webkit-fill-available; height: 100%"></iframe>
    <p>
      <a href="{{ site.zowe_video_deck_url }}">Download Slides (.pptx)</a>&nbsp;|&nbsp;
      <a href="{{ site.zowe_video_transcript_url }}">Download Transcript (.txt)</a>
    </p>
  </div>
</div>

<div style="padding: 4% 7% 5% 7%" class="bg-light">
    <h2 class="text-center" style="color: black !important; margin-bottom: 5%">What would you like to do with Zowe?</h2>
    <div class="row">
      <div class="col-sm text-center">
        <a href="/learn"><button type="button" class="btn btn-primary btn-lg btn-block">Learn</button></a>
        <p style="margin-top: 1rem">Learn how Zowe works and what it can do for you</p>
      </div>
      <div class="col-sm text-center">
        <a href="https://docs.zowe.org/stable/user-guide/installandconfig.html"><button type="button" class="btn btn-primary btn-lg btn-block">Use</button></a>
        <p style="margin-top: 1rem">Get started with installing and using Zowe</p>
      </div>
      <div class="col-sm text-center">
        <a href="/extend"><button type="button" class="btn btn-primary btn-lg btn-block">Extend</button></a>
        <p style="margin-top: 1rem">Build the next generation of mainframe tooling on top of Zowe</p>
      </div>
      <div class="col-sm text-center">
        <a href="/contribute"><button type="button" class="btn btn-primary btn-lg btn-block">Contribute</button></a>
        <p style="margin-top: 1rem">Contribute to the open source community developing Zowe</p>
      </div>
    </div>
</div> 

  {% if site.data.upcoming_events.size >= 1 %}
  <section id="events" style="margin-top: 3%">
    <div style="padding: 0% 7%">
      <h2 class="mb-3 text-center">Upcoming events</h2>
      <div class="row py-4">
        {% for events in site.data.upcoming_events limit:3 %}
        <div class="col-md-4 px-3 pb-4 pb-md-0"> <!-- ml-auto mr-auto -->
          <div class="w-100 px-4 py-4 rounded shadow bg-light h-100">
          {% if events.url %}
            <h5 class="border-bottom border-primary pb-2"><a href="{{ events.url }}">{{ events.event }}</a></h5>
          {% else %}
            <h5 class="border-bottom border-primary pb-2">{{ events.event }}</h5>
          {% endif %}
            <span style="font-weight: 600">{{ events.schedule }}</span>
            <br>
            <span class="text-muted small">{{ events.description }}</span>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
  </section>
  {% endif %}

<div style="padding: 4% 7% 5% 7%">
  <div>
    <h2 class="text-center" style="color: black !important; margin-bottom: 3%">Zowe components</h2>
  </div>

  <div>
    <div class="row" style="margin-bottom: 4%">
      <div class="col-md-7 col-sm order-last order-sm-first">
        <a id="app-framework-intro"><h4>Zowe Application Framework</h4></a>
        <p style="margin: 1rem auto">  
        A web user interface (UI) that provides a virtual desktop containing a number of apps allowing access to z/OS function. Base Zowe includes apps for traditional access such as a 3270 terminal and a VT Terminal, as well as an editor and explorers for working with JES, MVS Data Sets and Unix System Services.
        </p>
        <p>
          <a href="{{ site.app_framework_github_url }}">Code on GitHub</a>&nbsp;|&nbsp;
          <a href="{{ site.app_framework_slack_url }}">Connect on Slack</a>&nbsp;|&nbsp;
          <a href="{{ site.app_framework_doc_url }}">Learn more</a>&nbsp;|&nbsp;
          <a href="{{ site.app_framework_tour_url }}">View Tour</a>
        </p>
      </div>
      <div class="col-md-5 col-sm order-first order-sm-last">
        <img class="image-zowe-use" src="assets/img/zowe-desktop-image.png">
      </div>
    </div>
    <hr class="w-75 mt-5 mb-5">
    <div class="row" style="margin-bottom: 4%">
      <div class="col-md-5 col-sm">
        <img class="image-zowe-use" src="assets/img/zowe-apiml-image.png">
      </div>
      <div class="col-md-7 col-sm">
        <a id="apiml-intro"><h4>API Mediation Layer</h4></a>
          <p style="margin: 1rem auto">Provides a gateway that acts as a reverse proxy for z/OS services, together with a catalog of REST APIs and a dynamic discovery capability. Base Zowe provides core services for working with MVS Data Sets, JES, as well as working with z/OSMF REST APIs. The API Mediation Layer also provides a framework for Single Sign On (SSO). 
          </p>
          <p>
            <a href="{{ site.apiml_github_url }}">Code on GitHub</a>&nbsp;|&nbsp;
            <a href="{{ site.apiml_slack_url }}">Connect on Slack</a>&nbsp;|&nbsp;
            <a href="{{ site.apiml_doc_url }}">Learn more</a>
          </p>
      </div>
    </div>
    <hr class="w-75 mt-5 mb-5">
    <div class="row" style="margin-bottom: 4%">
      <div class="col-md-7 col-sm order-last order-sm-first">
        <a id="cli-intro"><h4>Zowe CLI</h4></a>
        <p style="margin: 1rem auto">Provides a command-line interface that lets you interact with the mainframe remotely and use common tools such as Integrated Development Environments (IDEs), shell commands, bash scripts, and build tools for mainframe development. It provides a set of utilities and services for application developers that want to become efficient in supporting and building z/OS applications quickly. The CLI provides a core set of commands for working with data sets, USS, JES, as well as issuing TSO and console commands.</p>
          <p>
            <a href="{{ site.zowe_cli_github_url }}">Code on GitHub</a>&nbsp;|&nbsp;
            <a href="{{ site.zowe_cli_slack_url }}">Connect on Slack</a>&nbsp;|&nbsp;
            <a href="{{ site.zowe_cli_doc_url }}">Learn more</a>
          </p>
      </div>
      <div class="col-md-5 col-sm order-first order-sm-last">
        <img class="image-zowe-use" src="assets/img/zowe-cli.png">
      </div>
    </div>
    <hr class="w-75 mt-5 mb-5">
    <div class="row" style="margin-bottom: 4%">
      <div class="col-md-5 col-sm">
        <img class="image-zowe-use" src="assets/img/zowe-explorer-image.png">
      </div>
      <div class="col-md-7 col-sm">
        <a id="zowe-explorer-intro"><h4>Zowe Explorer</h4></a>
          <p style="margin: 1rem auto">A Visual Studio Code extension that modernizes the way developers and system administrators interact with z/OS mainframes. Zowe Explorer lets you interact with data sets, USS files, and jobs that are stored on z/OS. The extension complements your Zowe CLI experience and lets you use authentication services like API Mediation Layer.</p>
          <p>
            <a href="{{ site.zowe_explorer_github_url }}">Code on GitHub</a>&nbsp;|&nbsp;
            <a href="{{ site.zowe_explorer_slack_url }}">Connect on Slack</a>&nbsp;|&nbsp;
            <a href="{{ site.zowe_explorer_doc_url }}">Learn more</a>
          </p>
      </div>
    </div>
    <hr class="w-75 mt-5 mb-5">
    <div class="row" style="margin-bottom: 4%">
      <div class="col-md-7 col-sm order-last order-sm-first">
        <a id="zowe-client-sdk-intro"><h4>Zowe Client SDKs (under development)</h4></a>
        <p style="margin: 1rem auto">Provides access to a set of programmatic APIs that you can use to build client applications or scripts that interact with z/OS. SDKs are available for Node.js and Python.</p>
          <p>
            <a href="{{ site.zowe_sdk_github_url }}">Code on GitHub</a>&nbsp;|&nbsp;
            <a href="{{ site.zowe_sdk_slack_url }}">Connect on Slack</a>&nbsp;|&nbsp;
            <a href="{{ site.zowe_sdk_doc_url }}">Learn more</a>
          </p>
      </div>
      <div class="col-md-5 col-sm order-first order-sm-last">
        <img class="image-zowe-use" src="assets/img/zowe-client-sdk-image.png">
      </div>
    </div>
    <hr class="w-75 mt-5 mb-5">
    <div class="row" style="margin-bottom: 4%">
      <div class="col-md-5 col-sm">
        <img class="image-zowe-use" src="assets/img/zowe-mobile-image.png">
      </div>
      <div class="col-md-7 col-sm">
        <a id="zowe-mobile-intro"><h4>Zowe Mobile (Incubator)</h4></a>
          <p style="margin: 1rem auto">Lets you interact with your Zowe instance running on the mainframe from your mobile. </p>
          <p>
            <a href="{{ site.zowe_mobile_github_url }}">Code on GitHub</a>&nbsp;|&nbsp;
            <a href="{{ site.zowe_mobile_slack_url }}">Connect on Slack</a>&nbsp;|&nbsp;
            <a href="{{ site.zowe_mobile_doc_url }}">Learn more</a>
          </p>
      </div>
    </div>
    <hr class="w-75 mt-5 mb-5">
    <div class="row" style="margin-bottom: 4%">
      <div class="col-md-7 col-sm order-last order-sm-first">
        <a id="zebra-intro"><h4>ZEBRA (Incubator)</h4></a>
        <p style="margin: 1rem auto">Provides re-usable and industry compliant JSON formatted RMF/SMF data records, so that many other ISV SW and users can exploit them using open-source SW for many ways.</p>
          <p>
            <a href="{{ site.zebra_github_url }}">Code on GitHub</a>&nbsp;|&nbsp;
            <a href="{{ site.zebra_slack_url }}">Connect on Slack</a>&nbsp;|&nbsp;
            <a href="{{ site.zebra_doc_url }}">Learn more</a>
          </p>
      </div>
      <div class="col-md-5 col-sm order-first order-sm-last">
        <img class="image-zowe-use" src="assets/img/zebra-image.png">
      </div>
    </div>
  </div>
</div>

<div style="padding: 2% 3%; color: black !important;" class="bg-light"> 
<h2 class="text-center" style="color: black !important; margin-bottom: 5%">Zowe by the numbers</h2>
  <div class="row" style="margin-bottom: 2%">
    <div class="col-md text-center">
      <a style="color: initial; text-decoration: none" href="{{ site.zowe_metrics_url }}"><img style="width:15%" src="assets/img/logo-cli-download.svg" />
        <h3 style="margin-bottom: 0rem" id="cli-downloads"></h3>
        <h6>Zowe CLI Downloads</h6>
      </a>
    </div>
    <div class="col-md text-center">
      <a style="color: initial; text-decoration: none" href="{{ site.vscode_marketplace_url }}"><img style="width:15%" src="assets/img/logo-explorer-download.svg" />
        <h3 style="margin-bottom: 0rem" id="explorer-downloads"></h3>
        <h6>Zowe Explorer Downloads</h6>
      </a>
    </div>
    <div class="col-md text-center">
      <a style="color: initial; text-decoration: none" href="{{ site.zowe_metrics_url }}"><img style="width:15%" src="assets/img/logo-zowe-build-download.svg">
        <h3 style="margin-bottom: 0rem" id="server-downloads"></h3>
        <h6>Zowe z/OS Build Downloads</h6>
      </a>
    </div>
  </div>
  <div class="row">
    <div class="col-md text-center">
      <a style="color: initial; text-decoration: none" href="{{ site.slack_url }}"><img style="width:15%" src="assets/img/logo-slack-black.svg" />
        <h3 style="margin-bottom: 0rem" id="slack-members"></h3>
        <h6>Slack Community Members</h6>
      </a>
    </div>
    <div class="col-md text-center">
      <a style="color: initial; text-decoration: none" href="{{ site.github_repo_url }}"><img style="width:15%" src="assets/img/logo-github-back.svg" />
        <h3 style="margin-bottom: 0rem" id="github-contributors"></h3>
        <h6>Contributors</h6>
      </a>
    </div>
    <div class="col-md text-center">
      <a style="color: initial; text-decoration: none" href="{{ site.conformance_page_url }}"><img style="width:15%" src="assets/img/logo-vendor-product.svg" />
        <h3 style="margin-bottom: 0rem" id="conformant-product-value"></h3>
        <h6>Zowe Conformant Products</h6>
      </a>
    </div>
  </div>
  <div style="margin-bottom: 2%; margin-top: 4%">
    <a href="{{ site.zowe_metrics_url }}"><h5 class="text-right"><svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg> Check out more Zowe community metrics</h5></a>
  </div>
</div>

<div style="padding: 4% 7% 5% 7%">
  <div style="margin-bottom: 4%">
    <h2 class="text-center" style="color: black !important; margin-bottom: 5%">From Zowe blog</h2>
  </div>
  <div id="medium-widget" style="margin-top: 5%"></div>
    <script src="https://medium-widget.pixelpoint.io/widget.js"></script>
    <script>MediumWidget.Init({renderTo: '#medium-widget', params: {"resource":"https://medium.com/zowe","postsPerLine":2,"limit":4,"picture":"small","fields":["description","publishAt"],"ratio":"landscape"}})</script>
  <div style="margin-bottom: 4%">
    <a href="{{ site.zowe_medium_blog_url }}"><h5 class="text-right"><svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg> Check our other blogs</h5></a>
  </div>
    
</div>
<div>


  
  


