---
title: 'Defense-as-Skill: Evolving Runtime Guard Skill for Skill-Augmented Agents'
title_zh: 防御即技能：面向技能增强型Agent的运行时防护技能进化框架
authors:
- Xiaofang Yang
- Ziqi Miao
- Dianbo Sui
- Jing Shao
- Lijun Li
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Fudan University
- Harbin Institute of Technology, Weihai
arxiv_id: '2609.01487'
url: https://arxiv.org/abs/2609.01487
pdf_url: https://arxiv.org/pdf/2609.01487
published: '2026-09-01'
collected: '2026-09-02'
category: Agent
direction: Agent 运行时安全 · 技能化防护
tags:
- LLM Agent
- Skill Augmentation
- Runtime Guardrail
- MCTS
- Adversarial Defense
one_liner: 将运行时安全防护封装为可进化Agent技能，无需修改底层即可拦截恶意技能攻击
practical_value: '- 做Agent安全防护时可参考将防护逻辑封装为标准化可加载技能，无需修改Agent底层runtime，大幅降低跨平台部署成本，尤其适合电商多场景Agent（客服、选品、运营）的快速安全加固

  - 安全类技能不会被普通的任务-技能匹配逻辑召回，必须在系统侧显式指定防护技能的持久调用责任，这一结论可直接复用在所有带技能库的Agent系统设计中

  - 可以借鉴MCTS驱动的技能进化流程，基于真实业务攻防反馈迭代优化防护策略，平衡安全拦截率与正常任务完成率，避免过度拦截影响用户体验

  - 技能化的防护比同内容的扁平化系统提示词效果更优、token消耗更低，这一结论可指导Agent端各类策略（如合规校验、用户意图边界判定）的模块化封装'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前技能增强型Agent（SAA）可加载持久化可复用技能提升任务效率，但恶意技能可潜伏至业务场景匹配时才触发攻击，包括泄露用户隐私、越权操作数据、执行恶意脚本等，传统预安装扫描、系统提示词加安全规则、权限硬控等方案要么漏防，要么大幅降低正常任务效率，且难以跨Agent框架迁移，亟需轻量、可进化、不侵入底层的运行时防护方案。

### 方法关键点
- Defense-as-Skill范式将运行时防护逻辑封装为可安装、可编辑、可进化的普通技能SkillSonar，与业务技能并行加载，在每次动作执行前校验是否超出用户任务边界，输出允许/重规划/要求用户确认三类决策，无需修改Agent底层runtime
- SCOPE-R数据集覆盖6类技能风险、21个子类，包含206个经实际攻击验证的恶意样本、43个良性任务样本，支持ID/OOD泛化评估
- 基于MCTS的防护技能进化算法，以攻击拦截率为核心目标，兼顾任务完成率、用户确认负担、token消耗，通过真实执行反馈迭代优化防护技能的规则细节

### 关键实验结果
在GLM-5、Claude Haiku 4.5、GPT-5.4三个基座，Claude Code、OpenClaw两个Agent框架上验证，相比无防护基线，SkillSonar可将ID攻击成功率从0.482降至0.104，OOD攻击成功率从0.606降至0.115，同时任务完成率仅损失约4%，token开销与普通防护方案持平；相比同内容扁平化系统提示词，攻击拦截率提升24.9个百分点，token消耗降低21%。

### 最值得记住的一句话
将安全逻辑封装为可进化的标准化技能，是平衡Agent安全性、通用性、迭代效率的高性价比路径，可作为底层机制级防护的重要补充。
