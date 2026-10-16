---
title: 'Twice Upon a Time: Complementary Representations for Time-Series Reasoning'
title_zh: 基于双互补视觉表示的通用时间序列语言模型推理框架
authors:
- Hedi Zisling
- Liran Nochumsohn
- Ilan Naiman
- Mihir Parmar
- Omri Azencot
affiliations:
- Ben-Gurion University
- Google
arxiv_id: '2610.22327'
url: https://arxiv.org/abs/2610.22327
pdf_url: https://arxiv.org/pdf/2610.22327
published: '2026-10-15'
collected: '2026-10-16'
category: LLM
direction: 时序大模型 · 互补表示推理
tags:
- Time-Series LLM
- Multimodal Fusion
- LoRA
- Vision-Language Model
- Time Series Reasoning
one_liner: 结合线图与归一化延迟嵌入双视图，大幅提升通用时间序列语言模型推理性能
practical_value: '- 处理电商时序数据（用户行为序列、商品销量、流量波动等）时可复用互补表示思路：同时保留原始数值可视化视图+归一化后聚焦时序结构的视图，兼顾数值计算和趋势/周期挖掘需求

  - 多模态LLM融合可参考双编码器+分层注入架构：不同视图用专属编码器提取特征，除输入层token拼接外，将中间层特征注入LLM早期层，大幅提升融合效率

  - 微调领域特定LLM时可复用两阶段LoRA训练策略：先对齐新增模态与LLM语义空间，再做指令微调，冻结主干大幅降低训练成本和数据量要求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有时间序列语言模型（TSLM）普遍采用单一表示，固定的归纳偏置无法同时满足数值读取（需保留原始刻度）和时序结构推理（需归一化消去振幅偏移干扰）两类需求，导致通用推理性能受限，亟需更灵活的表示设计。

### 方法关键点
- 双互补视觉视图设计：原始线图保留绝对数值、刻度等测量框架信息；归一化延迟嵌入将时序重构成相空间轨迹，消去正振幅缩放和偏移干扰，暴露隐含时序结构
- 双编码器架构：线图用Qwen3-VL原生SigLIP-2编码器，延迟嵌入用DINOv3编码器，分别编码后压缩为230个、64个视觉token拼接输入LLM
- 多层特征融合：采用DeepStack机制将两个视图的中间层特征分别注入LLM前三层的对应token位置，强化跨视图交互
- 两阶段LoRA训练：第一阶段冻结LLM和线图编码器，微调DINOv3的LoRA和投影层对齐延迟模态；第二阶段冻结视觉通路，微调LLM的LoRA做时序推理指令微调

### 关键实验结果
在TSRBench、TSExam、ChatTS三个权威时序推理基准测试，对比Qwen3-VL-8B、ChatTS-14B、TS-Reasoner-7B等同规模基线：
1. 双视图模型TSRBench准确率达53.2%，较单一线图视图提升8个百分点，远超最强专用TSLM基线的36.7%，接近GPT-5（文本+视觉输入）的55.6%
2. TSExam准确率89.9%，多变量ChatTS数值对齐准确率86.8%，均优于所有同规模基线

最值得记住的结论：单一表示的固定归纳偏置无法覆盖通用时序推理的多元需求，互补表示是提升通用时间序列语言模型性能的高效设计原则
