---
title: 'Wan-Dancer: A Hierarchical Framework for Minute-scale Coherent Music-to-Dance
  Generation'
title_zh: Wan-Dancer：实现分钟级连贯音乐转舞蹈生成的分层框架
authors:
- Mingyang Huang
- Peng Zhang
- Li Hu
- Guangyuan Wang
- Bang Zhang
affiliations:
- Tongyi Lab, Alibaba Group
arxiv_id: '2607.09581'
url: https://arxiv.org/abs/2607.09581
pdf_url: https://arxiv.org/pdf/2607.09581
published: '2026-07-10'
collected: '2026-07-13'
category: Multimodal
direction: 多模态生成 · 长时序音乐转舞蹈生成
tags:
- VideoGeneration
- Music-to-Dance
- DiffusionModel
- RoPE
- Long-Form-Video
one_liner: 提出分层音乐转舞蹈生成框架，突破20秒时长限制，可生成超1分钟720P/30fps高稳定连贯舞蹈视频
practical_value: '- 长时序生成的「全局关键帧规划+局部时序细化」分层架构，可直接复用在电商长视频生成、虚拟人直播内容生产场景，解决长时内容一致性问题

  - 时间映射RoPE嵌入实现动态帧率适配的方法，可迁移至多模态时序对齐任务，比如直播口播与商品展示环节的时序匹配优化

  - 光流损失提升运动连续性的思路，可用于优化生成式商品展示视频、虚拟人动作的流畅度，减少跳变与穿模问题'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有扩散模型生成音乐转舞蹈视频的时长上限仅20秒，长时生成存在时序漂移、身份不一致、动作重复等缺陷，无法满足分钟级内容生产需求。
### 方法关键点
1. 分层解耦生成流程为全局关键帧规划+局部时序细化，引入全曲音乐上下文保证长时连贯性
2. 采用时间映射RoPE嵌入实现动态帧率适配，精准对齐音乐节奏与舞蹈动作
3. 新增光流损失提升动作连续性，加入运动速度控制模块保留快速动作的高保真细节
### 关键结果
突破传统时长限制，可稳定生成超1分钟的720P/30fps舞蹈视频，时序稳定性优于现有SOTA；支持音频+文本双条件输入，可适配5种不同舞蹈品类，达到长时连贯舞蹈视频合成新SOTA。
