---
title: 'Self-Improvements in Modern Agentic Systems: A Survey'
title_zh: 现代智能体系统自提升机制全景综述
authors:
- Zhe Ren
- Yimeng Chen
- Dandan Guo
- Guowei Rong
- Tonghui Li
- R. B. Xiong
- Qingfeng Lan
- Wenyi Wang
- Li Nanbo
- Yibo Yang
affiliations:
- Jilin University
- King Abdullah University of Science and Technology
- University of Alberta
- The Swiss AI Lab IDSIA/USI/SUPSI
arxiv_id: '2607.13104'
url: https://arxiv.org/abs/2607.13104
pdf_url: https://arxiv.org/pdf/2607.13104
published: '2026-07-13'
collected: '2026-07-17'
category: Agent
direction: 智能体自提升 · 统一分类框架
tags:
- Self-Improving Agent
- Foundation Model
- Scaffold Optimization
- LLM Agent
- Agent Evaluation
one_liner: 构建基础模型驱动自提升智能体的统一分类框架与技术全景梳理
practical_value: '- 落地电商/推荐场景Agent时，优先选择脚手架优化路径（prompt迭代、记忆更新、工具路由调整）实现快速自适配，比LoRA微调大模型成本低、迭代周期短，适配业务高频变化需求

  - 可复用综述中的prompt自优化闭环（执行→评估→文本梯度更新），自动迭代商品推荐话术、客服应答prompt、搜索Query改写规则，降低人工调优成本

  - 搭建自提升Agent评估体系时，可复用双轨范式：用业务指标（CTR、转化率、问题解决率）做量化评估，搭配LLM Judge做体验类指标评估，平衡效率与准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
自提升智能体已从研究原型逐步走向落地，当前领域存在术语不统一、机制零散的问题，多数研究将基础模型微调与Agent脚手架优化视为独立方向，缺乏统一的形式化框架，且很少追溯自提升机制的经典AI理论根源，亟需系统性梳理技术路径、落地范式与风险挑战。
### 方法关键点
- 将基础模型驱动的智能体形式化为(模型参数θ, 运行脚手架Σ)的二元结构，其中Σ包含prompt、记忆、工具集、控制逻辑四大核心组件
- 自提升机制分为两类核心路径：①基础模型改进：通过内在生成演示、内在评估反馈、外在探索经验三类信号更新θ，实现能力的长期稳定固化；②脚手架改进：通过非参数化方式更新prompt/记忆/工具/全脚手架，实现快速、可逆的场景化能力迭代
- 系统梳理2023-2026年近200项相关工作，覆盖技术演进路线、6大核心应用领域、双轨评估范式，总结了可控自提升的安全约束与未来方向
### 关键结论
作为综述类工作，对比同领域5篇相关综述，首次完整覆盖历史溯源、信号来源、更新载体、评估体系、领域应用五大核心维度，填补了现有研究未统一模型参数与脚手架优化视角的空白。
> 最值得记住的一句话：智能体自提升的核心是将自身执行产生的信号转化为对参数或脚手架的持久化更新，短期场景适配优先选脚手架优化，长期能力沉淀优先选参数更新
