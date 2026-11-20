---
title: A Model of Diverse Sampling from Language Models
title_zh: 基于行列式点过程的大语言模型多样化采样方法PoolDPP
authors:
- Manuel Prada-Corral
- Yahya Emara
- Timothy J. O'Donnell
- Ryan Cotterell
- Tim Vieira
affiliations:
- ETH Zürich
- MPI-IS
- ELLIS Institute Tübingen
- Cornell University
- McGill University
arxiv_id: '2611.25003'
url: https://arxiv.org/abs/2611.25003
pdf_url: https://arxiv.org/pdf/2611.25003
published: '2026-11-18'
collected: '2026-11-20'
category: LLM
direction: LLM解码 · 多样化采样优化
tags:
- DPP
- Diverse Sampling
- LLM Decoding
- Determinantal Point Process
- Pareto Frontier
one_liner: 提出PoolDPP框架结合DPP实现LLM输出质量-多样性平衡，附带有限样本误差保证
practical_value: '- 电商搜索query推荐、商品推荐的多样性重排可复用PoolDPP双温度设计：本地温度采样候选池，全局温度调整质量-多样性权重，效果优于传统MMR、K-means重排

  - Agent多轮工具调用结果召回、生成式回答多视角输出场景，可直接用PoolDPP-MAP做确定性多样选择，在歧义理解任务上比K-means高2.5%的有效意图覆盖率

  - 业务场景可按需选择推理模式：需要可重复结果用PoolDPP-MAP，需要多轮随机多样输出用PoolDPP-Sampling，两者选择开销远低于LM采样开销，工程落地成本低'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有LLM独立采样输出易聚类在相同语义模式，传统温度采样、启发式多样性解码缺乏全局一致的多样性定义，无法平衡输出质量与语义多样性，在歧义问题解决、多视角生成、开放域推理等场景效果受限。

### 方法关键点
- 用K-DPP建模多样化采样任务，将每个输出的归一化嵌入方向作为相似度判断依据，嵌入模长乘以LM输出概率的1/T次方（T为全局温度）作为质量项，子集概率与质量加权嵌入张成的体积平方成正比，自然实现质量和多样性的联合优化
- PoolDPP近似推理框架：先通过局部退火的祖先采样得到N个候选，对候选做重要性权重校正匹配全局退火质量分布，再在候选池上运行K-DPP采样，提供两种推理模式：随机采样的PoolDPP-Sampling和确定性贪心MAP选择的PoolDPP-MAP
- 有限样本理论保证：PoolDPP-Sampling输出分布与目标K-DPP的KL散度随候选池大小N以O(1/N)速率衰减

### 关键实验
在三类任务上验证效果：FineWeb开放生成、Ambrosia歧义文本转SQL、GSM8K数学推理，对比基线包括温度采样、K-means重排、MMR、多样波束搜索等。核心结果：1）Ambrosia任务上PoolDPP-MAP在同等精度下覆盖率比K-means高2.5%，推高召回-精度帕累托前沿；2）GSM8K任务上PoolDPP在pass@K下降不超过0.01的前提下，多样性比基线最高提升52%；3）候选池构建占90%以上 runtime，DPP选择开销可忽略。

最值得记住的结论：通过嵌入几何定义语义多样性、双温度分别控制候选池分布和质量-多样性权衡的DPP采样框架，是兼顾理论保证和落地可行性的LLM多样化生成方案。
