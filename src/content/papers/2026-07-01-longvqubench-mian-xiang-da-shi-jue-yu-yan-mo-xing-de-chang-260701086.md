---
title: 'LongVQUBench: Benchmarking Long-Term Video Quality Understanding of Vision-Language
  Models'
title_zh: LongVQUBench：面向大视觉语言模型的长期视频质量理解基准
authors:
- Arpita Nema
- Hanwei Zhu
- Xi Zhang
- Weisi Lin
affiliations:
- Nanyang Technological University, Singapore
arxiv_id: '2607.01086'
url: https://arxiv.org/abs/2607.01086
pdf_url: https://arxiv.org/pdf/2607.01086
published: '2026-07-01'
collected: '2026-07-02'
category: Eval
direction: 多模态大模型 · 长视频理解评估
tags:
- LVLM
- Video Understanding
- Benchmark
- Long-sequence Evaluation
- Multimodal
one_liner: 构建含1200+多类型长视频的分层评估基准，揭示现有LVLM长时序视频质量推理短板
practical_value: '- 长视频内容推荐场景可复用三级分层评估框架，从局部失真、跨事件关联、全局质量三个维度校验多模态推荐模型的内容理解能力

  - UGC/PGC长视频内容审核场景可借鉴NDQA稀疏扰动注入范式，构造难例测试集提升审核模型的细粒度异常检测能力

  - 视频内容生成Agent研发可参考该基准的评估维度，优化长视频生成的时序一致性和整体画质表现'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LVLM长时序视频质量理解缺乏有效评测基准，过往benchmark仅覆盖短片段、孤立失真，忽略长视频的时序连续性、累积退化和复杂推理需求。

### 方法关键点
构建LongVQUBench，覆盖1200+涵盖电影、纪录片、监控、第一视角录制、动画的长视频，配套1500+选择题/开放题；设计三级递进评估范式：局部事件质量理解（LQU）、跨事件质量推理（CQR）、全局质量理解（GQU），全流程嵌入稀疏扰动注入的NDQA评测范式，探测细粒度检测推理能力。

### 关键结果数字
对14个SOTA LVLM的测试显示，模型性能随视频长度、推理深度提升显著下降，验证现有LVLM长时序融合、感知归因能力存在明显短板。
