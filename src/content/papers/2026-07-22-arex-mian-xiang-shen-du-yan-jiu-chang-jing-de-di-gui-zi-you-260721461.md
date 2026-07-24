---
title: 'AREX: Towards a Recursively Self-Improving Agent for Deep Research'
title_zh: AREX：面向深度研究场景的递归自优化智能体
authors:
- Shuqi Lu
- Chaofan Li
- Kun Luo
- Zhang Zhang
- Hui Wang
- Hongwang Xiao
- Zheng Liu
- Lei Xiong
- Jiahao Wang
- Sen Wang
affiliations:
- Beijing Academy of Artificial Intelligence (BAAI)
arxiv_id: '2607.21461'
url: https://arxiv.org/abs/2607.21461
pdf_url: https://arxiv.org/pdf/2607.21461
published: '2026-07-22'
collected: '2026-07-24'
category: Agent
direction: Agent 长序列任务递归自优化
tags:
- Recursive Agent
- Long-horizon Reasoning
- Tool Use
- Context Compression
- MoE
- Reinforcement Learning
one_liner: 提出双循环递归自优化研究Agent架构，在多搜索推理基准上超同规模基线
practical_value: '- 双循环架构可迁移到电商搜索导购Agent：内循环完成商品召回、候选初筛，外循环基于用户约束（价格/品牌/偏好）做定向补搜，避免无效重复检索

  - 自主上下文更新工具可复用在长会话推荐场景：多轮交互中自动压缩历史，保留已验证偏好、排除无效候选、聚焦未满足需求，降低上下文冗余

  - 关键步骤聚焦训练策略可借鉴到排序/召回模型训练：对决策关键节点（如query改写、候选筛选步骤）加权重训，提升长序列任务样本利用效率

  - 置信度驱动的终止/重跑机制可用于电商大模型文案生成、智能客服应答：低置信度结果自动触发定向优化，提升输出准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有深度研究Agent多依靠延长搜索轨迹提升效果，容易出现早期错误残留、无效路径重复访问、候选过早接受等问题，且长轨迹下上下文冗余会严重干扰决策，同时长序列任务的稀疏奖励也导致训练效率低下。

### 方法关键点
- 双循环递归架构：内循环执行搜索/工具调用、整合证据生成带置信度的候选答案；外循环按约束逐一审验答案，高置信度直接输出，可恢复的低置信度结果保留有效证据、生成定向优化目标进入下一轮，不可恢复则重启
- 自主上下文更新工具：模型自主决定更新时机（如调整搜索策略、淘汰候选后），压缩历史轨迹为紧凑状态，保留已验证结论、未解决约束、无效候选、下一步计划，丢弃冗余信息
- 多阶段训练策略：先渐进式训练工具使用+推理能力，再针对关键决策节点（证据发现、路径修正、上下文更新）做聚焦监督，最后用步骤感知的强化学习优化，解决长轨迹稀疏奖励问题
- 发布两个版本：4B稠密模型AREX-Turbo，122B总参/10B激活参的MoE模型AREX-Base

### 关键结果数字
在BrowseComp、GAIA、WideSearch、DeepSearchQA、HLE等6个基准上测试，AREX-Base在WideSearch-en上达82.0为当前最优，在BrowseComp达82.5、DeepSearchQA达89.9，超过397B参数的Qwen3.5，性能对标头部闭源模型；4B的AREX-Turbo在5个基准上超过35B的Qwen3.5；消融实验显示上下文更新+外循环共带来22.9个点的BrowseCom准确率提升。

最值得记住的一句话：利用发现-验证的不对称性，将验证作为主动控制信号而非最终过滤规则，是提升长序列Agent效率的核心路径。
