---
title: 'Edge-Native Multimodal RAG: Hardware-Aware Quantization and Architectural
  Optimization for Consumer GPUs'
title_zh: 边缘原生多模态RAG：面向消费级GPU的硬件感知量化与架构优化
authors:
- Zahraa Selim
- Menna Hamed
- Wesam Ahmed
- Sohyla Said
- Sara Basheer
- Rami Zewail
affiliations:
- Egypt-Japan University of Science and Technology (E-JUST)
arxiv_id: '2611.14924'
url: https://arxiv.org/abs/2611.14924
pdf_url: https://arxiv.org/pdf/2611.14924
published: '2026-11-11'
collected: '2026-11-13'
category: RAG
direction: 边缘多模态RAG 硬件感知优化
tags:
- Multimodal RAG
- Quantization
- Edge AI
- Consumer GPU
- Prompt Engineering
one_liner: 针对T4等消费级GPU优化多模态RAG，实现8.37GB显存占用并修复量化推理损失
practical_value: '- 消费级GPU（T4/RTX3060等Turing架构）部署RAG/生成式推荐推理服务时，优先选NF4 4bit量化而非GPTQ，避免长上下文崩溃，稳定性优先于峰值吞吐

  - 多模态RAG无需接入大参数端到端VLM，采用Florence-2做视觉转文本的解耦架构，仅430MB显存 overhead 即可实现视觉推理，可直接复用在商品图文/短视频检索场景

  - 量化模型的推理精度损失无需微调修复，新增结构化Few-Shot Prompt即可将推理类任务准确率从35%提升至92%，同时降低47%生成 latency，适合电商客服/商品问答等成本敏感场景

  - RAG检索层采用BM25+BGE的RRF融合方案，无额外训练成本即可将Recall@5从单稠密检索的0.7提升至0.85，可直接复用在商品/内容召回链路'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
7B参数LLM采用FP16精度部署即占用14GB显存，叠加RAG所需的向量索引、KV cache、多模态模块后，总开销超过12-16GB消费级GPU的显存上限；同时现有量化方案普遍存在长上下文不稳定、推理损失大的问题，端到端多模态模型显存开销过高，缺乏可落地的硬件感知工程优化方案。
### 方法关键点
- 硬件感知量化选型：在T4（Turing架构）上对比GPTQ、AWQ、NF4三种4bit量化方案，权衡稳定性与性能选择NF4作为Mistral-7B基座的量化方案
- 解耦多模态架构：接入独立的Florence-2 Base模块做视觉处理，将图像转为结构化文本后输入LLM，避免端到端VLM的高额显存开销
- 检索层优化：采用BGE稠密向量+BM25稀疏检索的RRF融合方案，提升召回准确率
- 推理优化：通过结构化Few-Shot Prompt同时解决量化带来的推理损失、生成 latency过高的问题
### 关键结果
全链路多模态RAG峰值显存仅8.37GB，可在12-16GB消费级GPU稳定运行；NF4量化下推理吞吐12.29tok/s，长上下文无崩溃。结构化Few-Shot Prompt将量化模型数学推理准确率从35%提升至92%，同时生成 latency下降47%，计算强度保持1.88 GFLOPs/token不变。混合检索Recall@5达0.85，较单稠密检索提升21.4%；解耦视觉方案较文本基线准确率提升192.7%，效果接近1.86B参数Moondream2但显存节省50%。
### 核心结论
消费级GPU部署RAG的核心设计原则是「稳定性优先于峰值吞吐，架构解耦优先于端到端效果，Prompt优化优先于微调成本」
