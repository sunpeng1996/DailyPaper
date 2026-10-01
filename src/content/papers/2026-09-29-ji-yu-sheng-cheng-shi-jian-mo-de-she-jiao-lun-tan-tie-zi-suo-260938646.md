---
title: Exploring Forum Post Retrieval with Generative Modeling
title_zh: 基于生成式建模的社交论坛帖子检索方案探索
authors:
- Yang Li
- Yaguang Liu
- Heng Liu
- Shengbo Guo
- Samson Komo
- Jane Kou
- Yulian Zhou
- Gang Yang
- Shubhojeet Sarkar
- Gaurav Chakravorty
affiliations:
- William & Mary
- Meta
arxiv_id: '2609.38646'
url: https://arxiv.org/abs/2609.38646
pdf_url: https://arxiv.org/pdf/2609.38646
published: '2026-09-29'
collected: '2026-10-01'
category: GenRec
direction: 生成式推荐 · Semantic ID跨域迁移
tags:
- Generative Recommendation
- Semantic ID
- RQ-VAE
- SFT
- Cold Start
- LLM4Rec
one_liner: 针对冷启动新推荐场景，提出基于跨平台Semantic ID迁移的生成式推荐落地方案与设计指南
practical_value: '- 冷启动场景可直接复用成熟业务预训练的RQ-VAE层级Semantic ID，无需为新场景单独训练ID编码器，大幅降低冷启动数据成本

  - 生成式推荐优先选择3层2048码本的SID配置，HR@10是4层SID的2.2倍，后续接轻量排序层即可解决SID碰撞问题，性价比最优

  - 训练成本优化：优先给用户行为历史增加动作类型标注的Prompt模版，收益高于文本-SID对齐预训练且无额外训练成本；优先选择3B级小基座，效果与12B大模型几乎一致，推理成本降低75%

  - 生成式推荐场景暂时无需尝试GRPO/DPO等RL后训练方法，输出仅3-4个token导致奖励稀疏度超过95%，无正向收益且浪费算力'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
新上线的推荐场景（如Facebook Forum）交互数据极稀疏，无法从零训练生成式推荐模型，传统嵌入检索的跨域迁移成本高，亟需探索低成本的冷启动生成式推荐落地路径。
### 方法关键点
- 跨域ID复用：直接复用Facebook Feed数据预训练RQ-VAE生成的层级前缀Semantic ID，支持3层/4层配置，每层2048个编码，语义相近内容共享前缀，无需为新场景单独训练ID编码器
- 两阶段微调：第一阶段用原生存在的「帖子文本↔SID」双向配对数据做对齐，让LLM习得SID的语义关联；第二阶段基于用户包含强弱交互的时序行为序列做SFT，直接生成用户下一个正交互的帖子SID
- 训练优化：采用固定长度10的行为历史，Prompt为每个行为增加动作标注（如点赞、浏览），仅对输出的SID token计算损失
### 关键结果
实验基于Facebook Groups真实交互数据，测试集覆盖86648名用户，核心结论：
1. 3层SID的HR@10达0.0667，是4层SID的2.2倍，为影响效果的最核心因素
2. 带动作标注的Prompt比纯SID序列Prompt HR@10高2%，收益高于单独做文本-SID对齐预训练
3. Llama 3.2 3B效果与12B Gemma几乎持平（HR@10仅差0.9%），推理成本仅为后者的1/4
4. GRPO后训练无正向收益，HR@10比SFT基线低2.4%，95%的训练批次无有效奖励信号
### 核心记忆点
生成式推荐落地时，低成本的设计选择（SID层数、Prompt模版、小基座）对效果的影响远大于高成本的大模型、长序列、RL后训练
