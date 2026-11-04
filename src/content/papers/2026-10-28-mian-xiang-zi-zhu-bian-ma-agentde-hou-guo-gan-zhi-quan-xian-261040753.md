---
title: '"Shall We Approve?" Consequence-Aware Approval for Autonomous Coding Agents'
title_zh: 面向自主编码Agent的后果感知权限审批机制Caper
authors:
- Weiheng Wu
- Junkai Chen
- Zhensu Sun
- Jieke Shi
- Yunbo Lyu
- David Lo
affiliations:
- Singapore Management University
arxiv_id: '2610.40753'
url: https://arxiv.org/abs/2610.40753
pdf_url: https://arxiv.org/pdf/2610.40753
published: '2026-10-28'
collected: '2026-11-04'
category: Agent
direction: Agent 工具调用安全管控
tags:
- Agent-Safety
- Tool-Calling
- Sandbox
- LLM-Guardrail
- Coding-Agent
one_liner: 通过沙箱预执行观测Shell命令真实效果，大幅降低编码Agent操作的有害结果率
practical_value: '- 搭建Agent工具调用安全体系时，可复用「沙箱预执行+效果审核+事务回滚」架构，替代纯静态规则/文本护栏，尤其适合操作用户数据、运营资源的电商Agent场景，避免误删数据、误发营销信息等事故

  - 系统调用trace处理可直接借鉴精简后果报告的trick：仅保留文件变更、网络请求、敏感数据读取等核心事件，冗余信息聚合压缩，既降低LLM输入长度，又不丢失风险判断关键信息

  - Agent拦截反馈设计可参考：拦截时返回明确的风险原因+重规划指引，而非直接终止任务，可在提升安全性的同时尽量保留高任务完成率，适配生产环境可用性要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有编码Agent的Shell命令审批方案（规则匹配、护栏模型、权限分类器）均基于指令文本判断，无法识别隐藏在调用脚本、Makefile、二进制程序中的风险，同一条命令在不同工作空间可能产生完全不同的效果，极易引发数据泄露、文件删除、配置篡改等安全事故，而人工全量审批又存在效率低、审批疲劳的问题。
### 方法关键点
- 事务性预执行：每条Shell命令先在快照沙箱中执行，默认禁用外部网络，通过strace追踪全量系统调用，审批通过则保留执行状态，不通过则直接回滚到执行前快照
- 精简后果报告：从原始系统调用trace中仅提取关键风险相关事件（持久化文件变更、网络连接尝试、敏感数据读取、用户可见输出），聚合冗余信息，报告体积比原始trace小99%，上限控制在8KB
- LLM审批+可执行反馈：LLM结合用户任务、交互历史、后果报告判断是否放行，拦截时返回明确风险原因，引导Agent重新规划安全执行路径
### 关键实验
在SABER（682个覆盖8类危害的Shell任务）和自建YoloFS-Ext（204个含隐藏风险的任务，对应安全孪生对照组）上对比6个现有方案：SABER上有害结果率低至6.7%，比最优基线的14.8%降低超过50%；YoloFS-Ext上有害结果率7.8%，远优于基线最低的35.3%，同时安全孪生任务的误拦率仅1.0%，安全完成率为所有方案最高。
### 核心结论
基于文本的审批本质是猜测风险，只有观测实际执行效果才能精准区分危险操作和它的安全孪生版本。
