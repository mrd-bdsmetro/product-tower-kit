---
status: active
type: api-documentation
owner: MR.D
last_updated: 2026-05-12
tags: [claudekit, api, vidcap, reviewweb, youtube, scraping, seo]
pmf_impact: medium
---

# ClaudeKit API Documentation

## Overview

ClaudeKit API là proxy layer cung cấp 2 dịch vụ: **VidCap** (YouTube processing) và **ReviewWeb** (web scraping + SEO).

- **Base URL:** `https://claudekit.cc`
- **Auth:** Header `X-API-Key: ck_live_xxx` hoặc `Authorization: Bearer ck_live_xxx`
- **Rate Limit:** 10,000 requests/giờ
- **Timeout:** ~120s per request

## Quick Test

```powershell
# Test VidCap info
Invoke-RestMethod -Uri "https://claudekit.cc/api/proxy/vidcap/v1/youtube/info?url=https://youtube.com/watch?v=dQw4w9WgXcQ" -Headers @{"X-API-Key"="ck_live_xxx"} | ConvertTo-Json -Depth 5
```

---

## VidCap API

**Base path:** `/api/proxy/vidcap/v1`

### Health Check

```
GET /api/proxy/vidcap/v1/healthz
```

### List AI Models

```
GET /api/proxy/vidcap/v1/ai/models
```

### Get Video Info

```
GET /api/proxy/vidcap/v1/youtube/info?url={youtube_url}
```

**Response fields:**
- `id`, `title`, `channel`, `duration`
- `view_count`, `like_count`, `comment_count`
- `tags[]`, `categories[]`
- `thumbnails[]`, `description`

```powershell
Invoke-RestMethod -Uri "https://claudekit.cc/api/proxy/vidcap/v1/youtube/info?url=https://youtube.com/watch?v=dQw4w9WgXcQ" -Headers @{"X-API-Key"="ck_live_xxx"}
```

### Get Media Formats

```
GET /api/proxy/vidcap/v1/youtube/media?url={youtube_url}
```

Returns available quality options and formats.

### Download Video

```
GET /api/proxy/vidcap/v1/youtube/download?url={youtube_url}&format={format}
```

Returns download URL. `format` is optional.

### Get Captions/Subtitles

```
GET /api/proxy/vidcap/v1/youtube/caption?url={youtube_url}&lang={lang}
```

**Parameters:**
- `url` (required): YouTube video URL
- `lang` (optional): Language code, default `en`

```powershell
# English captions
Invoke-RestMethod -Uri "https://claudekit.cc/api/proxy/vidcap/v1/youtube/caption?url=https://youtube.com/watch?v=dQw4w9WgXcQ" -Headers @{"X-API-Key"="ck_live_xxx"}

# Vietnamese captions
Invoke-RestMethod -Uri "https://claudekit.cc/api/proxy/vidcap/v1/youtube/caption?url=https://youtube.com/watch?v=dQw4w9WgXcQ&lang=vi" -Headers @{"X-API-Key"="ck_live_xxx"}
```

**Response fields:**
- `id`: Caption ID
- `ext`: Format (ttml, srt, vtt)
- `content`: Transcript with timestamps `[at X seconds]`
- `locale`: Language code

### AI Summary

```
GET /api/proxy/vidcap/v1/youtube/summary?url={youtube_url}
```

Returns AI-generated summary with sections and timestamps.

```powershell
Invoke-RestMethod -Uri "https://claudekit.cc/api/proxy/vidcap/v1/youtube/summary?url=https://youtube.com/watch?v=dQw4w9WgXcQ" -Headers @{"X-API-Key"="ck_live_xxx"}
```

**Response fields:**
- `name`: Summary title
- `description`: Brief description
- `content`: Markdown summary with sections
- `parts[]`: Timestamped segments with `title`, `from`, `to`, `url`
- `conclusion`: Final conclusion
- `model`: AI model used
- `cost`: API cost

### Custom Summary

```
POST /api/proxy/vidcap/v1/youtube/summary-custom
```

**Body:**
```json
{
  "url": "https://youtube.com/watch?v=...",
  "prompt": "Summarize the key technical points",
  "model": "gemini-1.5-flash"
}
```

### Convert to Article

```
GET /api/proxy/vidcap/v1/youtube/article?url={youtube_url}
```

Converts video content to article format.

### Screenshot

**Single frame:**
```
GET /api/proxy/vidcap/v1/youtube/screenshot?url={youtube_url}&timestamp={seconds}
```

**Multiple frames:**
```
GET /api/proxy/vidcap/v1/youtube/screenshot-multiple?url={youtube_url}&count={count}
```

### Get Comments

```
GET /api/proxy/vidcap/v1/youtube/comments?url={youtube_url}&limit={limit}
```

**Parameters:**
- `url` (required): YouTube video URL
- `limit` (optional): Number of comments, default varies

### Search Videos

```
GET /api/proxy/vidcap/v1/youtube/search?q={query}&limit={limit}
```

```powershell
Invoke-RestMethod -Uri "https://claudekit.cc/api/proxy/vidcap/v1/youtube/search?q=claude+ai+tutorial&limit=10" -Headers @{"X-API-Key"="ck_live_xxx"}
```

---

## ReviewWeb API

**Base path:** `/api/proxy/reviewweb/v1`

### Health Check

```
GET /api/proxy/reviewweb/v1/healthz
```

### Get Profile

```
GET /api/proxy/reviewweb/v1/profile
```

Returns account info and usage statistics.

---

### Scrape Endpoints

**Scrape single URL:**
```
POST /api/proxy/reviewweb/v1/scrape
```

```json
{
  "url": "https://example.com",
  "waitFor": "networkidle",
  "timeout": 30000
}
```

**Scrape multiple URLs:**
```
POST /api/proxy/reviewweb/v1/scrape/urls
```

```json
{
  "urls": ["https://example.com", "https://another.com"]
}
```

**Links map:**
```
POST /api/proxy/reviewweb/v1/scrape/links-map
```

```json
{
  "url": "https://example.com",
  "depth": 1
}
```

---

### Extract Endpoints

**Extract content from URL:**
```
POST /api/proxy/reviewweb/v1/extract
```

```json
{
  "url": "https://example.com"
}
```

**Extract from multiple URLs:**
```
POST /api/proxy/reviewweb/v1/extract/urls
```

```json
{
  "urls": ["https://example.com", "https://another.com"]
}
```

---

### Convert to Markdown

**Single URL:**
```
POST /api/proxy/reviewweb/v1/convert/markdown
```

```json
{
  "url": "https://example.com"
}
```

**Multiple URLs:**
```
POST /api/proxy/reviewweb/v1/convert/markdown/urls
```

```json
{
  "urls": ["https://example.com", "https://another.com"]
}
```

```powershell
Invoke-RestMethod -Uri "https://claudekit.cc/api/proxy/reviewweb/v1/convert/markdown" -Method Post -Headers @{"X-API-Key"="ck_live_xxx"; "Content-Type"="application/json"} -Body '{"url":"https://example.com"}' | ConvertTo-Json -Depth 5
```

---

### Screenshot

```
POST /api/proxy/reviewweb/v1/screenshot
```

```json
{
  "url": "https://example.com",
  "fullPage": false,
  "width": 1920,
  "height": 1080
}
```

**Get screenshot by ID:**
```
GET /api/proxy/reviewweb/v1/screenshot/{id}
```

---

### Website Review

```
POST /api/proxy/reviewweb/v1/review
```

```json
{
  "url": "https://example.com"
}
```

**Get review by ID:**
```
GET /api/proxy/reviewweb/v1/review/{reviewId}
```

---

## SEO Endpoints

**Base path:** `/api/proxy/reviewweb/v1`

### AI Summaries

**Summarize URL:**
```
POST /api/proxy/reviewweb/v1/summarize/url
```

```json
{
  "url": "https://example.com",
  "model": "gemini-1.5-flash"
}
```

**Summarize entire website:**
```
POST /api/proxy/reviewweb/v1/summarize/website
```

```json
{
  "url": "https://example.com",
  "depth": 2,
  "model": "gemini-1.5-flash"
}
```

**Summarize multiple URLs:**
```
POST /api/proxy/reviewweb/v1/summarize/urls
```

```json
{
  "urls": ["https://example.com", "https://another.com"],
  "model": "gemini-1.5-flash"
}
```

**List available AI models:**
```
GET /api/proxy/reviewweb/v1/ai/models
```

---

### SEO Insights

**Backlink analysis:**
```
POST /api/proxy/reviewweb/v1/seo-insights/backlinks
```

```json
{
  "domain": "example.com"
}
```

Returns: referring domains, anchor text distribution, link quality.

**Keyword ideas:**
```
POST /api/proxy/reviewweb/v1/seo-insights/keyword-ideas
```

```json
{
  "keyword": "ai tools",
  "country": "US"
}
```

Returns: keyword suggestions with search volume and competition.

**Keyword difficulty:**
```
POST /api/proxy/reviewweb/v1/seo-insights/keyword-difficulty
```

```json
{
  "keyword": "ai tools",
  "country": "US"
}
```

Returns: difficulty score 0-100.

**Traffic analysis:**
```
POST /api/proxy/reviewweb/v1/seo-insights/traffic
```

```json
{
  "domain": "example.com"
}
```

Returns: estimated monthly visits, traffic sources, trends.

---

### URL Utilities

**Check URL alive:**
```
POST /api/proxy/reviewweb/v1/url/is-alive
```

```json
{
  "url": "https://example.com"
}
```

**Resolve redirects:**
```
POST /api/proxy/reviewweb/v1/url/get-url-after-redirects
```

```json
{
  "url": "https://bit.ly/xxx"
}
```

---

## Use Cases

### Content Pipeline

```powershell
# 1. Get video info
$info = Invoke-RestMethod -Uri "https://claudekit.cc/api/proxy/vidcap/v1/youtube/info?url=https://youtube.com/watch?v=xxx" -Headers @{"X-API-Key"="ck_live_xxx"}

# 2. Get AI summary
$summary = Invoke-RestMethod -Uri "https://claudekit.cc/api/proxy/vidcap/v1/youtube/summary?url=https://youtube.com/watch?v=xxx" -Headers @{"X-API-Key"="ck_live_xxx"}

# 3. Convert to markdown
$md = Invoke-RestMethod -Uri "https://claudekit.cc/api/proxy/reviewweb/v1/convert/markdown" -Method Post -Headers @{"X-API-Key"="ck_live_xxx"; "Content-Type"="application/json"} -Body '{"url":"https://example.com"}'
```

### Competitor Analysis

```powershell
# 1. Scrape competitor website
$html = Invoke-RestMethod -Uri "https://claudekit.cc/api/proxy/reviewweb/v1/scrape" -Method Post -Headers @{"X-API-Key"="ck_live_xxx"; "Content-Type"="application/json"} -Body '{"url":"https://competitor.com"}'

# 2. Get backlinks
$backlinks = Invoke-RestMethod -Uri "https://claudekit.cc/api/proxy/reviewweb/v1/seo-insights/backlinks" -Method Post -Headers @{"X-API-Key"="ck_live_xxx"; "Content-Type"="application/json"} -Body '{"domain":"competitor.com"}'

# 3. Get traffic estimate
$traffic = Invoke-RestMethod -Uri "https://claudekit.cc/api/proxy/reviewweb/v1/seo-insights/traffic" -Method Post -Headers @{"X-API-Key"="ck_live_xxx"; "Content-Type"="application/json"} -Body '{"domain":"competitor.com"}'
```

### YouTube Research

```powershell
# 1. Search videos
$search = Invoke-RestMethod -Uri "https://claudekit.cc/api/proxy/vidcap/v1/youtube/search?q=product+review+tech&limit=10" -Headers @{"X-API-Key"="ck_live_xxx"}

# 2. Get video details
$info = Invoke-RestMethod -Uri "https://claudekit.cc/api/proxy/vidcap/v1/youtube/info?url=https://youtube.com/watch?v=xxx" -Headers @{"X-API-Key"="ck_live_xxx"}

# 3. Get captions
$captions = Invoke-RestMethod -Uri "https://claudekit.cc/api/proxy/vidcap/v1/youtube/caption?url=https://youtube.com/watch?v=xxx&lang=en" -Headers @{"X-API-Key"="ck_live_xxx"}
```

---

## Error Handling

**Response structure:**
```json
{
  "status": 1,
  "data": {...},
  "messages": ["Ok."]
}
```

| Status | Meaning |
|--------|---------|
| `1` | Success |
| `0` | Error |

**Rate limit exceeded:** HTTP 429
**Invalid API key:** HTTP 401
**Not found:** HTTP 404

---

## Cost Tracking

Response includes `usage` object:

```json
{
  "usage": {
    "prompt_tokens": 292,
    "completion_tokens": 67,
    "total_tokens": 359,
    "cost": 0.00034353
  }
}
```

Monitor via dashboard: `https://claudekit.cc/dashboard`

---

## Resources

- Docs: `https://docs.claudekit.cc/vi`
- Dashboard: `https://claudekit.cc/dashboard`
- Base URL: `https://claudekit.cc`

---
*ClaudeKit API v1.0.0 — 2026-05-12*