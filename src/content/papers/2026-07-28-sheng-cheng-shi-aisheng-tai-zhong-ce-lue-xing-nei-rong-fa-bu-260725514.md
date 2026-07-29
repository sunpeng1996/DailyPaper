---
title: Learning Dynamics of Strategic Publishers in Generative AI Ecosystems
title_zh: 生成式AI生态中策略性内容发布者的学习动态
authors:
- Sagie Dekel
- Omer Madmon
- Moshe Tennenholtz
- Oren Kurland
affiliations:
- Technion - Israel Institute of Technology
arxiv_id: '2607.25514'
url: https://arxiv.org/abs/2607.25514
pdf_url: https://arxiv.org/pdf/2607.25514
published: '2026-07-28'
collected: '2026-07-29'
category: Other
direction: 生成式搜索生态 · 博弈论机制设计
tags:
- Generative AI Search
- Game Theory
- Ecosystem Stability
- Mechanism Design
- Welfare Trade-off
one_liner: 构建博弈论模型分析生成式搜索生态发布者竞争动态，提出稳定机制及福利权衡方案
practical_value: '- 做生成式搜索/问答产品时，可参考本文的归因曝光竞争模型，提前评估内容供给侧的策略性作弊风险，避免生态失稳

  - 内容选择机制设计阶段可引入潜在博弈框架判断收敛性，平衡平台、内容创作者、用户三方的福利目标，避免盲目追求单一指标

  - 电商内容导购/生成式种草场景可复用该博弈分析思路，优化达人/商家内容的引用分配规则，减少恶意内容优化行为'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有生成式AI搜索系统以「生成回答+引用来源」的形式返回结果，内容发布者为获取曝光会策略性调整内容竞争引用位，此前缺乏对该新型竞争模式下生态稳定性的量化分析框架。
### 方法关键点
1. 首次构建面向生成式AI生态的博弈论模型，刻画发布者基于归因曝光的竞争关系
2. 用潜在博弈理论分析不同内容选择机制下的发布者最优响应学习动态，将动态收敛到纳什均衡作为生态稳定的判定标准
3. 结合大量仿真实验验证理论结论，分析稳定性、发布者福利、用户福利三者的关联
### 关键结果
验证了当前主流生成式搜索采用的内容选择机制普遍存在不稳定性；提出的稳定机制可实现生态收敛，同时揭示稳定机制并不必然最大化总福利，三者间存在核心权衡，合理选择机制可实现发布者与用户多维度福利的预期平衡。
