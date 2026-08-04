---
title: 'Agentic Commerce World: An Auditable and Verifiable Environment for Vibe Commerce'
title_zh: 面向Vibe Commerce的可审计可验证多Agent电商交互环境ACWORLD
authors:
- Shicheng Fan
- Mingdai Yang
- Duohao Wang
- Canyu Chen
- Yongfeng Zhang
- Hua Wei
- Manling Li
- Julian McAuley
- Kun Zhang
- Philip S. Yu
affiliations:
- University of Illinois at Chicago
- Microsoft AI
- Rutgers University
- Northwestern University
- University of California San Diego
arxiv_id: '2608.02441'
url: https://arxiv.org/abs/2608.02441
pdf_url: https://arxiv.org/pdf/2608.02441
published: '2026-08-03'
collected: '2026-08-04'
category: MultiAgent
direction: 多智体电商交互仿真与基准评测
tags:
- Agentic Commerce
- Multi-Agent
- Benchmark
- E-commerce
- Verifiable Execution
- Vibe Commerce
one_liner: 提出可审计多Agent电商交互环境ACWORLD与双轨基准，支持隐私目标下的交易评测
practical_value: '- 可复用VCP协议「决策-验证-状态更新」的解耦架构，搭建电商Agent可信执行链路，绑定每个动作的身份与权限，避免隐私泄露、越权下单等生产风险

  - 评测电商Agent时可复用双轨设计：先通过小规模覆盖80项核心能力的任务做梯度验证，再基于大规模商品目录测试检索、选品等真实业务瓶颈，降低评测成本

  - 可借鉴其过程性原子谓词打分逻辑，无需依赖LLM Judge，直接基于执行轨迹自动评分，大幅提升Agent策略迭代的评测效率

  - 微调电商Agent时可参考其80项能力的任务定义，定向做技能优化，针对性提升议价、多品交易、合规性等场景的表现'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有电商Agent相关协议仅支持部署链路协调，无法做策略可控评测；现有电商Agent基准多固定交易对手或平台逻辑，无法模拟真实场景中买卖双方独立决策、私有目标不公开的多Agent交互模式，也无法对交易全链路做可复现的审计追溯。
### 方法关键点
- 定义Vibe Commerce Protocol（VCP），将Agent决策、平台权限验证、全局状态更新三个环节完全解耦，所有动作绑定执行身份，仅验证通过的动作可更新全局状态，全链路轨迹可回溯、可重放评分
- 实现ACWORLD持久化多对多电商环境，支持买卖双方Agent保留私有目标、独立决策，通过统一接口交互，所有交易记录可审计，状态可复现
- 设计双轨评测基准：能力覆盖轨包含200个任务，覆盖10个交易场景、80项Agent核心能力；大目录轨包含60个任务，基于78.5万+可交易商品，测试大规模商品检索、交易的实际表现
### 关键结果
测试10款主流LLM，能力覆盖轨平均得分区间为65.9%~85.6%，大目录轨平均得分区间为56.1%~91.4%；仅看最终交易状态会漏掉11.5%的决策错误，87.9%的未满分轨迹仍保留有效过程信号。

最值得记住的一句话：电商Agent评测不能仅看最终交易结果，全链路可验证的过程轨迹才能准确识别决策错误，也能为策略学习提供更细粒度的奖励信号
