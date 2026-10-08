---
title: 'TimeBraid: Unifying Time Series and Language for Understanding and Forecasting'
title_zh: TimeBraid：统一时序与语言模态的理解与预测模型
authors:
- Xinyue Wang
- Jiacheng Pang
- Kun Zhou
- Kexin Zhang
- Defu Cao
- Fan Feng
- Faisal
- Songyao Jin
- Yan Liu
- Biwei Huang
affiliations:
- University of California San Diego
- University of Southern California
- Aether AI
arxiv_id: '2609.29792'
url: https://arxiv.org/abs/2609.29792
pdf_url: https://arxiv.org/pdf/2609.29792
published: '2026-09-23'
collected: '2026-10-08'
category: Multimodal
direction: 多模态时序建模 · 文本引导可控预测
tags:
- Time-Series-Forecasting
- Multimodal-Alignment
- LLM-Integration
- Temporal-Reasoning
- Foundation-Model
one_liner: 通过全局残差注意力对齐预训练LLM与时序基座，单模型支持双向时序文本任务与可控预测
practical_value: '- 电商销量/流量/库存预测场景可复用双阶段时序-文本对齐方案，将促销规则、运营文案、舆情等非结构化文本直接融入预测流程，替代传统手工文本特征工程

  - 全局残差注意力跨模态融合方案可直接复用现有预训练LLM与时序基座，相比传统MLP投影对齐避免破坏原生预训练能力，大幅降低训练成本

  - 推理侧可调节文本引导权重λ的设计，适配不同业务场景：大促/活动期调高权重贴合规则预期，日常平稳期调低权重符合历史时序规律

  - 训练侧asinh归一化+损失截断技巧可解决时序回归损失波动大易冲毁LLM表征的问题，落地时直接复用可大幅提升多模态训练稳定性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有跨时序-文本方案普遍通过向单模态基座添加投影层实现融合，会引入表征gap，仅能覆盖单方向任务（要么时序理解要么预测），无法同时保留预训练LLM的推理能力与时序基座的零样本预测能力，缺乏统一的双向交互框架。

### 方法关键点
- 三专家架构：推理专家用预训练LLM处理文本指令与输出，感知/预测专家用预训练时序基座处理时序信号，双塔共享时序表征即可达到三塔效果，无需额外增加参数量
- 全局残差注意力：将两个模态的表征投影到独立共享空间做联合因果注意力，输出层零初始化，训练初期等价于恒等映射，完全保留预训练模型原生能力
- 双阶段训练：第一阶段用2.2M时序-文本配对数据做模态对齐，第二阶段用4.9M多任务指令样本做SFT，覆盖理解、预测、问答等全场景任务
- 训练时引入asinh归一化+损失截断，解决时序回归损失波动大破坏LLM表征的问题；推理时支持调节文本引导权重λ，灵活适配不同场景的文本依赖度

### 关键结果
- 理解任务：6.7B版本TSAQA准确率达80.65%，仅比专项LoRA微调的8B Llama3.1低4.6pct，远超GPT-5.4的63.1%；TB-MCQ得分36.58%，接近GPT-5.4的38.5%
- 预测任务：上下文引导预测场景下CGTSF数据集MSE比最优纯时序基座低43%；Ctrl-F可控预测Top1准确率达43.33%，远高于纯时序基座的33.3%随机水平；CAF数据集CRPS达0.225，优于所有开源方案

### 核心结论
跨模态融合时，将不同模态对齐到独立共享空间，比强行把某一模态投影到另一模态的原生表征空间，更能同时保留双方的预训练能力
