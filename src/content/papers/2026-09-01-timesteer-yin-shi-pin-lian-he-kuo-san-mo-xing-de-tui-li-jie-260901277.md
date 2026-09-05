---
title: 'TimeSteer: Inference-Time Speech Scheduling in Joint Audio-Visual Diffusion
  Models'
title_zh: TimeSteer：音视频联合扩散模型的推理阶段语音时序调度
authors:
- Chao Zhou
- Yiling Chen
- Qi Chu
- Tao Gong
- Nenghai Yu
- Tianyi We
arxiv_id: '2609.01277'
url: https://arxiv.org/abs/2609.01277
pdf_url: https://arxiv.org/pdf/2609.01277
published: '2026-09-01'
collected: '2026-09-05'
category: Multimodal
direction: 多模态生成 · 时序可控调度
tags:
- Diffusion Model
- Audio-Visual Generation
- Inference Control
- Temporal Scheduling
- Benchmark
one_liner: 提出无需微调的TimeSteer框架，实现音视频生成中语音起止时间可控调度，配套首个时序调度基准SpeechShift
practical_value: '- 推理阶段无需微调调整生成时序的思路，可迁移到生成式推荐场景，控制推荐结果展示、广告投放的时间窗口，无需重训大模型

  - 利用模型注意力头定位隐空间内容区间的方法，可复用在商品文案、短视频脚本等生成内容的片段调整任务，无需全量重生成

  - 无训练的隐空间重映射技巧，可用于电商短视频的语音与口型、商品画面的时序对齐，降低多模态内容生成的推理成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有预训练音视频联合扩散模型仅支持控制生成内容，无法显式指定语音起止时间，无法满足影视制作、交互Agent等场景的时序约束需求，微调骨干模型调整时序的成本极高。
### 方法关键点
1. 挖掘扩散去噪过程两个固有属性：时序敏感的文本-音频交叉注意力头可定位语音在隐空间的原始区间，预测的干净隐空间天然对齐语音与视觉动作，无需重生成即可调整时序；
2. 无训练框架TimeSteer包含两大模块：源区间定位模块识别语音原始隐空间区间，区域感知隐空间重映射模块将关联的音视频隐层内容迁移到用户指定的目标区间；
3. 构建首个音视频生成区间级语音调度基准SpeechShift。
### 关键结果
在两个主流音视频扩散骨干模型上验证，相比无训练基线时序可控性大幅提升，同时生成质量保持行业竞争水平。
