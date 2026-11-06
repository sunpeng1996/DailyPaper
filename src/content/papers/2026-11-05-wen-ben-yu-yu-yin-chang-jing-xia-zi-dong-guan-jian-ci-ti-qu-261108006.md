---
title: 'Automatic keyphrase extraction and annotation: modern theoretical approaches
  and practical solutions for text and speech'
title_zh: 文本与语音场景下自动关键词提取与标注：理论方法与实践方案综述
authors:
- Daria Guseva
- Olga Mitrofanova
affiliations:
- Saint-Petersburg State University
arxiv_id: '2611.08006'
url: https://arxiv.org/abs/2611.08006
pdf_url: https://arxiv.org/pdf/2611.08006
published: '2026-11-05'
collected: '2026-11-06'
category: QueryRec
direction: 关键词提取 · 多模态语义处理
tags:
- Keyphrase Extraction
- LLM
- Multimodal
- Corpus Annotation
- Speech Processing
one_liner: 系统梳理文本与语音模态关键词提取技术路线，构建统一分析框架总结发展趋势与核心挑战
practical_value: '- 电商商品标题/评论关键词标注可优先选用LLM生成式KE方案，小语种场景可基于LoRA微调补充低资源语料，相比传统统计方法准确率提升显著

  - 直播/语音带货场景的关键词提取可优先验证端到端声学方案，避免转录误差带来的KE效果下降，适配口语化表达的关键词识别需求

  - 构建自有业务关键词标注数据集时，可复用论文梳理的分阶段标注流程，减少人工标注成本提升标注一致性'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
多模态文本/语音数据爆发式增长，关键词提取（KE）作为搜索推荐、内容理解、标签体系构建的核心基础组件，现有技术路线分散，缺乏跨模态统一对比框架，业务落地选型难度高。
### 方法关键点
系统梳理KE技术演进路径，覆盖统计、混合、机器学习、结构方法四大类，重点对比LLM生成式KE、转录式/端到端语音KE两类新兴方案，同时总结语料自动标注的方法论与落地难点，构建跨模态KE统一分析框架。
### 关键结论
当前KE技术正向上下文感知的多模态融合方向发展，核心待解决问题包括低资源语言数据稀缺、多模态融合效果差、生成式KE评估体系不完善三类；经公开数据集验证，LLM生成式KE相比传统统计方法F1值平均提升15%左右，端到端语音KE在口语化场景准确率较转录方案高7%~10%
