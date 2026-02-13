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

## Implementation Pattern
1. Host app selects report context + filter (segment/users/devices/app/category/domain scope).
2. Host app renders `DeviceActivityReport(context, filter:)`.
3. Report extension scene receives filtered data and generates configuration.
4. Scene content renders charts/cards using async results iteration.
5. Keep report rendering local; avoid network-dependent architecture.

## Failure Modes
- Putting business API calls in report extension (sandbox violation model).
- Forgetting authorization dependency for report data availability.
- Overly heavy report scene causing render lag.

## Validation Checklist
- [ ] At least one custom `DeviceActivityReport.Context` is defined and handled.
- [ ] Report extension has matching scene per used context.
- [ ] Async results iteration works for segment/category/app/domain paths.
- [ ] Report output degrades gracefully with empty data.

## Sources
- `../evidence/05-deviceactivity-report-sdk-signatures.md`
- https://developer.apple.com/documentation/deviceactivity/deviceactivityreport
- https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/context
- https://developer.apple.com/documentation/deviceactivity/deviceactivityreportextension
- https://developer.apple.com/documentation/deviceactivity/deviceactivityreportscene
- https://developer.apple.com/documentation/deviceactivity/deviceactivityfilter

## Confidence Notes
- Report extension architecture and sandbox notes are `sdk-backed`.
- Charting implementation guidance is `inference` and should be validated per app UX goals.
