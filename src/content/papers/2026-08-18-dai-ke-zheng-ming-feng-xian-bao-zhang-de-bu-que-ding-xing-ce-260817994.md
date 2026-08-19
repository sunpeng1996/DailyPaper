---
title: 'Judge, Retrieve, or Abstain: Uncertainty-Guarded LLM Judging with Provable
  Risk Guarantees'
title_zh: 带可证明风险保障的不确定性感知LLM评测框架：判定、检索或弃权
authors:
- Sher Badshah
- Ali Emami
- Hassan Sajjad
affiliations:
- Dalhousie University
- New York University Abu Dhabi
- Emory University
arxiv_id: '2608.17994'
url: https://arxiv.org/abs/2608.17994
pdf_url: https://arxiv.org/pdf/2608.17994
published: '2026-08-18'
collected: '2026-08-19'
category: Eval
direction: LLM评测 · 风险可控的选择性评估
tags:
- LLM-as-Judge
- Uncertainty Quantification
- RAG
- Conformal Prediction
- Risk Control
one_liner: 提出双模式路由的LLM-as-judge框架，严格控制判决错误率同时大幅提升覆盖度
practical_value: '- 做Agent工具调用路由时可复用双阈值校准逻辑：用小样本标注集校准不确定性阈值，不确定时触发RAG/工具调用，既降低调用成本又保障输出正确率符合业务要求

  - 生成式推荐/广告的输出内容审核场景，可借鉴Clopper-Pearson区间的风险控制方法，将bad case率严格控制在预设阈值内，避免违规内容流出

  - 线上服务的性能优化可参考自适应调用逻辑：对高置信度场景直接用小模型推理，低置信度才调用大模型/外部工具，平衡推理成本与效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM-as-judge已经成为大模型输出规模化评测的标准方案，但客观事实类评测面临两大核心痛点：仅用参数知识容易出现幻觉/知识不足导致误判，全量调用检索工具又会增加额外计算成本，且两种方案都无法对接受判决的错误率提供正式的可控保障，错误评测会传导到下游业务决策引发损失。

### 方法关键点
- 双模式路由框架：模式1用LLM参数知识直接评测，输出判决和基于预测熵的不确定性得分，得分低于校准阈值则直接接受判决；得分超阈值则触发模式2，调用网页检索补充证据后重新评测，二次得分低于阈值则接受，否则弃权转人工审核
- 风险校准方法：在带标注的小样本校准集上，基于Clopper-Pearson二项分布上置信界，联合搜索两个模式的最优阈值，在保障错误发现率（FDR）低于用户指定的α水平的前提下最大化接受判决的覆盖度
- 理论证明：双模式路由下的失败指标依然满足独立同分布伯努利假设，因此有限样本下的FDR控制保障依然成立，无需额外分布假设

### 关键结果
在4个开放域QA数据集（TriviaQA、Natural Questions、HotpotQA、PopQA）上测试4个不同规模的LLM法官，对比单模式基线：1）所有配置下实测FDR均低于预设目标α，风险控制效果稳定；2）自适应检索比单模式基线覆盖度最高提升75个百分点（如NQ-Open数据集上Qwen3-8B法官覆盖度从7%提升至82%）；3）检索结果漂移3个月后，FDR依然保持低于目标阈值，鲁棒性良好。

**最值得记住的一句话**：通过小样本校准的不确定性路由，完全可以在不牺牲风险可控性的前提下，大幅降低LLM应用的推理和工具调用成本。
