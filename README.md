# Bloomfield Stadium Event Calendar Automation

## Problem
Traffic congestion around Bloomfield Stadium becomes severe on match days and event nights. While event information exists on the municipality website, it is fragmented across multiple teams, concerts, and national games, and there is no single calendar focused exclusively on Bloomfield Stadium events. Additionally, the existing calendar does not support notifications, making it difficult to plan ahead and avoid traffic disruptions.

## Solution
I built an automated system that scrapes event data from the municipality website, normalizes and converts it into a calendar-friendly format, and ensures accurate timezone handling. The system publishes the events as a shareable calendar feed compatible with Google and Apple Calendar, and runs on a scheduled automation to keep the information continuously up to date without manual intervention.

## Architecture
- **Data Source:** Event data is scraped from the Tel Aviv Municipality website, which publishes official schedules for matches and events held at Bloomfield Stadium.
- **Processing:** A Python-based scraper using BeautifulSoup extracts event titles and times, normalizes timezone data, and converts the results into an iCalendar (.ics) format.
- **Automation:** The scraper runs as an AWS Lambda function triggered on a scheduled basis using Amazon EventBridge.
- **Storage & Distribution:** The generated calendar file is uploaded to an Amazon S3 bucket and served publicly, allowing seamless subscription from Google Calendar and Apple Calendar.

## Tech Stack
- **Language:** Python  
- **Cloud Services:** AWS Lambda, Amazon S3, Amazon EventBridge  
- **Libraries:** BeautifulSoup, `ics`, `datetime`, `zoneinfo`  

## How It Works
1. An Amazon EventBridge rule triggers the AWS Lambda function on a scheduled basis.
2. The Lambda function fetches the latest event data from the Tel Aviv Municipality website.
3. Event titles and timestamps are parsed and normalized using Python.
4. All event times are converted to UTC to ensure correct alignment across different calendar clients and daylight-saving changes.
5. The processed events are compiled into an iCalendar (.ics) file.
6. The calendar file is uploaded to an Amazon S3 bucket and served publicly for subscription.

## Deployment Overview
- The system is deployed using a fully serverless architecture built around AWS Lambda.
- Execution is scheduled and managed by Amazon EventBridge, ensuring regular, automated updates without manual intervention.
- Calendar hosting and distribution are handled via Amazon S3, eliminating the need for infrastructure maintenance.

## Result
The output is a publicly accessible calendar feed that can be subscribed to using Google Calendar, Apple Calendar, or any iCalendar-compatible application. Users can configure personalized notifications in advance, making it easier to plan ahead and avoid traffic congestion around Bloomfield Stadium on match days and event nights.

## Future Improvements
- Personalized alerting based on team preferences, allowing users to receive notifications only for relevant matches or events.
- Infrastructure as Code (IaC) using tools such as Terraform to enable reproducible and version-controlled cloud deployments.
- Monitoring and alerting to detect scraping failures or upstream website changes and ensure system reliability.
