---
title: 'Subjective Risk Decomposition: A New View for Uncertainty Quantification'
title_zh: 主观风险分解：不确定性量化的新视角
authors:
- Raghad Alamri
- Michele Caprio
- Gavin Brown
affiliations:
- Department of Computer Science, The University of Manchester
- Department of Computer Science, University of Warwick
arxiv_id: '2607.15196'
url: https://arxiv.org/abs/2607.15196
pdf_url: https://arxiv.org/pdf/2607.15196
published: '2026-07-16'
collected: '2026-07-19'
category: Training
direction: 不确定性量化 · 风险分解理论
tags:
- Uncertainty Quantification
- Epistemic Uncertainty
- Aleatoric Uncertainty
- Subjective Risk
- Strictly Proper Loss
one_liner: 将认知与随机不确定性归为严格正则损失下主观风险分解结果，提供UQ通用理论框架
practical_value: '- 推荐排序模型的不确定性预估可参考该框架，针对业务自定义严格正则损失推导适配的认知/随机不确定性分解项，替代通用熵分解，更贴合业务目标

  - 冷启动、长尾推荐的鲁棒性优化场景中，可基于分解得到的认知不确定性项判断样本是否需要补充标注/探索，提升探索效率

  - LLM4Rec生成结果的可信度评估场景下，可基于自定义生成损失推导对应的不确定性分解，辅助生成结果的筛选与拒识'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有不确定性量化（UQ）领域的认知/随机不确定性度量多依赖自定义公理，缺乏统一理论支撑，不同业务场景下的度量选型无明确指导原则。
### 方法关键点
1. 提出不确定性并非底层原生定义，而是高层建模决策的衍生结果，基于严格正则损失对主观风险做分解，即可自动得到对应场景的认知与随机不确定性项；
2. 证明该框架可复现逆交叉熵等经典UQ度量的分解结果，覆盖多数已有UQ方案；
3. 拓展至学习理论范畴，建立了主观风险下超额风险、近似误差、估计误差与UQ项的关联。
### 关键结果
统一了UQ领域数十种现有不确定性度量的理论基础，为任意建模场景下的定制化UQ方案提供了可落地的推导范式。
