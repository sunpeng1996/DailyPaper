---
title: Learning Multimodal Embeddings with Evidence-Aligned Readout
title_zh: 基于证据对齐读出的多模态嵌入学习方法
authors:
- Zirong Chen
- Fuda Ye
- Enjun Du
- Junfu Pu
- Xinlei Wang
- Xinyu Zuo
- Lisheng Duan
- Haijin Liang
- Jin Ma
- Jiachuan Wang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Tencent Yuanbao
- Tsinghua University
- ARC Lab, Tencent
- The University of Hong Kong
arxiv_id: '2609.33659'
url: https://arxiv.org/abs/2609.33659
pdf_url: https://arxiv.org/pdf/2609.33659
published: '2026-09-27'
collected: '2026-09-29'
category: GenRec
direction: 多模态检索嵌入 · 证据对齐读出
tags:
- Multimodal Embedding
- EviAlign
- Contrastive Learning
- MLLM
- Retrieval
one_liner: 提出EviAlign框架联合语义证据生成与边界读出，仅500K训练对在12项多模态检索任务达76.9平均Recall@1
practical_value: '- 多模态检索场景可直接复用EviAlign的语义证据拆分逻辑：将商品/查询的多模态信息拆分为Entity（商品主体）、Attribute（属性）、Relation（搭配/空间关系）、Detail（细粒度特征）、Summary（全局描述）五类，配合自定义边界token做读出，不需要改动现有单向量检索索引架构

  - 训练时可复用联合损失设计：同时优化语义证据生成的LM损失和对比检索损失，仅需500K训练对即可达到接近千万级数据训练的基线效果，适合小样本业务场景快速迭代

  - 电商图搜、组合检索（参考图+文本修改需求）场景可直接借鉴证据生成逻辑：生成目标检索对象的描述而非仅标注参考图特征，大幅提升组合检索的准确率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有MLLM生成的检索相关证据无法有效融入嵌入表示，单纯增加推理链或多读出点的收益有限，且未解决证据语义结构与嵌入读出位置的对齐问题，小训练数据下性能难以满足电商多模态检索、组合搜索等业务需求。
### 方法关键点
- 提出EviAlign框架，共享MLLM同时完成语义证据生成和边界读出：将检索证据拆分为Entity、Attribute、Relation、Detail、Summary5类语义单元，每类末尾新增自定义边界token（<ENT>/<ATT>/<REL>/<DET>/<SUM>）
- 训练采用联合损失：对称批次内对比检索损失（NCE）+ 语义证据生成的语言模型损失，两类任务共享证据结构
- 推理时自回归生成语义证据序列，读取各边界token的最后一层隐状态，平均池化后归一化得到单向量嵌入，完全兼容现有检索索引架构
### 关键结果
在12项MMEB多模态检索任务上验证，仅用500K训练对，基于Qwen3-VL-8B backbone的EviAlign平均Recall@1达76.9，超过同训练数据量级下所有基线；2×3控制实验显示，语义证据与边界读出的协同设计带来1.74点的额外收益，语义证据+末尾读出与自由格式CoT+末尾读出性能几乎持平，仅对齐读出位置才能充分释放结构化证据的价值。
> 最值得记住的一句话：结构化检索证据的价值需要与嵌入读出位置协同设计才能充分释放，无需改动现有单向量检索架构即可获得显著性能提升
