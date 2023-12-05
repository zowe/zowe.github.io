---
title: "Download"
extraHeaders: google-analytics-downloads-header.html
extraJs: post-download-script.html
---
<section class="whitebackground">
    <h1 class="title" id="page_title">Thank you for downloading the Zowe binary</h1>
    <p>
        If you had an issue or your download did not start, please <strong><a id="download_link" href="legal.html">click
                here</a></strong> to try again.
    </p>
    <details>
        <summary id='verify_drop'><b>Verify Hash and Signature of Zowe Binary</b></summary>
        <p>These commands are tested on both <strong>Mac OS X v10.13.6</strong> and <strong>Ubuntu v17.11.</strong></p>
        <br>
        <h2><b>Step 1</b> - Verify Hash Code</h2>
        <p>You can download hash code file <b><a id="hash_download"
                    href="https://zowe.jfrog.io/zowe/list/libs-release-local/org/zowe/1.0.0/zowe-1.0.0.pax.sha512"
                    download
                    onclick="gs && ga('send', 'event', 'download', 'Zowe Binary Hash', 'zowe-1.0.0.pax.sha512');">zowe-1.0.0.pax.sha512</a></b>,
            then use this command to check:</p>
        <code id="hash_code">(gpg --print-md SHA512 zowe-1.0.0.pax &gt; zowe-1.0.0.pax.sha512.my) && diff
        zowe-1.0.0.pax.sha512.my zowe-1.0.0.pax.sha512 && echo matched || echo "not match"</code>
        <p>If you see "<b>matched</b>" means the binary you have downloaded is the same one that was officially
            distributed by the Zowe project. You can delete temporary "<b id="hash_my">zowe-1.0.0.pax.sha512.my</b>"
            after that.</p><br>
        <p>You can also use other commands, like "<code>sha512</code>", "<code>sha512sum</code>", or "<code>openssl
          dgst -sha512</code>" to generate <b>SHA512</b> hash code. Just those hash code results are in a
            different format from what we provided but the values should be the same.</p>

        <h2><b>Step 2</b> - Verify With Signature File</h2>
        <p>In addition to the SHA512 hash we ensure that the hash is verifiable as well. This is done by digitally
            signing the hash text file with a KEY from one of the Zowe developers.</p><br>
        <p>You can download the signature file <b><a id="signature_download"
                    href="https://zowe.jfrog.io/zowe/list/libs-release-local/org/zowe/1.0.0/zowe-1.0.0.pax.asc">zowe-1.0.0.pax.asc</a></b>,
            and public key <strong><a id="keyfile"
                    href="https://raw.githubusercontent.com/zowe/zowe-install-packaging/master/signing_keys/KEYS.jack"
                    download target="_blank">KEYS</a></strong>.</p>
        <p>There are few steps:</p>
        <ol class="verify-list">
            <li>Import the public key with command: <code id="keyfile_import_command">gpg --import KEYS</code></li>
            <li>If you never use gpg before, you may need to generate keys first: <code>gpg --gen-key</code>.
                Otherwise, please proceed to next step.</li>
            <li>Sign the downloaded public key with command: <code id="gpg-sign-key">gpg --sign-key KEY</code></li>
            <li>Verify the file with command: <code
                    id="gpg_command">gpg --verify zowe-1.0.0.pax.asc zowe-1.0.0.pax</code></li>
            <li>You can remove the imported key with command: <code id="gpg-delete-key">gpg --delete-key KEY</code></li>
        </ol>
        <p>If you see output like this that matches the info in the public key you downloaded you can be assured
            that the binary file you have has come from the Zowe project.</p>
        <code>
        gpg: &nbsp; &nbsp; &nbsp; &nbsp; using RSA key <span id="key_id">KEY</span><br>
        gpg: Good signature from "<span id="key_signer">SIGNER (CODE SIGNING KEY)</span> " [full]
      </code>
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