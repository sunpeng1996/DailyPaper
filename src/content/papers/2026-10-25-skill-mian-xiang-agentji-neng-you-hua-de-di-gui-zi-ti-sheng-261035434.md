---
title: 'Skill^{infty}: Recursive Self-Improvement for Agent Skill Optimization'
title_zh: Skill∞：面向Agent技能优化的递归自提升框架
authors:
- Wangcheng Tao
- Zhanglu Yan
- Han Wu
- Weng-Fai Wong
affiliations:
- National University of Singapore
- City University of Hong Kong
arxiv_id: '2610.35434'
url: https://arxiv.org/abs/2610.35434
pdf_url: https://arxiv.org/pdf/2610.35434
published: '2026-10-25'
collected: '2026-10-27'
category: Agent
direction: Agent技能优化 · 递归自提升
tags:
- Recursive Self-Improvement
- Agent Skill
- Meta Skill
- Self-Evolving Agent
- LLM Agent
one_liner: 提出递归自提升的Agent技能优化框架，元技能可自我迭代且跨域复用，效果优于人工构建技能
practical_value: '- 可复用「元技能与任务技能解耦」的设计：将电商/推荐Agent的通用优化逻辑（如排序调优、文案生成规则迭代、用户负反馈归因）封装为元技能，一次迭代后可复用在商品推荐、广告投放、搜索引导等多任务，摊薄自提升成本

  - 可借鉴Agent主导的优化流程：替代传统固定规则的prompt/技能调优逻辑，让Agent自行诊断推荐/搜索链路的错误trace、生成优化候选、交叉验证效果，大幅降低人工调优的人力成本

  - 可复用独立审核+自适应预算分配机制：在推荐Agent技能迭代中加入独立审核环节，避免优化引入的业务风险（如违规文案、不合理排序）；自适应分配调优预算，对效果提升空间大的任务倾斜资源'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent技能优化方法多采用人工设计的固定流程，即使引入元技能也绑定单任务、无法跨域复用，优化效果易触达人工设计的天花板；技能优化逻辑本身可被编码为可迭代的技能，是实现递归自提升（RSI）、突破能力上限的低成本可行路径。

### 方法关键点
- 双循环递归架构：设置元技能、任务技能两层，元技能既指导任务技能优化，也可通过完全相同的流程优化自身，形成自增强闭环
- Agent主导的6步迭代流程：元Agent自主执行「检查历史→诊断执行trace→生成优化候选→效果评估→独立审核→迭代决策」，替代固定启发式调优规则
- 元技能与任务解耦：元技能在多领域技能优化任务上预迭代后，可直接复用于新任务的技能优化，摊薄自提升的算力与时间成本
- 全链路原生技能发现：两层技能均通过Agent原生机制加载，无人工prompt注入，优化效果可直接复现到部署环境

### 关键实验
在83个跨8领域的SkillsBench任务上，以GPT-6 Luna为底座，Skill∞ pass率达60.7%，优于人工构建技能的56.4%、SOTA方法SkillEvolver的54.5%；在KernelBench上平均加速比达1.62，是SkillEvolver的3倍以上；去掉元技能自提升能力后，pass率下降到55.9%；跨底座模型、跨Agent框架时仍保持优于人工技能的表现。

### 核心结论
将优化流程本身封装为可迭代的元技能，是让Agent能力突破人工设计天花板、实现自增强的低成本可行路径。
