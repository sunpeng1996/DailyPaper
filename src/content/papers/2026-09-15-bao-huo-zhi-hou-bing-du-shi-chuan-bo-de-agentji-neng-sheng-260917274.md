---
title: 'After the Party: Governing What a Viral Agent-Skill Ecosystem Left Behind'
title_zh: 爆火之后：病毒式传播的Agent技能生态遗留问题治理
authors:
- Yunpeng Xiong
- Ting Zhang
affiliations:
- Monash University
arxiv_id: '2609.17274'
url: https://arxiv.org/abs/2609.17274
pdf_url: https://arxiv.org/pdf/2609.17274
published: '2026-09-15'
collected: '2026-09-16'
category: Agent
direction: Agent技能生态安全治理
tags:
- Agent Skill
- Ecosystem Governance
- Security Measurement
- Open Source Registry
- Scanner Validation
one_liner: 基于爆火的OpenClaw Agent技能生态实证分析，揭示现有三类治理信号的不可靠性及治理优化方向
practical_value: '- 若业务搭建Agent技能/插件市场，不要直接用下载量、点赞、版本数等元数据做准入或排序依据，这类特征的有效性受创建 cohort、技能年龄影响极大，生态爆发式增长后会完全失效

  - 做Agent技能安全检测时，不要依赖单一扫描器：LLM扫描器灵敏度最高（61.06%）但特异性低，静态分析特异性最高（95.38%）但灵敏度低，建议多扫描器组合，且对匹配到高权限规则的技能优先进入人工审核队列

  - 企业内部Agent技能库可采用分层治理方案：元数据支持发现、内容扫描做风险初筛、宿主侧权限限制/沙箱执行做 runtime 兜底，避免把单一维度的信号作为唯一安全判定标准

  - 所有用于治理的模型和阈值要绑定观测窗口、创建 cohort 标签，每次生态出现爆发式增长后必须重新校准，避免Goodhart定律失效问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
2026年上半年OpenClaw开源Agent病毒式传播，其公共技能注册库ClawHub存量91天内接近翻倍，63.25%的6月可见技能仅用两个月就创建完成。爆火后大量技能未被有效审核，现有注册库依赖的元数据、社区反馈、自动扫描器三类治理信号均未经过有效性验证，存在严重安全风险。

### 方法关键点
- 基于2026年3月、6月、7月三次ClawHub快照，结合OpenClaw的Git提交、Issue、PR数据做纵向追踪分析
- 验证下载量、点赞、版本数、文件数等7种常用元数据特征与技能持续可见性的关联稳定性，控制创建cohort、技能年龄变量
- 自定义12种高权限能力的文本匹配规则，统计权限证据与社区反馈的重合度，量化可审核性缺口
- 对比LLM扫描器、静态分析扫描器、VirusTotal三类工具的检测一致性，基于人工标注的180个样本验证扫描效果

### 关键结果
- 技能下载极度集中，Top10%的技能占总下载量的46.93%；77.86%的技能零点赞零评论，85.06%的可解析技能携带高权限证据
- 7种元数据特征的预测性全部不稳定，调整年龄、限制为爆火前创建的cohort后所有正相关全部反转
- 三类扫描器共同覆盖的61990个技能中，23702个检测结果不一致，加权灵敏度仅21.67%~61.06%，未被任何扫描器标记的样本中仍有24.16%被人工判定为需要审核

### 核心结论
Agent技能生态的快速增长会让原有治理信号快速失效，治理不能依赖简单元数据或单一扫描器，必须建立可测量、可验证的分层治理体系
