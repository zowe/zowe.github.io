---
title: "Zowe Response to eMudhra Certificate Authority Compromise"
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<section class="whitebackground">
  <h1>Zowe Response to eMudhra Certificate Authority Compromise</h1>
  <p class="text-muted">Published: October 2026 | Zowe Security Workgroup</p>

  <div class="alert alert-warning" role="alert">
    <strong>Zowe Community Security Advisory:</strong> Multiple intermediate Certificate Authorities (CAs) operated by eMudhra were recently compromised due to weak cryptographic key generation. Zowe users and administrators are strongly advised to update their language runtimes (including Node.js and Java) and system trust stores across all Zowe components as soon as possible.
  </div>

  <h2>Recommended Actions</h2>

  <h3>1. Upgrade Node.js Runtimes</h3>
  <p>Node.js versions earlier than <strong>26.12.1</strong>, <strong>24.22.1</strong>, and <strong>22.23.4</strong> bundle vulnerable certificate trust stores. Users of Zowe CLI and server-side Node.js components should upgrade their Node.js runtimes to patched releases:</p>
  <ul>
    <li>Node.js v26: Upgrade to <strong>&gt;= 26.12.1</strong></li>
    <li>Node.js v24: Upgrade to <strong>&gt;= 24.22.1</strong></li>
    <li>Node.js v22: Upgrade to <strong>&gt;= 22.23.4</strong></li>
  </ul>
  <p>For users of Zowe Explorer, update your VS Code environment to <strong>1.143.1</strong> or later.</p>

  <h3>2. Update Java / JVM Environments</h3>
  <p>Ensure that Java runtime environments (JRE/JDK) powering the Zowe API Mediation Layer and other Java services on z/OS have received the latest security updates from IBM's Java distribution.</p>

  <h3>3. Inspect Custom Truststores and Certificates</h3>
  <p>If you have any eMudhra certificate authorities in your z/OS keyrings, remove them and restart Zowe.</p>
</section>
