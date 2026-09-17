---
title: 'Beyond Truncation: Rethinking LLM Decoding as Ensemble Pruning'
title_zh: 超越截断：将LLM解码问题重构为集成剪枝任务
authors:
- Dunyao Xue
- Chengshuo Du
- Zhengbo Wang
- Wenlin Dai
- Cheng Meng
affiliations:
- Institute of Statistics and Big Data, Renmin University of China
- Big Data and Responsible Artificial Intelligence for National Governance, Renmin
  University of China
- Center for Applied Statistics, Renmin University of China
arxiv_id: '2609.18723'
url: https://arxiv.org/abs/2609.18723
pdf_url: https://arxiv.org/pdf/2609.18723
published: '2026-09-16'
collected: '2026-09-17'
category: LLM
direction: LLM 解码优化 · 集成剪枝
tags:
- LLM Decoding
- Ensemble Pruning
- Mahalanobis Distance
- Inference Optimization
- Generation Quality
one_liner: 提出融合token概率与语义几何的ME-Decoding框架，显著提升LLM推理与生成性能
practical_value: '- 电商文案生成、广告创意生成、Agent推理环节可直接接入ME-Decoding作为解码组件，相比Top-p/Min-p等传统方案，在高温度采样下仍能维持输出逻辑一致性，幻觉率降低的同时保留生成多样性

  - 可将「概率+语义相似度联合选点」的思路迁移到生成式推荐的Semantic ID生成、搜索query推荐的候选截断环节，解决现有概率截断导致的候选冗余问题，优化准确率与多样性的权衡

  - 工程上可复用自适应带宽核、增量Cholesky因子更新、单峰早停等trick，无需微调模型参数，额外推理开销极小，适配高吞吐的搜索/推荐/广告推理链路'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM解码策略多仅基于标量概率做截断，忽略token间的语义几何关联，导致候选冗余、高温度采样下幻觉率飙升；已有的几何感知解码方法要么计算开销高、要么依赖后处理导致推理不稳定，无法兼顾质量、效率与多样性，限制了LLM在工业生成场景的落地。
### 方法关键点
- 将LLM解码重构为集成剪枝任务：把候选token视为集成成员，token概率对应个体置信度，嵌入空间相似度对应语义冗余度，联合优化精度与多样性
- 设计Mahalanobis-Ensemble Score（MES）作为优化目标，通过自适应带宽高斯核构造token相似度矩阵，马氏距离天然降权高冗余候选，同时引入熵正则约束候选集规模
- 提出近线性复杂度的贪心选择算法，增量维护Cholesky因子避免重复矩阵求逆，基于MES序列单峰性实现早停，有理论近似最优保证
### 关键实验
在GSM8K、GPQA推理任务，AlpacaEval、MT-Bench开放生成任务上对比Min-p、Top-p、p-less、Top-W等SOTA解码方法：GSM8K平均准确率72.66%，较次优方案高2.04pp；GPQA平均准确率32.96%，较次优方案高1.4pp；开放生成任务平均排名第一，CPU推理开销仅为Top-W的1/2.7~1/7.4，接近传统概率截断方法。
最值得记住的结论：LLM解码的核心不是保留最高概率的token，而是选择高置信度且语义互补的最小候选集。
