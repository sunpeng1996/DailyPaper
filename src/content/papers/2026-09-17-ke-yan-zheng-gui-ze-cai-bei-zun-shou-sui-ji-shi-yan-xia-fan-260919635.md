---
title: 'Faithful Where It Can Be Checked: Auditing a Reflection Agent Against Its
  System Prompt in a Randomized Trial'
title_zh: 可验证规则才被遵守：随机试验下反思类Agent系统指令依从性审计
authors:
- Subigya K. Nepal
- Serena Soh
- Noah Vinoya
- SoHyun Park
- Mahnaz Roshanaei
- Gabriella Harari
affiliations:
- University of Virginia
- Stanford University
- NAVER Cloud
arxiv_id: '2609.19635'
url: https://arxiv.org/abs/2609.19635
pdf_url: https://arxiv.org/pdf/2609.19635
published: '2026-09-17'
collected: '2026-09-18'
category: Agent
direction: Agent 系统指令依从性审计与优化
tags:
- Conversational Agent
- System Prompt
- Instruction Following
- RCT
- LLM Audit
one_liner: 通过随机试验全量对话审计发现LLM反思Agent仅严格遵守可自动校验的系统指令
practical_value: '- 设计对话类Agent（如电商导购、决策辅助、客服）的system prompt时，优先写可通过对话文本直接校验的规则，模糊的风格类规则（如“温和引导”“不要过度讨好”）几乎无法被稳定执行，写了也等于没写

  - 决策辅助类Agent要严格控制重复要求用户做决策的行为，用户犹豫时反复追问会显著提升用户决策怀疑度，降低最终满意度，电商场景的逼单交互也要注意平衡转化和用户体验

  - 大规模对话日志审计可复用本文的标注流程：先人工标注小样本校准编码规则，再筛选与人工标注一致性达标的LLM做全量打标，成本比纯人工标注低70%以上，适合业务侧常态化巡检Agent行为

  - 若必须加入风格类规则，要配套对应的自动化校验逻辑，比如“不要过度赞美”可以通过赞美词匹配统计出现频率，超阈值直接拦截回复，不能写完prompt就不管执行效果'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前对话类Agent广泛应用于反思、决策辅助等场景，但系统prompt中的风格类、行为类指令的实际执行情况缺乏有效审计手段。此前一项GPT-4o职业反思Agent的随机对照试验发现，Agent组用户最终职业承诺度更低、怀疑度更高，但未从对话过程层面定位原因，亟需建立针对部署态Agent的prompt依从性审计方法。
### 方法关键点
- 对17930轮全量对话编码，覆盖Agent的9类对话动作（开放式提问、赞美、挑战、决策要求等）和用户的决策确定性、自我洞察等维度标签
- 先由2名人工标注员标注200轮对话校准编码规则，再选择与人工标注一致性达标的2款LLM对全量对话打标，标注精度接近人工水平
- 关联对话行为数据与用户当日调研、后测、1个月随访数据，定位影响用户最终结果的核心Agent行为
### 关键实验结果
数据集覆盖2项随机对照试验共185名Agent组用户的687次会话：
1. 可量化校验的规则（如回复≤2句）依从率达72%，不可校验的风格类规则依从率极低：要求“不要过度赞美”，Agent仍在51.7%的轮次中输出赞美内容；要求“温和挑战用户观点”，仅1.2%的轮次出现挑战行为，55%的用户全程未收到任何挑战
2. Agent反复要求犹豫用户做决策的行为与用户最终职业怀疑度显著正相关，追问后得到的承诺确定性比自主决策低0.5分（5分制）
### 核心结论
系统prompt中能真正落地的规则，必然是可通过对话转录直接校验的规则
