---
title: 'Beyond Relevance: An Empirical Study of Multimodal LLMs for Diversity-Aware
  Recommendation Reranking'
title_zh: 多模态大模型用于多样性感知推荐重排的实证研究
authors:
- Chengkai Liu
- Yan Fu
- Huiyuan Chen
- Sheikh Sarwar
- Qilin Qi
affiliations:
- Amazon
arxiv_id: '2611.28379'
url: https://arxiv.org/abs/2611.28379
pdf_url: https://arxiv.org/pdf/2611.28379
published: '2026-11-20'
collected: '2026-11-24'
category: RecSys
direction: 推荐重排 · 多模态LLM 多样性优化
tags:
- Multimodal LLM
- Reranking
- Diversity
- Recommendation System
- Zero-shot
one_liner: 提出训练无关的多模态重排框架，实证明确视觉信息对推荐增益的域依赖特性
practical_value: '- 视频/内容类推荐场景优先引入MLLM多模态重排，可同时提升NDCG与α-NDCG；电商实物类场景先做AB测试验证视觉信息增益再上线，避免冗余投入

  - 重排阶段可直接用结构化提示引导MLLM平衡相关性与多样性，无需额外引入人工调参的MMR类trade-off公式，适配多场景快速迭代

  - 多模态prompt可采用历史/候选item的拼接合成图+对应编号标题的对齐方式，降低多图输入的prompt构造复杂度，适配多数商用MLLM接口

  - 资源有限时可仅对召回top20小候选集做MLLM重排，既控制推理成本，又能拿到重排增益，适合高价值流量场景试点'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM推荐重排方案大多仅依赖文本元数据，核心优化目标集中在相关性，未充分挖掘视觉信号对多样性的补充价值；视觉导向场景（如流媒体、内容推荐）中图像可传递文本未覆盖的风格、审美偏好，但视觉信息的增益边界、MLLM能否同时提升相关性与多样性缺乏系统性实证结论，无法指导业务场景选型。
### 方法关键点
- 训练无关的MMRerank框架：无需任务微调，仅通过结构化多模态prompt实现重排，将用户历史交互、候选item的图像横向拼接为合成图，与对应编号标题一一对齐实现跨模态匹配，降低prompt构造复杂度
- 多样性引导prompt设计：内置4条规则引导MLLM同时关注视觉特征、时序偏好、探索利用平衡、相关性与类目多样性联合优化，要求输出JSON格式的候选ID排序，降低后处理成本
- 兼容主流部署模式：既支持独立对候选集排序，也可对传统序列推荐模型的topN召回结果做二次重排
### 关键实验结果
覆盖3个公开亚马逊商品数据集（美妆、运动、玩具）+1个内部Prime Video流媒体数据集，对比基准为SASRec、文本-only MLLM重排，测试模型包括开源InternVL3-38B、商用Claude Sonnet 4.6：
- 视频域效果突出：引入图像相对文本-only提升NDCG@5最高121.9%，相对SASRec基准最高提升NDCG@5 71.0%、α-NDCG@5 14.1%
- 电商商品域视觉增益不稳定：多数场景提升不足5%甚至出现负向效果
### 核心结论
多模态信息对推荐的增益并非通用，仅在文本元信息不足的视觉导向场景有明确价值，需结合域特性与模型底座做针对性评估。
