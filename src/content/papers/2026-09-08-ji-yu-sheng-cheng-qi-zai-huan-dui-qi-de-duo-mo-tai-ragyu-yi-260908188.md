---
title: Bridging the Semantic-Utility Gap in Multimodal RAG via Generator-in-the-Loop
  Alignment
title_zh: 基于生成器在环对齐的多模态RAG语义效用差距弥合方法
authors:
- Zhan-Lun Chang
- Dong-Jun Han
- Seyyedali Hosseinalipour
- Mung Chiang
- Christopher G. Brinton
affiliations:
- Purdue University
- Yonsei University
- University at Buffalo–SUNY
arxiv_id: '2609.08188'
url: https://arxiv.org/abs/2609.08188
pdf_url: https://arxiv.org/pdf/2609.08188
published: '2026-09-08'
collected: '2026-09-09'
category: RAG
direction: 多模态RAG · 重排器对齐优化
tags:
- Multimodal RAG
- LoRA
- Cross-Encoder
- Preference Alignment
- VLM
one_liner: 无需人工文档标注，用冻结VLM生成答案效用标签微调LoRA重排器提升多模态RAG效果
practical_value: '- 多模态RAG场景可复用HyDE模态桥方案：用冻结VLM将图文查询转成文本假设理由，再做文本密集检索，无需训练专用多模态检索模型，大幅降低工程成本

  - 重排器低标注成本训练方案：用冻结生成器的回答正确性做监督信号，自动挖掘正负偏好对，仅微调重排器LoRA参数，适合电商图文搜索、商品问答等场景的RAG优化

  - 可复用迭代对齐机制：定期用当前重排器重新挖掘偏好对刷新训练数据，避免训练信号过时，比固定数据集训练效果最高提升2.58个百分点

  - 三种对齐损失可按需选择：侧重排序选Triplet loss，想和基线对齐选DPO，简单直接选SFT，均适配答案效用标签的训练信号'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
标准多模态RAG的检索、重排模块仅优化语义相似度，存在语义-效用gap：语义相关的文档可能无法帮助生成器输出正确答案，甚至引入错误信息。传统重排器训练依赖昂贵的人工文档级 relevance 标注，多模态场景下还要额外解决图文跨模态检索的模态gap问题，现有基于似然的对齐信号是间接指标，不能直接反映生成器的真实回答正确性。

### 方法关键点
1. 两阶段框架：Stage1用冻结VLM基于图文查询生成HyDE假设文本理由，拼接原查询后用文本编码器做FAISS密集检索，解决跨模态gap，召回候选文档池
2. Stage2偏好挖掘：将每个候选文档喂给冻结VLM，若生成答案匹配ground truth则标为正样例，否则标负样例，自动构建正负偏好对，无需人工标注
3. 仅用LoRA微调跨编码器重排器，支持Triplet loss、SFT、DPO三种对齐损失
4. 支持周期性重挖掘偏好对，随重排器迭代刷新训练数据，避免信号过时

### 关键结果数字
在VQA-X、A-OKVQA数据集上测试，采用Qwen3-VL-4B-Instruct、Qwen3.5-2B两种VLM：
- 相比基线重排器，生成器引导的偏好训练在Triplet loss下，VQA-X准确率最高提升1.52%，A-OKVQA最高提升4.84%
- 效果显著优于随机、仅语义排序、REPLUG-style似然基线，三种对齐损失下均稳定领先
- 周期性重挖掘偏好对比固定训练集，最高带来2.58个百分点的准确率提升

### 核心结论
RAG的检索重排优化目标应该从语义相似度转向下游生成的回答效用，用冻结生成器的真实回答反馈做监督信号，无需人工标注即可低成本实现重排器和生成器的对齐
