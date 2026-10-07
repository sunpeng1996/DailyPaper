---
title: 'Making LLMs Say What They Think: Measuring and Improving CoT-Interpretability
  Alignment'
title_zh: 度量并提升大模型思维链输出与内部推理过程的对齐度
authors:
- Yihuai Hong
- Shauli Ravfogel
- Chen Zhao
- Eunsol Choi
affiliations:
- New York University
- NYU Shanghai
arxiv_id: '2609.38972'
url: https://arxiv.org/abs/2609.38972
pdf_url: https://arxiv.org/pdf/2609.38972
published: '2026-09-29'
collected: '2026-10-07'
category: LLM
direction: 大模型推理 · CoT可信度优化
tags:
- Chain-of-Thought
- Interpretability
- Parametric Faithfulness
- Alignment
- Post-training
one_liner: 提出CIA指标量化CoT与内部推理对齐度，通过后训练可显著提升CoT可信度且不降低任务精度
practical_value: '- 做Agent推理链路可解释性审计时，可复用CIA度量框架，通过轻量线性探针检测内部推理状态与输出CoT的匹配度，避免CoT造假导致的决策不可控，比如导购Agent的推荐理由是否匹配内部召回逻辑

  - 需提升CoT可信度的场景（比如电商智能客服售后推理、广告投放理由生成），可复用文中双奖励后训练方案，用DPO/RS做微调，无需改模型结构即可提升20%左右的CoT可信度，且不损失任务效果

  - 多跳推理类任务（比如用户需求拆解、多属性商品匹配）的CoT优化优先用Rejection Sampling，数值计算类任务优先用DPO，同类型任务的优化增益可迁移，无需每个任务单独从零调优'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
CoT常被用作LLM推理过程的可信依据，但现有研究证实CoT往往不反映模型真实内部计算，甚至可被随意篡改而不影响最终输出，在电商导购、智能客服等高风险应用中，不可信的CoT会引发用户信任危机，亟需可量化的对齐度度量方案和低成本优化手段。
### 方法关键点
- 定义CIA（CoT-Interpretability Alignment）指标：通过线性探针、Tuned Lens等可解释性工具识别模型内部是否采用目标推理策略，与CoT输出中显式提到的推理策略做匹配，计算二者的宏F1作为对齐度得分，与任务正确性完全解耦。
- 后训练优化采用双奖励机制：同时纳入任务精度奖励、CoT与内部推理对齐奖励，对比了Rejection Sampling（RS）、DPO、GRPO三种轻量后训练方案的优化效果。
- 区分两类对齐优化模式：知识类推理任务靠优化CoT输出匹配原有内部逻辑，数值计算类任务靠调整内部推理路径匹配输出的CoT。
### 关键结果
在3类典型推理任务（双跳事实推理、误导性hint干预、两位数乘法）、3个主流8B/9B级开源LLM上验证：基准CIA得分仅0.448~0.759，后训练后CIA平均相对提升25.5%，同时任务精度基本保持甚至最高提升18.5%，优化增益可跨同类型任务、跨不同可解释性度量工具迁移。

最值得记住的一句话：CoT的参数可信度可量化、可低成本优化，知识类推理任务的对齐优化效果可跨任务迁移，无需每个场景单独全量训练。
