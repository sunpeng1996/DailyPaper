---
title: 'Reconstruction: A Blind Benchmark for Recovering Research Ideas from Pre-Publication
  Bibliographies'
title_zh: Reconstruction：仅用预出版参考文献还原研究想法的盲测基准
authors:
- Shaolong Chen
- Yanlin Fei
- Nazhou Liu
- Xinmiao Yu
- Lei Li
- Rahul Thapa
- Madalina Ciobanu
- Qingqing Mao
- Ritankar Das
affiliations:
- Prentis AI
- Stanford University
- Titan Holdings
arxiv_id: '2608.16645'
url: https://arxiv.org/abs/2608.16645
pdf_url: https://arxiv.org/pdf/2608.16645
published: '2026-08-17'
collected: '2026-08-18'
category: MultiAgent
direction: 多智体协作 · LLM评估基准
tags:
- Multi-Agent
- Benchmark
- LLM Evaluation
- Scientific Ideation
- Swiss Tournament
one_liner: 提出防泄漏的研究想法还原盲基准，搭配多Agent pipeline将匹配率相对单模型提升2.4倍
practical_value: '- 可将「多模型并行生成→跨模型评审→瑞士轮选优」的多Agent pipeline直接迁移到电商种草文案/商品标题生成、推荐理由生成场景，无需额外检索就能提升内容匹配度，相对单模型有2倍左右的潜在增益

  - 严格的反泄漏设计（时间截断、匿名ID、信息隔离、生成方回避评审）可复用在推荐/广告系统的离线A/B测试、新模型冷启动评估中，避免数据泄露导致的效果虚高

  - 推理侧缩放思路（从多模型生成的大量候选中选优）适合成本不敏感的高价值生成场景（如大促营销文案、个性化push文案），可在可控成本内大幅提升点击率转化率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM科研创新能力评估多聚焦开放性生成的新颖性，缺乏严格可控的基准衡量模型基于既有文献推理、还原真实创新点的能力，也无法验证多Agent协作在受限信息推理任务上的真实增益。
### 方法关键点
- 反泄漏基准设计：仅保留种子论文预出版时间前的参考文献，隐藏种子本身及同期/后续文献，参考文献用匿名ID，彻底避免prompt阶段目标信息泄露
- 单模型基线：7款前沿LLM基于盲参考文献生成5个研究假设，由排除自身的其余模型作为独立评委，计算生成假设与种子核心研究点的Match率
- 多Agent pipeline：筛选4个最优单模型并行生成假设，按slot对齐后开展跨模型评审（生成方回避），经瑞士轮锦标赛选出每个slot的最优假设，全程无外部检索
- 评估规则：评委需回避自身生成的假设，避免自评估偏差，核心指标为单篇论文平均Match率（生成假设与种子核心研究点的匹配比例）
### 关键实验
数据集覆盖ML、天文、化学、材料、医学、物理6个领域共643篇论文，单模型最优平均Match率仅13.3%，单领域得分落在3~15%区间；多Agent pipeline的Match率提升至23~42%，平均36%，相对最优单模型提升2.4倍，95%置信区间[2.3,2.6]，在343篇论文上表现优于单模型最优结果，仅160篇更差。
### 核心结论
仅靠跨模型评审+锦标赛选优的多Agent协作，无需额外检索或知识注入，就能在严格信息隔离的推理任务上实现相对单模型2倍以上的效果提升
