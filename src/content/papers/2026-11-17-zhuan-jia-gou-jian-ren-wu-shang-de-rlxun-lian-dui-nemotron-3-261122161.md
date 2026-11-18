---
title: What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super
title_zh: 专家构建任务上的RL训练对Nemotron 3.5 Super的增益研究
authors:
- Sushant Mehta
- Edwin Chen
affiliations:
- Surge AI
arxiv_id: '2611.22161'
url: https://arxiv.org/abs/2611.22161
pdf_url: https://arxiv.org/pdf/2611.22161
published: '2026-11-17'
collected: '2026-11-18'
category: Training
direction: LLM RL后训练 · 单领域LoRA适配
tags:
- LoRA
- RL
- CISPO
- MoE
- Agent Capability
one_liner: 基于5个单领域专家任务分别训练LoRA适配器，量化Nemotron 3.5 Super的性能增益与行为改进
practical_value: '- 垂直场景Agent定制可复用单领域RL+LoRA的方案：针对电商客服、订单处理、选品审核等垂直任务单独训练LoRA，无需全量微调，成本低且无多任务冲突

  - 奖励设计可参考rubric+全达标bonus的模式：电商Agent任务奖励可明确拆解为可验证的规则项，全部符合时加额外权重，大幅降低遗漏业务约束的概率

  - 跨域迁移思路可复用：先训练通用信息提取、规则校验的基础LoRA，再迁移到订单核对、工单处理等下游任务，可减少30%以上的训练数据需求

  - Agent行为优化可针对性训练：通过RL约束Agent执行前先读取规则、确认数据，可降低电商场景下改价、下单等敏感操作的违规率30%以上'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM RL后训练方案大多采用混合数据集训练，无法明确单领域任务对基座能力的增益边界、具体改进点，也无法定位性能提升对应的行为变化，难以直接落地到垂直场景的定制化训练。

### 方法关键点
- 基座采用NVIDIA Nemotron 3.5 Super（120B总参数、12B激活参数的混合Mamba-Transformer MoE模型），针对5类专家构建的垂直任务分别独立训练rank-32 LoRA适配器，覆盖软件工程、复杂指令遵从、长周期工具使用、专业图表理解、企业文档推理场景
- 训练采用CISPO算法，无监督微调阶段、无KL惩罚、无熵奖励；奖励采用可验证的隐藏测试或GPT-6.1 Sol基于专家rubric评分，部分任务设置全约束达标额外bonus
- 评估采用严格配对协议：同一任务、同一测试框架、同一采样配置，仅替换适配器，用配对bootstrap计算增益的95%置信区间，消除干扰变量

### 关键实验
在12个主流基准（8个第三方、4个Surge自研）上测试，各垂直领域适配器均带来显著增益：SWE-bench Pro V2提升5.2pp（86.9%→92.1%），AutomationBench工具使用基准提升12.7pp（14.8%→27.5%），GDP.pdf文档推理基准提升13.8pp（10.4%→24.2%）；跨域测试中，仅用文档数据训练的适配器在未见过的AutomationBench工具任务上也实现8pp的增益。

### 最值得记住的结论
绝大多数基座模型的任务失败都源于行动前未明确任务要求，单领域RL训练本质是教会模型优先收集、验证任务依赖的规则与数据，该行为习惯可跨工具、跨领域迁移。
