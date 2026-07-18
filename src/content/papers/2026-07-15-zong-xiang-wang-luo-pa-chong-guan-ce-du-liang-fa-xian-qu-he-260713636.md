---
title: 'Measuring What the Crawler Sees: Discovery Curves, Core Persistence, and Shell
  Dynamics in Longitudinal Web Crawls'
title_zh: 纵向网络爬虫观测度量：发现曲线、核心留存率与外壳动态
authors:
- Michael Paris
- Hande Celikkanat
- Luca Foppiano
affiliations:
- Common Crawl Foundation
arxiv_id: '2607.13636'
url: https://arxiv.org/abs/2607.13636
pdf_url: https://arxiv.org/pdf/2607.13636
published: '2026-07-15'
collected: '2026-07-18'
category: Other
direction: 网络爬取度量 · 双成分urn模型
tags:
- Web Crawl
- Urn Model
- Discovery Curve
- URL Persistence
- Crawl Coverage
one_liner: 提出双成分urn模型与发现曲线指标，量化纵向网络爬取的URL留存与覆盖率异质性
practical_value: '- 电商竞品数据/商品页爬虫场景：可复用双成分urn模型区分核心页（头部商品、活动页）与外壳页（长尾冷门商品）的留存差异，优化爬取频次与配额分配，提升核心数据覆盖率

  - RAG外部网页数据源维护场景：可复用发现曲线指标量化不同时间窗口的URL覆盖度，优化增量爬取周期，降低无效爬取成本

  - LLM预训练/微调语料清洗场景：可参考核心留存率$κ$过滤低留存的噪声外壳数据，提升语料的有效信息密度'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有纵向网络爬取的成对containment度量基于同质urn假设，默认URL群体分布均匀，无法刻画真实爬取的异质性，也不能直接度量滑动窗口下的累积URL覆盖效果。

### 方法关键点
1. 定义发现曲线$U(s,T)$，量化起始于$s$的$T$次爬取滑动窗口的累积URL覆盖范围，推导其与单轮URL留存率$\alpha$、覆盖率$c$的闭式关系；
2. 同质urn假设成立时，containment与发现曲线对$(\alpha,c)$的拟合结果一致，二者偏差可直接衡量群体异质性，据此提出双成分urn模型，引入持久核心占比$\kappa$与外壳参数$(\alpha_\partial, c_\partial)$拟合偏差。

### 关键结果
在2020-2025 Common Crawl（域粒度）、德国学术网（URL粒度）数据集上验证，双成分模型可解释两类度量的偏差，外壳仍存在非均匀性残差，核心占比$\kappa$可作为排名泛化的标量入口。
