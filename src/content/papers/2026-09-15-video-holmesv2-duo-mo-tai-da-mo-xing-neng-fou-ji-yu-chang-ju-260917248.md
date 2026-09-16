---
title: 'Video-HolmesV2: Can MLLMs Reason with Spatio-Temporal Audio-Visual Evidence
  in Long Videos?'
title_zh: Video-HolmesV2：多模态大模型能否基于长视频时空音视证据推理
authors:
- Zhaoyang Wei
- Zipeng Wang
- Yushe Cao
- Chenhui Qiang
- Shuaibing Cheng
- Xuesong Yang
- Sen Nie
- Bowen Jiang
- Wenchao Ding
- Yanchao Hao
affiliations:
- University of Chinese Academy of Sciences, China
- Tencent, China
- Tsinghua University, China
arxiv_id: '2609.17248'
url: https://arxiv.org/abs/2609.17248
pdf_url: https://arxiv.org/pdf/2609.17248
published: '2026-09-15'
collected: '2026-09-16'
category: Multimodal
direction: 多模态大模型 · 长视频音视推理
tags:
- MLLM
- Video Understanding
- Audio-Visual Reasoning
- Long-Context Processing
- Benchmark
one_liner: 构建长视频音视耦合推理基准Video-HolmesV2，配套评估方案与音频引导的token压缩方法
practical_value: '- 电商直播/带货长视频的内容标签生成、合规审核场景，可复用音频引导的token压缩方法，大幅降低长上下文token开销，同时减少理解幻觉

  - 涉及多模态证据校验的业务（如直播虚假宣传识别、短视频侵权判定），可借鉴多模型交叉验证pipeline+时空证据感知指标，降低误判率

  - 长视频内容召回排序场景，可引入音视耦合特征锚定机制，提升长视频语义表征的精准度，优化跨模态匹配效果'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有MLLM长视频理解评估偏重视觉特征忽略音频线索，稠密采样策略存在证据捕获与上下文冗余的固有trade-off，易引发注意力分散、token爆炸、幻觉等问题，缺乏要求模型举证时空音视证据的严谨评估体系。
### 方法关键点
1. 推出面向深度音视耦合的推理基准Video-HolmesV2，强制模型输出精准时空音视证据支撑答案，消除猜测和幻觉带来的评估偏差；
2. 配套多模型交叉验证pipeline保障任务严谨性，设计时空证据感知指标实现细粒度评估校准；
3. 提出音频-文本引导的token压缩框架，融合任务意图与音频锚点蒸馏高价值推理线索，缓解长上下文噪声。
### 关键结果
测试中头部专有MLLM准确率不足60%，所提方法效果优于同类开源全模态模型。
