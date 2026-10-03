---
title: 'VTR-Bench: A Systematic Benchmark for Evaluating Visual Text Rendering in
  Video Generation'
title_zh: VTR-Bench：视频生成场景下视觉文本渲染的系统化评测基准
authors:
- Yu Huang
- Jungang Li
- Zhiyuan Wang
- Yonghua Hei
- Song Dai
- Jiayu Yang
- Deyuan Liu
- Xiang Zheng
- Xiaoshuang Shi
- Hao Cheng
affiliations:
- City University of Hong Kong
- The Hong Kong University of Science and Technology (Guangzhou)
- Westlake University
- University of Electronic Science and Technology of China
- The Hong Kong University of Science and Technology
arxiv_id: '2610.01499'
url: https://arxiv.org/abs/2610.01499
pdf_url: https://arxiv.org/pdf/2610.01499
published: '2026-09-30'
collected: '2026-10-03'
category: Eval
direction: 视频生成 · 视觉文本渲染评测
tags:
- Video Generation
- Evaluation Benchmark
- Agent Framework
- Text Rendering
- Automatic Evaluation
one_liner: 推出覆盖5类场景的VTR-Bench评测基准，配套自动评估pipeline与关键帧引导的Agent优化框架
practical_value: '- 电商营销短视频生成场景可复用VTR-Bench的评估逻辑，批量校验生成视频中促销文字、商品名的渲染准确率，替代部分人工审核

  - 可迁移关键帧引导的Agentic Framework架构：用统一调度Agent协调生成、视觉校验、迭代优化环节，降低生成内容的文字错误率

  - 参考其分场景prompt构造方法，针对电商广告、科普短视频等业务场景定制专属评测集，对齐业务需求

  - 当前SOTA视频生成模型文字渲染WER仍达25%，业务落地时必须叠加独立的OCR校验环节，避免错字导致合规风险'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有视频生成评测基准仅关注视觉质量、美学性与物理合理性，忽略了场景内文字这一核心信息载体的渲染效果，生成的广告、科普类视频常出现文字错误，无法满足实际业务需求。
### 方法关键点
1. 构建VTR-Bench评测集，覆盖5类落地场景共300条标注prompt，聚焦文字渲染能力评测
2. 设计对齐人工标准的自动化评估pipeline，分别通过载体专属OCR转录评估文字保真度、prompt专属查询链评估场景与运动合规性
3. 提出关键帧引导的Agentic Framework，由Director Agent统一调度生成、评估、迭代优化全链路，通过视觉反馈降低文字错误率
### 关键结果
对11款SOTA视频生成模型的测试显示，文字渲染为行业普遍短板，最优模型的整体词错误率(WER)仍达0.250
