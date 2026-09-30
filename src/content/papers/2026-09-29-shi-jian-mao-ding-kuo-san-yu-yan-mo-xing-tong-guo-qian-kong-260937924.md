---
title: 'Time-Anchored Diffusion Language Models: Latent-Space Caching for Fast Generation'
title_zh: 时间锚定扩散语言模型：通过潜空间缓存实现快速生成
authors:
- Joel Anto Paul
- Litu Rout
- Aditya Akella
- Sanjay Shakkottai
affiliations:
- University of Texas at Austin
arxiv_id: '2609.37924'
url: https://arxiv.org/abs/2609.37924
pdf_url: https://arxiv.org/pdf/2609.37924
published: '2026-09-29'
collected: '2026-09-30'
category: LLM
direction: 扩散语言模型 · 潜空间缓存推理加速
tags:
- Diffusion Language Model
- Latent Caching
- Inference Acceleration
- Post-training
- Pretraining
- Model Optimization
one_liner: 提出无需显式锚点标签的时间锚定扩散框架，通过潜空间缓存大幅提升扩散语言模型推理吞吐量
practical_value: '- 生成式推荐/电商文案生成场景如果用Diffusion LLM做基座，可直接复用TADM:Post-train方案，仅需微调3M左右参数的fusion模块，就能获得49%~79%的推理吞吐量提升，且几乎不损失生成质量，落地成本极低

  - 架构拆分思路可迁移到所有多步迭代生成场景（比如多轮refine的推荐理由生成、Agent思考链生成）：将模型拆为计算量占比高的全局语义建模模块和轻量的当前步解码模块，全局模块定期执行并缓存结果，大幅降低重复计算

  - 可调的锚点刷新间隔K可直接适配不同业务的SLA要求：对 latency 敏感的广告实时文案生成场景调大K，对生成质量要求高的商品长描述生成场景调小K，灵活平衡效果与成本

  - 自监督锚点学习无需额外标注重要token，业务场景不需要额外构造标注数据集，进一步降低落地门槛'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
扩散语言模型（DLM）支持双向注意力、并行生成、迭代纠错，在推理、代码、生成任务上表现逼近自回归LLM，但多轮去噪步骤需要重复执行完整模型前向，推理成本远高于自回归解码，现有KV缓存方案是局部层级的，未针对跨时间步的语义复用做优化，无法充分降低冗余计算。

### 方法关键点
- 核心观察：锚点表征编码序列的语义意图、全局结构、中间规划等持久属性，跨相邻扩散步语义仍然有效，仅隐层表征轻微过时，可通过当前步状态修正
- 架构拆分：模型拆为4组件：轻量共享网络、重计算锚点网络、极小门控fusion模块、轻量去噪网络；锚点网络每K步执行一次，结果存入潜空间缓存，其余步仅执行共享+fusion+去噪网络
- 两套落地方案：TADM:Post-train适配已预训练的DLM，冻结主干仅微调3.1M参数的fusion模块；TADM:Pretraining在预训练阶段引入缓存复用逻辑，直接学习可缓存的潜表征
- 推理逻辑：锚点缓存每K步刷新一次，fusion模块自适应融合缓存锚点与当前步表征后输入去噪网络，K值可灵活调整质量-计算tradeoff

### 关键实验
- TADM:Post-train基于DiffusionGemma-26B，在GSM8K、HumanEval、LiveCodeBench、AIME26等数学/代码/STEM基准上，吞吐量提升49%~79%，精度浮动在±1pp以内
- TADM:Pretraining在OpenWebText上训练，对比ADLM吞吐量最高提升73%，Transformer层计算量降低38%，MAUVE等生成质量指标与ReMDM相当

### 核心结论
迭代式生成模型中，语义级持久潜表征的跨步复用，是比局部层级KV缓存更高效的推理加速路径。
