---
title: 'WQ-Fusion: Dynamic Gated Attention for Cross-Domain Audio Representation'
title_zh: WQ-Fusion：用于跨域音频表征的动态门控注意力机制
authors:
- Mingda Lin
- Lei Ding
- Xinyue Zhou
- Tiantian Xiong
- Hanchen Pei
- Gongping Huang
- Hao Zhang
- Jingdong Chen
- Jacob Benesty
affiliations:
- School of Electronic Information, Wuhan University
- Tencent AI Lab Seattle
- CIAIC, Northwestern Polytechnical University
- INRS-EMT, University of Quebec
arxiv_id: '2606.26556'
url: https://arxiv.org/abs/2606.26556
pdf_url: https://arxiv.org/pdf/2606.26556
published: '2026-06-25'
collected: '2026-06-27'
category: Other
direction: 跨域音频表征 · 双编码器融合
tags:
- Audio Representation
- Dual Encoder
- Gated Attention
- Cross-Domain Learning
- Whisper
- Qwen
one_liner: WQ-Fusion融合Whisper与Qwen双编码器，通过自适应调制与逐元素门控注意力实现跨域音频动态特征选择
practical_value: '- 电商语音搜索/语音交互场景下，可借鉴双编码器融合思路，结合声学编码器与语义大模型编码器，提升音频query的表征质量

  - 多源异构特征融合场景（如多模态召回、跨域推荐）中，用逐元素门控注意力替代静态拼接，实现动态特征选择，适配不同下游任务的特征偏好

  - 异构预训练模型表征对齐时，可引入自适应特征调制模块，降低不同模型的特征空间差异，提升融合表征的泛化性'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**
现有预训练音频模型在单一专项任务表现优异，但跨多样声学域的通用表征学习仍存在核心挑战：传统静态特征拼接的融合方式无法动态适配不同域的特征需求，难以兼顾声学细节与高层语义维度的选择性强调，限制了跨域表征的泛化能力。

**方法关键点**
WQ-Fusion 为融合 Whisper（声学表征）与 Qwen（语义表征）的双编码器跨域音频表征框架，核心包含两个关键模块：一是自适应特征调制模块，对齐异构编码器的特征空间，降低不同模型的异质性差异；二是逐元素门控注意力机制，替代传统静态拼接，实现细粒度动态特征选择，可根据输入自适应激活相关的声学与语义维度，高效路由异质信息。

**关键结果**
在 Interspeech 2026 音频编码器能力挑战赛（Track A）基准测试中，整体得分达 0.836，显著优于最强单编码器基线模型。
