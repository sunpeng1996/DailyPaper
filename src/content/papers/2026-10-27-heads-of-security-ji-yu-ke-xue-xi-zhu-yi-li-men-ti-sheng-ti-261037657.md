---
title: 'Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness'
title_zh: Heads of Security：基于可学习注意力门提升提示注入鲁棒性
authors:
- Igor Shilov
- Xiaoxue Yang
- Alexander Panfilov
- Evgenii Kortukov
- Matthieu Meeus
- Peter Romov
- Wojciech Samek
- Jonas Geiping
- Yves-Alexandre de Montjoye
affiliations:
- Imperial College London
- Tübingen AI Center
- ELLIS Institute Tübingen
- Max Planck Institute for Intelligent Systems
- Fraunhofer HHI
arxiv_id: '2610.37657'
url: https://arxiv.org/abs/2610.37657
pdf_url: https://arxiv.org/pdf/2610.37657
published: '2026-10-27'
collected: '2026-10-28'
category: LLM
direction: LLM安全 · 提示注入防御
tags:
- Prompt Injection
- Attention Mechanism
- LLM Security
- Instruction-Data Separation
- Agent Security
one_liner: 通过为每个注意力头学习信任通道权重，实现低损耗高鲁棒的提示注入防御
practical_value: '- 电商导购/搜索推荐Agent可直接复用HoS架构：将系统指令、用户合法Query标记为TRUSTED，外部检索的商品评论、商家描述、第三方UGC标记为UNTRUSTED，几乎不损失推理能力的前提下大幅降低提示注入风险

  - 训练成本极低，仅需训练万级别的注意力门参数，远低于LoRA/全参数微调成本，业务侧可快速适配现有开源LLM，无需重新训练大模型

  - 可复用信任通道划分思路，对Agent工具返回结果、用户自定义内容等不同来源token设置差异化注意力权重，避免恶意内容诱导模型生成虚假优惠、泄露用户隐私等违规行为'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM及Agent大量接入外部数据与工具，间接提示注入攻击风险持续升高，现有防御方案存在明显缺陷：微调类方案（如SecAlign）在少样本、多轮对话场景性能下降严重，架构修改类方案（如ASIDE）会导致工具调用能力退化，且开源模型的注入防御能力远落后于闭源模型，亟需低性能损耗、高鲁棒性的低成本防御方案。
### 方法关键点
- 为Transformer每层每个注意力头引入可学习的通道注意力门，将token划分为TRUSTED（系统/用户指令、模型自身输出）、UNTRUSTED（第三方内容、工具返回结果）、TEMPLATE（聊天模板token）三类，门控参数控制不同通道间的注意力权重
- 仅训练万级别的门控参数，Llama-3.3-70B仅需训练4.6万个参数，远低于微调方案的数百万/数十亿参数规模
- 采用与SecAlign相同的DPO训练目标，偏好数据对为「用户指令+注入内容组合下，优先选择响应用户指令、忽略注入内容的输出」
### 关键实验
对比基线为SOTA微调防御SecAlign++、架构级防御ASIDE，测试模型为Llama-3.3-70B-Instruct、GPT-OSS-20B：
- 攻击鲁棒性：黑盒RL-Hammer攻击下，GPT-OSS-20B原模型ASR为97%、SecAlign为85%，HoS仅为10%；Llama-3.3-70B原模型ASR为99%、SecAlign为82%，HoS仅为1%；白盒Claudini攻击下，HoS达到相同ASR需要3倍以上计算量
- 性能保留：5-shot MMLU-Pro上，HoS准确率67%接近原模型的68%，SecAlign仅为59%、ASIDE仅为52%；多轮对话场景HoS性能几乎无下降，SecAlign性能下降最高达57%
- Agent场景：AgentDojo等基准上，HoS工具调用utility接近原模型，ASR降至1%以下，ASIDE utility仅为10%几乎不可用

> 核心结论：通过约束注意力机制而非全量微调模型行为，即可实现兼顾鲁棒性与性能的指令-数据分离，是当前成本最低、效果最好的开源LLM提示注入防御方案之一
