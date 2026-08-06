---
title: 'AVE-Compass: Towards Holistic Evaluation for Audio-Video Editing Abilities'
title_zh: AVE-Compass：面向音视频编辑能力的全维度评估框架
authors:
- Yuqing Wen
- Yukai Huang
- Qianqian Xie
- Jiangtao Wu
- Yibin Lin
- Yikai Gu
- Jialu Chen
- Yuanxing Zhang
- Jiaheng Liu
affiliations:
- Nanjing University
- Kuaishou Technology
- National University of Singapore
- Beijing University of Posts and Telecommunications
- University of Illinois Urbana-Champaign
arxiv_id: '2607.24821'
url: https://arxiv.org/abs/2607.24821
pdf_url: https://arxiv.org/pdf/2607.24821
published: '2026-07-16'
collected: '2026-08-06'
category: Agent
direction: 音视频编辑评估 · 模块化Agent优化
tags:
- Evaluation Benchmark
- Modular Agent
- Cross-modal Alignment
- Self-Reflection
- Audio-Video Editing
one_liner: 推出音视频联合编辑评估基准AVE-Compass，提出模块化编辑Agent提升跨模态编辑效果
practical_value: '- 电商短视频/直播自动剪辑业务可复用AVE-Agent的指令拆解+自反思迭代架构，提升音画同步的剪辑准确率

  - 多模态生成效果评估可参考checklist式MLLM打分+自动化指标结合的方案，降低人工评估成本，提升一致性

  - 音视频联合编辑的4个评估维度（指令遵循/保真/真实感/跨模态对齐）可直接复用为短视频产品效果验收标准'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有音视频编辑基准仅单独评估视觉或单模态编辑能力，未覆盖真实场景中音画耦合的联合编辑需求，跨模态一致性评估存在明显缺口。
### 方法关键点
1. 构建AVE-Compass评估基准，包含145条源视频、196条音画耦合编辑指令、2688条细粒度检查项，覆盖指令遵循、内容保真、真实感、编辑意图4个评估维度，采用checklist式MLLM打分+自动化跨模态/音视频指标结合的评估方案；
2. 提出模块化AVE-Agent框架，将复杂编辑指令拆解为有依赖关系的子任务，通过自反思+评估反馈迭代优化编辑结果。
### 关键结果
现有SOTA模型在跨模态编辑任务上表现较差，AVE-Agent在指令执行、内容保真、音画对齐指标上均有明显提升，同时保持有竞争力的感知质量。
