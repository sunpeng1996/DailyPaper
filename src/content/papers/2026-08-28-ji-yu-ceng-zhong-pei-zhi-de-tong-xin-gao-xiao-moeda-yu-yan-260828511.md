---
title: Training Communication-Efficient Mixture-of-Experts Language Models with Layer
  Re-Configuration
title_zh: 基于层重配置的通信高效MoE大语言模型训练方法
authors:
- Simeng Sun
- Roger Waleffe
affiliations:
- NVIDIA
arxiv_id: '2608.28511'
url: https://arxiv.org/abs/2608.28511
pdf_url: https://arxiv.org/pdf/2608.28511
published: '2026-08-28'
collected: '2026-08-31'
category: Training
direction: MoE大模型训练 · 通信效率优化
tags:
- MoE
- Communication Efficiency
- Model Training
- Layer Configuration
- Mamba-2
- Inference Optimization
one_liner: 通过异构层重配置减少MoE层数，降低训练通信开销同时保持模型效果与推理性能
practical_value: '- 业务训练自定义MoE垂直大模型（如电商Agent、生成式推荐场景）时，可复用CE-MoE层设计思路：减少MoE层数、增加Mamba-2/注意力层+少量更宽专家，总参不变前提下降低30%+训练GPU成本

  - 自研MoE推理服务优化时，参考「减少MoE层数、加宽单层专家」的思路，可降低路由开销与同步次数，实测吞吐量提升28%~36%，适配高并发业务场景

  - 堆叠连续token-mixer层时优先选择Mamba-2而非纯注意力，可避免rank collapse导致的训练不稳定，无需额外正则即可稳定训练深度异构模型'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
MoE大模型训练时跨节点all-to-all的token调度通信占端到端训练时间比例极高，现有优化多聚焦系统层面，架构层面的通信量缩减方案要么破坏标准层结构，要么容易引发训练不稳定、效果下降，亟需在不损失模型效果的前提下降低MoE训练成本的可行方案。
### 方法关键点
- 提出异构层布局CE-MoE，打破传统MoE「token-mixing层+MoE层」交替的固定范式，大幅减少MoE层数，将节省的参数配额分配给更多Mamba-2/注意力token-mixing层、更宽的单层MoE专家与dense FFN层，总参数量与激活参数量和基线对齐。
- 采用分阶段贪心算法生成层顺序，将注意力、MoE、dense FFN层均匀分布在Mamba-2主干上，避免连续channel-mixing层导致的效果折损。
- 验证连续堆叠Mamba-2层不会出现纯注意力层的rank collapse问题，训练稳定性远优于纯注意力堆叠结构。
### 关键结果
在2B~31.5B参数量的全规模验证中，和参数匹配的全MoE基线对比：
- 训练GPU小时数降低30.5%~35.0%，验证集损失与基线基本持平；31.5B规模下节省33.3%GPU小时，下游任务平均得分小幅提升，推理吞吐量提升28%~36%。
- 节省的训练成本可置换为更多训练token：31.5B规模下用21%更少GPU小时训练1.25倍token，下游任务平均得分从66.26提升至66.67。
> 最值得记住：MoE效果不与MoE层数正相关，更少更宽的MoE层搭配更多token-mixing层，可同时降低训练推理成本并保持效果
