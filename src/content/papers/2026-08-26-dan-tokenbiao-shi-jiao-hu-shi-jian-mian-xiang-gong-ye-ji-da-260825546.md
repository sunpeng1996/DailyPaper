---
title: 'An Event is Worth One Token: Event Tokenization for Industrial-scale LLM Recommendation'
title_zh: 单Token表示交互事件：面向工业级大模型推荐的事件Token化方法
authors:
- Fan Xia
- Zhaoheng Zheng
- Iman Setayesh
- Ruogu Lin
- Yiqin Pan
- Samarth Mittal
- Wentao Bao
- Vinti Pandey
- Sachin Patil
- Jianpeng Cheng
affiliations:
- Meta AI
arxiv_id: '2608.25546'
url: https://arxiv.org/abs/2608.25546
pdf_url: https://arxiv.org/pdf/2608.25546
published: '2026-08-26'
collected: '2026-08-27'
category: GenRec
direction: 生成式推荐 · 事件Token化
tags:
- Event Tokenization
- LLM4Rec
- Sequential Recommendation
- Industrial RecSys
- AMBER
one_liner: 提出AMBER架构，将用户交互全量异构特征压缩为Event Token，解耦事件快照分辨率与线上推理算力
practical_value: '- 架构层面可直接复用异步Token化+缓存设计：将用户全量历史交互特征离线预编码为固定长度Event Token存入特征库，线上推理直接读取，彻底规避实时拉取/计算长序列全量特征的算力、延迟瓶颈

  - 工程落地trick直接复用：用DANN对抗正则+EMA权重更新约束多版本Tokenizer的表示空间一致，解决迭代更新后历史缓存Token失效的问题；配合Matryoshka
  Dropout+量化感知训练，可在几乎无损前提下将Token存储成本降低8倍

  - 低风险落地路径：不需要全链路替换为LLM推荐，可先将预训练好的Event Token作为补充历史特征输入现有传统召回/排序模型，参考文中实验可获得0.05%+的NE提升，快速拿到业务收益

  - 扩容决策参考：优先扩容Event Tokenizer的容量而非下游LLM的参数，在总算力开销不变的前提下，提升事件快照分辨率的收益远高于单纯扩容下游LLM'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前工业级LLM推荐面临序列长度与事件快照分辨率的强约束：自回归模型为了压缩上下文长度，只能将历史事件简化为Semantic ID或少量特征，丢失用户属性、上下文、交互结果等大量核心信号，且信息损失会在自回归序列中逐层累积；而实时计算全量历史特征的算力开销极高，无法适配亿级用户的大规模推荐场景。
### 方法关键点
- 核心架构AMBER分为两部分：Event Tokenizer将每个交互事件的全量异构特征（用户/商品/上下文/交互结果等）端到端压缩为单个d_z维Event Token；下游User LLM基于Token序列做自回归推荐预测
- 训练推理解耦：Event Tokenizer在事件发生时异步触发计算，输出Token直接缓存入用户特征序列，线上推理直接读取缓存，不需要实时计算全量历史特征
- 工业落地优化：采用DANN对抗正则+EMA权重更新缓解Tokenizer迭代带来的表示漂移；Matryoshka Dropout+量化感知训练降低Token存储开销8倍；共享Tokenizer配合动态特征掩码适配召回、排序等多任务，实现跨实体正迁移
- 三阶段训练流程：先冻结LLM训练Tokenizer对齐LLM embedding空间，再联合训练，最后循环迭代适配分布漂移
### 关键实验
基于Meta PB级工业推荐日志，对比现有最优工业基线、Semantic ID+CU embedding、HSTU等方案：排序场景NE比公平对比基线低0.4%，与现有最优模型融合后NE降低0.16%；检索场景Soft Recall比基线高0.31%~0.51%；直接作为特征输入现有非LLM排序模型，NE降低0.06%，达到统计显著的业务收益阈值。
### 核心结论
仅优化训练侧算力的模型扩容不是系统最优，综合考虑训练+线上服务的总算力，提升历史事件的快照分辨率才是生成式推荐更高效的扩容方向。
