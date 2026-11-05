---
title: Matching the Training-Time Weight Rule in Inference-Time Expert Deactivation
title_zh: MoE推理阶段专家停用需匹配训练时权重规则
authors:
- Hao Cheng
- Zhiyu Yang
- Bo Ma
- Hanzhang Jia
affiliations:
- Zhejiang Gongshang University
- University of Sussex
- Chang'an University
arxiv_id: '2611.05804'
url: https://arxiv.org/abs/2611.05804
pdf_url: https://arxiv.org/pdf/2611.05804
published: '2026-11-04'
collected: '2026-11-05'
category: LLM
direction: MoE LLM 推理优化 · 专家停用策略
tags:
- MoE
- Expert Pruning
- Inference Optimization
- Weight Normalization
- LLM Deployment
one_liner: 对比4种MoE专家停用实现，证明匹配训练权重规则可大幅降低推理性能损失
practical_value: '- 业务中使用MoE大模型做推荐生成/Agent推理时，专家剪枝、动态停用操作必须严格对齐训练时的权重计算规则，避免规则不匹配导致的数量级级别的性能下降

  - 针对不同训练规则的MoE选择对应停用方案：训练用原始路由概率的模型（如DeepSeek V2、OLMoE）优先用freezing或unnormalized
  re-routing，禁止使用剩余专家重归一化；训练用选中集归一化的模型（如Qwen3、Granite）优先用removal按原规则重计算权重，禁止使用无归一化重路由

  - 动态调整激活专家数降本时，在规则匹配前提下，激活数可在训练值附近小范围调整（如训练k=8可调整到4~16），性能损失可控；不要为了进一步降本使用规则不匹配的方案，得不偿失

  - 剪枝专家时优先按激活频率/激活值排序选择待剪专家，相比随机剪枝可降低30%以上的困惑度上升幅度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
MoE大模型部署时为降低存储、调度成本，常采用专家剪枝、动态停用等策略，但现有研究大多仅关注专家选择标准，未系统对比不同停用实现的性能差异，也未关联训练时的权重规则，导致实际部署时性能退化幅度不可控，甚至出现数量级级别的损失。

### 方法关键点
- 梳理4种主流专家停用实现：removal（屏蔽禁用专家后重路由，沿用原权重规则）、freezing（保留原路由结果，仅将禁用专家权重置0）、remaining-expert renormalization（剩余专家权重重归一化至和为1）、unnormalized re-routing（重路由时直接使用原始softmax概率，不做选中集归一化）
- 提出权重和模型，将性能损失拆解为专家贡献丢失、分支缩放两部分，关联训练时的两类权重规则（原始路由概率、选中集归一化），可预测不同实现的退化程度
- 实验覆盖4个模型家族的6个公开checkpoint，专家禁用比例从12.5%到50%，采用C4语料做校准选择待剪专家，评估指标包含WikiText-2困惑度、多选择任务（MMLU、ARC等）、GSM8K生成准确率

### 关键结果
- 50%专家禁用时，匹配训练规则的实现困惑度仅为基线的1.4~73倍，规则不匹配的实现困惑度可达基线的14~28740倍，最大性能差距超4个数量级
- 训练用原始概率的模型（OLMoE、DeepSeek V2）使用剩余专家重归一化时退化最严重，训练用选中集归一化的模型（Granite、Qwen3）使用无归一化重路由时退化最严重，与理论预测完全吻合
- 激活专家数越少，规则不匹配的惩罚越大：OLMoE仅激活2个专家时，规则不匹配的困惑度是匹配方案的1894倍

### 核心结论
MoE推理阶段任何修改专家激活的操作，都必须优先对齐训练时的权重计算规则，否则性能损失远大于专家剪枝本身带来的影响
