---
title: Reasoning-Token Spikes Under Prompted Untruthful Responding in Large Language
  Models
title_zh: 大模型被引导生成不实回答时推理Token数量显著上升
authors:
- Maverick Morales
- Tomáš Dominik
- Vermut Gao
- Katrina Shirey
- Paulius Rimkevičius
- Aaron Schurger
- Uri Maoz
affiliations:
- Chapman University
- University of California, Los Angeles
- California Institute of Technology
- INSERM U992, Cognitive Neuroimaging Unit
arxiv_id: '2610.10405'
url: https://arxiv.org/abs/2610.10405
pdf_url: https://arxiv.org/pdf/2610.10405
published: '2026-10-07'
collected: '2026-10-08'
category: LLM
direction: 大模型对齐 · 不实行为检测
tags:
- LLM
- Reasoning
- Alignment
- Deception Detection
- Chain-of-Thought
one_liner: 发现推理Token数量差异可作为无内容依赖的信号初步区分大模型真实与被引导的不实回答
practical_value: '- 做Agent可信性校验时，可新增推理Token计数作为轻量风控特征，无需解析CoT内容就能快速识别被引导的不实回答，适配黑盒LLM调用场景

  - 电商智能客服、商品文案生成场景下，可通过统计推理Token数量阈值快速拦截不实营销话术、虚假承诺类生成内容，降低合规风险

  - 做LLM对齐优化时，可将推理Token数量作为辅助loss信号，减少模型生成不实内容时的额外推理开销，提升真实回答的生成效率'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前依赖CoT语义内容检测大模型欺骗行为的方案，需推理轨迹可访问、可读且与计算逻辑对齐，而现有研究表明CoT输出可能逐渐不可信甚至不可获取，亟需低带宽、无内容依赖的检测信号。

### 方法关键点
基于认知负荷理论，选取推理Token生成数量作为观测信号，测试3款具备推理能力的LLM在真实回答、刻意说谎、不关心真假三类prompt引导下，回答210道覆盖分析、描述、规范推理及道德/非道德领域的选择题时的推理Token差异。

### 关键结果数字
三类模型在真实回答场景下的推理Token数量均显著低于说谎、不关心真假场景，组级差异稳定，可作为推理轨迹不可靠场景下区分真实/不实回答的候选信号。
