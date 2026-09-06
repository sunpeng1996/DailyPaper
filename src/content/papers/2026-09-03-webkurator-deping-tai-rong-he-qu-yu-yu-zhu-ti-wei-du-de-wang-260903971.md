---
title: 'The WebKurator.de Platform: Combined Regional and Topical Web Curation'
title_zh: WebKurator.de平台：融合区域与主题维度的网页内容策展系统
authors:
- Michael Dinzinger
- Natanael Arndt
- Ben Böck
- Jelena Mitrović
- Michael Granitzer
affiliations:
- University of Passau
- Deutsche Nationalbibliothek
- IT:U Austria
arxiv_id: '2609.03971'
url: https://arxiv.org/abs/2609.03971
pdf_url: https://arxiv.org/pdf/2609.03971
published: '2026-09-03'
collected: '2026-09-06'
category: Other
direction: 网页内容策展 · 多维度分类标注
tags:
- Web Curation
- Geographic Information Extraction
- Web Archiving
- LLM Classification
- Web Directories
one_liner: 提出分离主题分类与地理标注的二维网页策展模型，搭建面向德语区的协同式网页内容策展平台
practical_value: '- 本地生活类推荐可参考主题+地理二维分离的标注框架，避免维度混杂导致的召回准确率下降

  - 商家备案页地址提取+地理编码的实现方案，可直接复用在本地商家库的标准化构建流程中

  - LLM自动分类+人工审核的冷启动路径，适合快速搭建垂直领域内容/商品库的标注体系'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
国家图书馆等记忆机构需留存具备文化、区域价值的网页内容，现有Curlie等目录式方案采用单一主题层级，地理维度与主题、语言维度混杂，分类精度与检索效率不足。
### 方法关键点
1. 提出二维策展模型，显式拆分主题分类与地理标注两个独立维度，解决原有维度混杂问题
2. 融合LLM主题分类、imprint页地址提取+地理编码的自动化标注能力，搭配用户提交+专家审核的协同迭代机制
3. 基于德国备案网站数据集冷启动，降低平台初始搭建成本
### 关键结果
基于5.54百万德语网站数据集启动，3.14百万含imprint页的站点中成功提取并编码地址，其中2.58百万（占比85.17%）为德国境内站点且匹配主题标签，构成平台初始资源池
