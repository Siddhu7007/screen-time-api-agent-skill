# 20 Source Index and Confidence Matrix

## Purpose
Provide a single index of all evidence sources and confidence tiers used in this corpus.

## Canonical API Surface
- N/A (meta-index file).

## Implementation Pattern
Confidence tiers:
- `high`: canonical Apple docs, WWDC, SDK interfaces/headers.
- `medium`: Apple forum clarifications and corroborated field posts.
- `low`: uncorroborated or incomplete evidence.

Source matrix:

| URL | source_type | confidence | rationale |
|---|---|---|---|
| https://developer.apple.com/documentation/screentimeapidocumentation | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/ManagedSettings/ConnectionWithFrameworks | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/FamilyControls | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/Xcode/configuring-family-controls | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/ManagedSettings | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/ManagedSettingsUI | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/DeviceActivity | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/shieldaction | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/shieldactionresponse | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/application | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/applicationtoken | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/activitycategory | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/activitycategorytoken | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/webdomain | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/webdomaintoken | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/familycontrols/authorizationcenter | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/familycontrols/authorizationstatus | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.family-controls | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/familycontrols/requesting-the-family-controls-entitlement | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/familycontrols/familycontrolsmember | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/familycontrols/familyactivitypicker | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/familycontrols/familyactivityselection | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/familycontrols/displayingactivitylabels | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/familycontrols/activitylabel | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/familycontrols/familycontrolserror | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/screentime | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityreport | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityevent | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityschedule | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/startmonitoring(_:during:events:) | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivitymonitor | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/monitoringerror | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/monitoringerror/intervaltooshort | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityevent/init(applications:categories:webdomains:threshold:) | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityevent/name | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityevent/name/init(rawvalue:) | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityevent/name/init(_:) | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityevent/includesallactivity | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/context | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/init(_:filter:) | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/body | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityreportextension | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityreportscene | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityreportbuilder | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityfilter | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivitydata | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityresults | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityresults/iterator | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityresults/makeasynciterator() | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityauthorization | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/deviceactivity/deviceactivityauthorizing | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/shieldconfiguration | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettingsui/shieldconfigurationextension | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettingsui/shieldconfigurationdatasource | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/managedsettingsstore | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/managedsettingsstore/clearallsettings() | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/managedsettingsstore/shield | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/shieldsettings | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/shieldsettings/applications-swift.property | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/shieldsettings/webdomains-swift.property | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/shieldsettings/activitycategorypolicy | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/shieldsettings/activitycategorypolicy/all(except:) | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/shieldsettings/activitycategorypolicy/specific(_:except:) | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/applicationsettings | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/applicationsettings/blockedapplications | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/webcontentsettings | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/webcontentsettings/filterpolicy | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/managedsettings/webcontentsettings/blockedbyfilter-swift.property | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/screentime/stwebhistory | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/screentime/stscreentimeconfigurationobserver | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/screentime/stwebpagecontroller | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/documentation/analytics-reports/app-runtime-usage | Apple Doc | high | Canonical Apple source |
| https://developer.apple.com/videos/play/wwdc2021/10123/ | WWDC | high | Canonical Apple source |
| https://developer.apple.com/videos/play/wwdc2022/110336/ | WWDC | high | Canonical Apple source |
| https://developer.apple.com/videos/play/wwdc2022/110341/ | WWDC | high | Canonical Apple source |
| https://developer.apple.com/contact/request/family-controls-distribution | Apple Portal | high | Canonical Apple source |
| https://developer.apple.com/help/account/capabilities/capability-requests/ | Apple Help | high | Canonical Apple source |
| https://developer.apple.com/help/account/reference/supported-capabilities-ios | Apple Help | high | Canonical Apple source |
| https://developer.apple.com/help/glossary/family-controls/ | Apple Help | high | Canonical Apple source |
| https://medium.com/@juliusbrussee/a-developers-guide-to-apple-s-screen-time-apis-familycontrols-managedsettings-deviceactivity-e660147367d7 | Medium | medium | Field deep dive; corroborate with canonical/SDK |
| https://letvar.medium.com/time-after-screen-time-part-1-the-underworld-of-a-barely-known-api-2574a2e6922a | Medium | medium | Field deep dive; corroborate with canonical/SDK |
| https://letvar.medium.com/time-after-screen-time-part-2-the-device-activity-report-extension-10eeeb595fbd | Medium | medium | Field deep dive; corroborate with canonical/SDK |
| https://letvar.medium.com/time-after-screen-time-part-3-the-device-activity-monitor-extension-284da931391b | Medium | medium | Field deep dive; corroborate with canonical/SDK |
| https://developer.apple.com/forums/thread/727075 | Apple Forum | medium | Apple forum clarification |
| https://developer.apple.com/forums/thread/718169 | Apple Forum | medium | Apple forum clarification |
| https://developer.apple.com/forums/thread/722618 | Apple Forum | medium | Apple forum clarification |
| https://developer.apple.com/forums/thread/725036 | Apple Forum | medium | Apple forum clarification |
| https://developer.apple.com/forums/thread/806285 | Apple Forum | medium | Apple forum clarification |

## Failure Modes
- Mixing canonical and field guidance without labels.
- Treating SDK doc-string constraints as immutable across future SDK releases.

## Validation Checklist
- [ ] Every guide cites at least one canonical source.
- [ ] Every non-trivial claim is tagged by evidence class.
- [ ] Inference claims include caveats.
- [ ] All requested URLs are present in source inventory and this matrix.

## Sources
- `../evidence/00-source-url-inventory.md`
- `../evidence/01-familycontrols-sdk-signatures.md`
- `../evidence/02-managedsettings-sdk-signatures.md`
- `../evidence/03-managedsettingsui-sdk-signatures.md`
- `../evidence/04-deviceactivity-sdk-signatures.md`
- `../evidence/05-deviceactivity-report-sdk-signatures.md`
- `../evidence/06-screentime-framework-headers.md`
- `../evidence/07-claim-reconciliation.md`

## Confidence Notes
- URL inventory and matrix alignment is generated from the same source list and verified by script.
