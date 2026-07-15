---
title: 'StoryTeller: Training-Free Narrative Grounding for Long-Form Audio Description'
title_zh: StoryTeller：面向长音频描述的免训练叙事接地框架
authors:
- Seung Hyun Hahm
- Minh T. Dinh
- SouYoung Jin
affiliations:
- Dartmouth College
arxiv_id: '2607.11798'
url: https://arxiv.org/abs/2607.11798
pdf_url: https://arxiv.org/pdf/2607.11798
published: '2026-07-13'
collected: '2026-07-15'
category: Multimodal
direction: 多模态长视频理解 · 免训练叙事对齐
tags:
- Long-Form Video Understanding
- Training-Free
- RAG
- VLM
- Narrative Grounding
one_liner: 提出免训练长音频描述框架，通过可验证叙事记忆与元数据校验提升跨场景描述连贯性与事实性
practical_value: '- 长序列生成类任务（如电商长篇商品测评生成、直播间内容旁白生成）可复用「动态校验式记忆池」架构，跨片段保留核心上下文，避免前后矛盾

  - 外部知识增强的多模态生成场景可借鉴「RAG+VLM事实校验」流，仅保留与本地模态输入匹配的外部知识，大幅降低幻觉

  - 长内容生成效果的评估可复用QA-based评估思路，通过上下文关联问题的回答准确率间接衡量叙事连贯性，降低人工评估成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有VLM处理长视频音频描述任务时独立拆分片段处理，缺失跨场景人物、事件、上下文关联信息，生成内容叙事连贯性差、事实性不足；现有方案普遍依赖任务微调、字幕/剧本/预训练人物特征等前置输入，落地成本高。
### 方法关键点
1. 完全免训练架构，无需标注数据、任务微调或前置特征预处理，仅需原始视频+影片名称即可运行；
2. 维护经校验的叙事记忆池，跨场景传递故事核心信息，保证生成内容前后连贯；
3. 支持可选召回公开影片元数据补全上下文，通过语义过滤+VLM校验两步机制，仅保留和当前视频内容匹配的召回知识，避免幻觉。
### 关键结果
在标准AD基准与多类长视频测试集上，自动指标、QA基叙事评估、人工评估三类评测均显著优于强基线，叙事连贯性、事实对齐性、故事可理解度均获得稳定提升，同步推出StoryAD-QA长文本叙事效果评估基准。
