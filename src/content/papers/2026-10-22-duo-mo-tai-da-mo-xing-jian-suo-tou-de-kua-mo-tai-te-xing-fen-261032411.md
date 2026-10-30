---
title: A Broader Look into MLLM's Retrieval Heads
title_zh: 多模态大模型检索头的跨模态特性分析与优化方法
authors:
- Jia Wang
- Yuqing Li
- Jiangnan Li
- Zheng Lin
- Mo Yu
affiliations:
- 中国科学院信息工程研究所
- 中国科学院大学网络空间安全学院
- 腾讯
arxiv_id: '2610.32411'
url: https://arxiv.org/abs/2610.32411
pdf_url: https://arxiv.org/pdf/2610.32411
published: '2026-10-22'
collected: '2026-10-30'
category: Multimodal
direction: 多模态大模型 · 检索头机制与优化
tags:
- MLLM
- Retrieval Heads
- Multimodal Retrieval
- Attention Mechanism
- Long Context
one_liner: 揭示多模态大模型检索头跨模态共享特性，提出定向优化方法显著提升多模态检索性能
practical_value: '- 电商多模态商品检索、多模态客服Agent场景，可复用检索头识别方法定位仅占总头数2%左右的核心证据定位头，定向裁剪降低推理开销

  - 多模态文档/商品详情页召回排序场景，可复用检索头+排名损失的优化方案，仅用LoRA微调检索头对应注意力投影，即可在3类主流MLLM上稳定提升Recall@1

  - 长上下文多模态理解场景（如长视频商品讲解信息提取），可利用跨模态共享检索头特性，仅用文本标注数据优化即可覆盖音/视觉模态检索需求，降低标注成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有检索头研究多局限于文本/图文模态，未覆盖音视频等全模态场景，且缺乏将检索头机制转化为性能提升的实用方法，无法满足多模态长上下文理解的产业需求。
### 方法关键点
- 构建配对AV-NIAH测试集，相同答案分别以语音、屏幕文字形式嵌入长视频，控制背景、问题不变，实现跨模态检索头的统一对比
- 定义校准检索分数$s_{lh}$，减去无意义问题的注意力基线，精准定位跨模态共享的检索头
- 设计检索头定向优化流程：固定识别出的检索头集合，基于排名损失微调对应注意力投影的LoRA权重，实现多模态文档检索性能提升
### 关键结果
- 覆盖18个不同模态的LLM/VLM/全模态模型checkpoint，验证跨模态共享检索头占总头数比例不足2%，移除后几乎完全消除音视频检索能力，同时显著降低文档理解、空间感知、视觉数学等任务表现
- 在MMDocIR多模态文档检索数据集上，该优化方案使Qwen3-VL-8B的Page Recall@1提升6.03个点，Qwen2.5-VL-7B提升5.69个点，Gemma3-12B提升2.17个点，无布局监督下Layout Recall@1也有稳定提升
- 微调对域外任务的影响不超过1个点，无明显负迁移
### 核心结论
多模态大模型的检索能力仅依赖极少量跨模态共享的稀疏注意力头，定向优化这些头即可用极低的微调成本实现多模态检索性能的稳定提升
