---
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<section class="whitebackground">
  <h1 id="download" style="margin-bottom: 1.5rem">Version 2 Information</h1>
  <p>Everything you need in order to be ready for the next major version release</p>

  <div>
    <h2 style="margin-bottom: 1.5rem; margin-top: 2%">Latest Announcements</h2>
    <p>The preview of the docs-site is available at: <a href="https://docs.zowe.org/v2.0.x/getting-started/overview">Docs-site</a></p>
    <p>Download the latest release at: final</p>
    <p>Final enhancements are available: <a href="https://ibm.box.com/s/8qhpmnuym8d5alhijlb1lsse6h520m62">Box note</a></p>
  </div>

  <div>
    <h2 style="margin-bottom: 1.5rem; margin-top: 2%">Compatibility statements</h2>
    <p></p>
  </div>

  <h2>For Users</h2>

  <div class="card-deck">
  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.slack_url }}">API Mediation Layer</a></h5>
      </div>
      <p class="card-text"></p>
    </div>
  </div>
  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.omp_calendar_url }}">CLI</a></h5>
      </div>
      <p class="card-text">CLI Breaking changes</p>
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
      <p class="card-text"></p>
    </div>
  </div>
  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.slack_url }}">Web UI</a></h5>
      </div>
      <p class="card-text"></p>
    </div>
  </div>
  </div>

<h2>For Extenders</h2>

  <div class="card-deck">
  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.slack_url }}">API Mediation Layer</a></h5>
      </div>
      <p class="card-text"></p>
    </div>
  </div>
  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.omp_calendar_url }}">CLI</a></h5>
      </div>
      <p class="card-text">CLI Breaking changes</p>
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
      <p class="card-text"></p>
    </div>
  </div>
  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.slack_url }}">Web UI</a></h5>
      </div>
      <p class="card-text"></p>
    </div>
  </div>
  </div>

<h2>Breaking Changes</h2>

  <div class="card-deck">
  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.slack_url }}">API Mediation Layer</a></h5>
      </div>
      <p class="card-text">https://github.com/zowe/api-layer/issues/1510</p>
    </div>
  </div>
  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.omp_calendar_url }}">CLI</a></h5>
      </div>
      <p class="card-text">CLI Breaking changes</p>
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
      <p class="card-text"></p>
    </div>
  </div>
  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.slack_url }}">Web UI</a></h5>
      </div>
      <p class="card-text"></p>
    </div>
  </div>
  </div>

  <h2>Conformance Criteria</h2>

  <div class="card-deck">
  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.slack_url }}">API Mediation Layer</a></h5>
      </div>
      <p class="card-text">Change to Item number 8: For versioned and non-versioned APIs, service URLs must contain a service version before the service ID (all formats)
The new Item 8 will now read: For versioned and non-versioned APIs, service URLs must contain a service ID in the first place in the path, before the service version (all formats) </p>
        <p>Clarification to Item number 6: The API ID must follow the same rules for Java packages. Example of the API ID: zowe.apiml.apicatalog. The new Item 6 will now read: Services must provide API ID to allow for Automated CLI Client Configuration.</p>
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
      <p class="card-text"></p>
    </div>
  </div>
  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.slack_url }}">Web UI</a></h5>
      </div>
      <p class="card-text"></p>
    </div>
  </div>
  </div>

</section>