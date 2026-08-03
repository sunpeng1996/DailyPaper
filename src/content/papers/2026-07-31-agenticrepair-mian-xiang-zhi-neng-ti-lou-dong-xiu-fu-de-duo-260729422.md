---
title: 'AgenticRepair: Multi-Faceted Program Context Engineering for Agentic Vulnerability
  Repair'
title_zh: AgenticRepair：面向智能体漏洞修复的多维度程序上下文构建框架
authors:
- Michael Fu
- Qiyue Mei
- Patanamon Thongtanunam
- Kla Tantithamthavorn
affiliations:
- The University of Melbourne
- Monash University
arxiv_id: '2607.29422'
url: https://arxiv.org/abs/2607.29422
pdf_url: https://arxiv.org/pdf/2607.29422
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: Agent 代码漏洞修复 · 多维度上下文工程
tags:
- Multi-Agent
- Program Repair
- Context Engineering
- Vulnerability Patching
- LLM Agent
one_liner: 通过多维度上下文工程与多Agent架构实现SOTA的自动化代码漏洞修复
practical_value: '- 复杂任务多Agent架构可复用「多子Agent并行采集专用上下文+主Agent集中决策」的范式，比如电商异常订单排查、推荐badcase根因定位场景，可将用户行为、商品规则、日志信息的采集拆分给专门子Agent并行执行，大幅降低主Agent的认知负载

  - 多源结构化上下文融合思路可迁移到推荐系统归因场景：将用户反馈、召回排序日志、商品属性变更历史三类上下文结构化整合后输入归因模型，能有效提升根因定位准确率

  - 可直接复用 ablation 结论：多Agent任务拆分的收益远高于单维度上下文优化的收益，做Agent系统时优先做角色分工比单点优化prompt/上下文内容ROI更高'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有通用程序修复Agent方案缺乏安全漏洞修复所需的专业上下文，无法覆盖跨文件、依赖历史代码逻辑的复杂漏洞，修复成功率远低于人工水平。
### 方法关键点
- 两阶段多Agent架构：第一阶段3个专用子Agent并行采集三类结构化上下文：代码结构上下文（数据流、控制流、内存操作模式）、运行时执行上下文（崩溃特征、栈回溯、内存异常状态）、提交历史上下文（漏洞引入的commit记录、代码变更逻辑）；
- 三类上下文整合后注入修复Agent的 episodic memory，修复Agent基于整合上下文迭代生成、验证补丁，直到通过sanitizer安全检查。
### 关键实验结果
- 数据集采用SEC-Bench共300个真实漏洞实例，包含200个CVE公开漏洞、100个OSS-Fuzz实测漏洞；
- 对比OpenHands、SWE-Agent、Aider等SOTA基线，AgenticRepair整体修复成功率达73%，较最强基线高出29个百分点；
- 40%的成功修复为跨文件补丁，可处理复杂多模块漏洞；
- 消融实验显示：移除任一单维度上下文仅带来0.5%-2%的性能下降，但替换为单Agent架构性能暴跌44.5%，基础模型能力不足也会带来大幅性能损失。

最值得记住的结论：多维度专业上下文工程+多Agent认知负载拆分，是Agent落地复杂专业领域任务的核心有效路径。
