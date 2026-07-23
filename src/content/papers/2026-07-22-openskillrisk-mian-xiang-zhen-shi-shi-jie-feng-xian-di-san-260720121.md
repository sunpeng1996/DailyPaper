---
title: 'OpenSkillRisk: Benchmarking Agent Safety When Using Real-World Risky Third-Party
  Skills'
title_zh: OpenSkillRisk：面向真实世界风险第三方技能的Agent安全基准
authors:
- Qiyuan Liu
- Tingfeng Hui
- Kun Zhan
- Kaike Zhang
- Ning Miao
affiliations:
- City University of Hong Kong
- Beijing University of Posts and Telecommunications
- Li Auto Inc.
arxiv_id: '2607.20121'
url: https://arxiv.org/abs/2607.20121
pdf_url: https://arxiv.org/pdf/2607.20121
published: '2026-07-22'
collected: '2026-07-23'
category: Agent
direction: Agent 第三方技能调用安全评估
tags:
- Agent Safety
- Third-party Skill
- Benchmark
- LLM Agent
- Risk Evaluation
one_liner: 构建包含263个真实风险技能的Agent安全基准，揭示主流Agent调用第三方技能的普遍安全漏洞
practical_value: '- 搭建企业内部Agent技能生态时，可复用论文的两阶段风险技能过滤流程：先规则静态扫描，再LLM+人工审核，前置拦截恶意/上下文依赖风险技能

  - 自研Agent框架时，可参考论文的细粒度行为分类（风险未感知/感知仍执行/告警拦截等），设计分层防御机制：风险识别→执行拦截→可选安全路径兜底

  - 部署Agent调用第三方技能时，优先选择主动加载预训练好的Guard Skill模式，配合沙箱隔离+用户二次确认，可将风险执行率降低10%以上，需平衡过防率

  - 做Agent安全评估时，可直接复用OpenSkillRisk的评估指标（ASR、Awareness率、Fsafe），量化自家Agent的安全表现，重点防控控制面劫持、权限提升这类高危盲区'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent广泛依赖第三方技能扩展开放场景能力，但公开技能市场的技能可能潜藏恶意代码、数据泄露、权限提升等执行时风险，现有安全基准多基于人工构造的攻击样本，无法覆盖真实生态的多样化风险，也缺少对Agent风险认知+执行行为的细粒度评估，难以支撑安全能力迭代。

### 方法关键点
- 数据集构建：从2个公开技能市场爬取17.5万+真实技能，经「规则静态过滤→LLM上下文审核→人工专家验证」的三级筛选，最终得到263个风险技能，分为7类攻击、2种风险类型（无条件恶意、上下文依赖风险）
- 评估体系：每个技能配套真实良性任务+隔离沙箱，避免实际危害；新增认知层面的Awareness率（主动识别风险并告警的比例），结合执行层面的ASR（攻击成功率），提出复合指标Fsafe综合评估安全能力；将Agent行为细分为5类，支持根因分析
- 防御验证：对比Guard Skill的两种加载模式（被动可选加载、主动预加载）的防护效果与过防成本

### 关键实验结果
测试覆盖3个主流CLI Agent框架（Codex、Gemini CLI、Claude Code）+13个前沿LLM，核心结论：
1. 最优配置（Claude Code + Claude Sonnet 4.6）仍有17.87%的概率执行不安全操作，现有Agent无可靠的风险技能处理能力
2. 上下文依赖风险比显性恶意风险更难检测：ASR从22.0%升至35.6%，Awareness率从62.9%降至51.4%
3. 系统级攻击（控制面劫持、权限提升）的Fsafe比数据级攻击低30个百分点以上，是最大安全盲区
4. 主动加载Guard Skill可将ASR平均降低15个百分点，但会带来22.5%的过防率

最值得记住的一句话：Agent调用第三方技能的安全不能仅依赖LLM的风险推理能力，必须结合框架层执行控制、前置技能审核、运行时沙箱隔离的多层防御机制。
