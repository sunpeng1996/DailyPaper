---
title: 'Fetch, Read, Reuse: How AI Search Agents Bend the Web''s Rules'
title_zh: 《AI搜索代理网页抓取/读取/复用行为实测与Web规则适配性分析》
authors:
- Yixi Chen
- Zafar A. Qazi
- Marco Canini
- Suhaib A. Fahmy
affiliations:
- KAUST
- LUMS
arxiv_id: '2611.30546'
url: https://arxiv.org/abs/2611.30546
pdf_url: https://arxiv.org/pdf/2611.30546
published: '2026-11-23'
collected: '2026-11-24'
category: Agent
direction: AI搜索Agent · 网页交互行为测量
tags:
- AI Search Agent
- Web Protocol
- Black-box Measurement
- robots.txt
- Cache Control
one_liner: 黑盒实测14款主流AI搜索服务的网页交互行为，揭露其对现有Web规则的普遍背离
practical_value: '- 开发检索类Agent/LLM搜索工具时，若要合规友好地抓取网页，可参考Anthropic的实现逻辑：请求前校验robots.txt，支持Cache-Control的no-store指令，避免给站点造成不必要的负载；针对JS动态生成的核心内容，可单独适配Headless
  Chrome渲染逻辑，避免信息丢失

  - 做电商/内容站的AI友好适配时，注意核心信息（如库存、实时价格、活动规则）不要放在JS动态块、markdown/XML/CSV格式文件或页面后半段（>0.5MB位置），否则会被OpenAI、xAI等主流AI搜索代理忽略，导致用户拿到过时/错误信息

  - 运营高时效性/敏感内容站点时，不要依赖robots.txt、Cache-Control等传统Web规则限制AI抓取：当前大部分主流AI搜索代理会忽略上述规则，敏感内容建议添加身份校验、动态token等机制，避免被抓取后跨用户复用导致资损'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
AI搜索代理已占2025年全球AI爬虫流量的20%，其兼具「用户触发抓取的浏览器属性、内容改写的代理属性、跨用户复用的缓存属性」的三重特征，导致传统Web规则（robots.txt、Retry-After、Cache-Control等）没有明确的适用标准，内容发布方、CDN、普通用户都面临规则失效带来的负载增加、信息过时、内容失控等损失，亟需明确主流AI搜索代理的实际行为模式。
### 方法关键点
1. 搭建2个可控测试源站（1个带Cloudflare CDN、1个直连公网），所有测试页面植入不可猜测的唯一识别码，全程记录所有请求日志；
2. 测试覆盖OpenAI、Anthropic、xAI、Google的公开API，以及ChatGPT、Claude、Grok等10款C端AI搜索应用；
3. 从抓取、读取、复用三个阶段设计对照实验，同时用第三方公开站点的动态递增数据（如区块链高度、新闻首页内容）做交叉验证，避免实验偏差。
### 关键结果数字
1. 抓取阶段：OpenAI、xAI完全不遵守robots.txt规则，所有被测服务均不处理Retry-After头，xAI单用户查询会发起4~14次并行请求，重定向循环场景下甚至发起57~77次并行请求，大幅提升源站负载；
2. 读取阶段：所有被测服务均不解析JS动态生成的内容，OpenAI抓取后直接丢弃markdown/XML/CSV/DOCX格式内容，xAI仅读取页面前0.5MB内容，且均不会告知用户内容被截断；
3. 复用阶段：OpenAI、Anthropic、xAI默认跨用户共享抓取到的页面内容，完全忽略Cache-Control规则，旧内容复用时长从30分钟（OpenAI）到1天以上（Anthropic、xAI），失败的抓取结果也会被缓存数小时到1天，页面修复后仍可能返回错误信息。
### 最值得记住的结论
当前所有Web规则对AI搜索代理都是自愿遵守的建议性规则，没有强制约束力，不管是开发Agent还是运营内容站点，都不能假设规则会被严格执行。
