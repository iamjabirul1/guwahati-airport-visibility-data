# Privacy policy — Northeast India Trip Planner (Chrome extension)

Last updated: 2026-10-27

This extension is published by Hotel Shiny Grand, Shyam Nagar, VIP, near LGBI Airport,
Borjhar, Guwahati, Assam 781015, India. Contact: WhatsApp or phone +91 91815 56418,
website https://hotelshinygrand.online.

## What the extension does

It shows short, dated travel notes for the page you are reading. When you click
"Open travel notes", it reads the **URL and title of the active tab only**, matches them
locally against a bundled list of travel topics, and displays notes in Chrome's side panel.

## Data we collect

**None.** The extension does not collect, transmit, sell or share any personal or browsing
data. Specifically:

- Page content, browsing history, form fields and keystrokes are never read or sent.
- The page URL and title are processed **on your device** to choose which note to show, and
  are not transmitted anywhere.
- There is no account, no sign-in, no analytics and no advertising identifier.
- The extension ships with all of its notes inside the package and works offline.

## On-device storage

Chrome's local storage keeps two things on your device only: the optional API endpoint value
(empty by default) and the last page classification for the current session. Clearing the
extension's data or uninstalling it removes both.

## Optional live endpoint

The advanced settings field lets you point the extension at a read-only travel API that you
run yourself. If you leave it empty — the default — the extension makes no network requests
at all. If you set one, the extension sends only the topic keyword (for example "permit") to
that endpoint, never the page URL or title.

## Permissions and why they exist

| Permission | Why |
|---|---|
| `activeTab` | Reads the URL and title of the tab you explicitly act on. |
| `scripting` | One-time read of that tab's URL and title after your click. Nothing is injected or modified. |
| `sidePanel` | Shows the notes beside your page. |
| `storage` | Keeps the optional endpoint value and the session's page classification on your device. |

## Changes

If this policy changes, the updated text appears here with a new date, and a note is added to
the extension's listing.

## Your control

Uninstall the extension at any time from `chrome://extensions`. Because nothing is collected,
there is no data to request or delete.
