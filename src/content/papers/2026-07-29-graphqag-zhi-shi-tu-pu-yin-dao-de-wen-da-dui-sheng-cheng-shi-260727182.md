---
title: 'GraphQAG: A Knowledge-Graph-Guided Visual Analytics Framework for Question-Answer
  Pairs Generation'
title_zh: GraphQAG：知识图谱引导的问答对生成视觉分析框架
authors:
- Yize Li
- Ruiqi Yu
- Tianya Pan
- Ningxin Li
- Songyue Li
- Xiangyang Wu
- Jinchang Li
- Zhiguang Zhou
arxiv_id: '2607.27182'
url: https://arxiv.org/abs/2607.27182
pdf_url: https://arxiv.org/pdf/2607.27182
published: '2026-07-29'
collected: '2026-08-01'
category: LLM
direction: LLM训练数据构造 · 知识图谱增强
tags:
- Knowledge Graph
- QA Generation
- Long Document Understanding
- Visual Analytics
- LLM Training Data
one_liner: 提出知识图谱引导的可视化分析框架，从长文档生成高覆盖高可信的高质量QA对
practical_value: '- 电商客服QA库、商品知识库构建可复用其三阶段流程：先抽取商品/品类/属性/活动等实体关系构建业务KG，再基于多跳路径约束LLM生成QA，天然覆盖跨场景关联知识

  - 长文档（如商品详情页、品牌手册、平台规则）的RAG训练数据构造，可引入KG路径约束提升QA对知识覆盖率，减少生成幻觉

  - 可借鉴KG可视化交互校验逻辑，对生成的推荐话术、商品文案、客服QA做可解释性校验，快速定位知识缺口迭代优化'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有QA生成方法无法有效处理长文档中分散在多段落、通过复杂实体关系关联的碎片化知识，普遍存在核心内容覆盖不全、跨段落语义关联缺失、多实体关系表达错误等问题，难以满足知识库构建、LLM post-training等场景的高质量数据需求。
### 方法关键点
GraphQAG采用三阶段工作流：1）长文档分段后抽取核心实体、关系，构建文档级知识图谱；2）基于实体、关系、多跳路径构建图结构生成空间，约束引导LLM生成QA对，避免偏离核心知识；3）以KG为交互可视化载体，支持用户探索知识结构、校验QA对的覆盖度与证据来源，通过图交互迭代优化QA集。
### 关键结果
通过16名参与者的用户研究、2个案例分析及专家访谈验证，GraphQAG可有效帮助用户识别知识覆盖缺口、校验生成QA质量、迭代优化QA集，产出的QA对全面性、可信度显著优于传统方案。
