---
title: 'Surviving the Router: Optimizing Skill Injections for Retrieval and Execution'
title_zh: CORSA：面向检索与执行的路由器感知技能注入优化方法
authors:
- Haneen Najjar
- Luca Scionis
- Haritz Puerto
- Sahar Abdelnabi
affiliations:
- Max Planck Institute for Intelligent Systems
- Tel Aviv University
- Sapienza University of Rome
- University of Cagliari
- ELLIS Institute Tübingen
arxiv_id: '2610.08098'
url: https://arxiv.org/abs/2610.08098
pdf_url: https://arxiv.org/pdf/2610.08098
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: Agent 技能注入攻击与安全防护
tags:
- LLM Agent
- Prompt Injection
- Skill Routing
- Attack Optimization
- Cybersecurity
one_liner: 提出集群优化的路由器感知技能注入攻击CORSA，兼顾检索、执行与用户效用且跨架构可迁移
practical_value: '- 搭建开放Agent技能生态时，必须将技能的检索排名逻辑纳入安全检测环节，原有仅检测已选中技能的逻辑会漏掉87%~97%的真实攻击

  - 做技能/工具路由算法可参考CORSA的优化逻辑反向做防御：新增技能名称、描述、正文的语义一致性校验，拦截刻意优化检索权重的恶意技能

  - 第三方技能准入检测优先采用LLM增强方案，实验显示Qwen3.8-27B增强的扫描召回率远高于静态扫描，静态扫描基本无法检测隐藏在SKILL.md中的注入

  - 技能路由架构优先选择带reranker的管线（如Qwen3-8B的检索+重排），对跨架构迁移的恶意技能抗性更强，恶意技能的Hit@1比其他路由低10~20个百分点'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有技能注入攻击的评估均默认恶意技能已被路由选中，完全忽略了多技能场景下路由检索的筛选作用，真实场景中普通注入的有效攻击成功率（ASR）会被路由器压低87%~97%，评估结果完全高估了真实威胁，无法支撑技能生态的安全防护。

### 方法关键点
- 提出CORSA两阶段集群优化框架，基于GEPA反射式进化搜索，无需路由器或LLM权重，仅通过反馈迭代优化恶意技能的名称、描述、正文内容
- Stage A单独优化检索目标，最大化技能在同簇任务下的Hit@1，保证恶意技能能排到检索结果首位
- Stage B在Stage A输出基础上优化端到端目标，同时保证检索排名不变、载荷可执行，且不破坏原有技能的正常功能
- 按语义将任务划分为8个簇，每个簇优化一个恶意技能，覆盖同域所有相关任务，避免单任务优化过拟合

### 关键实验
基于SkillRouter基准扩展8类恶意载荷，在2000个良性技能的竞争环境下测试，对比基线SkillJect：
1. CORSA的Hit@1达32.3%，是基线11%的近3倍；端到端ASR达22%，是基线10%的2.2倍，用户效用与基线持平（38.8% vs 38.3%）
2. 优化后的技能可跨模型、跨Agent脚手架、跨路由器迁移，在未见过的任务paraphrase场景下ASR仍有11.5%，合成新任务场景下ASR仍有5.4%
3. 静态扫描工具完全无法检测CORSA生成的恶意技能，Qwen3.8-27B增强的扫描最高可达7/8的召回率，仍存在漏报

**最值得记住的一句话：多技能Agent生态的安全防护必须覆盖路由检索环节，仅做执行侧的注入检测会漏掉绝大多数真实攻击**
