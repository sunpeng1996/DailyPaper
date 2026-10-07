---
title: 'Jarvis: A Proactive Speech Agent for Multi-Party Conversations'
title_zh: Jarvis：面向多人对话的主动式语音交互Agent
authors:
- Seunghyun Oh
- Hirotaka Hiraki
- Shuyue Stella Li
- Yulia Tsvetkov
- Shyamnath Gollakota
affiliations:
- University of Washington
- The University of Tokyo
arxiv_id: '2610.07506'
url: https://arxiv.org/abs/2610.07506
pdf_url: https://arxiv.org/pdf/2610.07506
published: '2026-10-05'
collected: '2026-10-07'
category: Agent
direction: 主动式对话Agent · 多人会议场景优化
tags:
- Proactive Agent
- Speech Agent
- Multi-party Conversation
- Document Grounded Generation
- RAG
one_liner: 基于共享文档的多人会议主动干预语音Agent，可自主判断发言时机、输出可溯源回答
practical_value: '- 可复用主动干预决策框架：将任务拆解为「问题检测→人类自修复校验→确定性门控触发」三级流程，适合客服、直播中控等需要主动纠错/补信息的场景，大幅降低误触率

  - 小模型+确定性校验的架构思路：不需要大模型端到端解决所有问题，用轻量MoE模型做语义分类，再叠加规则校验（如数字严格一致、60% token匹配），可在业务中低成本落地，兼顾准确率和实时性

  - 多人场景的发言时机策略：可迁移到直播带货、多人在线咨询场景，设置干预等待阈值、插话回收逻辑，平衡干预及时性和用户体验，避免打断正常对话流程'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有语音Agent均为被动响应、仅支持双人交互，无法适配多人会议等场景：既不能在无人主动提问时纠正事实错误、补充缺失信息，也难以把握发言时机避免干扰对话，且主动干预行为长期缺乏可量化的评估标准。
### 方法关键点
- 锚定可落地的问题边界：仅针对预共享文档可验证的认知错误（事实遗漏、错误陈述、错误归因）做干预，规避无标准答案的社交类决策
- 发布CHI-180-proactive基准数据集：覆盖180篇CHI论文的合成多人对话，植入4320个带明确理想动作标签的事件，解决主动干预效果难以量化的问题
- 系统采用「小模型+确定性校验」架构：用激活参数仅3B的Qwen3.6-35B MoE做语义分类，叠加规则校验（数字严格匹配、60%内容匹配校验自修复），设置2轮等待阈值给人类留足自修复空间，所有输出均绑定文档句子ID可溯源；交互模块支持空闲发言、举手申请、被打断自动恢复三种模式，同步展示引用证据
### 关键结果
CHI-180-proactive测试集上，Agent回答正确率95%-97%，人类自修复后保持沉默的准确率97%，信息缺口场景干预覆盖率91%，错误陈述场景干预覆盖率77%，98%的干预在问题出现后2-3轮内发起；23人live测试中，85%的干预在2轮内到达，164次干预中163次内容正确/部分正确，91%的用户偏好带引用溯源的展示。
> 最值得记住：主动Agent的核心是做低存在感的辅助者，优先给人类留足自修复空间，仅在明确能提供可验证价值时才介入
