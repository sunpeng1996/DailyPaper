---
title: 'The Resolution Hypothesis: Agent Evolution''s Key Is Identifying Improvements'
title_zh: 分辨率假说：Agent进化的核心瓶颈是有效识别性能提升
authors:
- Yuanhao Zeng
- Shaocheng Lan
- Ao Lu
- Kuang Yan
- Heng Lin
- Xinang Xu
- Yuan Luo
- Yueting Wang
- Yexin Li
- Ruo Shan
affiliations:
- ShanghaiTech University
- ByteDance
- BIGAI
- SUSTech
arxiv_id: '2611.23068'
url: https://arxiv.org/abs/2611.23068
pdf_url: https://arxiv.org/pdf/2611.23068
published: '2026-11-17'
collected: '2026-11-18'
category: Agent
direction: Agent自进化 · 评估噪声分析
tags:
- AgentEvolution
- EvaluationNoise
- SelfImprovingAgent
- LLMAgent
- ResolutionHypothesis
one_liner: 提出Agent进化的分辨率假说，验证其瓶颈为评估噪声而非候选生成能力
practical_value: '- 做自进化Agent（如导购Agent、推荐prompt自动优化）时，优先提升评估分辨率而非迭代提案算法：提案质量足够的前提下，噪声大的评估会让选择接近随机，白白浪费算力

  - 评估自进化算法效果时，必须做多次独立跑测+多次重评：现有文献中3.4pp的中位数提升远小于单跑标准差，单次跑测结果可信度极低，避免业务上线踩坑

  - 电商/推荐场景的自动prompt迭代、Skill优化可引入细粒度中间行为校验：比如导购Agent是否正确查询商品库、是否命中用户需求标签，这类指标的噪声比最终转化的端到端指标低13~57倍，能大幅提升选择准确率

  - 评估不同进化算法时可拆分提案和选择组件分别评测：用Quality@K衡量提案质量，用固定候选池的选择准确率衡量选择器效果，避免端到端噪声掩盖组件优劣'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前Agent自进化范式效果极不稳定：同方法在不同基准上表现波动剧烈，不同论文的方法排名经常反转，进化常陷入停滞，工业界落地自进化Agent（如导购Agent、自动prompt优化）时可复现性差、投入产出比不可控，底层原因缺乏系统性验证。

### 方法关键点
- 提出**分辨率假说**：Agent进化的核心瓶颈不是提案模块无法生成优质候选（prompt、技能、记忆等），而是评估噪声过大，无法可靠识别真实性能提升
- 超大规模实验设计：覆盖7种主流进化方法、6款SOTA LLM、4个权威Agent基准，累计完成1030次独立进化跑测、210万+测试轨迹、超1000万次LLM调用，是目前规模最大的Agent进化可复现性研究
- 分层验证逻辑：拆解评估噪声σ和跑测间方差τ两个波动来源，分别在方法级（不同算法排名）和候选级（单轮候选选择）验证假说

### 关键结果
- 方法级：现有文献中算法提升中位数仅3.4pp，远小于单跑标准差（1.7~4.5pp），Terminal-Bench上单跑选出4种最优算法的概率仅33%，接近随机选择的25%
- 候选级：候选池存在能带来最高8.3pp真实提升的优质候选，但现有选择机制（执行得分、LLM judge）的两两选择准确率仅45%~49.7%，和随机选择无统计差异
- 报告的大提升几乎都来自评估捷径：单条适配评估规则的语句就能复现90%的报告提升，修复评估逻辑后提升中位数从17.6pp降至0.8pp

### 核心结论
对自进化Agent而言，更高分辨率的反馈和更鲁棒的评估体系，比更强大的进化算法更重要
