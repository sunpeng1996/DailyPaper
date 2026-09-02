---
title: 'TRIAGE: Three-level Routing and Intelligent Agent Guidance for Efficient Execution'
title_zh: TRIAGE：三级路由与智能Agent引导的LLM Agent高效执行框架
authors:
- Ruocan Wei
affiliations:
- China Telecom Cloud, Beijing, China
arxiv_id: '2609.01428'
url: https://arxiv.org/abs/2609.01428
pdf_url: https://arxiv.org/pdf/2609.01428
published: '2026-09-01'
collected: '2026-09-02'
category: Agent
direction: LLM Agent执行效率优化 · 轨迹复用
tags:
- LLM Agent
- Token Efficiency
- Trajectory Reuse
- Routing
- TaaS
one_liner: 提出基于轨迹复用的三级路由框架TaaS，大幅降低LLM Agent执行的token消耗
practical_value: '- 电商客服、运营数据分析、广告效果查询等高重复Agent场景可直接复用三级路由逻辑：用轻量语义编码器做相似度匹配，精确匹配直接返回结果，参数相似的查询用历史轨迹模板替换，无需LLM推理，大幅降低token成本

  - 可复用TaaS（Trajectory-as-a-Skill）设计思路：无需人工预定义技能，自动将历史成功执行轨迹沉淀为参数化可复用技能，降低技能库的维护成本，尤其适合大促等高频固定查询场景

  - 路由策略选择可直接参考实验结论：结构化高重复查询场景优先采用零成本的阈值路由；仅当单查询执行成本远高于路由开销时，再考虑使用LLM路由，避免为优化反而增加额外成本

  - 冷启动优化技巧：业务上线前可导入历史高频查询的执行轨迹预生成技能库，跳过初始冷启动阶段，快速实现token成本下降'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
ReAct范式的LLM Agent每次查询都从零开始推理，相似查询会重复执行相同步骤，现有缓存、prompt压缩、投机解码等方案均无法消除重复推理的冗余，token成本居高不下，在BI分析、监控、客服等高重复查询场景浪费尤为严重。
### 方法关键点
- 核心创新TaaS（Trajectory-as-a-Skill）：将历史成功执行轨迹抽象为可复用技能，形成「存储-检索-复用-提炼」的闭环，系统使用频率越高，效率越高
- 三级路由机制：基于all-MiniLM-L6-v2语义编码器的余弦相似度做路由，L1（相似度≥0.98，精确匹配直接返回结果，0 token）、L2（相似度≥0.90，匹配提炼好的技能做参数替换，0 token）、L3（相似度<0.90，走全量ReAct，执行后轨迹自动入库）
- 自动技能提取：无需人工标注或预训练，自动将高频轨迹提炼为参数化模板，动态更新参数提取规则
### 关键实验
- 1007条安全监控查询场景：对比纯ReAct基线，总token节省62.3%，61.5%的查询走L1+L2零token路径，API调用减少58.2%；冷启动阶段前100条查询L2命中率就升至57%，平均单query token成本从198降至74.7
- ToolBench 15个域345条查询跨域验证：平均token节省76.3%，96.2%的查询走L1+L2路径，验证框架通用性
-  ablation实验：去掉L2机制后token节省率降至55%；LLM路由因路由开销过高反而导致总token消耗增加37.3%
### 核心结论
效率提升的核心是消除不必要的LLM调用，而非增加更复杂的LLM调用，阈值路由与轨迹复用的组合在高重复结构化查询场景下性价比远高于其他优化方案。
