---
title: 'Perceive Once, Escalate on Demand: Handing Off Visual KV Memory from Small
  to Large VLMs'
title_zh: 感知一次按需升级：小VLM到大VLM的视觉KV内存迁移方法
authors:
- Qiang Zhou
- Jianing Deng
- Siyan Dong
- Jingxian Chen
- Han-Yi Lin
- Jingtong Hu
affiliations:
- University of Pittsburgh
- University of Hong Kong
arxiv_id: '2611.26902'
url: https://arxiv.org/abs/2611.26902
pdf_url: https://arxiv.org/pdf/2611.26902
published: '2026-11-19'
collected: '2026-11-23'
category: Multimodal
direction: 多模态大模型 · 跨模型KV缓存复用
tags:
- KV cache
- VLM
- Model Cascade
- Knowledge Distillation
- Embodied Agent
one_liner: 提出无标注蒸馏的线性KV映射BATON，实现VLM级联时历史视觉记忆免重编码迁移
practical_value: '- 级联推理架构可直接复用该设计：小模型承接全量请求做初筛，低置信度请求升级到大模型时，迁移小模型已生成的KV cache，避免大模型重复编码长上下文，升级请求算力可降50%以上

  - 跨模型KV迁移无需追求缓存拟合度：不用做KV回归严格匹配大模型原生缓存，改用大模型输出作为蒸馏目标训练简单线性映射即可，落地成本低、效果优于拟合方案

  - 电商多模态场景可落地优化：短视频/商品图审核、多模态搜索场景中，小VLM实时处理用户上传的序列内容，低置信度case升级时无需重传全量历史，直接迁移KV即可提速降本

  - 视觉Agent长上下文记忆优化：无需每次调用大VLM都重编码历史观测，小模型持续维护KV内存，按需迁移即可支撑长时序交互的低成本推理，历史越长收益越高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
具身Agent、长视频理解等场景全程跑大VLM成本极高，通常采用小VLM持续处理、低置信度决策升级到大VLM的级联架构，但升级时大VLM需要重编码全量历史视觉帧，这部分开销占升级请求算力的90%以上。小VLM已经生成了历史的KV cache，直接跨模型复用该缓存是核心降本方向，但此前直接拟合大模型KV的方案效果极差，无法实用。
### 方法关键点
- 采用分层线性映射架构：每层独立训练简单线性转换，将小VLM的历史KV cache转换为大VLM可读取的格式，大VLM仅需编码当前帧和问题文本，无需处理历史帧
- 无标注蒸馏训练：不用标注数据，也不以拟合大模型原生KV为目标，而是用大模型重编码历史时的输出作为蒸馏目标，优化KL散度损失，仅保证映射后的KV能支撑大模型输出正确结果即可
- 混合路径设计：仅对历史部分的KV做映射，当前观测和问题由大VLM原生编码，保证当前信息的准确性
### 关键实验结果
在RoboMME机器人操作benchmark上，2B→8B Qwen3-VL级联、25%请求升级的情况下，BATON相比重编码方案算力降低28~47%，精度仅低0.5~1.0个点；历史长度为64帧时，单次升级算力降低8倍，推理速度提升2.6倍；在8个不同模型家族的大小VLM对上均有效，增益和大模型相比小模型的精度上限正相关，可零样本迁移到OpenEQA场景。
### 最值得记住的一句话
跨模型KV迁移不需要还原大模型的原生缓存，只需要提供大模型可使用的记忆即可，缓存的保真度和可用性没有直接关系。
