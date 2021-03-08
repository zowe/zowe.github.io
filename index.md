---
redirect_from:
  - "/home"
  - "/home/"
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<script>
  fetch(`https://wash.zowe.org:3000/api/cli`)
    .then((response) => response.json())
    .then((data) => {
      document.querySelector('#cli-downloads').innerHTML = data.downloads;
    });
  fetch(`https://wash.zowe.org:3000/api/explorer`)
    .then((response) => response.json())
    .then((data) => {
      document.querySelector('#explorer-downloads').innerHTML = data.downloads;
    });
  fetch(`https://wash.zowe.org:3000/api/server`)
    .then((response) => response.json())
    .then((data) => {
      document.querySelector('#server-downloads').innerHTML = data.downloads;
    });
  fetch(`https://wash.zowe.org:3000/api/omp`)
    .then((response) => response.json())
    .then((data) => {
      document.querySelector('#github-contributors').innerHTML = data.githubSubmittors;
    });
  fetch(`https://wash.zowe.org:3000/api/conformants`)
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
    <strong>Upcoming Events: </strong>Join the Quaterly Webinar to learn about the present and future of Zowe - find out more <a href="{{}}">here</a>
  </p>
  <p>
    <strong>New Features: </strong>
  </p> -->
  <strong>Zowe {{ site.data.releases[0].version }} is now available. You can download the installers and PTFs ({{ site.data.releases[0].smpe_numbers }}) for this release from the <a href="/download">Download</a> page. To learn what's new in this release, see the <a href="{{ site.docs_site_url }}/{{site.data.releases[0].documentation}}/getting-started/summaryofchanges.html">Release notes</a>.<br></strong>
  {% if site.data.announcements %}
    {% for announcement in site.data.announcements %}
    <strong>{{ announcement.announcement }}
      {% if announcement.link %}
        <a href="{{ announcement.link }}">Learn More</a>
      {% endif %}
      <br>
    </strong>
    {% endfor %}
  {% endif %}
</div>

<div style="text-align: center; padding: 3%; background-color: #74a9de; color: black !important">
  <h1 id="conformance">Welcome to Zowe</h1>
  <h4 style="">Combining the past and the present to build the future of mainframe</h4>
  <h5 style="margin-top: 5%;">A Linux Foundation project</h5>
</div>

<div class="row" style="padding: 5%">
  <div class="col-12 col-md-8">
    <p>Zowe offers modern interfaces that allow you to work with z/OS in a similar way to what you experience on modern cloud platforms. You can use these interfaces as delivered or through plug-ins and extensions that are created by clients or third-party vendors.
    </p>
    <br>
    <p>Zowe is an open source project created to further technologies that benefit the Z platform from all members of the Z community. Like Mac OS or Windows, Zowe comes with a set of APIs and OS capabilities that applications build on and also includes some applications out of the box.
    </p>
  </div>
  <div class="col-6 col-md-4">
    <object style="width:100%;height:330px;width:100%; float: none; clear: both; margin: 2px auto;" data="{{ site.  latest_video_embed }}">
    </object>
  </div>
</div>

<div style="padding: 2% 3%; background-color: #74a9de; color: black !important;">
  <div class="row" style="margin-bottom: 2%">
    <div class="col-md text-center">
      <img style="width:25%;" src="assets/img/github.svg" />
      <h6 style="margin-bottom: 0rem" id="cli-downloads"></h6>
      <h6>Zowe CLI Downloads</h6>
    </div>
    <div class="col-md text-center">
      <img style="width:25%" src="assets/img/github.svg" />
      <h6 style="margin-bottom: 0rem" id="explorer-downloads"></h6>
      <h6>Zowe Explorer Downloads</h6>
    </div>
    <div class="col-md text-center">
      <img style="width:25%" src="assets/img/github.svg" />
      <h6 style="margin-bottom: 0rem" id="server-downloads"></h6>
      <h6>Zowe Build Downloads</h6>
    </div>
  </div>
  <div class="row">
    <div class="col-md text-center">
      <img style="width:25%" src="assets/img/github.svg" />
      <h6 style="margin-bottom: 0rem">33000</h6>
      <h6>Slack Community Members</h6>
    </div>
    <div class="col-md text-center">
      <img style="width:25%" src="assets/img/github.svg" />
      <h6 style="margin-bottom: 0rem" id="github-contributors"></h6>
      <h6>Open Source Contributors</h6>
    </div>
    <div class="col-md text-center">
      <img style="width:25%" src="assets/img/github.svg" />
      <h6 style="margin-bottom: 0rem" id="conformant-product-value"></h6>
      <h6>Vendor Products</h6>
    </div>
  </div>
</div>

<div style="padding: 4% 7% 5% 7%">
  <div style="margin-bottom: 4%">
    <h2 style="color: black !important">How Mainframers Use Zowe</h2>
    <p>Zowe is made up of several products, each improving the learning ability, accessibility, and possibility of mainframe development.
    </p>
  </div>

  <div>
    <div class="row" style="margin-bottom: 4%">
      <div class="col-md-7 col-sm order-last order-sm-first">
        <h4>Zowe Application Framework</h4>
        <p style="margin: 1rem auto">A web user interface (UI) providing a virtual desktop containing a number of apps allowing access to z/OS function. Includes apps for traditional access such as a 3270 terminal and a VT Terminal, as well as an editor and explorers for working with JES, MVS Data Sets and Unix System Services.
        </p>
        <p>
          <a href="{{ site.ibm_ztrial_url }}">Case Study</a>&nbsp;|&nbsp;
          <a href="{{ site.ibm_ztrial_url }}">Documentation</a>&nbsp;|&nbsp;
          <a href="{{ site.ibm_ztrial_url }}">Code on Github</a>
        </p>
      </div>
      <div class="col-md-5 col-sm order-first order-sm-last">
        <img class="image-zowe-use" src="assets/img/ZLUXImage.png">
      </div>
    </div>
    <div class="row" style="margin-bottom: 4%">
      <div class="col-md-5 col-sm">
        <img class="image-zowe-use" src="assets/img/APIMLimage.png">
      </div>
      <div class="col-md-7 col-sm">
        <h4>API Mediation Layer</h4>
          <p style="margin: 1rem auto">A single point of access for mainframe service REST APIs, offering enterprise, cloud-like features such as high-availability, scalability, dynamic API discovery, consistent security, SSO, and documentation. Includes core services for working with MVS Data Sets, JES, and z/OSMF REST APIs.</p>
          <p>
            <a href="{{ site.ibm_ztrial_url }}">Case Study</a>&nbsp;|&nbsp;
            <a href="{{ site.ibm_ztrial_url }}">Documentation</a>&nbsp;|&nbsp;
            <a href="{{ site.ibm_ztrial_url }}">Code on Github</a>
          </p>
      </div>
    </div>
    <div class="row" style="margin-bottom: 4%">
      <div class="col-md-7 col-sm order-last order-sm-first">
        <h4>Zowe CLI</h4>
        <p style="margin: 1rem auto">A command line interface enabling remote mainframe interaction and use of common tools such as IDEs, shell commands, bash scripts, and build tools for mainframe development. It provides a set of utilities and services for application developers who want to become efficient in supporting and building z/OS applications quickly.</p>
          <p>
            <a href="{{ site.ibm_ztrial_url }}">Case Study</a>&nbsp;|&nbsp;
            <a href="{{ site.ibm_ztrial_url }}">Documentation</a>&nbsp;|&nbsp;
            <a href="{{ site.ibm_ztrial_url }}">Code on Github</a>
          </p>
      </div>
      <div class="col-md-5 col-sm order-first order-sm-last">
        <img class="image-zowe-use" src="assets/img/Zowe-CLI-Image.png">
      </div>
    </div>
    <div class="row" style="margin-bottom: 4%">
      <div class="col-md-5 col-sm">
        <img class="image-zowe-use" src="assets/img/Zowe-Explorer.png">
      </div>
      <div class="col-md-7 col-sm">
        <h4>Zowe Explorer</h4>
          <p style="margin: 1rem auto">A VS Code IDE extension enabling mainframe development using modern tooling by accessing USS files, datasets, and jobs that are stored on z/OS mainframes. The extension installs directly from VS Code, and complements the Zowe CLI experience.</p>
          <p>
            <a href="{{ site.ibm_ztrial_url }}">Case Study</a>&nbsp;|&nbsp;
            <a href="{{ site.ibm_ztrial_url }}">Documentation</a>&nbsp;|&nbsp;
            <a href="{{ site.ibm_ztrial_url }}">Code on Github</a>
          </p>
      </div>
    </div>
  </div>

  <div>
    <h2 class="text-center" style="color: black !important; margin-bottom: 5%">What Would You Like To Do With Zowe?</h2>
    <div class="row">
      <div class="col-sm text-center">
        <a href="/learn"><button type="button" class="btn btn-primary btn-lg btn-block">Learn</button></a>
        <p style="margin-top: 1rem">Learn how Zowe works and what it can do for you</p>
      </div>
      <div class="col-sm text-center">
        <a href="https://docs.zowe.org/"><button type="button" class="btn btn-primary btn-lg btn-block">Use</button></a>
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
  <div id="medium-widget" style="margin-top: 5%">
    </div>
      <script src="https://medium-widget.pixelpoint.io/widget.js"></script>
      <script>MediumWidget.Init({renderTo: '#medium-widget', params: {"resource":"https://medium.com/zowe","postsPerLine":2,"limit":4,"picture":"small","fields":["description","publishAt"],"ratio":"landscape"}})</script>

</div>
