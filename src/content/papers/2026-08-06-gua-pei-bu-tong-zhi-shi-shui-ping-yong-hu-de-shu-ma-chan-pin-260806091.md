---
title: '"I don''t know anything about laptops!" - User Perception of Digital Product
  Advisors Adapting to Their Knowledge Levels'
title_zh: 适配不同知识水平用户的数码产品对话顾问用户感知研究
authors:
- Kevin Schott
- Andrea Papenmeier
- Daniel Hienert
- Dagmar Kern
affiliations:
- GESIS – Leibniz Institute for the Social Sciences
- University of Twente
arxiv_id: '2608.06091'
url: https://arxiv.org/abs/2608.06091
pdf_url: https://arxiv.org/pdf/2608.06091
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: 电商对话Agent · 用户知识水平适配
tags:
- Conversational Commerce
- Product Advisor
- User Experience
- Personalization
- E-commerce Agent
one_liner: 通过251人笔记本选购实验，验证TCE信息格式可兼顾新老用户的对话导购体验
practical_value: '- 3C类电商对话导购默认采用TCE（技术参数+性能档位+属性解释）信息展示格式，无需拆分新手/专家双版本，该格式不会降低专家用户体验

  - 性能档位标签不可单独使用，必须搭配属性功能解释，否则新手感知帮助度显著低于纯参数基线，易造成参数理解困惑

  - 可通过1-7分的自我领域知识评分快速分层用户，无需复杂的客观知识测试，分层结果与用户实际体验需求匹配度高

  - 对话导购增加自定义参数入口，满足专家对品牌、价格等额外属性的需求，同时给新手提供多档位参数选项提升决策掌控感'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
对话式电商中，不同知识水平用户对复杂数码产品参数的理解能力差异极大：新手看不懂专业参数，易依赖第三方评价做出非最优决策，专家又可能被冗余信息干扰；现有对话导购缺乏适配不同知识水平用户的信息展示标准，相关实证研究十分稀缺。

### 方法关键点
- 采用2×4组间实验设计：用户按自我报告的笔记本知识评分分为新手（1-4分）/专家（5-7分），对照4种信息格式：纯技术参数T（基线）、参数+性能分类TC、参数+属性解释TE、参数+分类+解释TCE
- 测试场景为规则式笔记本选购对话导购，固定交互流程，仅变更参数展示的补充信息，排除其他干扰变量
- 评估指标覆盖信息适量度、感知学习量、信息相关性、信任度、信息帮助度5个核心维度

### 关键实验结果
招募251名英美用户完成实验，核心结论：
1. 新手组中TCE格式的信息适量度评分比T高26.1%、比TC高46.4%，感知学习量比T高38.8%、比TC高38.3%，帮助度比TC高41.4%
2. 专家组4种格式的所有评估指标均无显著差异，补充信息不会降低专家体验
3. 新手在无解释的T/TC组中属性理解困惑占比达60%，TCE组可将该占比降低到34%

### 核心结论
3C类对话导购无需做新手/专家分界面，默认用TCE格式即可兼顾所有用户的体验需求，单独添加性能分类反而会伤害新手体验。
