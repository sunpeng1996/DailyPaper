---
title: 'PolicyShiftGuard: Benchmarking and Improving Policy-Adaptive Image Guardrails'
title_zh: PolicyShiftGuard：政策自适应图像护栏的基准测试与优化
authors:
- Mingyang Song
- Luxin Xu
- Haoyu Sun
- Minzhou Pan
- Yu Cheng
- Bo Li
affiliations:
- Fudan University
- Tongji University
- Virtue AI
- The Chinese University of Hong Kong
- University of Chicago
arxiv_id: '2607.05910'
url: https://arxiv.org/abs/2607.05910
pdf_url: https://arxiv.org/pdf/2607.05910
published: '2026-07-07'
collected: '2026-07-16'
category: Multimodal
direction: 多模态内容安全 · 政策自适应护栏
tags:
- VLM
- Content Safety
- Guardrail
- Benchmark
- Policy Adaptation
one_liner: 构建政策自适应图像护栏测试基准，提出两阶段训练的轻量化政策敏感护栏模型达SOTA
practical_value: '- 电商UGC/广告素材审核场景可复用BP-Adapt pairwise损失，实现同一张图适配不同业务线的审核政策，避免重复训练模型

  - 政策变动频繁的内容审核场景，可参考RP-SFT两阶段训练范式，大幅提升模型对新增政策的泛化适配能力

  - 多模态内容审核工程部署中，可借鉴其紧凑输出格式设计，平衡审核精度与推理延迟，提升吞吐'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有图像安全护栏默认基于固定政策训练评估，将安全性视为图像固有属性，无法适配实际部署中不同业务、不同版本政策的合规性差异要求。
### 方法关键点
1. 构建的PolicyShiftBench基准覆盖265张图像的2000个政策区分实例，单图平均配对7.55个政策条件prompt，专门测试模型对当前生效政策的自适应能力，排除固定图像安全先验的干扰
2. 设计的两阶段训练轻量化政策自适应护栏：第一阶段做Randomized Policy SFT（RP-SFT），第二阶段引入BP-Adapt模块，对同图同风险类别的样本同时使用标注监督+ pairwise对比损失，拉大允许/拦截政策的决策边界
### 关键结果
7B参数模型在PolicyShiftBench上达SOTA，平均F1 76.9、平均PSS 72.1；可迁移至UnSafeBench、SafeEditBench，紧凑输出格式优化了延迟-性能trade-off；消融验证通/拦边界配对样本是政策自适应稳定的核心
