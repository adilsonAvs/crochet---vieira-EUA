# Cozy Loop Crochet — Product Requirements Document

## Original problem statement
Build a professional, US-focused crochet content hub in natural American English, designed for organic SEO, accessibility, responsive performance, and Google AdSense policy readiness. Required pages include Home, Blog, ten detailed articles, About, Contact, Privacy, Cookie Consent, Terms, 404, sitemap, robots, and internal linking.

## Architecture decisions
- React 19 with React Router for the editorial experience.
- FastAPI with MongoDB via the existing protected MONGO_URL and DB_NAME values.
- Contact messages are persisted in MongoDB; no external email service is used.
- Article content is represented as structured editorial data for predictable internal links, metadata, and route generation.
- Frontend calls only REACT_APP_BACKEND_URL.
- Warm organic editorial visual system using Playfair Display and Jakarta Sans.

## User personas
- US beginners looking for friendly, jargon-free crochet help.
- Intermediate makers choosing yarn, fixing mistakes, and starting larger patterns.
- Hobbyists exploring amigurumi, blankets, and a possible handmade side hustle.

## Core requirements (static)
- English US copy, original editorial structure, clear navigation, mobile-first layout.
- Ten article routes with categories, reading time, images, table of contents, related article link, and ad-safe placeholder.
- Contact form with name, email, subject, message, success/error feedback, and visible support email.
- Privacy and Terms pages cover cookies, analytics, advertising, CCPA-oriented rights, and responsible use.
- Cookie banner supports accept/reject and persists the reader choice.
- robots.txt and sitemap.xml include site pages and all ten articles.

## What's been implemented — 2026-08-11
- Built the Cozy Loop Crochet home/editorial hub with responsive hero, featured stories, newsletter signup feedback, and footer navigation.
- Added Blog category filters, pagination, ten article slugs, article detail views, internal linking, imagery, TOC, metadata, and ad placeholder.
- Added About, Contact, Privacy, Terms, custom 404, cookie consent, sitemap, and robots pages/assets.
- Added FastAPI contact persistence and validation through MongoDB.
- Verified production build, API root, contact POST, desktop/mobile navigation, article routes, cookie persistence, and no mobile overflow.

## What's been implemented — 2026-02-13 (AdSense rejection remediation)
Google AdSense rejected the site for "conteúdo superficial" / thin duplicate content. Root cause: the first 10 articles were sharing identical 150-word bodies from `CATEGORY_PARAGRAPHS`, and only 5 stock images were reused across 20 posts.

Fixes applied in this session:
- Rewrote all 10 short articles with fully unique long-form bodies (~800-1400 words each, 8-12 H2 sections each) covering `crochet-for-absolute-beginners`, `common-crochet-mistakes`, `even-crochet-stitches`, `read-crochet-pattern`, `best-yarn-for-crochet`, `amigurumi-101`, `crochet-hacks`, `fix-dropped-stitch`, `crochet-blanket-patterns`, `sell-crochet-online`.
- Total site-wide content: 23,076 words across 20 articles (avg 1,153 words/article; was ~1,355 words total, 17x increase).
- Assigned a unique verified crochet-related Pexels image to every one of the 20 articles (0 duplicates).
- Removed the fake "Advertisement" placeholder DOM node when `REACT_APP_ADSENSE_CLIENT` is empty, so AdSense reviewers see clean article layout.
- Refactored `articles_data.py`: replaced the `_short()` helper (which relied on the duplicated `CATEGORY_PARAGRAPHS` dict) with `_full()` accepting a per-article body.

## Prioritized backlog
- P0: DONE — editorial content is now 800-1400 words per article, all unique.
- P1: Add server-rendered or generated JSON-LD Article/Breadcrumb/HowTo metadata for every article route.
- P1: Connect the newsletter form to a consent-aware email provider when a provider is chosen.
- P2: Add search, author profile details, comments, and a richer admin editorial workflow.

## P0/P1/P2 remaining and next tasks
- P1: Resubmit the site to Google AdSense now that the thin-content issue is remediated.
- P1: Add FAQ schema markup on at least 5 highest-traffic articles for rich snippets.
- P1: Connect newsletter form to a real ESP (Resend or SendGrid) once user picks a provider.
- P1: Verify Pinterest Rich Pins scaffolding after AdSense approval.
- P2: Add site-wide search, expand author profile with credentials, downloadable print-friendly tutorial PDFs.
