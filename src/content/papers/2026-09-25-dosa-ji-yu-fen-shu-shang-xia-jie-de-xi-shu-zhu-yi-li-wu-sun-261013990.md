---
title: 'DoSA: Dots Sparse Attention'
title_zh: DoSA：基于分数上下界的稀疏注意力无损加速方法
authors:
- Fanxu Meng
- Taosong Fang
affiliations:
- Dots Studio, Xiaohongshu Inc.
arxiv_id: '2610.13990'
url: https://arxiv.org/abs/2610.13990
pdf_url: https://arxiv.org/pdf/2610.13990
published: '2026-09-25'
collected: '2026-10-14'
category: LLM
direction: 长上下文LLM · 稀疏注意力推理加速
tags:
- Sparse Attention
- Long-Context LLM
- Inference Optimization
- Top-K Pruning
- GPU Acceleration
one_liner: 通过分数上下界预筛候选token，无损加速长上下文大模型的稀疏注意力索引器
practical_value: '- 长上下文RAG/商品检索场景可复用上下界剪枝思路：先取召回结果种子集的K大分数做阈值下界，给每个候选算排序分上界，直接筛除上界低于下界的候选，减少全特征排序的计算量

  - 大规模推荐排序的GPU kernel优化可参考其执行流程：先做轻量粗筛丢弃大部分负例，仅对幸存候选做全特征精排+稀疏写回，大幅降低HBM带宽占用和计算量

  - 长会话Agent的解码阶段可复用时间相关性阈值优化：用最近几轮交互选中的token作为种子集生成筛选阈值，减少解码阶段的Top-K选择开销，提升响应速度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文LLM的稀疏注意力架构中，负责筛选Top-K候选token的索引器成本随上下文长度飙升，1M token时占prefill阶段GPU时间的73%~90.8%；现有Top-K加速方案仍需对每个候选做全头打分，成为长上下文推理的核心瓶颈。
### 方法关键点
- 剪枝逻辑：选取至少K个候选作为种子集，取其K大分数作为真实Top-K阈值的下界；为每个候选构造分数上界，上界低于下界的候选直接被筛除，保证无损不丢有效候选
- 分数界构造：优先保留权重高、激活难预测的索引头直接计算得分；对省略的正权重头用非负投影构造得分上界，对省略的负权重头用激活感知的聚合构造扣减下界，保证上界足够紧致
- GPU实现：分轻量预筛、幸存候选全头打分、稀疏写回三阶段，通过查询分组、多查询共享Key加载降低访存开销，适配Tensor Core密集计算特性
### 关键结果
在GLM-5.2、DeepSeek-V3.2上测试英文、中文、代码三类长文本 workload：1M token上下文下，索引器速度最高比SGLang快2.74×、比LiteTopK快1.69×；端到端Time-to-First-Token（TTFT）最高比SGLang快1.94×，接近减半长上下文首包延迟；平均97%以上的候选可在预筛阶段被直接丢弃，无需全头打分。

> 最值得记住：精确Top-K选择不需要计算每个候选的完整分数，仅需要足够证据证明某候选不可能进入Top-K即可将其提前筛除。
