---
title: Training-Free Pseudo-Fusion for Composed Image Retrieval with Diffusion Models
  and Multimodal Large Language Models
title_zh: 无需训练的伪融合框架：结合扩散模型与MLLM实现组合图像检索
authors:
- Fan Xu
- Luis A. Leiva
affiliations:
- University of Luxembourg
arxiv_id: '2608.23102'
url: https://arxiv.org/abs/2608.23102
pdf_url: https://arxiv.org/pdf/2608.23102
published: '2026-08-24'
collected: '2026-08-25'
category: RecSys
direction: 多模态商品检索 · 训练免微调
tags:
- Composed Image Retrieval
- MLLM
- Diffusion Model
- Training-Free
- Zero-Shot Retrieval
one_liner: 无需任务特定训练，通过模态转换将组合图像检索转为单模态检索，性能媲美SOTA
practical_value: '- 电商「参考图+文本修改」的商品搜索场景可直接复用T→I伪融合方案，无需额外标注训练，仅需接入现成MLLM生成组合描述，对接现有文搜图链路即可快速上线

  - 工程侧可提前将全量商品的图像特征预索引到FAISS向量库，用户请求时仅实时生成组合文本描述再做检索，平衡生成耗时与检索效率，适配大流量生产场景

  - MLLM生成组合描述时，设置低temperature（0.1左右）、适中top-p（0.9）、高top-k，可稳定提升检索效果，无需复杂prompt工程

  - 若采用扩散模型生成目标图做检索，需将image guidance scale控制在3以内，避免生成图与参考图过度相似，忽略文本修改的语义要求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统组合图像检索（CIR）依赖多模态特征融合模块的任务专项训练，标注成本高、跨域泛化能力差，零样本场景下落地难度大；现有免训练方案多采用多模型级联链路，误差累积严重，效果和效率难以兼顾。
### 方法关键点
- 提出PeFuse伪融合框架，无需任何任务微调，仅通过预训练MLLM、扩散模型做模态转换，将CIR拆解为4种单模态检索任务：T→I（MLLM生成参考图+修改文本的组合描述，走文搜图链路）、I→I（扩散模型生成符合修改要求的目标图，走图搜图链路）、T→T（MLLM同时生成查询描述和候选图描述，走文搜文链路）、I→T（生成查询目标图+候选图描述，走图搜文链路）
- 支持单向/双向两种转换模式：单向仅处理查询侧模态，链路更短延迟低；双向额外转换候选库图像为文本，适配纯文本检索场景
- 全链路复用CLIP类预训练检索模型的余弦相似度做排序，所有组件支持插拔替换，可快速适配不同业务场景
### 关键结果
在Fashion-IQ、CIRR、CIRCO、GeneCIS四个标准CIR基准数据集测试，T→I模式效果最优：采用OpenCLIP ViT-bigG/14 backbone时，CIRR数据集Recall@1达40.41%，超过绝大多数零样本方案，性能媲美需要专项训练的SOTA；对比直接拼接图像+文本特征的基线方案，效果提升3~4倍。
最值得记住的结论：组合图像检索场景下，将多模态查询转换为文本走文搜图的免训练方案，性价比远高于生成图像走图搜图的方案。
