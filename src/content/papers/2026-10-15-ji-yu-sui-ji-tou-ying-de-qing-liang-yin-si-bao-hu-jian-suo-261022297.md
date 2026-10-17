---
title: Private Retrieval Augmented Generation via Random Projection
title_zh: 基于随机投影的轻量隐私保护检索增强生成方法
authors:
- Dixi Yao
- Tahseen Rabbani
- Tian Li
affiliations:
- University of Chicago
arxiv_id: '2610.22297'
url: https://arxiv.org/abs/2610.22297
pdf_url: https://arxiv.org/pdf/2610.22297
published: '2026-10-15'
collected: '2026-10-17'
category: RAG
direction: 隐私增强RAG · 随机投影优化
tags:
- RAG
- Privacy Protection
- Random Projection
- Differential Privacy
- Embedding Retrieval
one_liner: 通过随机投影实现RAG隐私防护，效用显著优于差分隐私基线且隐私表现相当
practical_value: '- 电商内部知识库RAG（如客服助手、商家运营工具、商品合规审核场景）可直接复用该方案：离线预处理知识库嵌入、在线对用户查询做同矩阵投影，几乎不增加推理延迟，还能防止用户PII、内部运营数据被恶意提取

  - 无强差分隐私合规要求的业务场景，优先选择随机投影替代DP类隐私方案，平均效用提升50%以上，还省去DP方案的复杂参数调优（如噪声量级、裁剪阈值调试）

  - 投影维度k可根据业务需求灵活选择：追求更低离线计算延迟选k=25，追求更高检索效用选k=1600，默认k=100是兼顾性能与效果的最优选择

  - 电商个性化推荐、用户行为检索的RAG场景，可通过该方案避免用户敏感浏览、购买行为数据被攻击提取，同时保留检索相关性与推荐效果'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有RAG系统易被恶意构造的查询提取知识库中的敏感信息（如个人PII、企业内部数据、用户行为记录），主流基于差分隐私（DP）的防护方案存在效用损失大、实现复杂度高、推理延迟显著上升的问题，无法满足业务落地的效率与效果要求。

### 方法关键点
- 离线阶段对知识库所有文本嵌入用IID高斯随机矩阵R做投影，矩阵元素服从`N(0,1/k)`，k为投影维度，仅做一次预处理，无额外在线开销
- 在线推理阶段对用户查询嵌入复用相同的矩阵R做投影，在低维空间做相似度检索，可无缝兼容KNN-LM、Standard RAG两种主流RAG架构
- 基于Johnson-Lindenstrauss引理保证投影前后的L2距离与余弦相似度近似不变，同时通过随机扰动让语义相近的候选有概率替换原top检索结果，避免敏感信息被确定性提取

### 关键实验
在Enron邮件、ECHR法律文书、C4通用语料、HotpotQA多跳问答4个数据集上测试，对比基线包括原生RAG、DP-RP-G（差分隐私+随机投影）、DPSparseVoteRAG（DP投票方案）：相比DP基线，平均效用（PPL、QA F1）提升50%以上，推理延迟与原生RAG持平（仅0.08s/Token，远低于DPSparseVoteRAG的2.8s/Token）；隐私泄露率接近无RAG的原生LLM，远低于原生RAG（Enron数据集原生Standard RAG泄露217项敏感信息，本方法仅泄露3项）；支持10万级知识库扩展，知识库规模越大，隐私防护效果越好。

### 核心结论
对于无需强制差分隐私合规的RAG落地场景，随机投影是远优于差分隐私方案的高性价比隐私保护选择。
