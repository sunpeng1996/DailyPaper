---
title: 'PhysVista: Benchmarking Physical Intelligence in VLMs via a Perception-Reasoning-Assessment
  Loop'
title_zh: PhysVista：基于感知-推理-评估闭环的VLM物理智能评测基准
authors:
- Xinge Peng
- Yiting Lu
- Tianwu Zhi
- Wen Wen
- Jianzhao Liu
- Xin Li
- Zhibo Chen
affiliations:
- University of Science and Technology of China
- ByteDance
- City University of Hong Kong
arxiv_id: '2610.00559'
url: https://arxiv.org/abs/2610.00559
pdf_url: https://arxiv.org/pdf/2610.00559
published: '2026-09-29'
collected: '2026-10-03'
category: Eval
direction: 多模态大模型 · 物理智能评测
tags:
- VLM
- Benchmark
- Physical Intelligence
- Multimodal Evaluation
- Reasoning
one_liner: 提出覆盖全认知链路的多模态大模型物理智能细粒度评测基准PhysVista
practical_value: '- 做AI生成商品视频/素材合规校验时，可复用感知-推理-评估闭环框架：先识别场景物理状态、再推导合理动态、最终判断物理合理性，降低生成内容常识错误

  - 多模态商品理解任务中，可拆分event-level/scale-level两层推理粒度，分别校验事件逻辑（如水杯倾倒合理性）和数值尺度（如包装尺寸合规性），提升语义理解准确率

  - 构建AIGC素材质量评估体系时，可参考真实/生成样本混合的评测集构造思路，平衡通用场景和AIGC特有错误模式，提升评估鲁棒性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM物理智能评测多聚焦孤立认知阶段，忽略感知、推理、物理判断的协同性，无法有效诊断VLM对生成内容物理真实性的校验能力，难以支撑AIGC时代的内容质检需求。
### 方法关键点
1. 参考人类认知逻辑设计感知-推理-评估闭环评测框架，同步覆盖物理状态感知、物理动态推理、物理合理性评估三个核心阶段
2. 拆分事件级、尺度级两层推理粒度，支持物理理解缺陷的细粒度归因分析
3. 评测集混合真实视频与AI生成视频，覆盖多领域通用场景与AIGC新兴错误场景
### 关键结果
对多款主流VLM的测试显示，现有模型在物理推理和合理性评估上存在显著缺陷，视觉识别能力与真正的物理理解能力存在较大gap。
