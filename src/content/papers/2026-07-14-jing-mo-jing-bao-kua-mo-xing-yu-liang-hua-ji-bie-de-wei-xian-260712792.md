---
title: 'Silent Alarm: A J-Space Protocol for Comparing Danger Recognition Across Models
  and Quantization Levels'
title_zh: 《静默警报：跨模型与量化级别的危险识别J空间评估协议》
authors:
- Roman Prosvirnin
- Victor Minchenkov
- Alexey Soldatov
- Vladimir Bashun
arxiv_id: '2607.12792'
url: https://arxiv.org/abs/2607.12792
pdf_url: https://arxiv.org/pdf/2607.12792
published: '2026-07-14'
collected: '2026-07-15'
category: Eval
direction: LLM 安全鲁棒性评估
tags:
- LLM Safety
- Jailbreak Robustness
- Quantization
- Jacobian Space
- Model Evaluation
one_liner: 提出无需外部LLM评审的J空间内部安全评估协议，支持跨模型、量化级的越狱鲁棒性对比
practical_value: '- 部署LLM导购/文案生成Agent前，可复用JADR协议做本地安全鲁棒性检测，无需依赖外部LLM judge，降低评估成本

  - 对LLM做INT4/INT8量化压缩时，可通过SafetyAUC指标量化安全能力衰减，平衡推理性能与合规风险

  - 做LLM对齐微调时，可对比微调前后J空间表征差异，定位安全机制变化，避免对齐失效'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有越狱鲁棒性评估依赖外部LLM-as-judge，受评分流程影响大，仅能捕捉表层响应行为，无法直接探测模型内部安全机制的隐性脆弱性，也难以公平对比不同模型、量化版本的安全能力。

### 方法关键点
JADR评估协议在模型生成首个响应token前，基于Jacobian空间（J空间）的可解释概念表征，逐prompt、逐层统计Top-k J空间token，按6类行为场景维度分组，对比危险样本与安全样本的表征差异；计算完全基于待评估模型的激活值本地完成，无需外部评审模型，采用SafetyAUC指标结合bootstrap置信区间输出最终评估结果。

### 关键结果数字
覆盖6款模型（Qwen3全系列、Gemma 2 9B）的BF16/INT8/INT4三个量化级别验证，SafetyAUC可统计显著区分强弱内部安全机制的模型，准确捕捉不同量化策略对安全能力的差异化影响，评估结果与StrongREJECT行为评估结果一致。
