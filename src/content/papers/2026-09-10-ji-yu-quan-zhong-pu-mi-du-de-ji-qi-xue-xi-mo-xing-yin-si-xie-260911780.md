---
title: Predicting Privacy Leakage from Weight Spectral Density
title_zh: 基于权重谱密度的机器学习模型隐私泄露风险预测
authors:
- Richard J. Preen
- Jim Smith
affiliations:
- University of the West of England
arxiv_id: '2609.11780'
url: https://arxiv.org/abs/2609.11780
pdf_url: https://arxiv.org/pdf/2609.11780
published: '2026-09-10'
collected: '2026-09-13'
category: Eval
direction: 模型隐私审计 · 权重谱分析
tags:
- Membership Inference Attack
- Weight Spectral Density
- Privacy Auditing
- Model Evaluation
- Generalization
one_liner: 提出用低成本权重谱指标替代高开销影子模型实现高效MIA隐私风险审计
practical_value: '- 可直接调用WeightWatcher工具的stable rank、Log alpha-Norm指标快速审计推荐/广告/Agent模型的MIA隐私泄露风险，无需训练高成本影子模型，评估效率提升1个数量级以上

  - 两类谱指标与隐私风险的相关性优于传统泛化gap，可替换现有过拟合相关的隐私校验规则，适配大规模模型批量上线前的隐私审计场景

  - 针对电商用户敏感数据训练的模型，可将谱指标加入上线合规校验pipeline，降低用户训练数据泄露的合规风险'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前主流成员推理攻击（MIA）隐私审计需训练高计算成本的影子模型，无法支撑大规模模型批量隐私校验，传统泛化指标对隐私泄露的表征能力不足，难以满足可信环境下模型发布的合规校验需求。
### 方法关键点
基于重尾自正则框架提取权重谱指标，在图像、表格分类任务上验证多个WeightWatcher谱指标与MIA隐私泄露风险的相关性，对比传统泛化gap的表征效果。
### 关键结果
stable rank与MIA整体成功率呈强正相关，低误报场景下Log alpha-Norm与MIA风险呈稳定负相关；两类指标与隐私泄露的相关性显著优于传统泛化gap，可作为低成本代理指标支撑大规模模型隐私审计。
