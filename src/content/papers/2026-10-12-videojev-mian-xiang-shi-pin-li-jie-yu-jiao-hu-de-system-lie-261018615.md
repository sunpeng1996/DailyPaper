---
title: 'VideoJev: System One Model for Video Understanding and Interaction'
title_zh: VideoJev：面向视频理解与交互的System One系列模型
authors:
- Yuhan Zhu
- Xiangyu Zeng
- Qingyi Si
- Chenxu Yang
- Yifei Li
- Luozheng Qin
- Junhao Zhou
- Dingyu Yao
- Jun Zhang
- Chuanyu Qin
affiliations:
- NJU
- JD.com
- UCAS
- THU
- XMU
arxiv_id: '2610.18615'
url: https://arxiv.org/abs/2610.18615
pdf_url: https://arxiv.org/pdf/2610.18615
published: '2026-10-12'
collected: '2026-10-14'
category: Multimodal
direction: 多模态大模型 · 视频理解决策
tags:
- MLLM
- Temporal Grounding
- Video QA
- System One
- Inference Optimization
one_liner: 将视频时序定位与多选QA统一为候选打分任务，复用视觉计算，兼顾精度与推理效率
practical_value: '- 电商直播/短视频场景的商品时序定位任务可复用候选区间打分方案，替代自回归时间戳生成，可获得2~3倍推理提速同时提升定位精度，适配实时业务需求

  - 同视频多轮查询场景可落地Cached+Joint inference优化：仅对视频做一次编码缓存，多查询合并单次forward，单查询边际成本低至几十ms，适合短视频问答、直播实时交互类产品

  - 时序定位与视频QA可联合训练互相增益，无需部署两个独立模型，时序监督强化语义证据定位能力，QA任务强化语义判别能力，降低训练与部署成本

  - 结构化输出类推荐/交互任务可迁移直接打分思路替代自回归生成，避免生成的不确定性与延迟，提升系统响应速度与结果稳定性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视频多模态大模型（MLLM）依赖自回归生成输出结果，即使是时序定位、多选QA这类结构化决策场景也需逐token生成，推理延迟高；同时同一段视频的多次查询会重复计算视觉特征，算力浪费严重，无法满足视觉Agent低延迟交互的需求。
### 方法关键点
- 架构改造：基于预训练MLLM，移除最终MLP层，替换输出头为共享候选打分器，新增<|option_end|>、<|decide|>特殊token，用归一化向量相似度计算候选得分，统一时序区间与文本选项的打分逻辑
- 推理优化：提供两种视觉计算复用模式：Cached inference单次编码缓存视频前缀，后续查询直接复用缓存；Joint inference将同视频的多个查询拼接后单次forward得到所有结果
- 训练设计：两阶段训练，第一阶段冻结主干仅训练打分头对齐特征，第二阶段联合训练主干与打分头；时序定位同时用BCE+Soft IoU损失监督，QA用交叉熵损失，支持双任务联合训练
### 关键结果
在3个时序定位基准（CharadesTL、ActivityNetTL、QVHighlightsTL）、4个视频QA基准（LVBench、Video-MME等）上测试：4B版本相对Qwen3.5-4B主干，时序定位平均mIoU提升6.7个点，推理加速2.8~3.1×；QA平均得分提升8个点，相对Thinking模式推理加速超129×。35B MoE版本相对Qwen3.6-35B-A3B主干，时序定位mIoU提升10.8个点，QA得分提升5.7个点，相对Thinking模式加速超100×。
### 最值得记住的结论
结构化决策类多模态任务放弃自回归生成改用直接候选打分，搭配上下文缓存复用，可同时获得精度提升与数量级推理提速，非常适配实时Agent场景。
