---
title: 'We Query, Therefore We Compute: On Oracle Computation beyond the Machine,
  with an Application to Agents'
title_zh: 面向Agent的超机器Oracle计算理论及RISC-V架构实现
authors:
- Kefan Liu
- Fengning Ou
- Yelin Luo
- Jingdi Lei
affiliations:
- Institute of Computing Technology, CAS
- University of Chinese Academy of Sciences
- Nanjing University
- Institute of Automation, CAS
- Nanyang Technological University
arxiv_id: '2610.09243'
url: https://arxiv.org/abs/2610.09243
pdf_url: https://arxiv.org/pdf/2610.09243
published: '2026-10-06'
collected: '2026-10-08'
category: Agent
direction: Agent系统底层抽象 · 统一范式
tags:
- Agent
- LLM
- Oracle Computation
- RISC-V
- Workflow
- Operating System
one_liner: 将LLM作为Oracle构建统一抽象机，打通Agent与Workflow范式，实现兼容RISC-V的ArchNights系统
practical_value: '- 可直接复用「Oracle+Priestess」二分架构设计业务Agent：将LLM作为黑盒Oracle负责生成决策，业务逻辑、工具调度、合规校验放在Priestess层，边界清晰易维护，适配电商导购Agent、广告投放优化Agent等落地场景

  - 统一Agent与Workflow的范式可复用：复杂业务链路（如电商大促活动自动化执行、用户全生命周期运营链路）可混合两种模式，固定流程用Workflow降本，开放决策用Agent提效，无需维护两套独立框架

  - 缓存优化结论可直接落地：明确Agent上下文栈与LLM KV cache的层级对应关系，做Agent上下文管理时可按yield符号（如工具调用结束标记）分段缓存，最高可降低一半KV
  cache重计算开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent系统研究缺乏统一底层抽象：形式化演算类工作未定义系统各组件的权责边界，类比操作系统的零散设计（调度、缓存、隔离）无通用理论支撑，且Workflow、Agent两种范式割裂，相同机制需重复实现两套，难以统一推导安全边界、缓存效率等共性问题。
### 方法关键点
- 将LLM/人类等外部智能体视为黑盒Oracle，在双栈下推自动机基础上扩展单条Oracle指令：以整栈内容为查询输入，回答追加到同栈，天然匹配Agent上下文自回归增长特性
- 引入两次对称性破缺构建O-2-PDA-TS抽象机：存储破缺S规定仅O栈可存储Oracle可执行程序，P栈内容仅作为数据；转移破缺T划分O模式（Oracle连续生成直到遇到yield符号）与P模式（执行工具调度、安全校验等逻辑），Priestess层天然成为Oracle任务的操作系统
- 基于抽象机实现ArchNights：扩展RISC-V ISA，实现类Linux内核，兼容gem5仿真，Agent与Workflow统一为任务程序的两种部署形态（程序在O栈为Agent，在P栈为Workflow）
### 关键结果
在Terminal-Bench 2.1基准测试中，以deepseek-v4.1-flash为Oracle，ArchNights-SE性能与mini-swe-agent、Terminus 2两款业界基准Agent相当。
### 核心结论
Agent和Workflow本质是同一抽象机上任务程序的两种部署位置，所有Agent系统的共性问题可基于统一模型一次推导，无需分范式重复实现
