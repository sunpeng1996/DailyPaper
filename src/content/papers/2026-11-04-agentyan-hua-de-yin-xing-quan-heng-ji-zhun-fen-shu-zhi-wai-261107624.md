---
title: 'Beneath the Surface: What We Overlook When We Talk About Agent Evolution'
title_zh: Agent演化的隐性权衡：基准分数之外的收益、退化与优化方案
authors:
- Xiaobo Wang
- Zimu Wang
- Siyu Ye
- Jiaqi Li
- Min Tang
- Jun Bai
- Yuling Shi
- Ruobing Wang
- Jingjing Zhang
- Chaofan Wang
affiliations:
- University of Science and Technology of China
- University of California, Berkeley
- Simple Agent Lab
- Beijing Institute for General Artificial Intelligence
- Shanghai Jiaotong University
arxiv_id: '2611.07624'
url: https://arxiv.org/abs/2611.07624
pdf_url: https://arxiv.org/pdf/2611.07624
published: '2026-11-04'
collected: '2026-11-09'
category: Agent
direction: Agent自演化 · 性能权衡与优化
tags:
- Agent Evolution
- Recursive Self-Improvement
- Harness Evolution
- Agent Evaluation
- LLM Agent
one_liner: 揭示Agent harness演化的隐性权衡，提出审计引导的AGE算法实现跨场景性能提升
practical_value: '- 业务Agent迭代不可仅依赖平均基准分，需同时监控**覆盖度增益、旧能力退化、部署成本**三个维度，避免高分Agent出现旧场景失效、调用成本过高等生产问题，适合电商导购、售后、推荐解释类Agent的效果验收

  - 可直接复用AGE的4个核心算子优化方案：select加退化感知平局规则、analyze基于行为轨迹做根因诊断、mutate做依赖闭包检查避免能力冲突、gate加成本约束准入，无需微调大模型即可提升harness层迭代效率

  - 跨场景迁移Agent时优先使用目标场景轨迹提取的针对性修改，比“仔细检查结果”类通用提示词增益高15%以上，适合不同类目、不同业务线的Agent快速适配

  - 高并发场景下可参考成本-覆盖度权衡逻辑：高可靠性Agent单次调用成本可能更高，但所需重试次数更少，整体部署成本反而更低，可用于大促等核心场景的Agent选型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent harness演化仅以基准平均分为优化目标，存在高分掩盖旧能力退化、部署成本飙升、跨场景迁移效果差等问题，无法直接落地生产，亟需厘清演化的实际收益与隐性代价，建立更可靠的演化范式。

### 方法关键点
- 针对4种主流Agent演化方法（AHE/HyperAgents/A-Evolve/GEPA），从**现象（收益/退化/成本）、泛化（同基准跨分桶/跨基准迁移）、机制（select/analyze/mutate/gate算子影响）**三个维度做系统性拆解
- 提出EvoAudit诊断框架，基于实证发现优化四个核心算子，组合为审计引导的AGE演化算法：select加退化感知平局打破规则、analyze基于行为轨迹做根因诊断、mutate做依赖闭包检查保留原有有效能力、gate加成本约束做准入控制
- 所有方案固定LLM权重，仅修改harness层（提示词、技能、编排、源码等），符合业务侧无需微调大模型的落地需求

### 关键结果
实验用τ3-Banking（97个通用任务）、Terminal-Bench 2（89个编码任务）评测，对比4种基线方法：AGE在通用任务上可靠性最高提升7.9个百分点、覆盖度提升10.3个百分点，编码任务上可靠性提升5.9个百分点、覆盖度提升3.4个百分点，同时旧能力退化率降低40%以上。

**最值得记住的一句话**：Agent演化的价值不取决于最终基准分数，而取决于它创造且能持续保留的有用行为、可接受的部署成本，以及跨场景的泛化能力。
