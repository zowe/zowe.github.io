---
title: "Download"
extraHeaders: google-analytics-downloads-header.html
extraJs: [common.html, post-download-script.html]
---
<section class="whitebackground" id="main-content">
    <h1 class="title" id="page_title">Thank you for downloading the Zowe binary</h1>
    <p>
        If you had an issue or your download did not start, please <strong><a id="download_link" href="/download">click
                here</a></strong> to try again or copy the following URL to your browser: 
        <span id="download_url_display"></span>
    </p>
    <script>
        // Retrieve the download URL from localStorage
        const lastDownloadURL = localStorage.getItem('zowe-last-download-url') || 'No download started yet.';
        const urlDisplay = document.getElementById('download_url_display');
        if (urlDisplay) {
            urlDisplay.textContent = lastDownloadURL; // Display the URL
        }
    </script>
    <details>
        <summary id='verify_drop'><b>How to verify binaries with digital signatures</b></summary>
        <br />
        <p>All Zowe binaries are signed using <a href="https://www.sigstore.dev/">Sigstore</a>, an <a href="https://openssf.org/">OpenSSF</a> project.</p>
        <h2 id="prereqs">Pre-Requisites</h2>
        <ul>
            <li>Make sure the Cosign CLI is installed. Follow <a href="https://docs.sigstore.dev/system_config/installation/">these installation instructions.</a> </li>
        </ul>
        <h3>Download the Verification Bundle</h3>
        <p id="download_bundle_step"></p>
        <h2><b>Online Verification</b></h2>

        <p>This verification method is the preferred option for digital signature validation, and requires an internet connection with access to the public sigstore infrastructure to work (*.sigstore.dev).
            Ensure that the the artifact you downloaded and its respective signing bundle you acquired <a href="#download_bundle_step">from the pre-requisite step</a> are in the same directory.
            Navigate to that directory with your terminal, and issue the following command:</p>

        <code id='cosign_verify_online'>cosign verify-blob ./artifact-you-downloaded --bundle ./bundle-you-downloaded 
                    --certificate-identity=https://github.com/zowe/zowe-install-packaging/.github/workflows/build-packaging.yml@refs/heads/v3.x/master 
                    --certificate-oidc-issuer=https://token.actions.githubusercontent.com
        </code><br /><br />

        If the verification succeeded, you will see:<br />

        <code>Verified OK</code><br /><br />

        If the veritication failed, you will see:<br />

        <code>Error: error verifying bundle: matching bundle to payload: ....more output</code>
        <br /><br />

        <h2><b>Offline Verification</b></h2>
       
        <p>This verification method is <b>>>not<<</b> the preferred option for digital signature validation, as the signature is not compared against the public transparency log. This method is useful mostly for artifact hash validation.
            Ensure that the the artifact you downloaded and its respective signing bundle you acquired <a href="#download_bundle_step">from the pre-requisite step</a> are in the same directory.
            Navigate to that directory with your terminal, and issue the following command:</p>

        <code id='cosign_verify_offline'>cosign verify-blob ./artifact-you-downloaded --bundle ./bundle-you-downloaded --offline=true 
                    --certificate-identity=https://github.com/zowe/zowe-install-packaging/.github/workflows/build-packaging.yml@refs/heads/v3.x/master 
                    --certificate-oidc-issuer=https://token.actions.githubusercontent.com
        </code><br /><br />

        If the verification succeeded, you will see:<br />

        <code>Verified OK</code><br /><br />

        If the veritication failed, you will see:<br />

        <code>Error: error verifying bundle: matching bundle to payload: ....more output</code>
    </details>
    <br />
    <details id="sbom_download_section" style="display: none;">
        <summary id='sbom_drop'><b>How to download Zowe SBOMs (Software Bill of Materials)</b></summary>
        <br />
        <p id="sbom_intro_text"></p>
        <h5>Downloading the SBOM</h5>
    
        <p>Choose one of the following SBOM options:</p>
        <ul id="sbom_download_options"></ul>
        <br />
        <h5>(Optional) Verifying SBOM Integrity</h5>

        <p>All Zowe SBOMs are signed using <a href="https://www.sigstore.dev/">Sigstore</a>, an <a href="https://openssf.org/">OpenSSF</a> project.</p>
        <p>Choose the cosign bundle which matches the download option you chose <a href="#sbom_download_options">above</a></p>
        <ul id="sbom_bundle_download_options"></ul>

        <p id="sbom_verification_instructions">See the <a href="#prereqs">How to verify binaries with digital signatures</a> to acquire the pre-requisite software,
             and for a description of online vs offline verficiation. Once you've reviewed that information, you can use the one of the below commands to digitally verify the SBOM. Each command assumes your SBOM and its respective signing bundle are in the same directory, and you have navigate your terminal there.</p>

        <b>Online Verification</b><br />
        <code id="sbom_online_verification"></code>
        <br /><br />
        <b>Offline Verification</b><br />
        <code id="sbom_offline_verification"></code>
    </details>

</section>

<section class="bluebackground" id="end-of-support-reminder" style="display: none;">
    <h2>Support for version 1 is ending</h2>
    <p>Zowe is approaching the end of support for major version 1, which you are currently downloading. The support will
        end on September 30, 2024. After this date, the community will not release any new versions or address any
        issues, including security fixes, related to version 1. To facilitate a smooth transition, we have prepared a
        comprehensive guide available here: <a
            href="https://docs.zowe.org/stable/extend/migrate-extensions">https://docs.zowe.org/stable/extend/migrate-extensions</a>.
        If you have any questions, please feel free to reach out to us via <a
            href="https://openmainframeproject.slack.com/archives/CC08782AG">OMP Slack #zowe-help channel</a> or <a
            href="https://github.com/zowe">Zowe GitHub</a></p>
</section>

<section class="whitebackground">
    <h2>Read the Zowe Documentation at <a href="https://docs.zowe.org">docs.zowe.org</a></h2>
    <p>After you download the Zowe package, you're ready to get started. Read the Zowe documentation to review the
        system requirements and follow the instructions to install Zowe.</p>
    <h2>Provide feedback and contribute to Zowe on <a href="https://github.com/zowe/community">GitHub</a></h2>
    <p>View the source code, provide feedback, and contribute to the project through Zowe GitHub.</p>
</section>