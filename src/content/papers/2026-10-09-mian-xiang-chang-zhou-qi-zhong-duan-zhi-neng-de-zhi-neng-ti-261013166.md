---
title: Scaling Agentic Data for Long-Horizon Terminal Intelligence
title_zh: 面向长周期终端智能的智能体数据规模化生成方法
authors:
- Shun Zou
- Ziyu Ma
- Yi Zou
- Yong Wang
- Lin Chen
- Zehui Chen
- Guanhua Chen
- Xiangxiang Chu
- Feng Zhao
affiliations:
- University of Science and Technology of China
- Alibaba Group AMAP
- Southern University of Science and Technology
arxiv_id: '2610.13166'
url: https://arxiv.org/abs/2610.13166
pdf_url: https://arxiv.org/pdf/2610.13166
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: 智能体 · 长周期任务训练数据合成
tags:
- Agent
- Long-horizon Task
- Data Synthesis
- SFT
- Terminal Agent
one_liner: 提出自动化长周期终端智能体数据合成引擎，仅用3K轨迹SFT即实现全基准性能提升
practical_value: '- 电商/运营类Agent训练数据构造可复用「独立挑战者校验」流程：先用非构造方的Agent跑通候选任务，定位被提前简化的核心步骤，避免训练数据存在信息泄露、导致Agent上线后无法处理真实场景问题

  - 长链路任务Agent训练可复用「渐进式任务扩展」思路：在同一目标下逐步新增阶段要求（如导购Agent从选品→下单→售后的全链路扩展），让Agent学会基于前序结果做连贯决策

  - 优先提升单条训练轨迹的信息密度而非盲目堆数据：仅3K条高质量长周期轨迹即可实现10%+的跨场景性能提升，数据效率是普通短轨迹数据集的10倍以上

  - 可直接复用其27种智能体行为模式分类，作为电商Agent（如客服、运营、导购）的训练目标和评估维度，覆盖探索、反馈迭代、结果校验等核心能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有终端智能体训练数据多为短轨迹，仅能支撑单步操作、工具调用能力学习，无法覆盖长周期任务中探索、策略迭代、跨阶段结果复用、错误校验等连贯行为模式；人工构造长周期任务时易提前简化核心工作，导致Agent训练时跳过关键决策环节，无法迁移到真实复杂场景。

### 方法关键点
- 挑战引导的长周期合成：从真实专业任务出发，用独立的挑战者Agent执行候选任务，对比预期与实际轨迹定位被简化的核心步骤，重构环境确保Agent必须完成所有核心决策环节
- 渐进式周期扩展：在同一目标下逐步新增任务要求，新增工作严格依赖前序执行结果和反馈，让核心行为模式贯穿全任务阶段
- 产出的训练轨迹平均包含8.6种核心智能体行为模式，覆盖25个专业领域

### 关键结果数字
- 构造了1.5K任务环境、2.85K训练轨迹组成的TerminalHorizon-3K数据集，轨迹平均交互轮次达52.8，是现有公开终端Agent数据集的3~10倍
- 对Qwen3.5-27B做SFT后，Terminal-Bench 2.0/2.1分别提升14.2%/13.85%，真实生产环境AutomationBench通过率提升11.7%，12个测试基准全量超越基线
- 仅用同类方法十分之一的训练数据量，性能即可超过同类SOTA模型3%

### 最值得记住的一句话
高质量长周期智能体轨迹的信息密度远高于短轨迹，少量精准构造的训练数据就能带来跨场景的性能提升，远优于盲目堆砌低质量短轨迹数据。
