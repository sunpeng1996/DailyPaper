---
title: 'Algebraic World Model: From Exploration to Proofs'
title_zh: 代数世界模型：从环境探索到形式化证明
authors:
- Guancheng Pan
- Qixin Tan
- Yang Yuan
- Andrew Chi-Chih Yao
affiliations:
- Zhejiang University
- Tsinghua University
- Shanghai QiZhi Institute
arxiv_id: '2610.40503'
url: https://arxiv.org/abs/2610.40503
pdf_url: https://arxiv.org/pdf/2610.40503
published: '2026-10-29'
collected: '2026-10-31'
category: Reasoning
direction: 形式化推理 · 未知环境建模与证明
tags:
- World Model
- Formal Reasoning
- Theorem Proving
- Lean 4
- ARC-AGI
one_liner: 提出可将未知环境交互转化为可形式化推理的AWM框架，支撑可达性与不可达性证明
practical_value: '- 未知环境交互下的规则归纳思路可迁移到电商新场景用户行为规则挖掘：先通过可执行假设迭代验证再固化规则，降低冷启动阶段的规则误差

  - 范畴论引导的规则简化方法可复用在推荐系统行为规则蒸馏：将复杂用户交互规律压缩为可解释、可验证的约束，提升推荐策略的可控性

  - 不可达性证明逻辑可迁移到广告投放/Agent决策约束校验：自动证明预设目标（如投放ROI阈值、用户转化路径）是否不可能达成，减少无效探索成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有面向数学的AI推理系统依赖预定义的数学定义与形式化规范，无法对未知陌生环境开展严谨推理，未知场景下的规则归纳与可验证推理存在能力缺口。
### 方法关键点
1. 先通过环境探索生成可执行Python假设，基于观测结果持续迭代修正；
2. 将验证后的假设整理为带类型对象与共享规则，用范畴论引导的变换简化模型结构；
3. 把最终模型导入Lean 4做形式化表达，可证明目标的可达性/不可达性，结论覆盖未探索轨迹。
### 关键结果
在2个不可完成游戏关卡上，6次运行全部生成内核校验的Lean证明排除所有合法赢法，Claude Opus 5.5、GPT-6 Astra 12次基线运行无一次成功；初始边界正确率AWM为4/6，Opus 5.5为1/6、GPT-6 Astra为0；获得更优解存在的反馈后AWM边界正确率达6/6；在ARC-AGI-3的25个公开游戏上，支撑Lean复现全部183关的赢局轨迹，配合Claude Opus 5得分99.9，认证的赢局路径动作仅为人类基线的43%
