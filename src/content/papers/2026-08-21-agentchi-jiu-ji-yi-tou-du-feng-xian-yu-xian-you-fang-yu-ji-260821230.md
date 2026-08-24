---
title: 'Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening
  and Provenance Ranking'
title_zh: Agent持久记忆投毒风险与现有防御机制的边界研究
authors:
- Arulnidhi Karunanidhi
affiliations:
- Quantify Labs Ltd
arxiv_id: '2608.21230'
url: https://arxiv.org/abs/2608.21230
pdf_url: https://arxiv.org/pdf/2608.21230
published: '2026-08-21'
collected: '2026-08-24'
category: Agent
direction: Agent 记忆安全与防御机制优化
tags:
- Agent Memory
- Poisoning Attack
- Content Screening
- Provenance Ranking
- RAG Security
one_liner: 揭示无payload的事实类记忆投毒可绕过现有内容筛查，且加性来源加权排序无可用参数区间
practical_value: '- 搭建基于RAG的电商导购/客服Agent时，不能仅依赖内容筛查防御记忆投毒，无恶意指令的虚假商品/活动信息完全无法被现有prompt注入检测器识别

  - 来源加权排序不要使用简单加性权重，已验证只要权重足够抵御投毒，就会完全过滤非信任渠道的有效内容（如用户UGC、第三方商品评价），可替换为固定配额的占位约束（如检索结果中非信任内容占比不超过20%）

  - 评估防御效果不能只看攻击成功率，必须加入正常业务效用留存指标，避免过度防御导致正常内容召回率暴跌

  - 上线记忆模块前要先计算加性排序的相似性margin，确保参数设置不会让来源项完全覆盖语义相似性的可调范围'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent持久记忆的防御体系仅针对携带恶意指令的prompt注入类攻击，完全没有覆盖无payload的纯虚假事实投毒风险；同时行业评估防御效果仅采用攻击成功率单一指标，既不衡量攻击后记忆的正常效用留存，也未量化基于来源的排序类防御的适用边界，存在巨大安全盲区。

### 方法关键点
- 攻击设计：构造最弱形式的投毒内容，仅生成陈述虚假事实的普通对话文本，无任何恶意指令、触发词，也未针对检索/检测系统做任何对抗优化，仅复用目标问题关键词提升语义相似度
- 防御评估：覆盖两类主流工业级防御：写路径四阶内容筛查管道（结构校验+敏感信息检测+规则注入检测+LLM分类）、读路径语义相似度+来源权重加性排序
- 评估指标：提出以「攻击后记忆效用留存率」为核心指标，同时同步报告检测的误报率，避免过度防御被掩盖

### 关键结果
- 投毒内容仅占语料1.2%时，无防御的LongMemEval基准准确率从0.85降至0.3，仅留存35%的正常效用
- 对间接prompt注入召回率达0.832、误报率仅1.5%的四阶内容筛查管道，对360条投毒内容的拦截率为0，本质原因是事实真伪判断需要外部 grounding，无法仅通过文本检测实现
- 加性来源加权排序的默认发货参数完全无效（p=0.8），调大权重后虽能将效用恢复至56%，但会完全过滤所有非信任渠道内容，若答案证据来自非信任渠道，准确率直接跌至0.0417，不存在同时兼顾防御和非信任内容召回的参数区间

**最值得记住的结论**：内容筛查无法防御纯事实伪造类投毒，加性来源加权排序没有可用参数区间，来源类防御需改用占位约束而非分数惩罚。
