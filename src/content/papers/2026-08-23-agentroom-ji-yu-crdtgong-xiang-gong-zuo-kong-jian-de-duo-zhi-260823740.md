---
title: 'AgentRoom: Concurrent Multi-Agent Coding in a CRDT-Backed Shared Workspace'
title_zh: AgentRoom：基于CRDT共享工作空间的多智能体并发编码框架
authors:
- Seonglae Cho
- Donghyun Lee
affiliations:
- Holistic AI
- University of California, Berkeley
arxiv_id: '2608.23740'
url: https://arxiv.org/abs/2608.23740
pdf_url: https://arxiv.org/pdf/2608.23740
published: '2026-08-23'
collected: '2026-08-27'
category: Agent
direction: 多Agent协作编码效率优化
tags:
- MultiAgent
- CRDT
- MCP
- LLM4Code
- Concurrent Generation
one_liner: 基于CRDT与MCP显式协调的多Agent并发编码框架，降低任务放弃率提升生成质量
practical_value: '- 多Agent协作任务（如多Agent生成电商营销文案、活动页代码、召回策略）可复用CRDT共享空间+MCP显式协调架构，替代传统串行转交模式，降低30%+的结果波动与近90%的任务放弃率

  - 多Agent并行执行时务必添加显式资源声明机制（如文件/模块/参数片段的所有权claim+广播），避免无协调并行的重复劳动与冲突，实测无协调并行效果甚至弱于单Agent

  - 业务落地优先验证2Agent配置，是ROI最优配比：超过2个Agent后协调成本超线性上升，质量反而下降，无需盲目堆Agent数量

  - 成本敏感场景可尝试2个小模型组成的AgentRoom，实测2个Haiku的编码效果超过单Sonnet大模型，成本仅为后者的1/2，可直接迁移到商品文案生成、客服应答等场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多Agent编码系统普遍采用串行阶段转交范式，或无协调并行采样后合并，单Agent在复杂任务上有近30%概率提前放弃，仅输出单文件骨架；CRDT隐式协调方案效果波动极大，存在21%提速/39%降速的两极分化结果，亟需验证显式协调+CRDT共享工作空间的方案能否在同算力下超过现有方案。
### 方法关键点
- 底层基于CRDT实现共享文件系统，2s内完成字符级写入合并，自带括号平衡检查，保证并发写入无字节级冲突
- 封装MCP工具集暴露给Agent调用：`room_claim`原子申请文件所有权、`room_broadcast`/`room_read`维护全局消息日志、`room_state`实时同步所有Agent状态，实现显式协调
- 采用提示层的advisory协作协议：要求Agent先读状态再写入、先申请文件所有权再编辑、冲突时切换目标文件、完成后广播通知，不做强制内核锁，允许跨Agent修复其他成员的bug
### 关键实验结果
基于5款前沿编码模型（Sonnet 4.6、Haiku 4.5、GPT-5.4等），在4个难度梯度的后端编码任务上验证：
- 同算力下，单Agent的任务放弃率是AgentRoom双Agent的13.7倍（p<1e-5），结果方差降低30%~45%
- T4高难度任务（15+文件双账本系统）上，AgentRoom双Agent的LLM质量分达0.669，比无协调并行合并方案高0.213（p=0.003），比ChatDev风格串行流水线方案高101%
- 最优Agent数量为2，超过2个后协调成本超线性上升，质量下降；2个Haiku组成的AgentRoom效果超过单Sonnet大模型，成本仅为后者的50%
### 核心结论
多Agent协作的核心增益来自显式协调，而非单纯堆并行或仅依赖底层CRDT合并，无协调的并行效果甚至弱于单Agent
