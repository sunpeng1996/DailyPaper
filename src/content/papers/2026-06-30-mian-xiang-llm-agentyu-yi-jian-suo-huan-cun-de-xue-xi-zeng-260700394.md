---
title: 'When Classic Cache Policies Fail: Learning-Augmented Replacement for Semantic
  Retrieval Buffers'
title_zh: 面向LLM Agent语义检索缓存的学习增强替换框架SOLAR
authors:
- Yushi Sun
- Bowen Cao
- Wai Lam
affiliations:
- Tencent LIGHTSPEED
- The Chinese University of Hong Kong
arxiv_id: '2607.00394'
url: https://arxiv.org/abs/2607.00394
pdf_url: https://arxiv.org/pdf/2607.00394
published: '2026-06-30'
collected: '2026-07-08'
category: Agent
direction: Agent 语义检索缓存替换策略优化
tags:
- Semantic Cache
- LLM Agent
- Cache Replacement
- Online Learning
- Thompson Sampling
one_liner: 揭示经典缓存策略在语义工作负载下失效，提出带理论保证的SOLAR框架，相对FIFO最多提升75%
practical_value: '- 电商/客服类长会话Agent可直接替换原有LRU/LFU缓存策略，紧容量（缓存10-50条历史）下用SOLAR可提升20%+回复准确率，额外开销<1ms几乎无感知

  - RAG动态记忆池（如用户行为/会话历史池）不要盲目扩容，实测条目超1000后检索精度会因语义混淆下降，可引入SOLAR的后悔门控准入机制控制池大小，维持高信噪比

  - 语义匹配类缓存业务选型时优先以FIFO为baseline，经典LRU/LFU/ARC策略在该场景下大概率表现比FIFO差，不要默认复用

  - 算力有限场景可单独复用SOLAR的准入控制模块（仅累计检索质量 regret 触发缓存更新），即可获得全框架70%以上的收益，改造工作量极小'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent 依赖检索缓存存储长会话/历史经验以突破上下文窗口限制，但现有缓存策略多沿用传统数据库的LRU/LFU等启发式规则，其假设的时间局部性、访问频率与效用相关性在语义匹配场景下完全不成立，实测经典策略甚至比简单FIFO表现更差，且缺乏理论保障，亟需适配语义工作负载的缓存替换方案。

### 方法关键点
- 首次将语义缓存问题建模为带切换开销的在线语义缓存替换问题，明确三个核心特征：软命中（检索质量连续而非0/1）、语义匹配（靠embedding相似而非精确ID命中）、效用非平稳（物品价值随话题漂移）
- 提出SOLAR框架包含两个协同模块：① 后悔门控准入：累计检索损失超过自适应阈值时才更新缓存，将缓存修改率压低到~17%，避免无用更新浪费开销；② 贝叶斯在线驱逐：为每个缓存项维护Beta后验分布，用Thompson采样选择驱逐目标，加入时序衰减和新奇度bonus适配非平稳场景
- 理论证明SOLAR的竞争比≤3（与缓存大小、时间 horizon 无关，FIFO竞争比为Ω(K)），驱逐 regret 为O(√(KT logT))，接近理论下界。

### 关键结果
在MemoryBench的LoCoMo（个人会话数据集）、DialSim（影视剧对话数据集）上对比8种缓存策略：紧容量（K=10）下SOLAR相对FIFO在LoCoMo提升22.7%、在DialSim提升75%；K=50下提升4.7%；当缓存容量超过有效工作集后FIFO反超，存在明确相变点；合成实验验证语义缓存容量约束来自检索噪声而非存储限制，池大小超过1000后检索质量下降55%。

### 核心洞见
语义检索场景下，判断是否需要更新缓存的时机比选择驱逐哪个物品更重要，经典缓存策略的前提假设完全不成立，不要盲目复用。
