---
title: 'Meta Expert: Cross-Layer Expert Sharing for Storage- and Retrieval-Efficient
  MoE'
title_zh: Meta Expert：通过跨层专家共享实现存储与检索高效的MoE模型
authors:
- Ermo Hua
- Xiangyu Hong
- Baiting Wu
- Che Jiang
- Haozheng Hou
- Yicheng Gu
- Hanjing Wang
- Qirui Zeng
- Ming Zhang
- Ning Ding
affiliations:
- Tsinghua University
- Shanghai AI Laboratory
arxiv_id: '2610.27598'
url: https://arxiv.org/abs/2610.27598
pdf_url: https://arxiv.org/pdf/2610.27598
published: '2026-10-19'
collected: '2026-10-23'
category: Training
direction: MoE结构优化 · 跨层专家共享
tags:
- MoE
- Parameter Efficiency
- Expert Sharing
- Transformer
- Scaling
one_liner: 提出跨层共享的Meta Expert结构，仅用70-80%专家数即可达到原生MoE同等性能
practical_value: '- 业务侧部署MoE结构的LLM/生成式推荐服务时，可复用Meta Expert跨层共享设计，在推理FLOPs不变的前提下降低20-30%专家参数量，压缩显存占用与部署成本

  - 推荐系统的多塔MoE召回/排序模型可参考跨层/跨塔专家共享思路，消除不同层、不同塔之间的专家冗余，在不涨参的前提下提升模型有效容量

  - 配置可直接复用论文最优实践：75%比例Meta专家+首尾2层保留Local专家+Meta专家拆分为2个交错子池，平衡参数效率与训练稳定性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有MoE模型各层独立配置专家，不同层的专家存储内容存在大量冗余，而循环Transformer的全层参数复用方案会带来额外串行计算开销，大幅提升推理延迟，亟需在不增加计算成本的前提下提升MoE的参数效率。
### 方法关键点
- 设计跨层共享的Meta Expert替代原有各层独立的Local Expert，所有层共用同一专家池与路由模块，单层激活专家数保持不变，推理FLOPs与原生MoE完全对齐
- 支持灵活的混合拓扑配置：可调整Meta与Local专家的总量比例、单层激活比例，也可在模型首尾层保留Local专家、将Meta专家拆分为多个子池循环访问，兼顾效率与训练稳定性
- 理论层面证明Meta Expert本质是提供了双向残差通路，浅层与深层的信息可在激活层面互相访问，大幅提升信息存储与检索效率
### 关键结果
在12/16/20/24层不同规模的MoE模型上与原生Vanilla MoE对比，保持总FLOPs一致的前提下：
- 仅需70-80%的专家数、75-90%的参数量即可达到与原生MoE相当的交叉熵损失，模型规模越大，参数节省幅度越高
- 最优配置（75% Meta专家+首尾2层Local专家+2个交错子池）在6B参数规模的下游任务上，MMLU、C-Eval等基准平均提升1-2pct，专家冗余度降低10-25%
> 最值得记住：MoE跨层的专家冗余并非固有成本，通过跨层共享设计可转化为更高的有效参数容量，且完全不增加推理延迟
