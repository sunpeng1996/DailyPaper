---
title: Multimodal Reranking Is a System One Decision
title_zh: 将多模态重排序建模为System One决策的通用实现方案
authors:
- Zhuchenyang Liu
- Yao Zhang
- Yu Xiao
affiliations:
- Aalto University
arxiv_id: '2610.28435'
url: https://arxiv.org/abs/2610.28435
pdf_url: https://arxiv.org/pdf/2610.28435
published: '2026-10-19'
collected: '2026-10-21'
category: RecSys
direction: 多模态检索重排 · 通用VLM能力复用
tags:
- Multimodal Reranking
- VLM
- System One
- Zero-shot
- Listwise Reranking
one_liner: 用通用VLM通过System One选择式推理做多模态重排，零-shot性能接近专用有监督重排器
practical_value: '- 重排prompt设计可放弃逐候选yes/no打分，改用多候选listwise选择式prompt，一次前向得到所有候选概率，解决分档不一致问题，还能减少推理次数

  - 若业务已部署大参数VLM做生成/对话，可复用该VLM通过读取选项token概率的方式做多模态重排，无需额外部署专用重排模型，降低运维成本

  - 小参数VLM做零-shot重排效果不如同规模专用重排模型，参数规模≥12B后才能稳定超过一阶段召回基线，选型时要平衡成本与效果

  - 文本领域的decision tuning可提升文档类多模态重排效果，无需额外标注多模态重排数据，降低训练成本'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态重排器多为专用有监督模型，需要单独训练、部署和维护，而RAG、多模态搜索系统通常已经部署了大VLM做生成类任务，存在明显的算力和架构冗余，探索通用VLM复用做重排的路径有很高工程价值。

### 方法关键点
- 将多模态重排建模为System One选择决策：把query和一阶段召回的top16候选拼成单条prompt，询问VLM哪个候选最匹配query，仅需一次前向传播
- 直接取VLM输出层A-P标签token的logits，归一化后得到每个候选的匹配概率，据此重排，无需解码生成文本
- 对比两种推理范式：listwise选择式（1次前向）vs 逐候选yes/no点式（16次前向），同时测试了仅用文本数据做decision tuning的迁移效果

### 关键结果
- 测试数据集：MMEB-V2图像/视觉文档检索、ViDoRe V3基准
- 零-shot Qwen3.8-27B使用选择式范式，全面优于有监督Qwen3-VL-Reranker-2B，在MMEB-V2视觉文档任务上nDCG@5达84.79，持平8B专用重排器，延迟仅为后者1.1-1.5倍
- 选择式范式比逐候选yes/no范式hit@1高5.4-7.3，后者效果甚至低于一阶段召回基线
- 仅在文本数据上做decision tuning的JEV-27B-VL，在文档重排任务上nDCG提升0.6-1.1个点，自然图像任务效果无明显变化

**最值得记住的一句话**：已经部署大VLM的系统可零额外成本复用做重排，listwise选择式范式效果远优于点式yes/no打分。
