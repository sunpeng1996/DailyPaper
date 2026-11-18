---
title: 'TPHC: Improving Hyper-Connections with Tensor-Parallel Grouped Updates'
title_zh: TPHC：基于张量并行分组更新的超连接优化方法
authors:
- Xinying Hu
- You Wu
- Haoyi Wu
- Jianchao Tan
- Kefeng Zhang
- Yuchen Xie
- Kewei Tu
affiliations:
- ShanghaiTech University
- Shanghai Engineering Research Center of Intelligent Vision and Imaging
- Meituan
arxiv_id: '2611.23026'
url: https://arxiv.org/abs/2611.23026
pdf_url: https://arxiv.org/pdf/2611.23026
published: '2026-11-16'
collected: '2026-11-18'
category: LLM
direction: 大语言模型 · 超连接架构优化
tags:
- Hyper-Connection
- Tensor Parallelism
- LLM Optimization
- Residual Connection
- Transformer
one_liner: 将张量并行分片与超连接流结合，无额外参算量提升多流超连接模型表现
practical_value: '- 业务侧LLM4Rec、Agent小模型训练可直接复用TPHC分组更新思路，基于现有TP训练框架改造，无额外attention/FFN参算量即可提升模型效果，落地成本极低

  - 带多分支残差的推荐大模型可参考TPHC的初始化策略，给每个分支绑定专属读写流，打破初始化对称，避免多分支特征同质化的坍塌问题

  - 大推荐模型多卡训练可借鉴流分片设计，将残支流与TP分片绑定，多流下通信量不随流数增长，8B模型从4流扩展到16流训练时间仅涨19%，大幅降低多流训练开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前mHC（流形约束超连接）通过将Transformer单残差路径扩展为多并行流的方式提升模型效果，但流数超过4后收益几乎停滞，核心原因是每个子层的单一输出会被广播到所有流，导致各流更新来源高度同质化，最终出现流坍塌；同时多流带来的训练成本随流数线性上涨，无法扩展到更大流数配置。
### 方法关键点
- 将张量并行（TP）的每个分片作为独立分组，每个分组读取专属的残支流混合特征，输出不做all-reduce合并，直接作为独立写回分量，每个流接收不同的输出混合，无额外增加attention/FFN的参数量和FLOPs
- 采用稀疏更新策略，每层仅更新k个流（k为TP分片数），用固定调度选择活跃流，将映射生成复杂度从O(N³C)降至O(kN²C + k³C)
- 初始化时给每个分组绑定专属读写流，打破初始化对称，避免早期流同质化
- 实现残支流分片，每个TP设备仅存储部分流，通信量不随流数N增长，大幅降低多流下的显存和训练开销
### 关键实验
基于1.1B Llama模型在100B token预训练数据上验证，对比Llama、mHC、mHC-TFA基线：
- 相同流数下，TPHC验证损失比mHC低0.7-1.0%，6个常识推理零样本准确率高0.3-0.7个百分点
- TPHC 8流效果超过mHC 16流，用更少流达到更高效果
- 8B模型下，TPHC 4流相比mHC 4流仅增加9%训练时间，流数从4升到16训练时间仅增加19%，远低于无分片的59%涨幅
### 核心结论
现有张量并行的中间计算结果可直接复用为多分支残差的独立更新源，在几乎不增加主模块参算量的前提下解决多流同质化问题，同时可通过流分片控制多流训练的成本涨幅
