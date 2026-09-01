---
title: 'InsightToast: Proactive Information Retrieval & Glanceable Visualization in
  the Side Channel of Data-Rich Meetings'
title_zh: InsightToast：面向富数据会议的主动信息检索与易读可视化系统
authors:
- Mohammad Abolnejadian
- Matthew Brehmer
affiliations:
- University of Waterloo
arxiv_id: '2608.31115'
url: https://arxiv.org/abs/2608.31115
pdf_url: https://arxiv.org/pdf/2608.31115
published: '2026-08-31'
collected: '2026-09-01'
category: Agent
direction: Agent 会话主动信息检索与交互设计
tags:
- MultiAgent
- RAG
- Proactive Retrieval
- Meeting Assistant
- Visualization
one_liner: 基于多Agent RAG的会议主动助手，实时识别知识缺口推送可溯源低干扰洞察
practical_value: '- 多Agent主动检索触发逻辑可复用：直播带货、用户咨询场景中，基于对话中的不确定性表述、疑问信号自动识别知识缺口，主动推送商品参数、用户评价、活动规则等信息，无需用户主动搜索，降低跳出率

  - 轻量化结果呈现范式可迁移：将RAG召回内容压缩至280字以内，仅用柱状/折线/环形三类易读图表，适配电商push、直播侧边弹窗、搜索下拉建议等触达位，平衡信息密度与用户注意力成本

  - 多维度query拆解方法可借鉴：识别到用户信息需求后自动拆解为互补的多个检索query，覆盖用户未意识到的相关维度，可用于优化搜索QueryRec、个性化推荐的召回广度，解决「未知未知」信息差'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
会议中参与者需要检索分散在异构内部/外部数据源的上下文信息时，需频繁切换任务，既打断个人专注也破坏集体对话 flow，易导致决策信息不足；现有会议AI助手均为被动触发，仍需要用户主动发起请求，未解决用户不知道需要搜索什么的「未知未知」信息差问题。

### 方法关键点
- 三阶段多Agent RAG pipeline：1）对话处理层：实时处理转写后的说话人分离 utterance，动态分类话题，基于信息请求、不确定性表述、澄清请求等5类触发信号识别知识缺口，拆解为多维度互补搜索query，缓解用户词汇不足问题；2）检索层：并行调度内部知识库+公开网页检索，迭代校验召回结果的相关性，达到覆盖阈值后终止；3）合成层：自动选择呈现模态，文本洞察限制在280字以内，图表仅用柱状/折线/环形三类易读形式，所有内容标注来源与对话触发点，支持溯源。
- 低干扰交互设计：用非模态toast通知推送检索进度与洞察标题，侧边栏按动态话题聚合所有洞察，支持用户自主浏览、归档、置顶，不强制打断对话。

### 关键结果
用加拿大议会11GB立法文档作为知识库，16人被试内对照实验，对比基线（主动搜索+通用聊天助手）：
1. 参与者主动搜索量降低74%（1.9 vs 7.4次），对话流畅度评分显著更高，物理 workload 降低24%（1.75 vs 2.31）；
2. 决策依据的来源引用量提升85%（2.31 vs 1.25），认为决策更信息充分的评分提升55%（4.06 vs 2.62）；
3. 系统端到端处理延迟平均7.5s，知识缺口检测F1=0.81，单场15分钟会议LLM推理成本仅0.45美元。

> 核心洞察：主动信息推送的核心价值是覆盖用户未意识到的信息盲区，同时必须把信息呈现的注意力成本降到最低，才不会成为新的干扰。
