---
title: 'Gathered, Not Admitted: How Attention Brings a Latent Variable into Verbalizable
  Form'
title_zh: 注意力如何将隐变量转化为LLM可表述表征：无需准入仅需聚合
authors:
- Parsa Mazaheri
affiliations:
- University of California, Santa Cruz
arxiv_id: '2608.15022'
url: https://arxiv.org/abs/2608.15022
pdf_url: https://arxiv.org/pdf/2608.15022
published: '2026-08-14'
collected: '2026-08-18'
category: LLM
direction: 大语言模型可解释性 · 工作空间机制
tags:
- LLM Interpretability
- Attention Mechanism
- Verbalizable Workspace
- Jacobian Lens
- Activation Patching
one_liner: 推翻隐变量准入工作空间假设，证明注意力中层聚合生成LLM可表述表征
practical_value: '- 做LLM4Rec/Agent推理路径调试时，可复用Jacobian lens方法观测任务相关隐变量的可见性变化，定位关键推理层

  - 优化长上下文推荐/多轮Agent的信息保留时，优先在模型0.55-0.66分数深度层做信息注入/修正，效果比浅层高至少17倍

  - 做模型行为归因时，不能仅依赖表征可见性判断因果贡献，相同可见度的不同组件对输出的影响差异可达7.4倍，必须结合干预实验验证'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
此前研究发现LLM存在可表述工作空间，任务需要灵活复用的隐变量在其中可见度更高，学界普遍假设存在准入门控决定隐变量是否进入工作空间，该机制从未被验证，且直接影响了当前很多工作空间导向的模型改造设计。

### 方法关键点
- 设计JGateBench基准，5组任务臂共享完全相同的上下文，仅任务指令不同，控制提示格式与准确率匹配，排除难度、提示结构等干扰因素
- 用Jacobian lens测量各层隐变量的可见性，结合激活补丁实验定位信息传输路径，区分「信息安装」与「信息存活」两个过程
- 覆盖Qwen3.6-27B、Gemma-4-31B、Llama-3.1-8B等4个不同架构的开源指令微调模型验证结论通用性

### 关键结果
- 任务需求可提升隐变量可见度+0.05百分位，即使是无需使用隐变量的控制组，也能用同一个线性映射解码出隐变量，直接推翻准入门控假设
- 隐变量由注意力在0.55-0.66分数深度的中层窗口聚合，传输效率比浅层高至少17倍，该窗口内MLP无正向贡献，且聚合强度随任务需求提升7倍，窗口位置跨架构一致
- 相同可见度的不同组件对输出的因果贡献差异可达7.4倍，表征可见度无法直接等同于对输出的实际影响

**最值得记住的一句话**：LLM的可表述表征不是靠门控准入的，是注意力按需聚合生成的，表征可见性不等于因果贡献。
