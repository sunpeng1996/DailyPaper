---
title: 'Preference Is Not Position: Evaluating Reranking on NevIR in Fixed Hybrid
  Candidate Pools'
title_zh: 固定混合候选池下NevIR任务重排序评估：偏好不等于位置
authors:
- Yuning Bian
- Lele Xu
- Yifan Yuan
- Xinyu Yin
- Chengyan Zhan
affiliations:
- Anhui University of Technology
arxiv_id: '2610.26260'
url: https://arxiv.org/abs/2610.26260
pdf_url: https://arxiv.org/pdf/2610.26260
published: '2026-10-19'
collected: '2026-10-20'
category: Eval
direction: 检索重排序 · 评估指标体系优化
tags:
- Reranking
- Evaluation
- NevIR
- Hybrid Retrieval
- Cross-Encoder
- LLM
one_liner: 揭示重排序局部pairwise偏好与目标文档位置的不一致性，提出多指标联合评估方案
practical_value: '- 重排序评估不能仅看pairwise偏好准确率，必须新增目标item的位置类指标（MRR、TopK占比），避免出现偏好正确但结果排太靠后无法触达用户的问题，尤其适配电商搜索/推荐用户仅浏览前几屏的业务特性

  - 训练排序模型时仅喂正负pair监督信号会导致目标item全局排序位置暴跌，可加入随机采样的背景候选作为弱监督，兼顾pair偏好准确性和全局排序效果

  - 落地LLM重排序时可仅对第一阶段融合的Top20候选打分，用原有融合分数作为tie-breaker，能同时提升偏好准确率和MRR，还可严格控制推理延迟，适配电商低延迟要求

  - LLM打分的同档位tie是剩余错误的主要来源，可针对tie的候选新增细粒度判异逻辑，无需全量调整就能进一步提升效果'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有重排序评估通常仅关注pairwise偏好准确率，忽略目标结果在全候选池的实际排序位置，尤其在含否定等强区分条件的检索场景下，即使偏好顺序正确，目标结果排靠后也完全无法被用户触达，无法衡量真实业务价值。

### 方法关键点
- 固定候选池为dense embedding、learned sparse、BM25三路检索结果的并集，所有对比方法共用同一候选集，排除检索环节差异的干扰
- 同时评估两个核心指标：严格per-query偏好准确率（目标文档得分严格高于反例的占比）、目标文档的全池MRR（衡量可触达性）
- 对比四类方案：固定加权融合baseline、仅用正负pair训练的LambdaMART、加入背景候选弱监督的LambdaMART、仅对融合Top20做LLM/交叉编码器重排序+融合分数tie-breaking的方案

### 关键结果
实验基于NevIR否定感知检索基准，共2736条测试query、1363对仅差否定的近同文档对：
1. 仅pair训练的LambdaMART偏好准确率比融合baseline高4.32pct（56.62% vs 52.30%），但MRR暴跌近一半（0.3055 vs 0.5764）
2. 加入8个随机背景候选弱监督的LambdaMART，MRR恢复到0.5859，偏好准确率仍高于baseline 2.23pct
3. 融合Top20+Qwen3-14B重排序方案，偏好准确率达77.45%、MRR达0.7509，较baseline分别提升25.15pct和0.1745；BGE交叉编码器对应指标为69.77%和0.7404
4. 27%的query出现LLM打分档位相同的情况，贡献了61%的剩余偏好错误

> 最值得记住的结论：重排序的业务价值由「偏好正确性」和「目标结果的可触达位置」共同决定，二者不可割裂评估
