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

## Prioritized backlog
- P0: Keep editorial content reviewed and expanded to the target 1,200–1,800 words per article before AdSense submission.
- P1: Add server-rendered or generated JSON-LD Article/Breadcrumb/HowTo metadata for every article route.
- P1: Connect the newsletter form to a consent-aware email provider when a provider is chosen.
- P2: Add search, author profile details, comments, and a richer admin editorial workflow.

## P0/P1/P2 remaining and next tasks
- P0: Editorial quality pass and final legal review before applying for AdSense.
- P1: Add structured data and canonical/Open Graph tags to document head.
- P1: Add analytics only after explicit cookie preference handling is connected.
- P2: Expand the journal with seasonal patterns and downloadable print-friendly tutorials.
