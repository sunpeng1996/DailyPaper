---
title: Just Noticeable Difference Modeling for Token Compression in Vision-Language-Action
  Models
title_zh: 面向视觉-语言-动作模型Token压缩的恰可察觉差异建模
authors:
- Zhuoyuan Li
- Rui Zhao
- Jin Wang
- Hanwei Zhu
- Cong Zhang
- Giuseppe Valenzise
- Weisi Lin
- Kin-Man Lam
affiliations:
- 香港理工大学
- 南洋理工大学
- 字节跳动
- 山东大学
- 巴黎萨克雷大学
arxiv_id: '2608.21247'
url: https://arxiv.org/abs/2608.21247
pdf_url: https://arxiv.org/pdf/2608.21247
published: '2026-08-21'
collected: '2026-08-24'
category: Agent
direction: 具身Agent · VLA推理Token压缩
tags:
- Token Compression
- KV cache
- VLA
- JND
- Embodied Agent
one_liner: 提出Action-JND动作感知阈值引导VLA模型Token压缩，高压缩比下大幅降延迟同时保动作精度
practical_value: '- 可将Action-JND核心思路迁移到多模态生成式推荐、大模型推理KV cache优化场景：放弃仅用注意力、语义相似度等间接指标选可压缩Token的方案，改为用Token变化对下游业务指标（如排序分、生成文案CTR、召回相关性）的影响阈值作为压缩判断依据，大幅提升激进压缩下的业务效果稳定性

  - 轻量即插即用的JND估计器设计可直接复用：不需要修改原有大模型结构，仅在现有Token压缩框架的候选Token排序环节新增业务感知打分模块，训练时冻结主干模型仅优化小参数量估计器，工程落地成本低，适合业务场景快速迭代

  - 高压缩比场景下的优化经验可复用：当线上latency要求严苛需要执行激进压缩时，直接用下游任务偏差作为压缩的约束目标，比间接冗余度指标的效果鲁棒性高1-2个数量级，适合电商大促、低功耗边缘设备部署等极端场景'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
VLA（视觉-语言-动作）等具身Agent模型推理需要处理大量高维视觉Token，现有Token压缩方案依赖视觉相似度、注意力权重等间接指标判断可压缩性，在高压缩比下容易导致下游动作预测偏差过大，破坏闭环控制的稳定性，亟需直接对齐下游动作输出的压缩判断准则。

### 方法关键点
- 提出Action-JND概念：扩展传统JND（恰可察觉差异）理论到具身感知场景，定义Token的可压缩阈值为Token扰动带来的VLA动作预测偏差不超过预设容忍范围
- 设计轻量Token级JND估计器：输入VLA提取的视觉Token特征，输出每个Token的动作容忍度得分；训练时仅优化估计器参数，冻结原有VLA主干，不需要重新训练大模型
- 即插即用兼容主流压缩范式：得分可直接接入KV cache复用、Token pruning两类压缩流程，KV cache复用优先选择高得分Token复用历史缓存，Token pruning优先剪去高得分Token，不修改原有压缩框架的调度逻辑

### 关键实验
在LIBERO机器人操作基准上测试，backbone采用OpenVLA、OpenVLA-OFT，对比VLA-Cache、FastV、SparseVLM等主流baseline：
- 60% KV cache复用率下，动作成功率比VLA-Cache高23.7个百分点
- 80% KV cache复用率下，动作成功率比VLA-Cache高41.65个百分点
- 同压缩比下推理延迟比原生VLA低~16%，控制频率提升~52%

Token压缩的判断准则不应仅关注Token本身的冗余度，而要直接对齐下游任务的可接受偏差边界，才能在激进压缩下兼顾效率与效果
