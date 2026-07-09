---
title: 'VaseMuseum: Digital Intelligent Museum for Ancient Greek Pottery'
title_zh: VaseMuseum：面向古希腊陶器的数字智能博物馆系统
authors:
- Jiazi Wang
- Nonghai Zhang
- Qiushi Xie
- Zeyu Zhang
- Yufeng Chen
- Yang Zhao
- Ling Shao
- Hao Tang
arxiv_id: '2607.06374'
url: https://arxiv.org/abs/2607.06374
pdf_url: https://arxiv.org/pdf/2607.06374
published: '2026-07-07'
collected: '2026-07-09'
category: Agent
direction: 多模态Agent · 文博领域可信问答
tags:
- Multimodal Agent
- VLM
- Hallucination Mitigation
- Knowledge Grounding
- RAG
one_liner: 提出轻量模块化多模态Agent框架VaseMuseum，提升文博场景VLM回答可信度与引用有效性
practical_value: '- 源级+响应级双重可信控制可复用在电商商品问答场景：生成前仅从官方商品库、权威资质文件等可信源选证据，生成后校验回答与证据一致性，避免参数、功效类幻觉

  - 免训练GRPO-style输出选择机制无需更新VLM backbone，仅靠推理端排序即可筛选符合业务要求的回答，适合中小团队快速落地低幻觉问答能力

  - 2D/3D统一感知推理架构可迁移到3D商品互动导购Agent，支撑AR试穿、3D家具预览等场景下的用户多模态查询解答'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
文博领域VLM交互讲解存在两大痛点：一是细粒度2D/3D视觉证据与专业策展知识对齐时，检索易引入弱来源、不可验证的引用；二是证据不完整/模糊时，VLM易输出高自信的幻觉回答，无法校准不确定性。

### 方法关键点
1. 模块化多模态Agent架构VaseAgent，支持2D图像、3D文物输入，包含多模态感知、3D-aware推理、权威知识检索、推理时可信控制模块；
2. 源级+响应级双重校验：生成前仅从权威文博网站、博物馆知识库选可验证证据，生成后校验输出主张与证据池一致性，证据不足/冲突时返回中立结论；
3. 训练-free GRPO-style选择机制，无需更新VLM backbone即可筛选带有效引用、置信度校准的回答。

### 关键结果
相比带搜索能力的VLM baseline，引用有效性显著提升，知识密集查询的幻觉率下降，模糊场景下中立回答占比更高。
