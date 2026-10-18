---
title: What Does LALM Post-training Learn? Rethinking Audio Understanding and Reasoning
  Capabilities
title_zh: 《LALM后训练究竟学到了什么？重审音频理解与推理能力》
authors:
- Hua-Hsuan Chen
- Xuanjun Chen
- Wei-Chung Lu
- Chih-Kai Yang
- Yu-Xiang Lin
- Sung-Feng Huang
- Haibin Wu
- Hung-yi Lee
affiliations:
- National Taiwan University
- NVIDIA
- Independent Researcher
- NTU AI-Core
arxiv_id: '2610.19476'
url: https://arxiv.org/abs/2610.19476
pdf_url: https://arxiv.org/pdf/2610.19476
published: '2026-10-14'
collected: '2026-10-18'
category: Training
direction: 多模态大模型 · 后训练能力分析
tags:
- LALM
- Post-training
- Audio Understanding
- Benchmark Shortcut
- Model Generalization
one_liner: 通过控制实验证明LALM后训练性能提升多来自适配任务文本格式而非真实音频理解能力
practical_value: '- 做多模态推荐/Agent后训练时，需设计无目标模态输入的对照实验，验证模型是否真的用到图像/音频等非文本信息，避免伪提升

  - 搭建业务评测集时需覆盖不同query格式、交互形式的case，避免模型仅适配benchmark格式过拟合，上线后效果跳水

  - 做SFT、GRPO等后训练时，混入格式多样的负样本，降低模型对任务特定文本cue的依赖，提升泛化性'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
LALM后训练在音频理解推理基准上表现出显著性能提升，但无法确认提升来自真实模态理解能力，还是仅适配了任务特定的出题格式。
### 方法关键点
设计两组对照实验解耦两类收益：1）替换输入有效音频为静音，验证模型是否真的依赖音频信号作答；2）修改问题格式（如选择题转开放式问答），验证模型对出题模式的适配程度，实验覆盖主流LALM结构与SFT、GRPO等多种后训练方法。
### 关键结果
- 移除有效音频替换为静音时，后训练带来的约40点性能提升仍可完整保留
- 变更问题格式后，后训练带来的提升几乎完全消失
- 绝大多数后训练收益来自对任务特定文本线索、答题模式的适配，而非通用音频理解推理能力
