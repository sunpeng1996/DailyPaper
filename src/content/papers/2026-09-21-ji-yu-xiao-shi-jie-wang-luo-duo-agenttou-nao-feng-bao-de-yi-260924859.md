---
title: Small-world Networks of Agents Brainstorm AI Risks to Support Ideation
title_zh: 基于小世界网络多Agent头脑风暴的AI风险创意识别框架
authors:
- Ke Zhou
- Edyta Bogucka
- Daniele Quercia
affiliations:
- Nokia Bell Labs, UK
- University of Nottingham, UK
- Politecnico di Torino, Italy
arxiv_id: '2609.24859'
url: https://arxiv.org/abs/2609.24859
pdf_url: https://arxiv.org/pdf/2609.24859
published: '2026-09-21'
collected: '2026-09-22'
category: MultiAgent
direction: 多智能体协作 · 创意生成与风险识别
tags:
- MultiAgent
- Small-world Network
- Brainstorming
- Risk Assessment
- LLM Agent
one_liner: 通过小世界网络连接多角色LLM Agent模拟利益相关者，挖掘传统方法遗漏的高新颖度AI系统性风险
practical_value: '- 做多Agent创意生成（营销文案、商品卖点、活动创意）或风险巡检场景时，优先选择小世界网络拓扑，相比平层、层级结构可同时提升产出的多样性和整体质量

  - 需要挖掘长尾、非共识的高价值信息（用户冷门痛点、业务边缘风险）时，可采用介数中心性对Agent产出排序，能显著提升非典型优质结果的检出率

  - 多角色Agent的角色枚举环节可复用递归雪球法，从初始核心角色出发迭代扩展再语义去重，避免遗漏边缘角色的独特视角'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
AI风险评估的初始创意阶段常从空白或有限预设风险列表启动，传统单LLM、平层多Agent方法易锚定共识性风险，遗漏跨角色的系统性、长尾风险；人工workshop成本高、难扩展，也无法有效覆盖边缘利益相关方的视角。
### 方法关键点
- 角色扩展：通过递归雪球法动态挖掘相关利益相关方角色，用语义相似度去重，覆盖初始列表遗漏的边缘角色
- 网络构建：将角色实例化为LLM Agent，分别搭建层级、小世界、随机三种拓扑的交互网络，保留高权重边并去环形成DAG，Agent按网络流向接收上游信息迭代生成风险
- 排序策略：提供度中心性、介数中心性、接近中心性三种风险排序逻辑，分别适配共识优先、新颖优先、全局信息优先的不同需求
### 关键实验
基于AI陪伴聊天bot场景测试，基准为45名AI从业者workshop生成的244条风险，对比单LLM提示、平层多Agent（Plurals）两个基线：①小世界网络+介数中心性组合的风险新颖度比单LLM高1.1分，比平层多Agent高0.5分（归一化5分制Likert），且未降低风险合理性、严重性；②用户实验中，用该方法输出作为种子的团队，比用从业者风险作为种子的团队多识别35%的总风险，其中人因交互、社会经济类长尾风险数量提升超130%。
### 核心结论
多Agent系统的产出质量不仅取决于角色定义，Agent之间的连接拓扑与排序逻辑对结果的影响远大于单个Agent的能力
