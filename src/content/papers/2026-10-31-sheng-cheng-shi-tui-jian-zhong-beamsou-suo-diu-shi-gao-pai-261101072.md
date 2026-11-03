---
title: Where Beam Search Loses Top-Ranked Items:First-Step Coverage in Generative
  Recommendation
title_zh: 生成式推荐中Beam搜索丢失高排位物品的根源：解码首步覆盖瓶颈
authors:
- Heng Yao
- Hanwei Zhu
affiliations:
- Ant Group
- Independent Researcher
arxiv_id: '2611.01072'
url: https://arxiv.org/abs/2611.01072
pdf_url: https://arxiv.org/pdf/2611.01072
published: '2026-10-31'
collected: '2026-11-03'
category: GenRec
direction: 生成式推荐 · Beam搜索优化
tags:
- Generative Recommendation
- Semantic ID
- Beam Search
- TIGER
- Serving Optimization
one_liner: 发现生成式推荐Beam搜索首步覆盖瓶颈，通过宽度前置分配用半预算复现宽Beam的排序结果
practical_value: '- 部署Semantic ID架构的生成式推荐系统无需修改模型、训练逻辑，仅将Beam宽度前置分配（首步加宽度、后续步骤缩窄），同等预算下可提升Search
  Recall@10最高10.9pct，或同等效果下降低约6%的解码延迟

  - 上线优化前先离线计算全量item的精确打分得到模型真实top-K排序，统计各解码步骤的剪枝损失分布，针对性分配各步Beam宽度，避免盲目提升全局Beam宽度浪费算力

  - 若业务仅需输出top-5/top-10短推荐列表，采用宽度前置的调度策略可将宽Beam的算力成本降低近50%，且完全对齐原宽Beam的排序结果，无效果损耗'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐普遍采用均匀宽度Beam搜索，算力会被无差别分配到每个Semantic ID解码步骤，而高排位物品被剪枝的损失来源一直未被精确定位，工业界急需不重训模型、不改变排序逻辑即可降低推理成本、提升搜索保真度的落地方案。
### 方法关键点
- 离线计算全量item的精确打分得到模型真实top-K排序，定义Search Recall@K衡量Beam搜索结果与真实排序的保真度，统计每个item被首次剪枝的解码步骤定位损失来源
- 总前缀容量预算固定的前提下，设计非均匀Beam宽度调度策略，将更多宽度分配到剪枝损失集中的解码首步，后续步骤逐步缩窄宽度，总算力与原有均匀Beam一致
- 全程不修改模型权重、Semantic ID规则、打分逻辑，避免业务上线的兼容性风险
### 关键实验
基于Amazon公开的Beauty、Sports、Toys三个电商数据集，在TIGER生成式推荐框架下，分别用RQ-KM和RQ-VAE两种Semantic ID tokenizer测试，对比基线为均匀Beam-50（预算151）、均匀Beam-100（预算301）：
- 首步宽度前置的Front-151策略（与Beam-50预算相同），Search Recall@10比均匀Beam-50提升0.96~10.90个百分点，效果接近预算高一倍的Beam-100
- 对RQ-VAE tokenizer的全量77373个测试用户，Front-151可100%复现Beam-100的top-10排序结果，解码延迟降低6.35~6.39%
### 核心结论
生成式推荐Beam搜索优化不要盲目提升全局宽度，先定位剪枝损失的发生步骤，针对性分配算力投入，才能用更低成本拿到更好的效果
