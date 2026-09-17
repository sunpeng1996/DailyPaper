---
title: 'Decodable but Misrouted: Sparse Features Uncover a Readout Gap in Vision-Language
  Models for Harmful Meme Detection'
title_zh: 稀疏特征揭示视觉语言模型有害meme检测的路由瓶颈
authors:
- Girish A. Koushik
- Diptesh Kanojia
- Helen Treharne
affiliations:
- University of Surrey
- Nature-Inspired Computing & Engineering, University of Surrey
- Surrey Centre for Cyber Security, University of Surrey
arxiv_id: '2609.18860'
url: https://arxiv.org/abs/2609.18860
pdf_url: https://arxiv.org/pdf/2609.18860
published: '2026-09-16'
collected: '2026-09-17'
category: Multimodal
direction: 多模态内容安全 · 有害检测瓶颈优化
tags:
- Multimodal Safety
- Sparse Autoencoder
- Vision-Language Model
- Harmful Content Detection
- LoRA
one_liner: 通过稀疏特征分析证明视觉语言模型有害meme检测瓶颈为证据路由而非表征缺失
practical_value: '- 电商/社区UGC多模态内容审核场景，可引入稀疏自编码器提取模型隐层特征，补全原生多模态模型的有害内容漏判，提升审核召回率

  - 多模态模型下游任务适配时，可采用probe-distilled LoRA方案优化特征路由逻辑，相比全量微调训练成本更低、适配效率更高

  - 跨语言多模态内容检测可复用本文验证的稀疏特征读出方法，覆盖小语种、混合语种场景的审核需求'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有视觉语言模型在有害meme检测场景下分类错误的根因不清晰，无法确定是内部表征缺失还是已表征的证据无法路由至输出层，且现有方案在多语言、混合语种场景下泛化性不足。

### 方法关键点
针对Gemma-3、Qwen3.5两款主流多模态大模型，采用稀疏自编码器、角色条件探针、因果干预、恢复实验等方法，在6个有害内容基准数据集上开展测试，额外覆盖西班牙语、印地语-英语混合语种场景。

### 关键结果数字
- 稀疏读出方案在所有6个二分类任务上均优于原生预测：Qwen平均macro-F1从0.432提升至0.740，Gemma从0.532提升至0.714
- 仅校准路由逻辑即可恢复93.3%的平均性能gap，探针蒸馏的LoRA可有效提升原生预测性能，多任务共享适配会产生负迁移
- Facebook Hateful Memes数据集上Gemma-3-12B的macro-F1从0.685提升至0.756，验证核心瓶颈为特征路由而非表征能力
