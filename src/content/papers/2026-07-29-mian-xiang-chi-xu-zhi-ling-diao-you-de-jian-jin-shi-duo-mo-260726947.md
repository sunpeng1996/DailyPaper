---
title: Progressive Multimodal Alignment for Continual Instruction Tuning
title_zh: 面向持续指令调优的渐进式多模态对齐框架PMA
authors:
- Duzhen Zhang
- Yahan Yu
- Qiaoyi Su
- Jiahua Dong
- Tielin Zhang
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Center for Excellence in Brain Science and Intelligence Technology, Chinese Academy
  of Sciences
- Kyoto University
- Migu Culture Technology Co.,Ltd.
- State Key Laboratory of Brain Cognition and Brain-inspired Intelligence Technology
arxiv_id: '2607.26947'
url: https://arxiv.org/abs/2607.26947
pdf_url: https://arxiv.org/pdf/2607.26947
published: '2026-07-29'
collected: '2026-07-30'
category: Training
direction: 多模态LLM · 持续指令调优
tags:
- MLLM
- Continual Learning
- Instruction Tuning
- Multimodal Alignment
- PEFT
one_liner: 通过动态扩展多模态投影专家解决持续指令调优中的投影层遗忘问题
practical_value: '- 做电商多模态商品理解/搜推模型持续迭代时，可参考PMA的投影层动态扩展思路，避免新增任务覆盖已有图文对齐能力，无需全量重训

  - 可复用轻量级MLP自动编码器做分布偏移检测的trick，无需人工标注任务ID即可自动判断是否需要新增专家，适配无监督业务数据变化场景

  - 保留预训练原始投影层作为锚点的设计可直接复用，大幅降低持续训练后旧任务性能退化，适合多阶段迭代的业务模型上线

  - 软路由加权融合多投影专家输出的方式，比硬路由更适配电商跨场景知识共享，相似品类任务可复用已有对齐能力，降低参数开销'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有多模态持续指令调优（MCIT）方法仅关注LLM主干的灾难性遗忘，忽略了负责跨模态对齐的共享投影层在多任务迭代中会发生对齐漂移，导致旧任务的图文映射失效，比如分类任务在训练完caption任务后输出长句而非短标签；而逐任务单独分配投影层的方案参数开销大、需要人工标注任务ID，不符合实际无标注业务场景需求。

### 方法关键点
- 用轻量级MLP自动编码器实现Representation Descriptor（RD），计算新任务多模态融合特征的重构误差z-score，当所有已有RD的样本匹配率低于60%时才新增投影专家，实现亚线性参数增长
- 基于图文融合特征训练可扩展路由层，无需任务ID就能自动为每个样本分配各投影专家的权重，软加权输出最终对齐后的视觉特征
- 冻结预训练原始投影层作为稳定锚点，所有旧专家、RD、旧路由参数在训练新任务时全冻结，避免旧知识被覆盖
- 框架与现有LLM侧PEFT持续调优方法完全解耦，可直接叠加在LoRA、MoELoRA、DISCO等现有方案上

### 关键实验
在UCIT、MLLM-DCL两个MCIT基准上测试，适配LLaVA-1.5、InternVL两种主流7B多模态backbone，对比DISCO、HiDE等SOTA方法：叠加PMA后，UCIT基准上DISCO的MFN（平均最终准确率）提升4.77个百分点，BWT（遗忘程度）绝对值降低2.4；MLLM-DCL基准上DISCO的MFN提升3.33个百分点，BWT绝对值降低1.66；仅用3个投影专家就能覆盖6个任务，参数增长远低于逐任务新增的方案。

### 核心结论
多模态持续调优的性能瓶颈不止在LLM主干，跨模态对齐的投影层遗忘是不可忽略的关键优化点，通过动态扩展专家+锚点冻结可以低成本解决该问题
