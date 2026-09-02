---
title: When Tokenization is Secretly Output Supervision
title_zh: 自回归语言模型中Token化本质为输出监督信号的机制研究
authors:
- Tanja Baeumel
- Josef van Genabith
- Simon Ostermann
affiliations:
- German Research Center for AI (DFKI)
- Saarland University
- Center for European Research in Trusted AI (CERTAIN)
arxiv_id: '2609.01386'
url: https://arxiv.org/abs/2609.01386
pdf_url: https://arxiv.org/pdf/2609.01386
published: '2026-09-01'
collected: '2026-09-02'
category: Training
direction: LLM训练 · Tokenization设计
tags:
- Tokenization
- Autoregressive LLM
- Supervision Signal
- Numeric Reasoning
- Model Evaluation
one_liner: 通过解耦输入输出Token化，证明自回归模型输出Token粒度决定任务难度与内部表征
practical_value: '- 电商场景下生成结构化内容（如价格、SKU编码、优惠金额）时，可采用细粒度输出Token化方案，拆分输出单元降低单步预测难度，大幅提升结构化生成准确率

  - 开展垂域LLM能力评测（如营销文案生成、数值类优惠计算、订单信息抽取能力对比）时，需对齐不同模型的输出Token化粒度，避免将任务定义差异误判为模型能力差异

  - 训练电商垂域小模型（如客服Agent、推荐理由生成模型）时，可解耦输入输出Token化，针对结构化输出单独设计输出Token粒度，平衡训练难度与推理效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有研究普遍将Token化视为LLM的输入预处理步骤，无法解释不同Token化策略下任务表现差异的底层原因；当前主流LLM评测未考虑Token化带来的监督信号差异，易导致模型能力对比结论出现系统性偏差。
### 方法关键点
- 提出Token化的输出监督新视角：自回归模型的输出Token粒度决定单步前向传播需要解决的任务粒度，直接对应损失计算的监督单元，本质上定义了模型的训练任务
- 设计2×2解耦实验：将输入与输出Token化完全拆分，设置整体（如三位数578作为单Token）/碎片化（拆分为[5,7,8]三个Token）两种粒度，控制模型架构、训练数据、优化器完全一致
- 提出最小计算假设：模型仅会表征当前输出监督要求的内容，无梯度压力时不会主动提前计算后续输出单元，通过线性探针验证模型内部表征差异
### 关键结果
在3位数加法任务上训练4层小Transformer，对比4组解耦配置：
- 输出Token化完全决定任务表现：同输出粒度的模型准确率高度接近，碎片化输出组准确率最高达100%，整体输出组最高仅85.3%，输入粒度对结果几乎无影响
- 探针实验验证最小计算假设：碎片化输出组在等号位置仅能解码第一个输出数字（准确率100%），后续数字解码准确率接近随机（≈10%）；整体输出组可同时解码所有3位数字
- 调研120篇近年*CL数值推理论文，仅9.2%报告模型的数值Token化策略，69%的跨模型对比未控制Token化粒度，结论存在系统性偏差
> 最值得记住的一句话：自回归模型的Token化不仅是输入预处理，更是定义训练任务本身的核心设计，跨模型能力对比需优先对齐输出监督粒度
