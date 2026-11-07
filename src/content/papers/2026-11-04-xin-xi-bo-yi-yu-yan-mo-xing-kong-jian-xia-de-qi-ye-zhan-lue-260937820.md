---
title: 'Information Games: Strategic Crowding and Firm Repositioning in Language-Model
  Space'
title_zh: 信息博弈：语言模型空间下的企业战略拥挤与重新定位
authors:
- Marcus Gawronsky
- Chun-Sung Huang
affiliations:
- Department of Finance and Tax, University of Cape Town
arxiv_id: '2609.37820'
url: https://arxiv.org/abs/2609.37820
pdf_url: https://arxiv.org/pdf/2609.37820
published: '2026-11-04'
collected: '2026-11-07'
category: MultiAgent
direction: 多智体竞争 · 企业策略空间量化分析
tags:
- MultiAgent
- LLM Embedding
- Wasserstein Distance
- Competitive Analysis
- Econometrics
one_liner: 用LLM向量表征企业新闻分布，构建多Agent模型量化战略调整与金融收益关联
practical_value: '- 用向量空间度量竞争主体策略相似性的思路，可迁移到电商竞品追踪、商家经营策略异动识别场景，替代传统人工标注竞品的方案

  - 多Agent模拟结合三明治估计的因果识别框架，可复用在推荐系统多方（平台/商家/用户）博弈的策略效果预估，降低在线实验成本

  - 非结构化文本分布距离与业务指标挂钩的分析方法，可直接用于搜索/广告场景的内容策略异动归因，提升问题定位效率'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
传统企业竞争策略分析依赖结构化财报数据，时效滞后且难以量化不同主体间的策略相似性，无法捕捉企业动态调整的竞争溢出效应。
### 方法关键点
1. 基于LLM生成企业公开新闻、分析师报告的向量表征，用Wasserstein距离衡量不同企业在信息空间的分布差异
2. 扩展多竞争框架构建带调整成本的企业策略调整模型，设计新型三明治估计器量化企业在信息空间的移动幅度与超额收益的关联
3. 搭配多Agent模拟验证新闻报道覆盖度不足等干扰因素下的估计鲁棒性
### 关键结果
2018-2022年纳斯达克上市公司样本验证得到，企业向高现金流机会调整时，信息空间向竞品靠近的幅度与超额收益呈显著正相关；多Agent模拟显示低报道覆盖会显著掩盖小规模策略调整效应
