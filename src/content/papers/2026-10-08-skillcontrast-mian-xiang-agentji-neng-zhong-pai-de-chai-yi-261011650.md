---
title: 'SkillContrast: Difference-Guided Text Selection for Agent Skill Reranking'
title_zh: SkillContrast：面向Agent技能重排的差异引导文本选择方法
authors:
- Jiandong Ding
- Honglei Ji
- Ming Liu
- Tao Duan
affiliations:
- 华为技术有限公司
- 同济大学附属上海东方医院
arxiv_id: '2610.11650'
url: https://arxiv.org/abs/2610.11650
pdf_url: https://arxiv.org/pdf/2610.11650
published: '2026-10-08'
collected: '2026-10-09'
category: Agent
direction: Agent 技能检索重排优化
tags:
- Agent Skill Retrieval
- Reranking
- Text Selection
- Training-free
- MMR
one_liner: 无需训练的Agent技能重排文本选择器，保留候选差异文本，降本同时提升重排准确率
practical_value: '- Agent技能检索场景可直接复用该无训练差异文本选择策略，无需微调Reranker即可提升相似技能区分度，降低高相似技能误召回风险，适配电商导购Agent、客服Agent的工具调用选择场景

  - 长文档重排场景可借鉴「候选差异+局部上下文」的文本截断思路，相比仅按query相关性选片段，能保留候选间核心区分信息，同时减少Reranker输入token量50%左右，降低推理算力成本

  - 电商相似商品/内容重排场景可迁移该思路，提取同赛道商品的差异化卖点（参数、价格、权益）作为大模型重排输入，提升精准推荐效果的同时降低大模型重排的算力开销'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agent技能检索的重排阶段，若仅按query相关性选择输入文本，会保留高相似技能的共享说明、遗漏适用条件、前置要求等差异信息，容易召回满足query语义但不符合实际使用条件的风险技能；若输入全量技能文本，又会带来过高的推理算力开销。

### 方法关键点
- 无训练设计：无需微调Reranker，仅对召回的候选技能做文本预处理
- 聚类对比：用TF-IDF相似度对召回的top20候选技能聚类，同簇内逐行对齐提取差异文本块
- 文本选择：保留差异块+前置上下文+开篇上下文作为重排输入，无相似候选的技能仍按query相关性选片段，控制单候选输入token量在300左右
- 重排流程：用冻结的Qwen3-Reranker打分，结合MMR做多样性排序输出top3结果

### 关键实验结果
在SameCapRisk-Bench的1235个请求上测试，对比TF-IDF query选择、前缀截断等baseline：
- 相同输入长度下，CH@3（召回有效技能且无风险技能）比TF-IDF query选择高54~72个样本
- 相比全量文本输入，输入token量降低51.1%~58.8%，0.6B Reranker的CH@3仅降10~18个，4B Reranker的CH@3持平甚至更高
- 单请求推理耗时降低10.4%，约节省76.8ms

### 核心结论
重排输入选择不能只看与query的相关性，候选间的差异化信息才是区分高相似候选、降低误召回的核心。
