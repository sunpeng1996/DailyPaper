---
title: Rethinking Routing Exploration in Modern Mixture-of-Experts
title_zh: 重新思考现代混合专家模型路由探索：MirrorMoE优化方案
authors:
- Bingcong Li
- Hao Ma
- Michael Muehlebach
- Niao He
- Yi Ma
affiliations:
- ETH Zurich
- The University of Hong Kong
- Max Planck Institute for Intelligent Systems
- WU Vienna
arxiv_id: '2610.22353'
url: https://arxiv.org/abs/2610.22353
pdf_url: https://arxiv.org/pdf/2610.22353
published: '2026-10-15'
collected: '2026-10-16'
category: Training
direction: MoE训练 · 路由探索优化
tags:
- MoE
- Routing Optimization
- Pre-training
- Shared Expert
- MirrorMoE
one_liner: 发现共享专家+细粒度分割MoE的路由探索困境，提出MirrorMoE自适应压缩探索空间提效
practical_value: '- 多目标推荐/广告的MoE架构可直接复用问题诊断逻辑：若增加共享专家后提升激活专家数K效果不升反降，可排查是否存在共享专家权重过高、路由探索被压制的问题

  - 可零成本迁移MirrorMoE路由trick到现有MoE结构：仅需修改路由层为原始+负logits镜像分布加权，聚合时用原始路由权重，训练后期cosine退火超参ρ，无额外推理开销即可提升效果

  - MoE负载均衡优化可复用：仅对高贡献的功能激活专家做负载均衡，忽略低权重被抑制的专家，既提升训练稳定性还能小幅降低训练耗时

  - 多技能Agent的工具/技能路由MoE同样适用：解决通用技能共享模块压制细分技能路由探索的问题，提升多技能调用的准确率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前主流MoE架构普遍采用「细粒度专家分割+共享专家」的组合设计：前者通过增大总专家数E和激活专家数K，获得组合更丰富的表达能力；后者让所有token激活固定专家学习通用特征，减少冗余学习。但二者存在固有矛盾：细粒度分割带来组合爆炸的路由空间，需要更强的路由探索能力，而共享专家会主导token表示生成，导致切换路由专家带来的输出方差极低，路由探索有效性被大幅削弱，最终出现增大K反而效果下降、共享专家收益消失的探索困境。
### 方法关键点
- 镜像路由：路由概率由原始路由分布（偏好高logit专家）和负logits生成的镜像分布（偏好低logit专家）加权求和得到，超参ρ控制镜像分布权重，训练阶段用cosine schedule将ρ退火到0
- 镜像聚合：激活专家仅用原始路由概率加权，低logit专家即使被激活，贡献权重也极低，被功能抑制，自适应压缩有效探索空间，匹配模型探索能力
- 负载均衡loss优化：仅针对原始路由概率做专家负载均衡，忽略被抑制的低贡献专家，降低训练不稳定风险
### 关键实验
在DCLM公开数据集上训练100M~2.4B共4个不同规模的带共享专家MoE，对比带/不带共享专家的基线MoE：
- 2.4B规模下，预训练perplexity降低0.67，6个下游常识推理任务平均得分提升1.64
- 激活专家数K从6提升到10时，基线共享专家MoE出现效果负增长，MirrorMoE保持效果随K增大持续提升，且始终优于无共享专家的MoE
- 训练单步耗时几乎无增加，甚至因负载更均衡略有降低

带共享专家的MoE性能瓶颈往往不是表达能力不足，而是路由探索能力与扩大的路由空间不匹配，自适应压缩探索空间比强行提升探索强度更高效
