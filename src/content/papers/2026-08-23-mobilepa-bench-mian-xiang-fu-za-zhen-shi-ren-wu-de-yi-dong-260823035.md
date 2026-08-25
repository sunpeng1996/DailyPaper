---
title: 'MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks'
title_zh: MobilePA-Bench：面向复杂真实任务的移动端规划Agent评测基准
authors:
- Yi Zhu
- Xiongwei Wu
- Qiyi Wang
- Tingyu Qu
- Jiajun Liu
- Sihan Cao
- Long Chen
- Weigao Sun
- Feida Zhu
- Yiran Zhong
affiliations:
- MAI Team, Alibaba
- Alibaba Token Foundry
arxiv_id: '2608.23035'
url: https://arxiv.org/abs/2608.23035
pdf_url: https://arxiv.org/pdf/2608.23035
published: '2026-08-23'
collected: '2026-08-25'
category: Agent
direction: 移动端Agent · 多能力统一评测
tags:
- Mobile Agent
- Agent Evaluation
- Tool Calling
- Multi-Agent Collaboration
- Memory Augmented Agent
one_liner: 推出工具优先的交互式状态化移动端规划Agent基准，覆盖4类核心能力13个领域共1705个真实任务
practical_value: '- 做端侧个人助理/电商服务Agent的团队可直接复用该基准的4维能力评估框架，替代零散的功能测试

  - 业务Agent可参考其统一工具化动作空间设计：把Sub-agent调度、用户Memory检索、组合Skill调用都封装成标准function call schema，降低规划层复杂度

  - 长流程任务的Agent评测可复用其3类证据对齐的验证逻辑：工具调用匹配/最终状态校验/行为合理性校验，避免单一指标误判

  - 电商高频长流程任务（比如退换货、差旅预订）可封装成预包装Skill直接调用，减少逐步骤规划的错误累积'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有移动端Agent评测存在两类明显缺陷：GUI-centric基准仅测试表层屏幕操作，忽略后台工具调用与长程规划能力；静态function call基准依赖离线API匹配，完全脱离真实运行时约束，无法衡量复杂真实任务下的端到端执行能力。
### 方法关键点
- 搭建轻量交互式状态化沙箱，内置13个功能领域共212个真实移动端工具，维护实时应用数据库与运行日志，返回结构化动态反馈，支持高吞吐量RL训练
- 设定4维核心评测体系：基础工具调用（参数匹配、依赖处理、错误恢复）、Sub-agent Collaboration（任务拆分与上下文传递）、Memory Usage（用户偏好/历史信息检索与落地）、Skill Usage（预包装组合流程复用）
- 设计三类证据对齐的验证逻辑：工具调用精确匹配、最终状态变更匹配、行为合理性校验，适配不同任务的完成判定需求，避免单一指标的过严或过松问题
### 关键结果
基于1705个真实用户任务测试13款前沿LLM，最优Claude-Opus-5整体加权得分仅75.52%；各维度最优表现分别为：基础工具调用83.85%、Sub-agent Collaboration77.53%、Memory Usage64.63%、Skill Usage78.00%，各维度最优结果分散在不同模型，无全能型规划Agent。
### 核心结论
当前前沿LLM在移动端复杂场景的端到端可靠性仍远未达落地要求，错误会跨能力边界级联放大，记忆应用与子Agent协作是当前最突出的性能瓶颈。
