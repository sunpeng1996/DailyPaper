---
title: Residual Guidance for Real-Time Interactive Video Generation
title_zh: 面向实时交互视频生成的残差引导方法
authors:
- NaHyeon Park
- Kyeong-Hwan Moon
- Youjin Jeon
- Hyunjung Shim
affiliations:
- KAIST
- POSTECH
arxiv_id: '2611.32820'
url: https://arxiv.org/abs/2611.32820
pdf_url: https://arxiv.org/pdf/2611.32820
published: '2026-11-23'
collected: '2026-11-25'
category: Other
direction: 交互式视频生成 · 上下文惯性优化
tags:
- VideoGeneration
- ResidualGuidance
- ContextInertia
- StreamingInference
- TrainingFree
one_liner: 提出无需训练的残差引导方法，破解流式交互视频生成的prompt切换上下文惯性问题
practical_value: '- 残差修正的无训练优化思路可迁移至LLM流式生成场景，解决Agent交互中途切换指令的上下文惯性问题，无需重新训练模型

  - 不修改KV cache、外置计算修正量叠加的思路，可适配流式RAG、生成式推荐的实时内容调整需求，兼顾上下文连续性与新指令响应

  - 单chunk仅新增1次前向传播的低开销设计，适合latency敏感的实时交互业务，比如直播带货实时画面/文案动态调整场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
实时交互视频生成支持用户中途切换prompt控制生成内容，但现有逐chunk生成的流式模型存在严重上下文惯性：切换prompt后仍延续旧内容生成，而直接修改缓存会破坏视觉连续性，现有优化方案存在明显瓶颈。
### 方法关键点
提出无训练的Residual Guidance（RG）方法，无需调整原有缓存机制：将上一chunk重新加噪后，在无缓存条件下用新prompt做一次去噪计算得到残差，将残差叠加到下一chunk的早期去噪步骤（该阶段新prompt被抑制最严重、内容决策权重最高），抵消上下文惯性。
### 关键结果
在单次prompt切换、多切换长序列生成等场景下，RG可大幅提升各类流式模型的prompt切换响应能力，同时保留原有视觉质量；无需训练/模型微调，单chunk仅新增1次前向传播，可快速接入现有实时视频生成管线。
