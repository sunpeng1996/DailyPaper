---
title: 'Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models
  Catch Up Where Imitation Fails'
title_zh: 协同演化Agent Harness与模型：On-Policy修正解决模仿学习失效问题
authors:
- Zhou Yu
- Bin Bi
- Shiva Kumar Pentyala
- Shubham Mehrotra
- Sougata Chaudhuri
- Shilpa Bhagavath
- Zeyuan Chen
- Ran Xu
- Phil Mui
- James Zhu
affiliations:
- Salesforce AI
arxiv_id: '2609.09134'
url: https://arxiv.org/abs/2609.09134
pdf_url: https://arxiv.org/pdf/2609.09134
published: '2026-09-08'
collected: '2026-09-09'
category: Agent
direction: Agent 与LLM协同优化 · Harness演化
tags:
- Agent Harness
- LoRA
- On-Policy Correction
- SFT
- Co-Evolution
one_liner: 提出On-Policy专家修正协同演化pipeline，解决弱模型在演化Harness下模仿强模型的性能退化问题
practical_value: '- 做领域定制Agent时避坑：不要在已优化好的Harness下直接用强模型全轨迹SFT弱模型，会破坏模型-Harness适配性导致性能下降

  - 可复用On-Policy修正思路：仅在弱模型自身生成的失败轨迹上，用专家修正单步错误点，保留原生规划风格，不破坏现有适配即可提升性能

  - 电商客服/运营Agent迭代时，可将Harness演化和LoRA轻量微调结合，用文中的协同演化pipeline，让小模型接近大模型效果，大幅降低推理成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
Agent性能由底层LLM和Harness（系统Prompt、工具集、上下文管理脚手架等）共同决定，现有Harness自动演化技术可让小模型在领域任务上接近前沿大模型效果，成本仅几分之一。但Harness演化和LoRA等轻量微调两个优化杠杆如何协同还不明确，直接模仿强模型轨迹的常规SFT方案在演化后的Harness下反而会让弱模型性能退化，需要解决该冲突。

### 方法关键点
- 先针对弱模型演化出适配的Harness，验证强专家模型可直接复用该Harness获得更高性能，明确弱模型性能天花板
- 放弃全轨迹模仿方案，设计On-Policy专家修正pipeline：用元Agent定位弱模型自身轨迹的失败单步，仅让专家重写该步，保留模型原生规划分布，避免破坏Harness适配
- 用修正后的轨迹做LoRA SFT，实现Harness和模型能力的协同增益

### 关键实验
在7个企业级Agent任务（薪资审计、预算审批、股票告警等）上测试：未演化Harness的弱Qwen3-Coder-30B性能为29.2%；Harness演化后性能提升到78.0%；直接用强模型全轨迹SFT弱模型，性能骤降到63.1%（平均降14.9个点，最高降29.9个点）；用On-Policy修正方案SFT后，性能进一步提升到79.7%，同时规划类失败率仅从1.1%升到1.8%，几乎无适配损失。

### 核心结论
在Harness-模型协同优化场景下，只有尊重模型与适配后Harness原生匹配关系的监督信号才有效，盲目模仿强模型全轨迹反而会抵消Harness优化的收益
