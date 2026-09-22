---
title: 'Inherit4Rec: Parameter Inheritance for Efficient Scaling of Recommendation
  Models'
title_zh: Inherit4Rec：面向推荐模型高效扩容的参数继承框架
authors:
- Ruihao Zhang
- Bo Chen
- Xiao Wang
- Jinlong Jiao
- Tijian Hu
- Qinglin Jia
- Xiuqiang He
- Xiangyu Zhao
- Chaoyi Ma
- Ruiming Tang
affiliations:
- Kuaishou Technology
- Shenzhen Technology University
- City University of Hong Kong
arxiv_id: '2609.23111'
url: https://arxiv.org/abs/2609.23111
pdf_url: https://arxiv.org/pdf/2609.23111
published: '2026-09-19'
collected: '2026-09-22'
category: RecSys
direction: 推荐系统高效扩容 · 参数继承
tags:
- Recommendation Scaling
- Parameter Inheritance
- MoE
- Efficient Training
- Dense-to-Sparse
one_liner: 提出支持推荐模型Dense到Dense扩容、Dense到Sparse转换的参数继承框架，大幅降低工业推荐模型扩容成本
practical_value: '- 模型扩容迭代时可复用D2D的混合扩容+非对称训练策略：新增参数用零和初始化保证扩容后线上效果无突降，旧参数保留优化器状态避免训练振荡，相比从零训练节省大量前期收敛成本

  - 做MoE稀疏化降本时，可借鉴D2S的共激活感知分区方案：用近期1-7天的流式业务数据计算FFN通道贡献度，高贡献通道设为共享专家，同激活模式通道归为同一路由专家，最小化稀疏化后的性能损失

  - MoE训练时可复用带负载均衡损失的训练策略，同时直接迁移原有稠密模型的参数和优化器状态，相比从零训练SMoE可降低72%的增量训练成本，工业场景性能损失可控制在0.02%以内'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐系统普遍通过提升模型容量突破性能瓶颈，但从零训练大尺寸模型需要消耗海量GPU算力与时间成本，现有面向LLM的参数继承方案针对静态语料设计，直接迁移到数据分布动态变化的推荐场景时，会出现严重的性能跳水，无法适配流式训练的工业推荐迭代需求。
### 方法关键点
- **Dense-to-Dense（D2D）扩容**：采用混合增长策略，新增通道复制原有门控、上投影参数，下投影采用零和约束的随机初始化，扩容后原有前向推理结果完全不变；配套非对称训练策略，原有参数保留优化器状态与原有学习率调度，新增参数使用独立的warmup学习率，保证优化轨迹连续无振荡。
- **Dense-to-Sparse（D2S）转换**：采用共激活感知分区，用近期流式数据计算FFN各通道的输出贡献度，Top贡献通道作为永久激活的共享专家，剩余通道按共激活相似度分组为路由专家，最大化保留稠密模型原有能力；新增负载均衡损失保证专家激活均衡，所有专家直接复用原有稠密模型的参数与优化器状态。
### 关键实验
在KuaiRand-1K公开数据集、快手工业短视频推荐数据集上验证：D2D相比现有最优参数继承方案，GAUC平均提升0.15%（公开）/0.05%（工业），与从零训练的目标大模型性能差距仅0.1%/0.05%；D2S相比现有最优稀疏转换方案，GAUC最高提升0.74%，仅比从零训练的SMoE性能低0.117%/0.019%，同时SMoE增量训练成本降低72%。
> 最值得记住的一句话：工业推荐模型扩容无需每次从零训练，适配流式动态分布的参数继承可在几乎无损性能的前提下，大幅降低模型迭代成本
