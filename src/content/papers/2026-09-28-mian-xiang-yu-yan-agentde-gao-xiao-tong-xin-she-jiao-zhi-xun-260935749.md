---
title: Towards Communication-Efficient Social Intelligence in Language Agents
title_zh: 面向语言Agent的高效通信社交智能训练方法
authors:
- Linxiao Gong
- Yijie Xu
- Tianfu Wang
- Yin Wu
- Yili Wang
- Xingbo Yao
- Huizai Yao
- Xilin Xia
- Haowen Yang
- Hui Xiong
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- University of Science and Technology of China
- The Hong Kong University of Science and Technology
arxiv_id: '2609.35749'
url: https://arxiv.org/abs/2609.35749
pdf_url: https://arxiv.org/pdf/2609.35749
published: '2026-09-28'
collected: '2026-09-29'
category: Agent
direction: 语言Agent · 高效通信社交智能训练
tags:
- Language Agent
- Communication Efficiency
- On-Policy Distillation
- Social Intelligence
- Training
one_liner: 提出双专家辅助的TACT训练框架，提升语言Agent社交目标达成率同时降低通信成本
practical_value: '- 可复用双专家优化框架落地电商客服/导购Agent：表达专家精简冗余话术（保留核心诉求、优惠信息），策略专家优化请求逻辑（比如把多轮询问的信息合并为单轮），减少用户交互轮次，提升转化效率同时降低推理成本

  - 通信成本拆解思路可复用：将交互成本拆分为单轮回复token数、总交互轮次两个独立维度分别优化，避免仅做单轮精简导致信息缺失，反而需要多轮澄清拉高整体成本

  - 局部反馈蒸馏机制可落地：无需等待全交互结束再给奖励，单轮请求后仅采样1次对端响应，基于目标达成增益/token成本的比值筛选最优动作做蒸馏，训练数据标注成本低，收敛速度更快'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有社交型语言Agent训练多优先保障目标达成，忽略通信成本，或是仅压缩单轮回复长度，未考虑动作策略不合理引发的多轮澄清开销，反而拉高整体交互成本，既增加推理开销，也影响对端体验。
### 方法关键点
- 双专家修订机制：表达专家在保留原始动作意图、承诺、核心信息的前提下精简冗余表述，策略专家可调整动作逻辑匹配对端约束，从表达、策略两个维度降低全链路通信成本
- 效率感知候选选择：针对原始动作与两个专家生成的候选动作，各采样1次对端响应，计算每个动作的局部目标达成增益，结合token成本筛选出「增益/成本比」最高的候选作为蒸馏参考
- 参考条件On-Policy Distillation：仅将选中的最优参考作为教师的额外输入，在学生原始生成的token前缀上做蒸馏，部署阶段无需依赖任何专家组件，无额外推理开销
### 关键实验
在SOTOPIA、AgentSense两个主流社交Agent benchmark上评测，对比初始学生模型、SFT+SDPO、Sotopia-RL等7个基线：
- SOTOPIA全量数据集上Goal得分达5.611，为所有方法最高，较SFT+SDPO高6.3%，同时token消耗低35.6%；Hard子集上Goal得分4.371，同样排名第一，较基线最高提升23.3%
- AgentSense数据集上较初始学生模型目标成功率提升5.8%，token消耗降低12.2%，交互消息数减少12.5%
### 核心结论
通信效率优化不能只盯着单轮回复长度，需同时优化表达精简和动作策略，兼顾局部收益与全交互的整体成本
