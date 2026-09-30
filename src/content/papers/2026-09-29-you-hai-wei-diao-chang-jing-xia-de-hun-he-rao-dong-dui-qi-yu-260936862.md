---
title: Safer Content or Firmer Refusals? A Hybrid Perturbation Defense for Alignment
  under Harmful Fine-tuning
title_zh: 有害微调场景下的混合扰动对齐防御：平衡内容安全与拒绝行为
authors:
- Muhammad Zeeshan Akram
- Mufid Kamel Marican
- Anvesh Reddy Yenugu
- Ali Zain Kaimkhani
- Minghong Fang
affiliations:
- University of Louisville
arxiv_id: '2609.36862'
url: https://arxiv.org/abs/2609.36862
pdf_url: https://arxiv.org/pdf/2609.36862
published: '2026-09-29'
collected: '2026-09-30'
category: LLM
direction: LLM安全对齐 · 有害微调鲁棒性
tags:
- LLM Safety
- Alignment
- Fine-tuning Defense
- Perturbation
- Robustness
one_liner: 融合嵌入扰动与梯度衰减的LLM对齐防御，实现内容安全与拒绝率可调权衡
practical_value: '- 若提供LLM LoRA微调服务（如电商商家自定义文案生成模型、行业Agent微调），可直接复用该框架，仅在官方对齐阶段注入防御，无需审核用户微调数据、不修改用户微调流程、无推理侧额外开销，适配隐私约束场景

  - 可参考超参数调优逻辑：业务优先保障输出内容合规（如生成推荐理由、商品文案不能涉黄涉暴）时调大嵌入扰动强度𝜌；要求Agent明确拒绝违规请求（如智能客服、导购Agent）时优先选择Booster-Only配置或调优梯度衰减强度𝜆

  - 做LLM安全评估时需同时观测「内容合规分」和「明确拒绝率」两个独立指标，避免单一指标导致的模型擦边输出、或误拒正常用户请求的问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Fine-tuning-as-a-service（FTaaS）普及后，用户上传的微调数据若混入少量有害样本，即可破坏预训练阶段的LLM安全对齐效果，且该攻击隐蔽性强，仅检测下游任务精度无法发现。传统数据过滤方案易漏检伪装的有害样本，事后修复方案需追溯攻击样本难度高，现有两种对齐阶段防御（Vaccine嵌入扰动、Booster权重梯度衰减）相互独立，未探索互补性。

### 方法关键点
- 提出VaccineBooster混合防御，在单步对齐训练中融合两种机制：先计算Booster的有害梯度衰减项，再通过Vaccine的扰动前向传播得到安全梯度，合并后更新模型参数
- 无需访问用户微调数据、不修改用户侧微调接口、无推理侧额外开销，仅需在官方对齐阶段一次性完成防御注入
- 提供两个可调超参数：𝜌控制注意力层嵌入扰动强度，𝜆控制权重梯度衰减强度，可灵活调整安全策略

### 关键实验结果
基于Llama-2-7B基模型、BeaverTails对齐数据集，模拟全有害样本投毒微调攻击，对比Vaccine-Only、Booster-Only基线：
- VaccineBooster取得最低OpenAI moderation score 0.315，内容安全性最优，攻击后拒绝率20%
- Booster-Only保留最高攻击后拒绝率50%，适合需要明确拒答的场景
- 消融实验显示增大𝜌可显著降低违规内容检出率，𝜌=4时moderation score低至0.221

### 核心结论
对齐防御存在内容安全与明确拒绝率的固有权衡，无通用最优配置，仅通过调优两个超参数即可覆盖大部分业务场景，无需切换不同防御方案
