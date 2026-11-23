---
title: 'Beyond Self-Critique: Epistemic Convergence Control for Multi-Agent Research
  Verification'
title_zh: 超越自我批判：多智能体科研验证的认知收敛控制方法
authors:
- Chrisantus Eze
affiliations:
- Oklahoma State University
arxiv_id: '2611.27839'
url: https://arxiv.org/abs/2611.27839
pdf_url: https://arxiv.org/pdf/2611.27839
published: '2026-11-20'
collected: '2026-11-23'
category: Agent
direction: 多Agent协作 · 认知验证收敛控制
tags:
- Multi-Agent
- Epistemic Verification
- Convergence Control
- LLM Agent
- Fact Checking
one_liner: 提出VerifyAgent多智能体验证框架，解决同基座多Agent辩论的自洽偏差与迭代效率问题
practical_value: '- 电商/广告内容审核、商品卖点真实性校验场景可复用不对称三角色架构，避免同基座LLM自校验的自确认偏差，提升违规内容/虚假宣传的召回率

  - 多Agent线上服务的迭代停止逻辑可直接复用Belief-Delta收敛准则，基于结构化业务状态的变化率动态终止流程，相比固定轮次方案可降低2倍以上的LLM调用成本

  - RAG落地场景（如推荐理由生成、营销文案创作）可借鉴证据锚定+独立NLI审计的方案，每一条生成内容都绑定检索到的原文片段，降低幻觉的同时提供可解释的审计链路'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前同基座LLM驱动的多智能体辩论框架存在两个核心痛点：一是对称角色共享底层权重，易出现自批判偏差，辩论沦为形式化自洽确认，难以有效检出争议性主张；二是固定轮次停止策略要么提前终止导致验证不充分，要么过度迭代浪费推理算力，且生成结论缺乏可审计的证据支撑，无法满足高可靠性验证场景的要求。

### 方法关键点
- 不对称角色架构：设计Advocate（挖掘支持证据）、Skeptic（质疑主张漏洞）、Arbitrator（更新认知状态）三类角色，搭配对立认知指令与角色嵌入相似度监控，当两类角色输出语义相似度超过0.85时触发重跑，强制视角分化
- Belief-Delta（ΔB）收敛准则：基于结构化认知状态（claim+验证状态+证据锚点）的变化比例判断收敛，默认阈值为10%，低于阈值即停止迭代，避免无效计算
- 证据锚定审计：所有被判定为支持的claim都绑定120字以上的原文片段，通过独立NLI交叉编码器校验片段与claim的蕴含关系，过滤无依据幻觉内容

### 关键实验
以DeepSeek-R1-32B为基座，在40个覆盖LLM推理、多Agent协作领域的科研假设上完成200次实验，对比对称MAD、Self-Refine、固定轮次等baseline：①角色嵌入相似度从0.918降至0.852（p<1e-7），争议主张检出率从15.4%提升至22.0%；②ΔB准则完全消除过度迭代，LLM调用量较固定3轮方案降低2.4倍；③幻觉率21.7%，与Self-Refine的25.9%相当，但所有结论均具备可审计证据锚点。

### 核心结论
同基座LLM多智能体的有效性核心不是角色话术的表层差异，而是底层认知指令的对立性与状态迭代的可量化收敛性。
