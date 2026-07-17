---
title: LLM-Based Re-Ranking for Real Estate Search
title_zh: 面向房产搜索场景的大语言模型重排序落地方法
authors:
- Nkateko Ntimane
- Rafel Guedes
- Tiago Cunha
- Pedro Nogueira
affiliations:
- QuintoAndar
- Growthloop
arxiv_id: '2607.14835'
url: https://arxiv.org/abs/2607.14835
pdf_url: https://arxiv.org/pdf/2607.14835
published: '2026-07-16'
collected: '2026-07-17'
category: RecSys
direction: 对话式搜索推荐 · LLM重排序落地
tags:
- LLM-Rerank
- Conversational-Search
- Point-wise-Ranking
- LLM-as-Judge
- A-B-Testing
one_liner: 面向房产对话搜索提出point-wise LLM重排方案，生产实现CTR+5.3%、预约到访+4.8%
practical_value: '- 可复用轻量化LLM重排架构：无需重构现有召回链路，仅对top-k候选做point-wise并行打分，latency可控，适合电商/本地生活/房产等垂类对话搜索业务快速上线验证

  - 用户偏好表征技巧：将不同权重的历史行为信号（点击弱、收藏/转化强）转为自然语言软偏好而非硬过滤规则，可有效捕捉用户隐含的权衡类需求（如愿意超预算换特定配套）

  - 低成本标注方案：缺少人工标注时，可采用合成query覆盖长尾场景+LLM-as-Judge标注+少量人工校验的范式，快速构建大规模领域relevance数据集

  - point-wise打分优化技巧：加入候选池统计特征（如当前候选的价格中位数、配套覆盖率），可解决单样本打分一致性问题，无需上高成本的list-wise方案即可获得相对收益'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
传统房产搜索依赖结构化过滤菜单，无法捕捉用户多维度、上下文依赖的隐含需求（如区位偏好、生活方式诉求、预算权衡等），对话式搜索成为用户交互新趋势，但现有排序模块无法有效利用多轮对话的丰富上下文；同时端到端生成式检索改造成本高、latency无法满足生产要求，需要低侵入的优化方案。
## 方法关键点
- 轻量化两阶段架构：传统检索模块生成候选集，LLM重排仅对top候选做point-wise并行打分，无需重构现有链路，满足交互类业务latency要求
- 自然语言用户画像构建：融合历史会话、多权重行为信号（点击<收藏<预约）、历史画像，信号冲突时优先最新显式表述，行为信号转为软偏好而非硬约束
- 多维度打分上下文：输入包含用户query、结构化过滤条件、文本用户画像、房产元数据+自由描述、候选集统计特征（价格区间、配套覆盖率等），输出0-1匹配度分排序
- 低成本数据集构建：合成6类覆盖长尾场景的query+生产真实query，采用LLM-as-Judge标注+少量人工校验，生成96万query-item对的领域测试集
## 关键结果
- 离线：全配置相比基线nDCG@5提升15.5%，Recall@5提升6.3%；加入候选集统计特征、房产自由描述、文本用户画像分别带来0.8%、0.9%、2.8%的nDCG@5增益
- 线上A/B测试：相比基线CTR提升5.3%，预约到访提升4.8%，端到端latency仅增加4.2s，推理成本上升7%，业务收益远高于投入成本
- LLM-as-Judge偏好评估：95%的测试样本更偏好重排后的排序结果
## 核心结论
对话式推荐场景下，仅在重排层接入LLM做point-wise打分是兼顾效果、latency、改造成本的可行落地方案，无需端到端重构检索架构即可拿到显著业务收益
