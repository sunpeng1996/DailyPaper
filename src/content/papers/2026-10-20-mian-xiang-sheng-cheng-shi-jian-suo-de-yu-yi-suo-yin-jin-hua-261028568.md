---
title: Evolving Semantic Indexes for Generative Retrieval
title_zh: 面向生成式检索的语义索引进化优化框架
authors:
- Jinming Nian
- Jyun-Yu Jiang
- Henry Tsai
- Yi Fang
- Zhirong Liang
affiliations:
- Santa Clara University
- Coupang
arxiv_id: '2610.28568'
url: https://arxiv.org/abs/2610.28568
pdf_url: https://arxiv.org/pdf/2610.28568
published: '2026-10-20'
collected: '2026-10-21'
category: GenRec
direction: 生成式检索 · Semantic ID自动优化
tags:
- Generative Retrieval
- Semantic ID
- Evolutionary Search
- Proxy Evaluation
- LLM
one_liner: 用开源本地LLM+轻量代理模型自动进化优化生成式检索的语义索引组件
practical_value: '- 做Generative Retrieval的Semantic ID迭代时，可引入1M参数量级的小代理模型做候选方案预筛选，单轮评估成本较训1B级模型降低15倍，大幅提升迭代效率

  - 可直接复用论文验证有效的SID优化trick：残差量化用余弦相似度代替欧氏距离匹配、SID训练加入query相关性对齐损失、碰撞后缀按组内语义质心相似度排序，均能稳定涨点

  - 用进化搜索优化GR pipeline时，优先固定训练/解码策略仅优化SID这类大小模型共享的结构，不要同时优化大模型训练目标，避免小代理的优化结果与大目标负相关

  - 无需依赖商用LLM API，本地部署30B级开源模型即可完成代码级的GR组件进化搜索，成本可控，适合业务侧快速试错'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式检索（GR）的效果高度依赖Semantic ID（SID）的设计，但SID构建、碰撞处理、训练目标等环节是离散且相互依赖的，无法通过端到端反向传播优化，长期依赖人工经验设计，迭代效率低；若每轮候选方案都训练1B级的GR模型做评估，计算成本极高，无法支撑大规模方案搜索。

### 方法关键点
- 两层进化框架：外层用本地部署的Gemma-4-31B-it开源模型作为变异器，对SID构建与碰撞处理的代码做SEARCH/REPLACE式变异，基于岛群进化算法维护候选种群，全程不调用商用LLM API
- 轻量代理评估：用1M参数的2层GPT-2作为代理评估器，仅用训练集数据训练，以Recall@100作为适应度分数，单轮评估耗时较训1B目标模型缩短15倍，大幅降低搜索成本
- 候选准入门控：过滤碰撞率>50%、运行超时、存在代码错误的无效候选，减少不必要的评估开销

### 关键实验结果
在NQ320K、MSMARCO300K、Coupang多语言电商数据集上验证，对比基于RQVAE+TIGER的种子GR系统：
1. NQ320K上联合进化SID与碰撞处理，Recall@1从55.8%提升至59.3%，Recall@100从85.8%提升至90.6%，代理与目标模型的Recall@100斯皮尔曼相关系数达0.90
2. 电商数据集上，SID进化后Recall@100相对BM25的增益从49.01pp提升至50.66pp

### 核心结论
代理评估的迁移性与优化的组件强相关，仅优化SID这类大小模型共享的结构时效果最稳定，优化大模型训练目标时小代理的结果反而会产生误导。
