---
title: 'IF:CARGO: LLM-Based Semantic Compilation for Al-Native Rule Programming Games'
title_zh: IF:CARGO：面向AI原生规则编程游戏的LLM语义编译系统
authors:
- Ting-Chen Hsu
- Lianye Zhang
- Jiangxu Lin
- Zhaoyi Yu
- Fei Qin
- Zihao Chen
affiliations:
- Communication University of China
- The Hong Kong Polytechnic University
- Lanzhou City University
- University of Electronic Science and Technology of China
arxiv_id: '2608.12195'
url: https://arxiv.org/abs/2608.12195
pdf_url: https://arxiv.org/pdf/2608.12195
published: '2026-08-12'
collected: '2026-08-16'
category: LLM
direction: LLM语义编译 · 自然语言转结构化指令
tags:
- LLM
- Semantic Compilation
- Natural Language Programming
- Human-AI Interaction
- Rule Engine
one_liner: 提出将LLM作为语义编译器而非自主智能体的架构，支持用户自然语言编写可确定性执行的规则
practical_value: '- 可复用「LLM语义编译+固定Schema约束」架构，将运营/商家输入的自然语言规则转成推荐/广告系统可执行指令，降低规则配置门槛

  - 借鉴「表达-执行-反馈-迭代」交互设计，优化LLM辅助的运营策略配置工具，提升用户可控感和调试效率

  - 面向非技术用户的规则配置场景，可采用「约束输入范围+保留用户决策权+确定性执行」模式，降低LLM幻觉带来的业务风险'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有LLM在互动系统中多用作内容生成、自主智能体，未探索将其作为语义编译工具支持用户自然语言规则编程的模式，端用户编程门槛高，自然语言表达的计算意图难以被系统确定性执行。
### 方法关键点
1. 架构上将LLM定位为语义编译器而非自主智能体，负责将用户输入的自然语言IF/THEN规则转换为约束化命令Schema
2. 下游引擎对结构化指令做确定性校验执行，形成「用户表达→LLM编译→系统执行→反馈迭代」的语义调试交互闭环
3. 招募24名参与者开展8个关卡的混合方法测试，从行为数据、主观感知多维度验证架构效果
### 关键结果
- 绝大多数参与者可快速理解LLM的翻译中介定位，能基于反馈迭代调整规则完成任务
- 定时指令、多主体协同、规则优先级三类场景会显著提升用户认知负担和调试难度
- 沉淀出可复用的AI原生系统设计范式：约束自然语言输入范围、保留用户决策权、保障执行确定性
