---
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<section class="whitebackground" style="float: none;">
  <h1 id="download" style="margin-bottom: 2rem">Extending Zowe</h1>
  <h2 id="table-of-contents" style="margin-bottom: 1.5rem">Table of Contents</h2>
  <div class="d-flex flex-column">
      <a href="#how-do-you-extend" class="card-link" style="margin-left: 1.25rem">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
      How do you extend Zowe?
      </a>
      <a href="#why-build-with-zowe" class="card-link">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
      Why build with Zowe? 
      </a>
      <a href="#conformance-program-v2" class="card-link">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
      Zowe Conformance Program V2
      </a>
      <a href="#conformance-program-v1" class="card-link">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
      Zowe Conformance Program V1
      </a>
  </div>

  <div style="padding-top: 3%">
    <h2 id="how-do-you-extend" style="margin-bottom: 2rem">How do you extend Zowe?</h2>
    <p>Zowe is designed to be an extensible tools platform. You can extend it to meet your needs or distribute the plug-ins to users who have already installed Zowe and want to introduce new functionality to it.</p>
    <p>You can extend Zowe in the following ways:</p>
    <div style="margin-left: 1%">
      <p style="margin-bottom: 0rem">1. Extend the Zowe Command Line Interface.</p>
      <p style="margin-bottom: 0rem">2. Add a REST API service to the API Mediation Layer.</p>
      <p style="margin-bottom: 0rem">3. Add an application plug-in to the Zowe Desktop.</p>
      <p>4. Extend the Zowe Explorer.</p>
    </div>
    <p>Learn more and get started with the <a href="{{ site.zowe_extend_doc_url }}">Extending documentation</a>.</p>
  </div>

  <div style="padding-top: 3%">
    <h2 id="why-build-with-zowe" style="margin-bottom: 1.5rem">Why build with Zowe?</h2>
      <p>Building your product or extension on top of Zowe has many advantages! Here are a few:</p>
      <div>
        <p><strong>Advanced Security</strong> - Zowe has multifactor authentication built in, ensuring your product keeps with modern security standards.</p>
        <p><strong>Modern DevOps practices</strong> - Automate your CI/CD pipeline with modern tools like Jenkins.</p>
        <p><strong>Aligned with new developers</strong> - The next generation of mainframe developers is using Zowe, and will be the ones who implement and use your extension.</p>
      </div>
  </div>

  <section style="padding-top: 3%;">
    <h2 id="conformance-program-v2" style="margin-bottom: 1.5rem;">Zowe Conformance Program V2</h2>
        <p>Administered by the Open Mainframe Project, the Zowe Conformance Program gives users the confidence that when they use a product, app, or distribution that extends Zowe, they can expect a high level of common functionality, interoperability, and user experience.</p>
        <p>As a vendor, getting a Zowe Conformance Badge for your application also ensures that your extension will continue to be supported as Zowe changes and grows.</p>
        <p>Getting a Zowe Conformance Badge happens in 3 steps:</p>
        <div style="color: black !important;"> 
          <div class="row">
            <div class="col-md text-center">
              <a class="col-md-3" href="{{ site.conformance_v2_step1_url }}"><button type="button" class="btn btn-primary btn-lg btn-block" style="white-space: break-spaces">1) Review program terms and conditions</button></a>
            </div>
            <div class="col-md text-center">
              <a class="col-md-3" href="{{ site.conformance_v2_step2_url }}"><button type="button" class="btn btn-primary btn-lg btn-block" style="white-space: break-spaces">2) Complete test evaluation guide</button></a>
            </div>
            <div class="col-md text-center">
              <a class="col-md-3" href="{{ site.conformance_v2_step3_url }}"><button type="button" class="btn btn-primary btn-lg btn-block" style="white-space: break-spaces">3) Submit the participation form</button></a>
            </div>
         </div>
       </div>
    <p style="margin-top: 1rem;">Learn more about the program at the <a href="{{ site.conformance_page_v2_url }}">&nbsp;Zowe Conformance Program website</a>.</p>
    <div>
      <div>
      <h3 style="text-align: left;">The following products have earned Zowe Conformant status</h3>
      <iframe frameBorder="0" id="landscape" scrolling="no" style="width: 1px; min-width: 100%" src="https://landscape.openmainframeproject.org/pages/zowe-conformant"></iframe><script src="https://landscape.openmainframeproject.org/iframeResizer.js"></script>
      </div>
    </div>
  </section>

  <section style="padding-top: 3%;">
    <h2 id="conformance-program-v1" style="margin-bottom: 1.5rem;">Zowe Conformance Program V1</h2>
        <p>Administered by the Open Mainframe Project, the Zowe Conformance Program gives users the confidence that when they use a product, app, or distribution that extends Zowe, they can expect a high level of common functionality, interoperability, and user experience.</p>
        <p>As a vendor, getting a Zowe Conformance Badge for your application also ensures that your extension will continue to be supported as Zowe changes and grows.</p>
        <p>Getting a Zowe Conformance Badge happens in 3 steps:</p>
        <div style="color: black !important;"> 
          <div class="row">
            <div class="col-md text-center">
              <a class="col-md-3" href="{{ site.conformance_step1_url }}"><button type="button" class="btn btn-primary btn-lg btn-block" style="white-space: break-spaces">1) Review program terms and conditions</button></a>
            </div>
            <div class="col-md text-center">
              <a class="col-md-3" href="{{ site.conformance_step2_url }}"><button type="button" class="btn btn-primary btn-lg btn-block" style="white-space: break-spaces">2) Complete test evaluation guide</button></a>
            </div>
            <div class="col-md text-center">
              <a class="col-md-3" href="{{ site.conformance_step3_url }}"><button type="button" class="btn btn-primary btn-lg btn-block" style="white-space: break-spaces">3) Submit the participation form</button></a>
            </div>
         </div>
       </div>
    <p style="margin-top: 1rem;">Learn more about the program at the <a href="{{ site.conformance_page_url }}">&nbsp;Zowe Conformance Program website</a>.</p>
    <div>
      <div>
      <h3 style="text-align: left;">The following products have earned Zowe Conformant status</h3>
      <iframe frameBorder="0" id="landscape" scrolling="no" style="width: 1px; min-width: 100%; min-height: 600px" src="https://landscape.openmainframeproject.org/pages/zowe-conformant"></iframe><script src="https://landscape.openmainframeproject.org/iframeResizer.js"></script>
      </div>
    </div>
  </section>
</section>
