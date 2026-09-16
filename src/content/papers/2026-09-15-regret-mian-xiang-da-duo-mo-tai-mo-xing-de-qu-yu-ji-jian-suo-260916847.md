---
title: 'RegRet: Enhancing Region-Level Retrieval in Large Multimodal Models'
title_zh: RegRet：面向大多模态模型的区域级检索增强框架
authors:
- Xun Liang
- Honghui Yang
- Weihang Pan
- Ruisi Zhao
- Boyuan Pan
- Yao Hu
- Wenxiao Wang
- Binbin Lin
- Deng Cai
affiliations:
- State Key Lab of CAD&CG, Zhejiang University
- Xiaohongshu Inc.
- School of Software Technology, Zhejiang University
arxiv_id: '2609.16847'
url: https://arxiv.org/abs/2609.16847
pdf_url: https://arxiv.org/pdf/2609.16847
published: '2026-09-15'
collected: '2026-09-16'
category: Multimodal
direction: 多模态检索 · 区域级匹配优化
tags:
- Multimodal Retrieval
- LMM
- Region-level Matching
- Benchmark
- Contrastive Learning
- E-commerce Search
one_liner: 提出区域感知编码器与三阶段训练策略，配套REGMB基准，提升LMM区域检索能力且不损失全局性能
practical_value: '- 电商以图搜商品场景可复用Region-Aware Encoder(RAE)设计：独立编码ROI并通过层间cross-attention融合全局背景信息，平衡局部特征与上下文，解决小目标搜索时背景干扰或信息缺失问题

  - 多模态检索模型训练可复用三阶段训练策略：先做区域细粒度字幕预训练、再纯文本对比学习迁移语言能力、最后区域对比学习微调，配合LoRA降低训练成本，通过独立投影层避免区域训练影响全局检索性能

  - 电商多模态检索评测可参考REGMB构建逻辑：补充跨场景、带细粒度标注的区域级正负样本对，覆盖文搜图、图搜文、图搜图、文图混搜4类核心场景，更贴合业务真实需求

  - 现有LMM适配区域检索时不要直接用裁剪/打标/辅助图等prompt策略，性能上限低；新增轻量RAE模块的投入产出比更高，性能提升超14%的同时推理速度比辅助图策略快22%'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有大多模态模型(LMM)主要聚焦全局检索任务，在电商以图搜品、多模态RAG等需要区域级匹配的场景下，要么过度聚焦局部丢失必要背景，要么被背景干扰导致匹配错误；同时缺乏大规模区域级对比训练数据和覆盖多场景的评测基准，制约区域检索性能落地。

### 方法关键点
- 模型架构：新增独立RAE模块，与原生全局视觉编码器(CE)层间交叉注意力融合，自适应平衡区域特征与背景上下文；RAE与CE使用独立投影层对齐LLM，冻结CE参数避免区域训练损伤全局能力
- 三阶段训练：①RAE预训练用细粒度区域字幕任务学习区域特征与背景关联；②纯文本对比学习将LLM生成能力转化为embedding能力；③区域对比学习混合全局+区域对比对微调，同时优化两级检索性能
- 数据基准：构建REGMB区域级多模态检索基准，包含225k对比对，覆盖4类检索任务，支持训练与评测

### 关键实验结果
在REGMB和公开ROxford、DeepFashion2等基准上对比CLIP系、LMM系基线：零样本RegRet-8B比最优LMM基线区域检索性能平均高14.3%；用REGMB微调后性能再提升7.4%，相比基线平均提升超20%；同时全局检索性能在M-BEIR基准上与SOTA持平甚至略优，推理速度比最优prompt策略快22%。

### 核心结论
区域检索的核心矛盾是局部特征与背景信息的平衡，独立区域编码器+分层融合的架构，比单纯优化prompt策略的投入产出比高得多。
