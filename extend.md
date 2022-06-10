---
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<section class="whitebackground" style="float: none;">
  <h1 id="download" style="margin-bottom: 2rem">Extending Zowe</h1>

  <p>
  Zowe is designed to be an extensible tools platform. You can extend it to meet your needs or distribute the plug-ins to users who have already installed Zowe and want to introduce new functionality to it.</p>

  <p>You can extend Zowe in the following ways:</p>
  <div style="margin-left: 1%">
  <p style="margin-bottom: 0rem">1. Extend the Zowe Command Line Interface.</p>
  <p style="margin-bottom: 0rem">2. Add a REST API service to the API Mediation Layer.</p>
  <p style="margin-bottom: 0rem">3. Add an application plug-in to the Zowe Desktop.</p>
  <p>4. Extend the Zowe Explorer.</p>
  </div>
  <p>Learn more and get started with the <a href="{{ site.zowe_extend_doc_url }}">Extending documentation</a>.</p>

  <div style="padding-top: 3%">
    <h2 style="margin-bottom: 1.5rem">Why build with Zowe?</h2>
      <p>Building your product or extension on top of Zowe has many advantages! Here are a few:</p>
      <div>
        <p><strong>Advanced Security</strong> - Zowe has multifactor authentication built in, ensuring your product keeps with modern security standards.</p>
        <p><strong>Modern DevOps practices</strong> - Automate your CI/CD pipeline with modern tools like Jenkins.</p>
        <p><strong>Aligned with new developers</strong> - The next generation of mainframe developers is using Zowe, and will be the ones who implement and use your extension.</p>
      </div>
  </div>

  <section style="padding-top: 3%;">
    <h2 style="margin-bottom: 1.5rem;">Zowe Conformance Program</h2>
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
    <p style="margin-top: 1rem;">The current version of Zowe Conformance is ZOWE V2, which covers Zowe version 2 and later. The previous <a href="https://www.openmainframeproject.org/all-projects/zowe/conformance/v1">Zowe Conformance ZOWE V1 Program</a> covers Zowe v1 version 1.9 and later, and the <a href="https://www.openmainframeproject.org/all-projects/zowe/conformance/2019-2">Zowe Conformance 2019</a> program covers Zowe version 1.0 through 1.8.</p>
    <p style="margin-top: 1rem;">Learn more about the program at the <a href="{{ site.conformance_page_url }}">&nbsp;Zowe Conformance Program website</a>.</p>

  <script>
    function toggleLandscape(idToShow, idToHide) {
      document.getElementById(idToShow+'-full').classList.add('active');
      document.getElementById(idToHide+'-full').classList.remove('active');

      document.getElementById(idToShow+'-tab').classList.add('active');
      document.getElementById(idToHide+'-tab').classList.remove('active');
    }  
  </script>

  <style>
    .landscape-tab {
      padding-left: 20px;
      padding-right: 20px;
      font-size: 24px;
    }

    .landscape-tab.active {
      background-color: gray;
      color: white;
    }

    .landscape-tab:hover {
      background-color: #ccc;
    }

    .landscape-tab.active:hover {
      background-color: #ccc;
      color: black;
    }

    .landscape-content {
       padding: 5px;
       display: none;
    }

    .landscape-content h3 {
      text-align: left; 
      padding-left: 10px;
    }

    .landscape-content iframe {
      width: 1px; 
      min-width: 100%; 
      height: 900px;
    }

    .landscape-content.active {
      display: block;
    }

    .landscape-heading {
      border-bottom: 2px black solid; 
      background-color: #eee;
    }

    .landscape-overall {
      border: 2px black solid;
    }
  </style>

  <div class="landscape-overall">
    <div class="landscape-heading" >
      <span class="landscape-tab active" id="landscape-v2-tab" onclick="toggleLandscape('landscape-v2', 'landscape-v1')">V2 Landscape</span>
      <span class="landscape-tab" id="landscape-v1-tab" onclick="toggleLandscape('landscape-v1', 'landscape-v2')">V1 Landscape</span>
    </div>
    <div class="landscape-content active" id="landscape-v2-full">
      <div>
      <h3>The following products have earned Zowe Conformant status for Zowe V2</h3>
      <iframe frameBorder="0" id="landscape-v2" src="https://landscape.openmainframeproject.org/pages/zowe-conformant"></iframe>
      </div>
    </div>
    <div class="landscape-content" id="landscape-v1-full">
      <div>
        <h3>The following products have earned Zowe Conformant status for Zowe V1</h3>
        <iframe frameBorder="0" id="landscape-v1" src="https://landscape.openmainframeproject.org/pages/zowe-conformant-v1"></iframe>
      </div>
    </div>
  </div>

</section>
</section>
