---
title: 'When Every Rollout Fails: Splicing Learner-Conditioned Options into Long-Horizon
  Agent RL'
title_zh: 长 horizon 智能体强化学习全失败场景下的学习者条件选项拼接方法
authors:
- Haowen Hou
- Yicheng Liu
- Zhen Huang
- Jiaqi Wang
affiliations:
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- JD.com
arxiv_id: '2611.34777'
url: https://arxiv.org/abs/2611.34777
pdf_url: https://arxiv.org/pdf/2611.34777
published: '2026-11-24'
collected: '2026-11-26'
category: Agent
direction: 长 horizon 智能体 RL 训练优化
tags:
- Reinforcement Learning
- GRPO
- Long-Horizon Agent
- External Guidance
- SPLICE
one_liner: 提出SPLICE方法从全失败RL轨迹中提取局部训练信号，提升长horizon智能体性能同时降低大模型调用成本
practical_value: '- 电商导购Agent、搜索交互Agent等长对话RL训练遇到全失败冷启动场景时，可复用SPLICE的路由逻辑：仅全失败批次调用大模型生成本地修正选项，无需预先收集全量专家轨迹，大幅降低大模型调用成本

  - 外部引导选项的评估可复用当前策略续跑的方案，无需强模型生成完整后续轨迹，既降低大模型开销，还能减少off-policy偏移，适配业务策略快速迭代的需求

  - 冷启动无正样本时，选项权重采用续跑回报softmax加权的方式，效果优于直接选最优或均匀加权，可直接复用至弱监督训练场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长horizon Agent RL采用GRPO训练时，同批次所有轨迹全失败的场景频繁出现，无reward差异导致梯度消失无法训练；传统方法依赖强模型生成完整成功轨迹，大模型调用成本高且off-policy偏移严重，训练效果受限。

### 方法关键点
- 训练路由：仅全失败组进入SPLICE分支，混合reward组沿用GRPO，全成功组直接跳过，最小化额外开销
- 局部选项生成：在失败轨迹中选拼接点，用提案模型生成上限为平均轨迹长度30%的短选项，避免生成完整长轨迹
- 学习者条件评估：每个选项拼接后用当前策略续跑3次，用平均回报作为选项价值，过滤零回报选项
- 局部加权训练：用回报softmax对选项加权，仅对选项内的token做长度归一化的监督训练，降低off-policy偏移

### 关键实验
在SWE-bench Verified代码修复、BrowseComp-Plus深度搜索两个长horizon任务上测试，对比GRPO、ReLIFT、SFT+RL等baseline：相比GRPO，SPLICE性能提升2.8~9.8个百分点，初始失败任务的毕业率提升10.8个百分点；相比全轨迹引导的ReLIFT，提案模型调用量降低17.5%，同时性能高2.1~6.0个百分点。

### 核心结论
长horizon Agent全失败训练场景下，局部低成本的定向修正比完整昂贵的专家轨迹收益更高。
