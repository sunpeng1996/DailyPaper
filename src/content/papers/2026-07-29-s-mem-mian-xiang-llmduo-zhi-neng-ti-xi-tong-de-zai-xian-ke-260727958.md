---
title: 'Σ-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems'
title_zh: Σ-Mem：面向LLM多智能体系统的在线可靠性记忆机制
authors:
- Peilin Feng
- Suorong Yang
- Soujanya Poria
affiliations:
- Nanyang Technological University
- DeCLaRe Lab
arxiv_id: '2607.27958'
url: https://arxiv.org/abs/2607.27958
pdf_url: https://arxiv.org/pdf/2607.27958
published: '2026-07-29'
collected: '2026-08-01'
category: MultiAgent
direction: 多智能体协调 · 可靠性记忆建模
tags:
- MultiAgent
- LLM Memory
- Reliability Modeling
- Online Adaptation
- Agent Coordination
one_liner: 提出基于对称矩阵的在线可靠性记忆Σ-Mem，无需重训即可实现多智能体自适应协调
practical_value: '- 多Agent导购/客服场景可复用该框架，存储不同Agent在品类咨询、售后、活动规则等任务下的历史准确率，无需重训即可动态选择最优Agent响应，降低人工运营成本

  - 生成式推荐的多模型融合场景，可借鉴对称矩阵+有界更新的设计，存储不同生成模型在用户群体、内容品类的可靠性，加权融合输出结果，避免单一模型的hallucination问题

  - 搜索Query改写的多模型投票场景，可直接复用M-weighted voting机制，基于历史反馈给不同模型分配动态权重，相比固定权重/多数投票可提升改写准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM多智能体系统的记忆仅存储交互内容，无法建模不同Agent在特定任务下的可信度，也无法捕捉Agent间的错误相关性。当中心模型无法直接验证答案正确性时（如无上下文的RAG、复杂推理场景），容易受共同偏差或关联错误误导，导致决策失效。

### 方法关键点
- 维护两类对称矩阵形式的可靠性证据：单Agent历史能力矩阵`Mp`，记录各Agent在不同任务类型下的历史准确率；Agent关系矩阵`G`，记录不同Agent正确性的相关性（正相关表示易共同正确/错误，负相关表示正确性对立）
- 基于Weyl不等式实现稳定在线更新：每次仅用正确性反馈对矩阵做有界小幅度更新，加时间衰减，无需重训底层模型，保证记忆不会被单次事件剧烈扰动
- 支持三类通用读写接口：① 残差steering引导中心模型的Peer选择；② 直接读取得分做无需响应的任务路由；③ 可靠性加权投票，适配不同多智能体架构需求

### 关键结果
在5个Qwen系列中心模型上测试：反事实可靠性漂移场景下，CF@90分位可将Qwen3-0.6B的准确率从46.22%提升至71.10%；跨unseen领域测试中27/30的case优于基线，BBH数据集上相对提升最高达48.6%；直接读取的M-routing和M-vote均优于多数投票和最优固定Peer基线，且性能随反馈数据量增加持续提升。

**最值得记住的一句话**：可靠性记忆不是聚合的辅助信号，而是可跨Peer集合、任务分布、选择机制复用的多智能体协调基础状态
