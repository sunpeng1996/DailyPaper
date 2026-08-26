---
title: 'Auditing Return Conditioning as a Control Knob: An Offline Diagnostic for
  Decision Transformer Recommendation'
title_zh: 决策Transformer推荐系统的回报条件控制能力离线诊断框架
authors:
- Jingyu Wang
affiliations:
- Independent Researcher
arxiv_id: '2608.24815'
url: https://arxiv.org/abs/2608.24815
pdf_url: https://arxiv.org/pdf/2608.24815
published: '2026-08-25'
collected: '2026-08-26'
category: RecSys
direction: 决策Transformer推荐 · 可控性离线评估
tags:
- Decision Transformer
- RTG
- Offline Evaluation
- Recommender System
- Controllability
one_liner: 提出4项离线诊断指标验证决策Transformer推荐中RTG条件的实际控制有效性
practical_value: '- 上线基于DT的可控推荐前，优先用文中4项离线检查验证RTG的实际控制效果，避免无效的RTG设计逻辑

  - 需通过RTG调控推荐分布时，优先修改全上下文窗口内所有历史RTG token，调控效率是仅改当前slot的10倍以上

  - RTG控制效果强依赖数据集特性，不要直接照搬公开数据集结论，需在自有业务数据上先做混洗RTG消融验证'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：决策Transformer（DT）类序列推荐常通过调整目标return-to-go（RTG）实现可控推荐，但RTG干预的实际控制效果极少被审计，不同RTG修改策略的效果差异也未被验证
**方法关键点**：提出4项离线诊断检查框架：1）RTG干预局部性测试（对比修改全上下文窗口/仅当前slot RTG的效果）；2）无RTG基线对照；3）奖励匹配校验；4）轨迹内混洗RTG消融，在两个公开数据集上开展对照实验
**关键结果**：MovieLens数据集上K=20全上下文RTG干预可让犯罪类内容推荐占比提升23.61±2.96pp，仅修改当前slot仅提升1.77±1.17pp，混洗RTG后提升降至2.08±1.20pp；MyAnimeList数据集上同类干预无明显调控效果，三类模型（真实RTG/无RTG/混洗RTG）的品类预测准确率接近，K=1时日志匹配率和匹配评分几乎无变化
