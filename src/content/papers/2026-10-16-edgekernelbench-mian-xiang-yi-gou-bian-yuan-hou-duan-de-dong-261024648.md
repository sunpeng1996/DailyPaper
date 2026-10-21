---
title: 'EdgeKernelBench: Unified LLM-Driven Kernel Generation for Edge Backends'
title_zh: EdgeKernelBench：面向异构边缘后端的LLM驱动内核生成基准与优化框架
authors:
- Yuhua Zheng
- Xueyi Chen
- Xinze Zou
- Xin Li
- Haoji Hu
- Huan Wang
affiliations:
- Westlake University
- Zhejiang University
arxiv_id: '2610.24648'
url: https://arxiv.org/abs/2610.24648
pdf_url: https://arxiv.org/pdf/2610.24648
published: '2026-10-16'
collected: '2026-10-21'
category: Agent
direction: Agent 边缘端LLM内核生成优化
tags:
- LLM Agent
- Kernel Generation
- Edge Computing
- Benchmark
- Intermediate Representation
one_liner: 提出边缘内核生成基准与分层优化Agent，大幅提升LLM生成内核的正确性与运行效率
practical_value: '- 分层Agent架构可直接复用：将复杂优化任务按抽象层级拆分，每层Agent仅负责对应层级决策，降低单Agent上下文压力，可迁移到推荐系统多阶段优化（召回/粗排/精排/重排）等场景，跨层通过统一中间表示传递信息。

  - 统一IR解耦思路可复用：定义与平台无关的上层中间表示，下层通过适配器适配不同硬件/ runtime，可解决跨端（APP/小程序/H5）推荐推理部署的重复开发问题，上层Agent生成的优化规则可跨端复用。

  - 硬件反馈驱动的迭代优化机制可迁移：推荐系统线上推理性能优化中，可通过Agent采集线上延迟、内存占用等实际运行反馈，迭代调整算子融合、Batch大小等参数，减少人工调试成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM内核生成方案主要面向服务器GPU，无法适配边缘端硬件异构、软件栈碎片化、资源约束严格的痛点，也缺乏体系化的评估基准，导致边缘端模型部署的自定义内核开发仍需大量人工投入，是边缘AI落地的核心瓶颈。

### 方法关键点
- 构建EdgeKernelBench基准：包含331个覆盖移动、AIoT、机器人等边缘场景的任务，按复杂度分为基础算子、组合算子、紧凑模型图三层，统一基于PyTorch定义参考实现，支持跨异构后端的统一评估。
- 设计统一IR部署框架：LLM仅生成与后端无关的统一IR，再通过编译器适配器自动适配CPU/LLVM、GPU/CUDA、GPU/OpenCL等边缘硬件，解耦上层优化逻辑与下层平台细节。
- 提出分层Agent LEKA：按IR层级拆分优化任务，每层Agent负责对应抽象层级的决策，配合硬件反馈驱动的迭代搜索，跨层保留优化结果，大幅降低单Agent的上下文负担和决策复杂度。

### 关键结果
- 5款主流LLM的one-shot生成测试中，最优模型Correct@1达64.5%，但Fast@1.0（性能超过TVM基线）仅25.5%，功能正确的内核不一定能带来实际性能收益。
- 在69个任务的Agent测试集上，LEKA将Correct@1从one-shot的42.0%提升到100%，Fast@1.0从13.0%提升到43.5%；相比同预算的Claude Code基线，Fast@1.0从26.1%提升到43.5%，几何平均性能达3.8倍。

最值得记住的结论：将复杂优化任务按抽象层级拆分、通过统一IR解耦上层逻辑与下层平台细节、结合真实运行反馈迭代优化，是Agent解决跨平台性能优化问题的通用有效范式。
