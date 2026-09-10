---
title: Difficulty-Adaptive Tree-Structured Policy Optimization for Expanding Reasoning
  Coverage in RLVR
title_zh: 面向RLVR推理覆盖度提升的难度自适应树结构策略优化
authors:
- Youngjun Yu
- Sanghwan Jang
- Hwanjo Yu
affiliations:
- POSTECH
arxiv_id: '2609.08650'
url: https://arxiv.org/abs/2609.08650
pdf_url: https://arxiv.org/pdf/2609.08650
published: '2026-09-07'
collected: '2026-09-10'
category: Training
direction: LLM推理训练 · RLVR策略优化
tags:
- RLVR
- Policy Optimization
- pass@k
- Tree-Structured Search
- Reasoning LLM
one_liner: 提出难度自适应句子熵引导的树结构策略优化DATPO，大幅提升RLVR训练的大模型推理覆盖度pass@k
practical_value: '- 做Agent推理/复杂Query理解的RL微调时，可复用难度自适应rollout策略，给难样本分配更多计算资源，避免简单样本过拟合浪费算力，提升模型泛化性

  - 需提升多候选召回/生成覆盖率（如推荐多兴趣召回、Agent多路径规划的pass@k）时，引入句子熵引导的树状采样，相同token预算下有效路径覆盖率比平行采样高20%以上

  - 多样性奖励设计可复用思路：仅对正样本路径加多样性奖励避免无效探索，同时随训练步长退火奖励系数，平衡探索效果与模型收敛速度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有RLVR（可验证奖励强化学习）训练只能提升大模型单样本推理准确率，却无法有效扩展模型内在推理覆盖度（pass@k）：训练时探索不足导致模型仅收敛到少量已知正确路径，测试时多数投票、best-of-N等 scaling 策略上限极低，哪怕大幅增加候选采样数量也很难产出新的有效路径。
### 方法关键点
- 提炼三大rollout设计原则：难度自适应分配算力不是单纯的效率优化手段，而是提升pass@k的核心策略；树状rollout比平行采样的正确答案发现效率更高；token级分支选择存在局部化问题，需提升到语义级粒度优化。
- 训练时先预估样本难度，越难的样本分配越多树扩展分支，简单样本减少冗余计算避免过拟合；采用句子级熵选择分支点，避免高熵token集中在局部导致的探索范围狭窄问题。
- 优势函数加入随训练退火的兄弟多样性奖励，仅给正样本路径增加多样性激励，既鼓励探索不同有效路径，又避免无效错误路径的冗余探索。
### 关键实验
基于Qwen2.5-3B、Qwen3-4B base模型在MATH、AIME、AMC等数学推理数据集测试，对比GRPO、Dr.GRPO、TreeRL、AttnRL等SOTA RLVR基线：相比最强基线AttnRL，DATPO在Qwen2.5-3B上pass@k提升1.9，Qwen3-4B上pass@k提升3.0；测试时多数投票带来的性能增益达7.2%，比基线高16%。
### 核心结论
提升多候选覆盖度的核心不是盲目增加采样数量，而是通过难度自适应分配算力、语义级分支选择最大化有效探索的效率。
