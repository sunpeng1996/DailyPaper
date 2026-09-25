---
title: 'KernelOPT: Dispatch-Aware Agentic Search for GPU Kernel Optimization'
title_zh: KernelOPT：感知编译器调度的多Agent GPU内核优化系统
authors:
- Aheli Poddar
- Sanskar Prasad
- Arindam Samanta
- Subha Chakraborty
- Vishal Goyal
- Rohit Singh Rathaur
affiliations:
- Red Hat
arxiv_id: '2609.30059'
url: https://arxiv.org/abs/2609.30059
pdf_url: https://arxiv.org/pdf/2609.30059
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: Agent 多智体GPU内核性能优化
tags:
- MultiAgent
- LLM4Code
- GPU Optimization
- Triton
- LangGraph
one_liner: 提出感知编译器调度的多Agent GPU内核优化框架，附带四级验证保证端到端正确性与性能收益
practical_value: '- 可复用四级验证级联设计：静态校验→多种子正确性→模型级精度校验→性能门控，适配推荐/广告大模型算子优化场景，避免局部优化导致的端到端精度/性能回退。

  - 多Agent协作架构可迁移：基于硬件profiling反馈的规划-执行-总结迭代框架+停滞检测逻辑，可直接用于向量召回内核、Transformer推理算子的自动化调优Agent开发。

  - 分层优化思路可复用：优先保留cuBLAS/cuDNN等高度优化的基础库，仅针对自定义Triton子内核做优化，大幅降低大模型推理加速的开发成本，适合电商推荐大模型部署场景。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
PyTorch Inductor默认生成的GPU内核性能远低于专家手写实现，现有LLM辅助内核优化方案仅针对独立内核优化，未尊重编译器已有的调度决策，也缺乏端到端的精度与性能校验，容易出现局部提速但整体性能下降、数值精度不符合要求的问题，无法直接用于生产级模型优化。
### 方法关键点
- 架构设计：基于LangGraph实现5个Agent协作，识别并保留cuBLAS/cuDNN等厂商高度优化的库调用，仅针对编译器生成的Triton子内核做优化，避免无效算力浪费。
- 四级验证级联：依次做静态有效性校验、多种子数值正确性校验、模型级精度校验（含float64 fallback逻辑区分数值噪声和算法错误）、性能门控（要求端到端速度不低于基线的97%），不满足则自动回退到编译器基线。
- 搜索机制：采用多样性感知的UCB beam搜索平衡探索与利用，新增经验记忆模块存储优化经验，搭配停滞检测器避免搜索方向趋同。
### 关键实验结果
在250个KernelBench问题上对比torch.compile基线，Level1（单算子）几何平均提速1.40×，Level2（复合算子）1.15×，Level3（完整模型）1.07×，最高单内核提速88.63×；消融实验显示去掉任意核心组件，优化成功率下降74%以上。
### 最值得记住的结论
LLM驱动的程序优化系统应当与编译器协同，利用其结构注解而非绕过它，才能兼顾优化效率与生产可用性。
