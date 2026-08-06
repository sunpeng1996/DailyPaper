---
title: 'Revealed Rationality: Label-Free Evaluation and Regularization from Representation
  Theorems'
title_zh: 显示理性：基于决策论表征定理的无标注模型评估与正则化
authors:
- Isaiah Andrews
affiliations:
- Massachusetts Institute of Technology
- NBER
arxiv_id: '2608.05015'
url: https://arxiv.org/abs/2608.05015
pdf_url: https://arxiv.org/pdf/2608.05015
published: '2026-08-05'
collected: '2026-08-06'
category: Training
direction: LLM训练与评估 · 无标注正则
tags:
- Rationality
- Label-free Evaluation
- Regularization
- LLM Alignment
- Revealed Preference
one_liner: 基于决策论表征定理实现无标注LLM理性合规性检验与连续正则惩罚
practical_value: '- 开发导购/决策类Agent时，可复用文中3种理性检验（概率一致性、偏好合理性、预期效用一致性）作为无标注评测指标，降低人工标注成本，避免Agent出现可被套利的决策漏洞（如定价、选品偏好前后矛盾被薅羊毛）

  - 训练决策类LLM/Agent时，可将文中的连续惩罚项（Dutch book损失、1-CCEI、1-E）作为辅助正则项加入训练目标，无需额外标注就能提升Agent决策的逻辑自洽性，减少推荐、定价、权益计算场景的前后矛盾错误

  - 做推荐系统用户偏好建模时，可复用Afriat定理的GARP检验逻辑，校验用户历史行为的理性程度，过滤非理性行为噪声，提升用户兴趣画像的准确性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM及Agent已广泛应用于信念表达、选项排序、动作推荐等场景，但现有研究证实LLM普遍存在概率判断矛盾、偏好传递失效等理性违规问题，可被构造Dutch book、money pump直接套利；现有评估与训练方法大多依赖外部标注或人工反馈，成本高且无法覆盖理性约束的全部隐含要求。

### 方法关键点
- 基于决策论表征定理「行为满足公理 ↔ 可被良定义目标合理化」的双向等价特性，设计完全无外部标注的理性检验方案，仅需模型对合成选择问题的响应即可计算违规程度。
- 落地三类可直接复用的检验框架：1）概率一致性：基于de Finetti定理，通过线性规划计算可套利的Dutch book规模作为连续惩罚；2）偏好合理性：基于Afriat定理，用1-CCEI（临界成本效率指数）作为偏好违反GARP公理的连续惩罚；3）不确定场景决策合理性：基于Echenique-Saito定理，用1-E作为主观预期效用违反SARSEU公理的连续惩罚。
- 所有惩罚项均可在多项式时间内计算，惩罚为0时模型行为完全符合对应理性标准，无遗漏检验风险。

### 关键结果
本研究为理论框架类工作，无自研实验，引用现有实证结果验证可行性：GPT-3.5在四类预算分配任务上平均CCEI超过0.997，表现优于人类受试者；概率一致性指标可正向预测LLM预测的ground truth准确率，加入一致性正则可显著提升LLM概率推理能力。

### 最值得记住的结论
理性一致性检验是现有标注依赖的训练/评估方法的补充而非替代，完全符合理性公理仅能保证行为可被某个目标合理化，无法保证该目标与业务需求对齐。
