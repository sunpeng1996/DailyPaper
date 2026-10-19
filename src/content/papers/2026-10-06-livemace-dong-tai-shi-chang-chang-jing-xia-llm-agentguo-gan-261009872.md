---
title: 'LiveMACE: Process-Aware Evaluation of LLM Agent Capabilities in Evolving Markets'
title_zh: LiveMACE：动态市场场景下LLM Agent过程感知能力评估基准
authors:
- Jun Zhao
- Leiming Fu
- Yanbo Wen
- Yiding Wang
- Xuantong Liu
- Yang Shu
- Yuyang Lu
- Xuanran Xing
- Jingqi Tong
- Hao Xu
affiliations:
- National University of Singapore
- Fudan University
- The University of Sydney
arxiv_id: '2610.09872'
url: https://arxiv.org/abs/2610.09872
pdf_url: https://arxiv.org/pdf/2610.09872
published: '2026-10-06'
collected: '2026-10-19'
category: Agent
direction: Agent 动态环境能力评估
tags:
- Agent Evaluation
- Dynamic Environment
- Process-aware
- LLM Agent
- Benchmark
one_liner: 以真实动态金融市场为测试床的过程感知Agent评估基准，明确能力与结果的差异
practical_value: '- 电商营销/交易类Agent评估不要只看GMV/转化率等最终结果，需补充工具调用合理性、规则合规率、记忆复用效率等过程诊断指标，避免动态流量环境下的短期结果波动误导能力判断

  - 开发长周期Agent的Persistent Memory模块时，拆分「存储质量」「检索效率」「实际应用效果」三个环节单独优化，不要只追求存储量累加，存储多不代表实际使用效果好

  - 涉及合规要求的业务场景（如营销投放预算约束、禁投品类规则），需同时评估「规则执行通过率」和「决策可审计性」两个维度，避免执行结果符合要求但决策逻辑错误的隐性风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent评估大多仅依赖最终结果指标，无法归因真实能力，尤其在动态演化环境中，结果是Agent行为与外部环境共同作用的产物，既无法定位能力瓶颈，也无法公平对比不同Agent的核心能力，亟需更科学的评估框架。

### 方法关键点
- 测试床选择真实动态的加密货币、美股市场，开展30天连续实盘模拟交易，环境独立演化且Agent动作存在长期持续性影响，避免静态测试环境的过拟合问题
- 控制变量设计5组Agent配置：Base（ReAct基础版）、Tool Use、Persistent Memory、Rule Following、Multi-Agent Collaboration，所有配置共享底层交互协议，可单独定位各能力维度表现
- 评估体系结合三类信号：最终交易结果指标、机制控制变量效果、全决策轨迹的过程诊断指标，每个能力维度均设计LLM judge+客观规则结合的量化指标

### 关键实验结果
测试5款前沿大模型（GPT-5.4、DeepSeek-V3.2、Gemini-3.1-Pro、Grok-4.20、Qwen3-Max），30天评估期内发现明显的结果-能力差距：交易收益排名出现21~29次序位反转，而对应能力维度的排名反转仅0~8次；不同模型存在显著能力异质性，GPT工具调用得分0.894最高，Grok记忆使用质量0.855最高，Gemini规则满足率0.872最高，DeepSeek多智能体协作得分0.806最高，且能力领先的模型不一定是收益最高的模型。

### 核心结论
动态环境中评估Agent，机制的访问权限、实际使用效率、最终业务收益是完全独立的三个维度，不能互相替代。
