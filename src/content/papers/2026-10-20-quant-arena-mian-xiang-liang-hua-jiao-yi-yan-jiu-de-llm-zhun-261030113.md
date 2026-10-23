---
title: 'Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research'
title_zh: Quant-Arena：面向量化交易研究的LLM Agent基准测试平台
authors:
- Houde Qian
- Zheng Jiang
- Wenyi Li
- Chenxi Xu
- Xinjie Lin
- Yuzhao Peng
- Ruoyu Han
- Youjie Zheng
- Kaisen Yang
- Qinhuai Na
affiliations:
- Navers Lab
- Einsia.AI
arxiv_id: '2610.30113'
url: https://arxiv.org/abs/2610.30113
pdf_url: https://arxiv.org/pdf/2610.30113
published: '2026-10-20'
collected: '2026-10-23'
category: Agent
direction: LLM Agent 量化场景评测基准构建
tags:
- LLM Agent
- Benchmark
- Quantitative Trading
- Agent Evaluation
one_liner: 推出面向端到端量化投研的LLM Agent基准Quant-Arena，基于真实A股数据做全链路策略效果评测
practical_value: '- 端到端Agent任务评测可借鉴「训练期给反馈、测试期封数据盲测」的范式，避免模型过拟合历史数据，适合推荐/广告策略的离线到在线效果验证

  - 多维度评分设计可复用：以核心业务指标（如电商GMV、量化超额收益）为主，过程指标（信号质量、特征多样性）为辅，平衡效果与可解释性

  - 仿真环境搭建可参考其加入真实业务约束（交易成本、市场冲击）的思路，让电商/广告的策略仿真结果更贴近线上真实表现'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有量化领域LLM评测仅覆盖公式、代码或单次交易决策，无法验证LLM Agent是否能完整走完投研迭代闭环，产出跨周期有效的交易策略。
### 方法关键点
1. 构建端到端量化投研基准Quant-Arena，采用真实A股数据，设置2022-2023年为带反馈的训练验证期，2024年为密封盲测期；
2. 要求Agent自主生成特征、股票打分代码，冻结策略后参与盲测；
3. 评估器加入真实交易约束、成本，甚至基于模拟订单簿的市场冲击，评分以实盘超额收益为主，辅以信号质量、特征多样性指标。
### 关键结果
共评测9款前沿LLM，其中GPT-6 Astra得分最高，但所有模型2024年盲测收益均未跑赢等权市场指数。
