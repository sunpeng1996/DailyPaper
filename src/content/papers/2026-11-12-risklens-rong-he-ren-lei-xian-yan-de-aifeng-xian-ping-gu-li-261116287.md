---
title: 'RiskLens: Human-Informed Incident Transfer for AI Risk Evaluation'
title_zh: RiskLens：融合人类先验的AI风险评估历史事故迁移框架
authors:
- Yiliu Tang
- Hangyue Zhang
- Yun Huang
affiliations:
- University of Illinois Urbana-Champaign, USA
arxiv_id: '2611.16287'
url: https://arxiv.org/abs/2611.16287
pdf_url: https://arxiv.org/pdf/2611.16287
published: '2026-11-12'
collected: '2026-11-14'
category: Eval
direction: AI风险评估 · 人机协同框架
tags:
- Risk-Evaluation
- Human-AI-Collaboration
- Ranking-Model
- Schema-Extension
- Transfer-Learning
one_liner: 提出融合人类先验特征的人机协同AI风险评估框架，实现跨产品历史事故风险迁移判别
practical_value: '- 电商推荐/Agent系统风控巡检可复用「历史风险事故+多维度特征匹配排序」思路，替代静态风险检查表，提升风险覆盖度

  - 可借鉴人机协同特征扩展方案，将运营、风控人员的一线经验沉淀为结构化特征维度，持续迭代风险判别模型

  - 风险评估冷启动阶段，可直接复用技术、运营、用户侧三类特征维度，快速搭建初始风险判别ranker'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
AI系统能力快速迭代，现有静态风险检查表、单次头脑风暴式风险评估无法高效判断历史事故是否会迁移到新产品，早期AI团队缺乏低成本、高覆盖的风险评估工具。
### 方法关键点
1. 搭建RiskLens人机协同工作流，核心包含实时爬取更新的AI事故/产品库、可刷新ranker、可扩展的人类先验feature schema
2. 特征体系覆盖技术、运营、用户侧三类维度，排序模型输出可迁移风险事故、对应场景、风险指标、缓解建议，用户标注反馈回流迭代特征与模型
### 关键结果
- 基于2034条AI事故、10443款AI产品训练的特征模型，相对通用基线胜率达86.2%，在20个月未来时间窗口测试集上性能稳定
- 引入13个人类标注的先验维度（危害分类、失效机制、vulnerable groups等）后，模型相对基线胜率提升至91.4%
