---
title: 'Large Knowledge Model: From Papers to a Scientific Reasoning Landscape'
title_zh: 大知识模型：从论文构建可计算的科学推理图景
authors:
- Yuan Huang
- Sihan Hu
- Hongyu Gu
- Chao Ma
- Jiaxing Zhang
- Zhiyong Zou
- Caiyu Fan
- Yan Xiao
- Mingjun Xu
- Chenyu Xie
affiliations:
- DP Technology, Beijing
- Institute of Theoretical Physics, Chinese Academy of Sciences
- Peking University
- Lanzhou University
- AI for Science Institute, Beijing
arxiv_id: '2609.27297'
url: https://arxiv.org/abs/2609.27297
pdf_url: https://arxiv.org/pdf/2609.27297
published: '2026-09-23'
collected: '2026-09-24'
category: RAG
direction: 科学领域RAG · 推理图知识建模
tags:
- Large Knowledge Model
- Reasoning Graph
- RAG
- Scientific QA
- Knowledge Representation
one_liner: 将学术论文转化为溯源推理图，构建三重视图的科学推理基础设施，提升检索与知识问答效果
practical_value: '- 知识加工思路可迁移：将商品详情、用户评价、客服话术等非结构化业务文本转化为带溯源的推理图，替代传统纯文本RAG的片段式召回，提升导购问答、售后问题解决的准确性

  - 多视图架构可复用：针对业务场景构建「用户需求-解决方案-效果证据」三对齐视图，支持需求召回、流程推荐、效果归因的连贯链路，适配电商Agent导购、投诉排查等场景

  - 混合检索策略可直接落地：将语义向量检索与推理图结构遍历结合，同时优化召回的相关性和上下文关联性，可直接用于商品搜索、问答系统的召回层升级

  - 溯源归因机制可借鉴：所有推理节点保留原始来源锚点，解决生成式回答的幻觉问题，可用于要求结果可解释的电商合规话术生成、虚假宣传拦截场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有科学文献检索与QA系统多基于文本片段匹配，缺乏对论文内在推理逻辑（问题、方法、结论、证据的关联）的建模，无法支撑跨论文的证据对比、方法复用与研究规划，科学Agent的知识访问效率和准确性存在瓶颈。
### 方法关键点
- 提出源锚定的论文级推理图表示：将每篇论文拆解为问题、主张、推理链、证据、方法等类型化节点，保留原始来源位置与上下文，通过有向边构建推理依赖关系
- 统一向量+图访问层：为每个推理节点生成语义向量支持跨表述的语义匹配，同时保留图结构支持推理路径遍历，通过哈希绑定实现跨论文的相同对象归一
- 构建三对齐的科学推理图景：包含问题图景（组织研究问题与开放方向）、工作流图景（聚合可复用的科研流程）、证据图景（关联结论的支持/反对证据与适用条件），三类视图共享底层推理节点
### 关键实验
基于PaSaMaster、ChemBench、PubMedQA、SciBench、ScholarQA数据集，对比Science Navigator、Web Search、谷歌学术等baseline，核心结果：
1. LKM混合检索在PaSaMaster上NDCG@5/10/20分别达22.19%/21.00%/20.93%，较Science Navigator最高提升1.65个百分点
2. 固定GPT-5.4作为生成模型，LKM检索较裸模型在ChemBench/PubMedQA/SciBench上准确率分别提升9.30/4.20/14.69个百分点
3. LKM图结构上下文在ScholarQA-CS/Multi上的引文F1较纯检索分别提升5.71/6.67个百分点，回答质量持平
### 核心结论
知识的价值不仅在于内容本身，更在于其所在的推理链路与上下文关联，结构化的知识表示是实现可信、可复用知识访问的核心前提
