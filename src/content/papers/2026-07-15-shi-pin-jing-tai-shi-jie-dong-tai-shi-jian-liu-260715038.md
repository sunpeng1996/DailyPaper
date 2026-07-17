---
title: Video = World + Event Stream
title_zh: 视频 = 静态世界 + 动态事件流
authors:
- Lianghua Huang
- Zhi-Fan Wu
- Yupeng Shi
- Wei Wang
- Mengyang Feng
- Cheng Yu
- Chen Liang
- Junjie He
- Chen-Wei Xie
- Yu Liu
affiliations:
- Wan Team, Alibaba Group
arxiv_id: '2607.15038'
url: https://arxiv.org/abs/2607.15038
pdf_url: https://arxiv.org/pdf/2607.15038
published: '2026-07-15'
collected: '2026-07-17'
category: Multimodal
direction: 多模态预训练 · 实时音视频交互Agent
tags:
- Multimodal Pretraining
- Real-time Interaction
- Audio-visual Model
- Streaming Agent
- Video Understanding
one_liner: 提出视频拆分为静态世界+动态事件流的预训练范式，推出低延迟实时音视频交互模型Wan-Streamer v0.3
practical_value: '- 可借鉴「静态持久上下文+动态事件流」的拆解范式，优化直播/短视频电商的用户行为、内容建模效率，降低冗余特征计算

  - 低延迟流式交互的工程优化思路可复用在实时直播互动Agent、音视频智能导购场景，平衡模型效果与响应速度

  - 通用视频预训练任务的设计思路可迁移到短视频/直播内容理解、商品多模态生成的预训练任务构建，提升下游任务性能'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
此前的Wan-Streamer版本绑定特定交互Agent任务，缺乏通用底层建模范式，预训练能力无法高效迁移到多类实时下游场景。
### 方法关键点
1. 提出视频通用拆解框架：将视频拆分为**静态World**（环境、场景、主体特征、声学环境等稳定上下文）与**动态Event Stream**（随时间变化的行为、语音、场景变动等内容）；
2. 基于该框架设计通用预训练任务：给定静态World和实时输入，预测世界的实时动态变化与响应，预训练能力可适配多类实时下游任务；
3. 落地到实时全双工音视频交互场景，Event Stream对应Agent的语音与自由行为，采用类vision-language-action链路映射多模态输入到输出动作。
### 关键结果
保持v0.2性能指标：支持640×368分辨率25FPS视频，流式单元160ms，模型侧响应延迟约200ms，350ms双向网络带宽下总交互延迟约550ms
