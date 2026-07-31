---
title: 'Chimera: Designing and Chinchilla-Scaling Hybrid Visual Diffusion Transformers'
title_zh: Chimera：混合视觉扩散Transformer的设计与Chinchilla式缩放
authors:
- Chongjian Ge
- Hanwen Jiang
- Tianyu Wang
- Jiuxiang Gu
- Yiran Xu
- Ziwen Chen
- Shaoteng Liu
- Jing Shi
- Yicong Hong
- Zefan Cai
affiliations:
- Adobe Research
arxiv_id: '2607.28611'
url: https://arxiv.org/abs/2607.28611
pdf_url: https://arxiv.org/pdf/2607.28611
published: '2026-07-29'
collected: '2026-07-31'
category: Multimodal
direction: 多模态生成 · 扩散Transformer架构优化与缩放
tags:
- Diffusion Transformer
- MoE
- Long Context
- Scaling Law
- Attention Optimization
one_liner: 提出混合线性+全局注意力的高效视觉扩散架构与异架构超参迁移缩放方法
practical_value: '- 混合KDA线性注意力+MLA全局注意力的架构设计，可迁移到长序列推荐/多模态召回排序模型，替代全注意力降低计算复杂度，支持更长用户行为序列建模

  - HeteroP模块级超参迁移方法，可复用在带MoE、多模块组合的异架构大模型（如推荐大模型、多模态Agent大模型）的跨规模调参，大幅减少大模型调优成本

  - 无位置编码（NoPE）+模态感知短卷积的设计，可借鉴到多模态Agent的长上下文处理模块、跨模态推荐的特征融合层，提升长序列外推能力与跨模态局部特征建模效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
高分辨率图像、长视频等场景下视觉token数量暴涨，传统扩散Transformer的全注意力二次复杂度成为性能瓶颈；LLM的长序列优化方案无法直接适配视觉扩散对时空局部性、跨模态双向交互的要求，且视觉领域缺乏异架构扩散模型的系统性缩放方法论，导致大模型训练成本高、长序列外推能力弱。

### 方法关键点
- 单流多模态架构：文本、图像、视频token统一拼接处理，无需模态专属分支，天然支持跨模态token级交互
- 混合注意力机制：3:1比例交替O(N)复杂度的KDA线性注意力与压缩KV的MLA全局注意力，平衡长序列效率与全局建模能力
- 模态感知短卷积替代位置编码：捕获多维度局部结构，实现无位置编码设计，大幅提升长序列外推能力
- 稀疏MoE层搭配iHC超连接、三明治归一化：在控制激活计算量的同时提升模型容量与训练稳定性
- HeteroP模块级超参迁移方案：支持异架构模型跨宽深度的超参自动适配，基于该方案拟合Chinchilla式计算最优缩放定律，覆盖激活参数量、训练token数、图文数据比例三个核心变量

### 关键结果
- 11B总参/2B激活参的Chimera模型，达到同等Wan-2.1 2B基线效果仅需1/7.3的计算量，训练成本仅为Z-Image-Turbo的1/20
- 零-shot视频生成长度外推到训练时长的6倍（5秒→30秒），FID仅下降6.5%，远低于基线的50%+
- 同等80G A100显存下支持1.68倍更长序列，255k token下推理速度提升2.14倍

> 最值得记住的一句话：架构设计与缩放方法论协同优化，是大模型在长序列、多模态场景下实现效率与能力平衡的核心路径
