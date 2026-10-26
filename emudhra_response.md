---
title: "Zowe Response to Recent Industry Vulnerabilities (eMudhra CA Compromise & Brotli node2shell)"
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<section class="whitebackground">
  <h1>Zowe Response to Recent Industry Vulnerabilities</h1>
  <p class="text-muted">Published: October 2026 | Zowe Security Workgroup</p>

  <div class="alert alert-warning" role="alert">
    <strong>Zowe Community Security Advisory:</strong> The Zowe project is actively responding to two recent industry-wide security issues impacting common runtimes: the <strong>eMudhra intermediate Certificate Authority (CA) compromise</strong> and the <strong>Brotli "node2shell" vulnerability (CVE-2026-111497)</strong>. Upgrading your Node.js runtimes to the latest maintenance releases resolves both vulnerabilities simultaneously across affected components.
  </div>

  <h2>Overview of Vulnerabilities</h2>
  <ul>
    <li><strong>eMudhra Certificate Authority Compromise:</strong> Multiple intermediate CAs operated by eMudhra were compromised due to weak cryptographic key generation. Runtimes and system trust stores must be updated to ensure these intermediate CAs are distrusted or removed.</li>
    <li><strong>Brotli "node2shell" Vulnerability (CVE-2026-111497):</strong> An out-of-bounds write flaw in the native Brotli decoder bundled with Node.js can lead to memory disclosure, crashes, or potential remote code execution when decompressing malformed Brotli data.</li>
  </ul>

  <h2>Recommended Actions</h2>

  <h3>1. Upgrade Node.js Runtimes</h3>
  <p>Upgrading Node.js addresses <strong>both</strong> the eMudhra root store distrust and the Brotli (node2shell) vulnerability. Node.js versions earlier than <strong>26.12.1</strong>, <strong>24.22.1</strong>, and <strong>22.23.4</strong> are vulnerable. Users of Zowe CLI and server-side Node.js components should upgrade their Node.js runtimes to the patched versions immediately:</p>
  <ul>
    <li>Node.js v26: Upgrade to <strong>&gt;= 26.12.1</strong></li>
    <li>Node.js v24: Upgrade to <strong>&gt;= 24.22.1</strong></li>
    <li>Node.js v22: Upgrade to <strong>&gt;= 22.23.4</strong></li>
  </ul>
  <p>For users of Zowe Explorer, update your VS Code environment to <strong>1.143.1</strong> or later.</p>

  <h3>2. Update Java / JVM Environments</h3>
  <p>Ensure that Java runtime environments (JRE/JDK) powering the Zowe API Mediation Layer and other Java services on z/OS have received the latest security updates from IBM's Java distribution to ensure root certificates and trust stores remain secure.</p>

  <h3>3. Inspect Custom Truststores and Keyrings</h3>
  <p>If you have any eMudhra certificate authorities in your z/OS keyrings or custom enterprise truststores, remove them and <strong>restart Zowe</strong>.</p>
</section>
