---
title: 'GuardAgent: A Memory-Augmented Agentic Framework for Adaptive Detection of
  Adversarial Promotions in LLM-Based Recommendation'
title_zh: GuardAgent：记忆增强Agent框架，检测LLM推荐的对抗性推广内容
authors:
- Shiyi Yang
- Xinshu Li
- Chen Wang
- Xiwei Xu
- Liming Zhu
- Lina Yao
affiliations:
- The University of New South Wales
- CSIRO
- Monash University
- Macquarie University
arxiv_id: '2611.22274'
url: https://arxiv.org/abs/2611.22274
pdf_url: https://arxiv.org/pdf/2611.22274
published: '2026-11-17'
collected: '2026-11-18'
category: RecSys
direction: 推荐系统安全 · LLM Agent 对抗检测
tags:
- LLM4Rec
- AdversarialDetection
- MemoryAugmentedAgent
- TrustworthyRS
- CognitiveLoop
one_liner: 提出带认知循环的记忆增强Agent，自适应检测LLM推荐中的对抗性推广攻击，性能超SOTA
practical_value: '- 电商内容审核场景可直接复用GuardAgent的认知循环架构，检测商家恶意篡改的商品标题/描述等推广作弊内容，其低FPR特性适配平台合规要求，减少对正常商家的误拦截

  - 双记忆（短时/长时记忆）+ 批量对比反思的机制可直接迁移，解决传统静态检测器对新型作弊手段泛化差的问题，无需频繁重训模型即可适配新攻击模式

  - 检测输出附带规则对齐的推理链，可直接对接平台审核的审计流程，大幅降低人工复核的成本，也便于规则迭代优化'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM 推荐系统中文本成为决策核心输入，商家可通过篡改商品文本元数据（加夸张修饰、注入 prompt 注入指令等）实现恶意刷曝光的攻击，传统基于异常交互或静态规则的检测器对这类推理阶段的文本攻击泛化差、误报高、无解释性，当前暂无适配推荐场景的专用对抗推广检测方案。

### 方法关键点
- 构建 Perception-Action-Reflection-Memory 的认知循环，可迭代学习新型攻击模式，无需参数微调即可实现能力迭代
- 采用双记忆架构：短时记忆存储近期决策、推理链和更新的规则，支持快速适配新攻击；长时记忆沉淀历史验证的知识，避免灾难性遗忘
- 反思阶段采用批量对比+双层对比分析（单样本内良性/恶意内容对比、跨样本的恶意模式聚合），动态精炼可解释的检测规则，避免过拟合单条错误样本
- 推理阶段结合当前最新规则+检索 TopK 相似历史案例，输出带规则对齐的可解释检测结果

### 关键实验
在 Amazon 商品、Yelp 商家两个真实数据集上，对比 Zero-shot LLM、检索 ICL、微调 PLM、困惑度检测器等 7 个基线：GuardAgent 在 Amazon 数据集上 ACC 达 93%、F1 达 92%，较次优基线分别提升 6pct、6pct；Yelp 数据集上 ACC 达 84%、F1 达 81%，较次优基线分别提升 4pct、4pct；对未见过的 DrunkAgent 新型攻击实现 100% 召回，FPR < 1%。

针对动态演化的作弊攻击，带记忆和反思能力的 Agent 架构比静态规则、微调模型的泛化性和可解释性更适配业务长期需求。
