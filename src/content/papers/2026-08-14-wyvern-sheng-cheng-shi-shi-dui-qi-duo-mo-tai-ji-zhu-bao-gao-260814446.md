---
title: 'Wyvern: An Agentic Framework for Generating Grounded Multimodal Reports'
title_zh: Wyvern：生成事实对齐多模态技术报告的多智能体框架
authors:
- Beatrice Alessandra Motetti
- Emilien Guandalino
- Daniele Jahier Pagliari
- Alessio Burrello
- Lorenz K. Müller
- Konstantin Berestizshevsky
- Lukas Cavigelli
affiliations:
- Politecnico di Torino
- Huawei Research Computing Systems Lab
arxiv_id: '2608.14446'
url: https://arxiv.org/abs/2608.14446
pdf_url: https://arxiv.org/pdf/2608.14446
published: '2026-08-14'
collected: '2026-08-17'
category: MultiAgent
direction: 多智能体协作 · 事实对齐多模态内容生成
tags:
- MultiAgent
- RAG
- Factuality
- Multimodal
- Content Generation
one_liner: 集成多模态内容插入与原子事实校验的多智能体技术报告自动化生成框架
practical_value: '- 可复用原子事实校验修正流程：生成内容后拆分原子claim+两轮核验（先引用摘要后全文）+自动修正，可直接迁移到电商商品卖点生成、营销文案生成的事实校验环节，降低虚假宣传风险

  - 多模态内容自动插入工程链路可复用：从候选素材提取语义描述→匹配对应章节→自动修改上下文无缝整合的流程，可用于生成带图/表的商品详情页、品类分析报告、用户个性化内容Feed

  - 多Agent分工设计可参考：按任务拆分独立单职能Agent（检索/筛选/生成/校验/润色），比单Agent端到端生成的可控性、可迭代性更强，适合企业级RAG类应用落地

  - 自动评估避坑结论可复用：LLM做长文本自动评估存在显著顺序偏置，且和人评相关性低，涉及内容质量的核心评估必须结合人工抽样校验'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前各领域信息爆发式增长，AI生成的长文本内容普遍存在幻觉、无可靠引用、缺乏多模态支撑的问题，现有自动化报告生成框架要么仅支持纯文本，要么无显式事实校验环节，生成内容可信度低，难以满足专业场景需求。
### 方法关键点
- 采用模块化多Agent架构，分三大核心阶段：①搜索阶段：自动生成检索query爬取网页，经多轮过滤、去重、摘要生成结构化知识库；②报告生成阶段：两步生成大纲、分段扩写文本，自动匹配插入相关图片、对比表格并修正上下文实现无缝融合；③事实校验阶段：拆分文本为原子claim，先基于引用摘要核验，可疑claim再调用原文二次核验，自动修正或删除无依据内容
- 所有Agent基于开源LLM实现，无专有模型依赖，支持本地化部署
### 关键结果
对比STORM、WebThinker、WikiAutoGen三个SOTA基线：
- 人评显示报告有用度分别领先3个基线100%、62.5%、87.5%，图片信息度比支持多模态的WikiAutoGen优87%
- 自动评估显示引用召回最高提升2.3×，引用精度最高提升1.6×，仅事实校验模块即可带来21%的引用召回提升
> 最值得记住的结论：多Agent分职能协作+显式事实校验，比单模型端到端优化的落地投入产出比更高，是提升生成式长内容可信度的核心路径。
