---
title: 'Characterizing Web Search by Conversational LLM Agents: From Search Decisions
  and Strategies to Results and Responses'
title_zh: 四大商业对话LLM Agent的Web搜索全链路行为特征分析
authors:
- Mahsa Amani
- Seungeon Lee
- Abhisek Dash
- Asmaa El Fraihi
- Yunah Jang
- Elisabeth Kirsten
- Qinyuan Wu
- Krishna P. Gummadi
- Manish Gupta
- Abhilasha Ravichander
affiliations:
- Max Planck Institute for Software Systems
- Ruhr University Bochum
- Saarland University
- Microsoft
- Seoul National University
arxiv_id: '2609.19244'
url: https://arxiv.org/abs/2609.19244
pdf_url: https://arxiv.org/pdf/2609.19244
published: '2026-09-16'
collected: '2026-09-18'
category: Agent
direction: Agent 搜索工具调用行为分析
tags:
- Agentic Search
- Tool Calling
- LLM Evaluation
- Web Search
- Grounded Generation
one_liner: 首次对比四大主流商业LLM Agent的搜索全链路行为，量化决策、策略、输出各环节差异
practical_value: '- 做Agent工具调用决策时不要盲目提升搜索调用率，高调用率不一定提升响应质量，可参考结论在系统prompt（harness）和模型决策间找平衡，比如电商导购Agent仅对实时商品、促销类query触发搜索，降低不必要的调用成本

  - Agent查询生成可复用迭代提效思路：将用户长prompt压缩为10~15词的精准搜索query，多轮迭代时逐步增加时间、地域、商品实体等约束缩小搜索范围，适合电商多轮导购场景的query改写

  - 做搜索增强回答的归因逻辑时，注意避免漏引有效搜索URL，论文显示14%~53%的回答内容来自未引用的搜索结果，既容易引发版权问题，也会降低用户信任，电商场景下商品信息必须绑定对应商品页引用提升合规性

  - 自建Agent专属搜索引擎时要注意领域覆盖平衡，避免平台偏向导致的信息茧房，比如电商搜索不要只召回自有平台商品，可接入第三方比价、测评类域名结果提升回答公信力'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前对话LLM Agent的Web搜索已成为主流功能，但全链路行为（从调用决策到结果生成）缺乏跨平台的系统性实证研究，搜索调用是否真能提升回答质量、各环节存在的潜在偏差与问题均不明确，难以支撑Agent搜索系统的优化。

### 方法关键点
- 采用双实验设置：invivo基于GDPR合规的用户数据捐赠，覆盖四大平台613位用户的17.1万条真实会话全链路搜索trace；invitro用脱敏后的1000条相同用户prompt调用各平台API，控制输入变量做横向对比
- 分析覆盖搜索全链路三个核心阶段：是否调用搜索的决策逻辑、query生成与迭代策略、搜索结果到回答的归因与落地
- 评估维度包含搜索调用率、query复杂度、搜索结果域名偏好、回答的事实性/完整性/相关性、引用率、claim归因准确率

### 关键结果数字
- 不同平台搜索调用决策差异极大：相同prompt下GPT-5.3调用率仅14%，Claude达83%；高调用率不必然提升质量，Claude开启搜索后回答事实性得分反而从3.41降至3.29
- Agent生成query长度集中在10~15词，多轮迭代中时间/地域/实体特异性平均提升10%~50%
- 平台专属搜索引擎存在强域名偏好：ChatGPT/Grok前10域名占搜索结果的21%~32%，Claude完全不返回reddit、YouTube结果，DeepSeek包含大量小红书内容
- 回答存在广泛漏引：14%~53%的回答claim来自未被引用的搜索结果，无搜索支撑的参数知识生成的claim事实性得分比引用搜索结果的低0.5~0.6分

### 核心结论
Agent搜索是多环节联动的决策过程，单独优化检索环节无法解决所有问题，必须同时优化调用时机、查询策略、归因逻辑三个阶段才能提升搜索增强回答的可靠性
