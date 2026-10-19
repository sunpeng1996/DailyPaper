---
title: 'QD-Rec: Open-Ended Evolution of Recommendations via Quality-Diversity'
title_zh: QD-Rec：基于质量-多样性的开放式推荐进化方法
authors:
- Takashi Ishida
- Taro Makino
- Issa Sugiura
affiliations:
- Sakana AI
arxiv_id: '2610.23470'
url: https://arxiv.org/abs/2610.23470
pdf_url: https://arxiv.org/pdf/2610.23470
published: '2026-10-16'
collected: '2026-10-19'
category: GenRec
direction: 生成式推荐 · 质量多样性优化
tags:
- QD-Search
- LLM4Rec
- Contextual Bandit
- Explainable Recommendation
- Diversity Optimization
one_liner: 将质量多样性搜索与LLM结合，为固定候选池生成带自然语言解释的高价值多样化推荐集合
practical_value: '- 高 stakes 推荐场景（比如广告投放选品、大客户运营、新赛道选品）可复用「item+自然语言解释」的成对优化范式，同时兼顾推荐质量和理由多样性，避免单一排序带来的决策盲区

  - 多样性感知 Contextual Bandit 选品逻辑可直接迁移到冷启动探索场景，在有限试错预算下最大化覆盖不同用户兴趣/商品品类的探索边界

  - LLM 生成假设的进化算子（变异/交叉/探索）+ 局部邻域 novelty 校验的 pipeline 可复用在生成式推荐的理由生成模块，低成本提升推荐解释的多样性和说服力

  - 本地邻域盲测 pairwise 对比的评估逻辑可替代全局打分，降低 LLM-as-Judge 的成本和偏好偏差，适合中小预算的推荐效果评估'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐系统大多输出单一排序列表，在并购标的选择、高价值客户定向、科研文献筛选等高风险决策场景下，用户需要同时对比多个带决策理由的多样化选项，而非仅依赖排序结果。传统多样性优化多依赖重排序，无法开放式探索同一个物品的不同推荐理由，也无法复用历史优质理由作为迭代垫脚石。

### 方法关键点
- 定义开放式推荐任务为「item + 自然语言假设（推荐理由）」成对优化，目标是在有限评估预算下生成兼具高质量和高多样性的推荐集合
- QD-Rec 核心流程：1）用多样性感知 Contextual Bandit 从固定候选池选 item，平衡未覆盖区域探索和优质方向利用；2）LLM 基于归档的历史优质假设，通过变异/交叉/探索三种算子生成当前 item 的推荐理由；3）先通过 embedding 检索 k 近邻做新颖性校验，新颖的直接入档；4）不新颖的和最近邻做 LLM 盲测 pairwise 对比，胜出则替换旧条目
- 两个消融版本：移除 Bandit 用随机选的 Novelty+Evo，同时移除 Bandit 和进化算子的零样本生成版本 Novelty

### 关键结果
在4个领域（Goodreads 图书推荐、并购标的筛选、营销客户定向、AI 论文推荐）测试，对比消融版本、MMR/DPP 重排序基线：1）QD-Rec 在大部分 LLM 评判场景下平均质量最优，并购场景质量相对纯 Novelty 基线提升21%；2）多数场景下归档规模最大，语义区域覆盖比纯 Novelty 基线高1倍以上；3）成本仅比零样本版本高30%，单 run 最高成本约62美元。

### 核心记忆点
即使候选池固定，推荐理由的开放式探索也能大幅提升推荐系统的决策价值，质量多样性搜索是平衡推荐质量和多样性的低成本路径。
