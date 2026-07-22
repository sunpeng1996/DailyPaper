---
title: 'ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU'
title_zh: ABot-World-0：单桌面GPU实现无限交互世界推演
authors:
- Fan Jiang
- Zhaoxu Sun
- Mengchao Wang
- Ziyu Zhu
- Chiyu Wang
- Yunpeng Zhang
- Wenlin Liu
- Yun Wang
- Xue Zheng
- Rui Sun
affiliations:
- AMAP CV Lab
- Alibaba Group
arxiv_id: '2607.19191'
url: https://arxiv.org/abs/2607.19191
pdf_url: https://arxiv.org/pdf/2607.19191
published: '2026-07-21'
collected: '2026-07-22'
category: Agent
direction: Agent 交互世界模型推理优化
tags:
- World Model
- Agent Interaction
- Low-bit Inference
- Knowledge Distillation
- Streaming Inference
one_liner: 单RTX 5090上实现16FPS 720P实时长时序可控交互世界推演
practical_value: '- LongForcing 训练策略可迁移到生成式推荐长序列 autoregressive 生成场景，缓解累积分布偏移与自回归漂移问题

  - 低比特DiT推理+轻量VAE解码器+内存感知调度的流式推理栈可直接复用在大模型边缘/端侧部署环节，降低显存占用与响应延迟

  - 多源数据14项规则质检+VLM评估+多模态对齐标注的流水线可复用在多模态训练数据构建流程，提升训练数据质量'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有交互世界模型推理成本高、延迟大，长时序自推演易出现分布偏移、身份一致性差问题，无法在消费级GPU上实现实时闭环交互。
### 方法关键点
1. 搭建覆盖AAA游戏、仿真引擎、互联网视频的多源数据基建，配套WorldExplorer反馈引导的Agent数据采集流水线，叠加14项规则质检、VLM评估、动作-文本同步标注；
2. 通过ODE蒸馏将双向动作条件教师模型渐进式蒸馏为因果学生模型，引入LongForcing对齐长序列自推演结果，缓解自回归漂移；
3. 协同设计流式推理栈，融合轻量VAE解码、高效注意力、内存感知调度、低比特DiT推理优化。
### 关键结果
单RTX 5090桌面GPU上可实现最高16FPS 720P视频流输出，动作到首帧延迟1.2s，峰值显存占用19GiB，长时序推演可控性与连贯性达到领先水平。
