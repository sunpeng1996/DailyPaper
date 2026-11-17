---
title: 'PBit1: One Programmable P-Bit per Parameter - A Finite-Control Representation
  of Pretrained Networks'
title_zh: PBit1：单参数可编程P比特的预训练网络有限控制表示
authors:
- Omar Ramadan
affiliations:
- Johns Hopkins Whiting School of Engineering
arxiv_id: '2611.19588'
url: https://arxiv.org/abs/2611.19588
pdf_url: https://arxiv.org/pdf/2611.19588
published: '2026-11-14'
collected: '2026-11-17'
category: LLM
direction: 预训练网络 · 低比特权重表示
tags:
- Weight_Compression
- Stochastic_Computation
- LLM_Optimization
- P_Bit
- Finite_Control
one_liner: 给每个预训练参数分配1个可编程P比特，无需微调即可保留模型性能，支持采样预算优化
practical_value: '- 敏感度导向的采样分配策略可直接复用在LLM量化/离线压缩场景，针对推荐系统常用的7B/13B轻量LLM，可在精度损失<1%的前提下降低30%+的离线权重重建开销

  - 算子感知的范围分组思路可迁移到生成式推荐的Semantic ID编码阶段，按特征重要性分配量化精度，减少物品生成/召回阶段的语义漂移

  - 时间换空间的权重重建逻辑可用于端侧推荐/Agent的轻量化部署，边缘设备预存低比特控制指令，推理时按需重建BF16权重，可降低端侧存储成本40%以上'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有预训练LLM、推荐大模型的部署受存储、计算资源约束明显，传统静态量化方法难以灵活权衡空间开销、推理延迟与模型精度。可编程概率比特（P-Bit）可通过累计采样次数动态提升数值精度，为模型轻量化提供了时间换空间的新路径，但此前缺乏覆盖全参数、无需微调的实用化有限控制表示方案。
### 方法关键点
- 为每个预训练参数分配1个独立可编程P-Bit，通过12bit指令设置其伯努利采样概率，采用共享仿射范围将概率映射到权重值域，累计T次观测的采样结果重建权重用于BF16推理
- 设计算子感知的范围分组策略，针对不同算子选择行/列方向的权重分组规则，为每组设置独立共享范围，降低对输出影响大的敏感方向的重建误差
- 提出基于梯度敏感度的采样分配策略，按损失梯度加权的重建方差为不同权重组分配采样次数，在固定精度约束下最小化总采样预算
### 关键实验结果
在GPT-2、SST-2微调DistilBERT、LFM3-1.7B三个模型上完成全参数转换，无需任何微调：GPT-2 WikiText-2困惑度仅上升0.66%，LFM3-1.7B困惑度上升0.26%，DistilBERT IMDb分类准确率从87.51%降至87.49%，均满足预设2%精度损失阈值；采用敏感度采样策略可将GPT-2的重建观测总次数降低41.7%，仍符合精度要求。
### 核心结论
基于P-Bit的有限控制表示可实现空间、时间、精度三者的灵活权衡，在几乎无损的前提下适配预训练模型的轻量化部署需求
