---
title: 'Your Retriever Already Knows: Distribution-Shape QPP for RAG Retrieval Sufficiency'
title_zh: 基于检索分数分布形态的RAG检索充分性QPP预测方法
authors:
- Matyáš Veselý
- Michal Průšek
- Jiří Franc
affiliations:
- Department of Mathematics, FNSPE CTU in Prague
- Institute of Information Theory and Automation, Czech Academy of Sciences
arxiv_id: '2609.11646'
url: https://arxiv.org/abs/2609.11646
pdf_url: https://arxiv.org/pdf/2609.11646
published: '2026-09-10'
collected: '2026-09-11'
category: RAG
direction: RAG检索质量预测 · QPP特征工程
tags:
- RAG
- Query Performance Prediction
- Retrieval Sufficiency
- Multimodal Retrieval
- Feature Engineering
one_liner: 提出无需读取文档内容的24维分布形态QPP特征集，实现比本地LLM法官高20%+AUROC、快3000倍的RAG检索充分性预测
practical_value: '- 电商/企业级RAG系统做检索充分性判断时，优先复用这套24维分数分布特征做轻量预测，单Query仅2ms延迟，比调用LLM做检索法官成本低3个数量级，适配高吞吐的客服、商品问答场景

  - 若已有LLM调用链路，不要将LLM作为独立的检索质量法官，而是把LLM的检索质量打分作为额外特征和分数特征融合，可进一步提升对抗Query识别率，适配合规、售后等对准确率要求高的场景

  - 跨业务线/品类部署时，可直接使用筛选后的13维S1-Lean特征集（8个分布特征+5个Query表面特征），无需全局语料统计即可获得更好的跨域泛化性，降低适配成本

  - 电商搜索的Query质量预判也可复用这套特征逻辑，提前识别召回结果无法满足需求的Query，触发改写/兜底逻辑，降低bad case率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG系统在推理阶段通常无可靠的检索成功信号，遇到歧义或OutOfScope Query时极易产生幻觉；尤其在数据敏感、禁止调用第三方LLM的安全关键场景，急需低成本、低延迟、可本地部署的检索充分性预测能力，用于在生成前决策是回答、弃权还是升级，从根源减少幻觉。

### 方法关键点
- 提出**GeneralQPP** 24维非词法特征集，完全无需读取文档内容：含15个检索分数分布特征（top-k gap、衰减斜率、偏度、双峰间隙、集中度等）、5个Query表面特征（字符长度、词数、是否含数字等）、4个全局语料相似性统计特征
- 三类方案对比范式：仅用分数的传统QPP方法、本地多模态MoE LLM法官、分数特征+LLM打分的混合方法
- 跨域场景下筛选出13维S1-Lean轻量特征子集，仅保留8个分布特征+5个Query特征，去除全局特征提升跨域泛化性

### 关键结果
- 实验覆盖ViDoRe 8领域视觉RAG benchmark（14514条Query）、捷克核监管SÚJB私有数据集（1510条Query，含500条对抗样本）
- GeneralQPP在ViDoRe上加权平均AUROC达0.856，超传统QPP基线0.021，超本地Qwen3.5 LLM法官0.207，单Query延迟仅2ms，速度是LLM法官的3000倍
- 混合方案（GeneralQPP+LLM打分）在SÚJB数据集上Hit@5 AUROC达0.911，对抗样本检测AUROC达0.954；留一域交叉验证下，13维S1-Lean特征比传统QPP基线AUROC高0.032

### 核心结论
检索分数的分布形态已经包含足够的检索充分性信号，绝大多数场景下无需调用LLM读取文档做检索质量判断，成本更低、速度更快、效果更好
