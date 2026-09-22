---
title: Rare Event Estimation via Iterative Unalignment
title_zh: 基于迭代失准的大模型生成罕见事件概率估计方法
authors:
- Hanming Yang
- Daksh Mittal
- Jing Dong
- Hongseok Namkoong
affiliations:
- Columbia Business School
arxiv_id: '2609.24969'
url: https://arxiv.org/abs/2609.24969
pdf_url: https://arxiv.org/pdf/2609.24969
published: '2026-09-21'
collected: '2026-09-22'
category: Agent
direction: Agent 长尾风险量化评估
tags:
- RareEventEstimation
- ImportanceSampling
- AgentSafety
- LLMAlignment
- LoRA
one_liner: 通过微调大模型权重构造重要性采样提议，实现1e-9级罕见事件高效估计，比朴素蒙特卡洛效率高800倍
practical_value: '- 电商/广告Agent场景可复用该框架量化罕见风险：比如工具调用时误删用户数据、生成违规营销文案的概率，无需百万级采样即可完成上线前风险校验

  - 生成式推荐场景可借鉴其微调约束策略：用每步反向KL散度+自适应正则控制生成分布偏离度，避免LoRA微调后生成结果脱离用户历史偏好

  - 长尾事件估计场景可复用其高效验证方法：用目标token的条件命中概率构造低方差参考真值，解决小概率事件无标注真值的评估难题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
自主Agent已开始大规模落地，即便概率低至1e-9的罕见失败事件（如误删生产库、发起不可逆大额交易、生成严重违规内容），在亿级用户部署规模下也会多次触发，造成灾难性损失。朴素蒙特卡洛估计这类小概率事件需要千亿级采样，成本完全不可接受；传统重要性采样方法依赖低维结构假设，无法适配大模型自回归生成的指数级序列空间。
### 方法关键点
- 提议分布参数化：将重要性采样的提议分布定义为基座模型的权重扰动版本（支持LoRA等高效微调方式），把原本需要遍历序列空间的提议构造问题转化为可微分的参数优化问题，单次参数更新即可同步调整所有前缀下的token分布
- 双目标优化：优化目标由两部分组成，可微surrogate信号（如目标事件相关token的平均对数概率）负责引导提议分布提升罕见事件的采样概率，逐步反向KL散度正则项约束提议分布与基座模型的分布偏差，避免重要性权重方差爆炸
- 自适应正则调优：基于有效样本量（ESSr）动态调整正则权重，事件样本占比低于10%时用全批次ESSr约束全局分布偏差，高于10%后用事件内ESSr约束事件内分布一致性，平衡放大效率与估计稳定性
### 关键结果
在120M参数量的GPT-2 Small和2.6B参数量的Gemma-2上验证，覆盖3类共300+罕见事件，最低事件概率低至1e-9；针对概率低于1e-7的事件，相对朴素蒙特卡洛的计算加权效率提升超800倍；训练后GPT-2仅需128个采样样本，即可得到95分位误差仅1.2个数量级的概率估计结果。
### 核心结论
针对大模型/Agent的长尾风险量化，无需依赖百万级朴素采样，通过梯度微调构造与基座分布对齐的重要性采样提议，可将评估成本降低2~3个数量级。
