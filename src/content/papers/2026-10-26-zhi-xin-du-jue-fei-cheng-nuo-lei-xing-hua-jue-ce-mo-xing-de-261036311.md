---
title: 'Confidence Is Not a Promise: A Reference Audit of Typed Decision Models'
title_zh: 置信度绝非承诺：类型化决策模型的参考审计
authors:
- Pedro Carvalho Brom
affiliations:
- Department of Mathematics, Federal Institute of Brasília, Brasília, Brazil
arxiv_id: '2610.36311'
url: https://arxiv.org/abs/2610.36311
pdf_url: https://arxiv.org/pdf/2610.36311
published: '2026-10-26'
collected: '2026-10-29'
category: Eval
direction: 模型校准 · 决策模型置信度审计
tags:
- Calibration
- Selective Classification
- Model Auditing
- Confidence Estimation
- Decision Model
one_liner: 多维度审计类型化决策模型置信度可靠性，对比不同校准策略的承诺履约效果
practical_value: '- 推荐/广告分类、审核任务的置信度阈值不要采用点估计选择，优先使用Learn then Test校准策略，可100%保证预设准确率承诺

  - 多语言/多地域部署LLM决策模型时，直接复用英文校准版本会出现跨Locale准确率不达标问题，需分Locale单独校准

  - 应对输入噪声（如用户搜索query拼写错误、评论错字）场景，可在训练时加入噪声数据，能提升噪声场景准确率且不损失干净数据效果

  - 数据漂移场景下无需全量重训，优先做窗口阈值重校准即可维持置信度承诺，成本远低于全量重训'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有业务系统普遍将类型化决策模型输出的置信度直接等同于准确率承诺，置信度可靠性未经验证，常导致线上实际准确率远低于预期。
### 方法关键点
对比开源Laya的5个checkpoint与闭源API服务Jev 1.13，跨190组可交换评估、51个Locale、4个业务域、数据漂移场景等多维度审计不同校准策略的承诺履约能力。
### 关键结果数字
点估计选阈值的方案在147/190次不满足预设准确率承诺，Learn then Test方案100%满足要求；Beta下界规则比Learn then Test在128/190次的决策覆盖量更高；英文校准的Jev仅8/51个Locale满足95%准确率承诺；加噪声训练可提升噪声场景准确率且无干净数据效果损失；漂移场景下窗口阈值重校准成本与纯校准相当，履约率远高于贝叶斯重训循环。
