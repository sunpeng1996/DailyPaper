---
title: 'AgentKGV: Agentic LLM-RAG Framework with Two-Stage Training for the Fact Verification
  of Knowledge Graphs'
title_zh: 面向知识图谱事实校验的双阶段训练Agentic LLM-RAG框架AgentKGV
authors:
- Yumin Heo
- Hyeon-gu Lee
- Sumin Seo
- Youngjoong Ko
affiliations:
- SungKyunKwan University
- NAVER
arxiv_id: '2607.09092'
url: https://arxiv.org/abs/2607.09092
pdf_url: https://arxiv.org/pdf/2607.09092
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: Agent结合RAG优化知识图谱事实校验
tags:
- Agent
- RAG
- Knowledge Graph
- SFT
- GRPO
- Fact Verification
one_liner: 提出融合动态路由与迭代查询改写的Agentic RAG框架，搭配双阶段训练实现高精度低成本KG事实校验
practical_value: '- 电商商品属性、用户行为三元组等结构化数据的事实校验场景，可复用基于(s,p,o)结构的多粒度查询改写方案，解决结构化数据到自然语言文档的模态匹配gap

  - Agent迭代检索场景下可直接复用双阶段训练范式：先用大模型蒸馏SFT对齐稳定决策能力，再用带检索成本惩罚的GRPO优化检索次数，兼顾精度与成本

  - 电商/搜索query改写场景，可借鉴预定义多组件组合模板的设计，让Agent动态选择查询粒度，覆盖长尾谓词/小众属性的语义表达差异

  - 多轮检索系统优化时，可引入历史检索结果压缩摘要模块，控制上下文长度的同时避免重复检索，降低推理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
自动构建的知识图谱（KG）普遍存在事实错误，传统图结构校验无法发现外部事实错误，LLM易出现幻觉，单轮RAG受限于结构化三元组与自然语言文档的表述差异，检索准确率低；工业级场景下现有Agentic RAG方案存在查询改写不稳定、检索次数过多成本过高的问题，亟需兼顾精度与成本的解决方案。

### 方法关键点
- 框架层面：设计动态路由模块，先判断是否可用内部参数知识直接校验，避免不必要检索；需检索时基于(s,p,o)结构选择多粒度组件组合生成初始查询，再根据历史检索结果迭代改写查询，搭配检索摘要模块压缩历史上下文，控制输入长度
- 训练层面：双阶段训练，第一阶段用大模型生成的正确校验轨迹做蒸馏SFT，对齐查询改写与证据推理能力，解决长尾谓词下的改写不稳定问题；第二阶段用带检索次数惩罚的GRPO做轨迹级优化，奖励正确校验结果、惩罚多余检索调用，优化检索效率

### 关键实验
在T-REx公开数据集长尾谓词拆分上，AgentKGV框架比单轮RAG macro-F1高5.5%p，加双阶段训练后进一步提升9.4%p；GRPO将平均检索调用次数从3.24降到1.63且精度无下降；在NAVER内部韩语企业KG上，双阶段训练版比IRCoT基线macro-F1高9.7%p。

Agentic RAG落地工业场景时，先用蒸馏SFT对齐能力下限，再用带成本约束的RL优化效率上限，是兼顾精度与成本的通用范式。
