---
title: 'APeB: Benchmarking Personalization Ability of Large Language Model Agents'
title_zh: APeB：大语言模型Agent个性化能力基准测试集
authors:
- Garry Yang
- Zizhe Chen
- Xinru Chen
- Yongqiang Chen
- Jianxiang Wang
- Deyu Zou
- Linyi Ding
- Jialiang Wu
- Yunzhong He
- Yu Gong
affiliations:
- The Chinese University of Hong Kong
- ByteDance
arxiv_id: '2607.03162'
url: https://arxiv.org/abs/2607.03162
pdf_url: https://arxiv.org/pdf/2607.03162
published: '2026-07-03'
collected: '2026-07-07'
category: Eval
direction: Agent个性化能力评测基准
tags:
- Personalization
- LLM Agent
- Benchmark
- E-commerce
- Query Refinement
one_liner: 基于真实电商行为日志构建含模糊意图的Agent个性化评测基准，揭示当前LLM早期搜索场景个性化短板
practical_value: '- 做模糊query场景下的个性化推荐/搜索时，可先增加一步历史感知的query改写模块（类似VQRA），仅使用同类别历史交互补全模糊意图，实测能稳定提升Hit@1，实现成本低收益明确

  - 构建内部LLM推荐/导购Agent的评测集时，可复用APeB的会话筛选逻辑：保留含多步query改写、多商品比对、异构交互（媒体+商品）的非平凡会话，避免用随机负例的「伪个性化」评测

  - Agent工作流选型要分场景：对用户明确query可采用ReAct等多步推理工作流提效，对早期模糊query不要盲目叠加复杂Agent流程，反而会放大意图理解错误降低效果

  - LLM做个性化排序时，无需默认塞入全量历史，优先选取和当前query同分类的历史交互即可，效果与取全量接近，还能节省context窗口占用'
score: 9
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前LLM Agent落地电商个性化场景时，普遍需处理用户模糊意图、异构嘈杂交互历史、高相似候选筛选三重核心挑战，但现有评测基准要么依赖用户人工明确的查询、要么采用简化历史/随机负例，无法真实衡量Agent在早期模糊搜索场景下的个性化推理能力，导致很多实验室效果优异的方案上线后表现不达预期。
### 方法关键点
- 从真实内容电商行为日志中筛选5648个非平凡购物会话：要求会话含至少2次query迭代改写、足够多浏览交互、最终购买和初始意图语义对齐，覆盖10+商品类目
- 每个评测case包含三部分：60天异构历史交互（含商品浏览/购买、视频/直播观看两类行为）、早期模糊intent query+后期明确refined query、用户浏览过的高相似hard候选集（含最终购买商品）
- 提出轻量优化基线VQRA：先基于同分类历史交互改写模糊intent query，再执行推荐任务，验证历史感知的query改写的增益
### 关键结果
- 对明确refined query，LLM+ReAct工作流Hit@1最高达43.3%，显著优于传统个性化商品搜索模型UniSAR的29.2%；但对模糊intent query，所有LLM的Hit@1仅23%~26%，甚至略低于UniSAR的25.9%，ReAct等多步推理流程增益极小甚至出现负向效果
- 无历史输入时LLM在intent query下Hit@1约22%，加入60条同分类历史后仅提升1~2个百分点，远低于UniSAR的84%提升幅度，说明当前LLM对历史偏好的提取利用能力存在明显短板
- 采用VQRA做query改写后，intent query下各LLM的Hit@1普遍提升1pct左右，最高达26.9%
### 核心结论
当前LLM的个性化能力短板核心不在语义匹配，而在模糊意图下对异构历史偏好的有效提取和利用，盲目叠加复杂Agent工作流反而会放大推理错误。
