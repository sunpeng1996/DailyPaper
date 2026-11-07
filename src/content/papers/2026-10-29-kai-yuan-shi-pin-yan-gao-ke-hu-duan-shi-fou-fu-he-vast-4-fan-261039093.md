---
title: Do Open-Source Video Ad Clients Follow VAST 4.3? An Empirical Study of Player
  Conformance
title_zh: 开源视频广告客户端是否符合VAST 4.3规范？播放器合规性实证研究
authors:
- Prashant Chaudhary
affiliations:
- Independent Researcher
arxiv_id: '2610.39093'
url: https://arxiv.org/abs/2610.39093
pdf_url: https://arxiv.org/pdf/2610.39093
published: '2026-10-29'
collected: '2026-11-07'
category: Other
direction: 视频广告SDK 规范合规性测试
tags:
- VAST
- Conformance Testing
- Ad SDK
- Video Ad
- Empirical Study
one_liner: 实证测试6款开源VAST客户端多环境合规性，披露78项问题并开源测试套件
practical_value: '- 自研/选型视频广告VAST客户端时，可直接复用本次开源的测试向量与测试框架，在Chrome、Safari等真实浏览器环境做合规性校验，避免统计误差导致的结算纠纷

  - 排查广告上报计数不一致问题时，优先核查Wrapper重定向链宏参数填充、Pod连播广告上报归属、不同JS runtime兼容性三类已知共性问题

  - 广告SDK迭代时可引入版本遍历测试机制，类似本次对36个版本的扫描方法，避免版本升级引入合规性偏差'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
视频广告通过VAST协议传输至流媒体/OTT端，播放器客户端的上报错误不会影响播放，只会在后期出现上下游广告计数不一致，引发结算纠纷，现有开源VAST客户端的4.3规范合规性缺乏系统性验证。
### 方法关键点
从VAST4.3规范提取108项要求，对6款开源客户端的8种配置，在Node.js、3种内核5款浏览器环境下，通过69个定制测试向量、IAB官方样例、fuzzing测试完成校验，对比Google闭源IMA SDK，同时扫描36个历史版本定位问题引入时机。
### 关键结果
共发现78项问题，单配置存在3~21项强制要求偏差；所有支持重定向链的开源客户端均未正确填充Wrapper请求的必填宏参数；存在跨环境兼容性问题，同一款库在jsdom下合规但在Chrome、Safari全系列浏览器下均不符合规范。
