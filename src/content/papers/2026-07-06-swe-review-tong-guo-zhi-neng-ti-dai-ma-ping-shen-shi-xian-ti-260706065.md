---
title: 'SWE-Review: Closing the Loop on Issue Resolution with Agentic Code Review'
title_zh: SWE-Review：通过智能体代码评审实现问题解决闭环
authors:
- Ruoyu Wang
- Jierun Chen
- Shaowei Wang
- Chaofan Tao
- Sidi Yang
- Yuxin Jiang
- Kim-Hui Yap
- Lifeng Shang
- Xiaohui Li
- Haoli Bai
affiliations:
- NTU
- Huawei Technologies
- HKU
arxiv_id: '2607.06065'
url: https://arxiv.org/abs/2607.06065
pdf_url: https://arxiv.org/pdf/2607.06065
published: '2026-07-06'
collected: '2026-07-09'
category: Agent
direction: 代码Agent · 闭环评审优化
tags:
- Agent
- Code Agent
- Closed Loop
- Benchmark
- SFT
one_liner: 提出支持代码库自主探索的智能体代码评审框架，配套基准数据集，大幅提升代码问题解决效率
practical_value: '- 架构可直接迁移到生成式推荐/广告文案/商品标题生成场景：单步生成后增加评审Agent做质量校验+结构化修改建议，替代纯单步生成，大幅提升产出合规性和业务效果

  - 训练可复用混合训练思路：将生成任务数据与评审任务数据混合SFT，单模型可同时具备生成与自我校验能力，无需部署两套大模型即可实现自闭环迭代，大幅降低推理成本

  - 测试时优化可复用评审引导的早停迭代机制：比传统best-of-N采样效率提升40%以上，适合推荐/广告创意生成、query改写等低延迟要求的场景

  - 评估指标设计可参考：评审效果不要仅对齐文本相似度，要设计下游业务效果指标（对应本文RRR，如修改后的点击率/转化率提升），避免伪优化'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前AI代码智能体多为单次生成PR的开环模式，无系统评审、诊断、修正流程；现有自动代码评审均为单步固定上下文方案，无法追溯跨模块根因，也缺乏端到端衡量评审对最终问题解决贡献的基准与训练数据。

### 方法关键点
- 评审Agent可自主探索代码库、执行测试、追溯依赖，输出二分类合并决策+结构化修正诊断，支撑「生成-评审-修正」闭环
- 构建SWE-Review-Bench基准，包含1384个不同质量的AI生成PR，配套Completion Rate（CR）、Decision Accuracy（DA）、Resolve Rate after Revision（RRR）三个端到端指标
- 开源8914条高质量智能体评审轨迹数据集SWE-Review-Traj，支持小模型SFT蒸馏评审能力
- 支持混合训练：评审轨迹与代码生成轨迹混合训练，得到同时具备生成与评审能力的单模型，可实现自闭环迭代

### 关键实验
在SWE-bench Verified数据集上，闭环流程将Qwen3-30B-A3B问题解决率从27.5%提升至56.9%，Qwen3-Coder-30B-A3B从50.9%提升至68.8%，GLM-5从72.2%提升至75.4%；智能体评审比单步固定上下文评审DA最高提升18.6%，RRR最高提升8.5%；混合训练8B单模型自迭代5轮后问题解决率从34.8%提升至44.0%；测试时优化阶段，评审引导的迭代修正仅用平均2.44个样本就达到38.4%的解决率，效率远优于best-of-N采样。

最值得记住的一句话：评审不是下游的质量校验工具，而是将单次生成升级为迭代优化闭环的核心枢纽，能同时提升训练效率和部署效果。
