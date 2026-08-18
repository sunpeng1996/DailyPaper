---
title: 'Coverage Is Not Containment: A Fundamental Limit of Admission-Time Defenses
  Against Coordinated Poisoning of Vector Retrieval'
title_zh: 向量检索协同投毒的准入防御根本局限性：覆盖不等于遏制
authors:
- Prashant Kumar Pathak
- Tarun Kumar Sharma
arxiv_id: '2608.16044'
url: https://arxiv.org/abs/2608.16044
pdf_url: https://arxiv.org/pdf/2608.16044
published: '2026-08-17'
collected: '2026-08-18'
category: RAG
direction: RAG向量库安全 · 投毒防御
tags:
- RAG
- VectorDB Security
- Corpus Poisoning
- Admission Control
- Adversarial Attack
one_liner: 证明所有RAG向量库准入时间防御无法对抗协同投毒，提出基于检索需求的检测方案效果提升显著
practical_value: '- 电商/客服场景的RAG系统不要仅依赖入库hub过滤作为唯一安全防线，这类方案完全无法抵御针对特定query的协同投毒，易导致商品推荐、问答回答被恶意篡改

  - 可直接复用文中检索时检测方案，基于召回内容新鲜度、对应query的真实用户需求集中度两个特征做校验，在1%FPR下可实现100%协同投毒召回

  - 分片部署向量库时避免使用单shard独立的集体检测规则，必须做全局入库流一致性校验，防止投毒内容拆分到不同shard绕过检测'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG已成为LLM落地的核心架构，向量库是其安全边界，攻击者可通过注入恶意文档篡改召回结果，进而控制LLM输出。当前主流的低成本防御方案是在文档入库时检测并过滤hub型恶意文档（即会被大量query召回的文档），但这类准入防御未考虑协同投毒场景：攻击者注入多条单独看起来无异常、不会被判定为hub的文档，共同抢占某个目标query的top-k结果，这类攻击的防御有效性此前未被系统研究。

### 方法关键点
- 提出协同锥型投毒算法：针对目标query生成位于窄锥体内的多个文档向量，每个文档单独计算的哨兵query反向kNN计数均低于准入阈值，可绕过入库检测，同时全部进入目标query的top-k结果集
- 从理论上证明所有仅依赖文档向量和哨兵query的入库时间防御，都无法区分投毒锥和合法的小众主题批量上传，二者在几何特征上服从几乎相同的分布，分类器区分能力等同于随机猜测
- 提出破解方案：在检索阶段引入用户真实需求信号，结合召回结果的新鲜度、对应query的需求集中度两个特征做异常检测

### 关键实验结果
实验覆盖BEIR 4个公开语料+通用网页语料，测试BGE、GTE、E5等5款主流文本编码器：
- 投毒效果：仅注入10条符合要求的文档，即可抢占目标query 10/10的top-k结果；端到端RAG pipeline（BGE-large+HNSW+Qwen2.5-7B）中，88%的目标query的回答会被篡改
- 入库防御上限：最强的训练分类器在1%FPR下仅能检出4.2%的投毒，几乎等同于随机猜测
- 检索时防御效果：相同1%FPR下可检出100%的投毒，效果提升23倍以上

**最值得记住的一句话：仅靠向量库入库端的防御不可能遏制协同投毒，安全防线必须从入库延伸到检索端，利用用户真实请求的需求信号做校验。**
