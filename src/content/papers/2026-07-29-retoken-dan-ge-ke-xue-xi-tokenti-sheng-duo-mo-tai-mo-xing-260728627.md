---
title: 'ReToken: One Token to Improve Vision-Language Models for Visual Retrieval'
title_zh: ReToken：单个可学习token提升多模态模型视觉检索性能
authors:
- Yao Xiao
- Reuben Tan
- Zhen Zhu
- Yuqun Wu
- Jianfeng Gao
- Derek Hoiem
affiliations:
- University of Illinois at Urbana-Champaign
- Microsoft Research
- Google DeepMind
arxiv_id: '2607.28627'
url: https://arxiv.org/abs/2607.28627
pdf_url: https://arxiv.org/pdf/2607.28627
published: '2026-07-29'
collected: '2026-07-31'
category: Multimodal
direction: 多模态长上下文 · 可学习检索token
tags:
- ReToken
- Vision-Language Model
- KV Cache
- Visual Retrieval
- Long Context
one_liner: 单个可学习检索token在value空间做视觉检索，零样本跨图像到视频提升长视觉上下文推理性能
practical_value: '- 可迁移到电商多模态RAG场景：在商品图文/短视频召回场景新增单个可学习检索token，替换现有query-key匹配逻辑，用value空间特征做召回，无需微调大模型本体，成本极低，可显著提升长商品池下的召回准确率

  - 长视频/多图理解场景可复用两阶段推理架构：先离线预处理所有视觉内容生成持久化KV cache，用户查询时仅需两次轻量前向（检索+生成），多个查询共享KV缓存，大幅降低长内容推理的GPU成本

  - 跨模态检索工程中可优先尝试value空间特征匹配，而非传统的query-key注意力得分匹配，实验证明value空间携带的语义对齐信号更强，在密集检索、多模态召回场景均可直接复用该结论'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有VLM处理长视觉上下文（多图、小时级视频）时存在两个核心问题：一是注意力得分与内容相关性弱，基于query-key的检索召回准确率极低；二是全量上下文推理GPU显存占用过高，无法落地工业场景。传统多模态RAG依赖外部独立检索器，需要二次编码，效率低且存在模态对齐损失，亟需轻量、嵌入VLM内部的检索方案。

### 方法关键点
- 仅新增单个可学习embedding（ReToken）和一层投影矩阵，VLM本体默认冻结，训练成本极低，单H100即可完成训练
- 放弃传统query-key注意力得分做检索，改用Transformer最后一层的value空间特征，计算ReToken与各视觉单元（帧/图）平均value向量的余弦相似度作为检索得分，用类别均衡的二分类交叉熵做监督
- 推理采用两阶段流水线：先离线预处理所有视觉内容生成持久化KV cache，查询时第一阶段用ReToken召回Top-K相关视觉单元，第二阶段仅基于召回单元的KV cache生成结果，多查询共享预处理缓存

### 关键实验
- 图像数据集Visual Haystacks上，冻结Qwen3VL-8B时比基线提升13.4个点，冻结InternVL3.5时提升12.4个点，相对增益超20%
- 仅用多图像QA训练的ReToken可零样本迁移到长视频场景，在平均时长68分钟的LVBench数据集上，Qwen3VL-8B准确率提升8个点
- 效率方面，单H100即可支持小时级视频推理，每查询仅增加0.4s左右的检索开销，生成阶段显存和耗时与基线一致

### 核心结论
预训练多模态模型中，value空间携带的文本-视觉对齐信号远强于query-key注意力得分，是更可靠的跨模态检索特征来源
