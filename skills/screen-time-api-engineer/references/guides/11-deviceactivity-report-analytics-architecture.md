# 11 DeviceActivity Report Analytics Architecture

## Purpose
Explain the correct architecture for in-app usage analytics rendering via report extension, including sandbox constraints.

## Canonical API Surface
- `DeviceActivityReport`
- `DeviceActivityReport.Context`
- `DeviceActivityReportExtension`
- `DeviceActivityReportScene`
- `DeviceActivityFilter`
- `DeviceActivityResults` async sequence APIs
- `DeviceActivityData.activityData(filteredBy:using:)`, `DeviceActivityData.Policy`, `DeviceActivityData.Error` (iOS 26.4+, data access only)

## Implementation Pattern
1. Host app selects report context + filter (segment/users/devices/app/category/domain scope).
2. Host app renders `DeviceActivityReport(context, filter:)`.
3. Report extension scene receives filtered data and generates configuration.
4. Scene content renders charts/cards using async results iteration.
5. Keep report rendering local; avoid network-dependent architecture.

## Host-App Data Fetch (iOS 26.4+)
- `DeviceActivityData.activityData(filteredBy:using:)` returns an async sequence of `DeviceActivityData` in the host app, outside the report extension.
- Requires the `com.apple.developer.family-controls.app-and-website-usage` entitlement and `.approvedWithDataAccess`. Customer installs work only in the EU; elsewhere the call throws.
- Apple's stated use: exporting activity data for use in another app or platform.
- `Policy.cached` is the default. `Policy.live` may still return cached data if the cache was updated recently. If a cached fetch fails with `.missingData`, retry with `.live`.
- This doesn't replace the report extension. For users without data access, the extension is still the only way to show usage.

## Failure Modes
- Putting business API calls in report extension (sandbox violation model).
- Forgetting authorization dependency for report data availability.
- Overly heavy report scene causing render lag.
- Building analytics only on `activityData(filteredBy:using:)`, which leaves users outside the EU with no report.

## Validation Checklist
- [ ] At least one custom `DeviceActivityReport.Context` is defined and handled.
- [ ] Report extension has matching scene per used context.
- [ ] Async results iteration works for segment/category/app/domain paths.
- [ ] Report output degrades gracefully with empty data.
- [ ] If the host-app fetch is used, the report-extension path still works when data access is unavailable.

## Sources
- `../evidence/05-deviceactivity-report-sdk-signatures.md`
- https://developer.apple.com/documentation/deviceactivity/deviceactivityreport
- https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/context
- https://developer.apple.com/documentation/deviceactivity/deviceactivityreportextension
- https://developer.apple.com/documentation/deviceactivity/deviceactivityreportscene
- https://developer.apple.com/documentation/deviceactivity/deviceactivityfilter
- https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/activitydata(filteredby:using:)
- https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/policy
- https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/error
- `../evidence/04-deviceactivity-sdk-signatures.md`

## Confidence Notes
- Report extension architecture and sandbox notes are `sdk-backed`.
- Host-app fetch requirements and EU-only availability are `canonical + sdk-backed` (iOS 26.4+).
- Charting implementation guidance is `inference` and should be validated per app UX goals.
