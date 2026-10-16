---
title: 'CARA: Causally Guided Retrieval Agent for Question Answering'
title_zh: CARA：面向问答场景的因果引导检索Agent
authors:
- Weicheng Liu
- Xiangcheng Wu
- Depeng Xu
- Haopeng Zhang
- Xi Niu
affiliations:
- University of North Carolina at Charlotte
arxiv_id: '2610.22017'
url: https://arxiv.org/abs/2610.22017
pdf_url: https://arxiv.org/pdf/2610.22017
published: '2026-10-15'
collected: '2026-10-16'
category: Agent
direction: RAG 检索Agent因果优化
tags:
- Retrieval Agent
- RAG
- Knowledge Graph
- Causal Reasoning
- Question Answering
one_liner: 提出无训练因果引导知识图谱检索Agent，通过双向因果评估优化检索路径与召回结果
practical_value: '- 做电商商品/评论知识图谱RAG问答时，可复用 consequentiality+essentiality 两个因果维度做证据筛选，代替纯语义相似度，避免召回文本匹配但不解决用户问题的内容

  - 多Agent并行检索结果融合可直接用RRF方法，无需训练就能提升结果鲁棒性，适配业务中多路径召回的结果合并场景

  - 检索Agent的跳转决策可加入路径一致性校验，避免多-hop探索偏离用户初始意图，降低无效检索开销

  - 做RAG效果评估时，可同时关注答案与ground truth的匹配度（如BERTScore）和内容与召回证据的一致性（如faithfulness），避免为了忠实度牺牲答案完整性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有知识图谱Agent检索仅依靠文本相似度和结构信息，容易召回和查询语义相关但对回答无实质帮助的证据，导致下游答案质量低、检索效率差，无法平衡广度搜索与多跳探索的资源分配。

### 方法关键点
- 无训练设计，仅通过Prompt实现因果推理模块，从两个维度评估候选证据的因果相关性：consequentiality（加入证据是否提升问题可回答性）、essentiality（移除证据是否削弱问题可回答性），加权得到节点因果相关性分
- 增加路径一致性评分，评估当前节点跳转是否符合已探索路径的推理逻辑，与因果分加权得到候选最终得分，指导Agent选择继续跳转、重新全局锚定或终止检索
- 多Agent并行独立探索，通过RRF融合多路径召回结果，兼顾单路径排序优先级与跨路径共识

### 关键实验
在STaRK的3个数据集（电商AMAZON、学术MAG、生物医疗PRIME）上对比BM25、KAR、ARK等基线：AMAZON数据集Hit@1达62.4%，较基线ARK提升3.4pp；MAG数据集BERTScore达40.2，较ARK提升1.0，faithfulness提升4pp；同时检索节点数减少20%以上，检索调用次数更低。

最值得记住的一句话：文本相似度仅能衡量关联度，对回答有实质贡献的证据需要从增量增益和不可替代性两个维度做因果判断。
