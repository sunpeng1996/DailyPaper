---
title: 'SimInter: Evidence-Grounded User Simulation with Interview-Based Profile Enrichment
  for Conversational Recommender Systems'
title_zh: SimInter：基于访谈式画像增强的对话推荐可信用户模拟器
authors:
- Erfan Shahabi
- Amirhossein Roshandel
- Mohammad Sadegh Sadeghi
- Azadeh Shakery
affiliations:
- University of Tehran
- Institute for Research in Fundamental Sciences (IPM)
arxiv_id: '2610.18308'
url: https://arxiv.org/abs/2610.18308
pdf_url: https://arxiv.org/pdf/2610.18308
published: '2026-10-13'
collected: '2026-10-14'
category: RecSys
direction: 对话推荐 · LLM用户模拟器优化
tags:
- Conversational Recommendation
- User Simulation
- LLM Agent
- Profile Enrichment
- Hallucination Mitigation
one_liner: 通过双LLM代理访谈+轮级审计生成无幻觉的丰富用户画像，提升对话推荐用户仿真真实度
practical_value: '- 做LLM用户仿真时可复用「统计特征锚定+不对称访谈+轮级幻觉审计」架构，规避静态画像的属性缺失和LLM生成的刻板印象/幻觉，实测用户行为维度丰富度提升88%

  - 访谈生成的用户属性全部绑定证据来源的思路可迁移到电商场景：从用户历史对话、评价、交互中提取决策风格、细粒度偏好等隐性特征，用于个性化推荐话术生成、冷启动用户画像补全

  - 跨模型分工的思路可复用：用不同LLM分别承担生成、审计、标签提取角色，减少同模型偏见传递，审计准确率可达95%以上，大幅降低人工校验成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
对话推荐系统（CRS）真人评估成本高、可复现性差，现有LLM用户模拟器依赖评分、人口属性等静态画像，缺失用户决策风格、细粒度偏好、领域expertise等隐性行为特征，直接让LLM推断又易产生刻板印象、幻觉问题，导致仿真行为同质化、与真实用户特征偏差大。
### 方法关键点
- 统计锚定：从用户历史交互中提取接受率、探索比例、偏好分布等特征作为基础画像，确保生成内容不脱离真实行为
- 不对称双Agent访谈：受访Agent锚定用户基础画像，采访Agent无额外信息仅做开放式引导，通过10轮对话挖掘隐性特征，避免自嗨式虚假属性生成
- 轮级审计：独立审计Agent逐轮校验，识别幻觉、历史矛盾、刻板印象三类问题，按严重程度分别触发整段重生成、问题轮剔除，过滤错误内容
- 证据绑定的画像增强：从审计后对话中提取6类隐性属性，每个属性绑定对应对话证据，用于后续用户仿真
### 关键实验
基于ReDial电影推荐数据集测试，对比纯统计特征基线、CSHI基线：
1. 表达的偏好维度熵从0.859提升至1.619，涨幅88%，Cohen's d=0.96，Holm调整后p<0.001
2. 94.3%的增强属性获人类标注的完全/部分支持，审计机制二分类过滤准确率达95.2%
3. 跨KBRD、UniCRS两类主流CRS模型的鲁棒性测试中，偏好维度熵仍保持0.28~0.56的显著提升
### 核心结论
用户仿真质量是多维度权衡，无需最大化所有多样性指标，优先提升对CRS评估最重要的行为维度丰富度，远比对次要指标的优化更有价值
