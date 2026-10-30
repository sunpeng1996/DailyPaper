---
title: 'VeriCUA: Verification as Agentic Exploration for Computer-Using Agents'
title_zh: VeriCUA：面向计算机操作Agent的智能探索式验证框架
authors:
- Qiushi Sun
- Da Yu
- Alexander Knop
- Amer Sinha
- Lingpeng Kong
- Ben Kao
- Ravi Kumar
- Pritish Kamath
affiliations:
- Google
- The University of Hong Kong
arxiv_id: '2610.40578'
url: https://arxiv.org/abs/2610.40578
pdf_url: https://arxiv.org/pdf/2610.40578
published: '2026-10-29'
collected: '2026-10-30'
category: Agent
direction: Agent 任务完成自动化验证
tags:
- Computer-Using-Agent
- Verification
- Agentic-Exploration
- Reward-Modeling
- Evaluation
one_liner: 提出平台无关的智能探索式验证框架，大幅提升计算机操作Agent任务校验准确率并降低误报
practical_value: '- 电商/运营类GUI Agent的任务校验（比如自动上架商品、客服工单处理）可直接复用VeriCUA的流程：先上下文探查生成校验规则，再混合调用GUI截图、后台数据接口采证，相比单VLM校验可降低假阳率70%以上

  - 低容错校验场景（比如Agent执行付费投放、优惠券发放后的结果校验）可复用证据分级机制：仅实采的后台状态、持久化数据等attested证据可判定成功，Agent自身的完成声明不单独作为判定依据，避免业务损失

  - 离线轨迹数据清洗场景（比如推荐系统行为轨迹质量校验、Agent历史执行样本筛选）可借鉴多路径探查+ fallback设计，在有限观测下平衡准确率和样本保留率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前计算机操作Agent（CUA）在桌面/移动/网页端的任务完成校验存在明显缺陷：VLM校验仅依赖提供的观测视图易漏关键证据，脚本化校验依赖预定义状态访问逻辑适用性差，跨平台定制校验的工程成本极高，而Agent训练、评估、数据清洗环节都需要低误报的可靠校验结果。

### 方法关键点
- 统一校验范式：将校验转化为动态证据采集评估流程，同时支持在线（实时环境）、离线（历史轨迹）双场景，跨平台通用
- 规则先行：先探查上下文（在线扫应用/目录/数据库schema，离线扫轨迹/帧/结构化数据），生成包含硬（必达）、软（附加）要求的可落地校验规则
- 混合采证：支持GUI工具（截图、OCR、a11y树读取）和代码工具（文件读、数据库查询、系统接口调用），优先解决未决的校验项
- 证据分级仲裁：仅attested类证据（实采状态、操作后截图等）可判定要求满足，asserted类证据（Agent自身的完成声明等）仅用于引导探查，证据不足可弃权，最终用显式规则输出结果

### 关键实验
在线场景测试AndroidWorld、OSWorld、ScienceBoard三个基准，相比VLM judge、自动生成校验器两个基线，准确率最高提升14.8pct，假阳率最低降至5.4%；离线场景测试OSReward、WebArena等基准，硬样本上准确率比最优基线高4.7pct，可拒绝80%的Agent虚假完成声明。

### 核心结论
Agent校验的核心是采集可信证据而非依赖模型直觉，多源证据融合+规则仲裁是实现低误报、高可靠判定的最优路径。
