---
title: 'Turns Matter: Advancing Streaming Video RL via Turn-Level Credit'
title_zh: TurnWise：基于轮次级信用的流视频强化学习优化方法
authors:
- Shuai Dong
- Kanghui Tian
- Linghan Chen
- Wenqi Shao
- Hongrui Wu
- Haowen Hou
- Yongfu Zhu
- Xuehui Wang
- Ziyue Wang
- Wenpu Liu
affiliations:
- Fudan University
- JD.com
- Shanghai Artificial Intelligence Laboratory
- Stanford University
- The Chinese University of Hong Kong
arxiv_id: '2611.06728'
url: https://arxiv.org/abs/2611.06728
pdf_url: https://arxiv.org/pdf/2611.06728
published: '2026-11-03'
collected: '2026-11-05'
category: Training
direction: 流视频VLM · RL训练优化
tags:
- GRPO
- Reinforcement Learning
- Turn-Level Credit
- Streaming Video
- VLM
- Policy Optimization
one_liner: 针对流视频RL全局信用分配偏差，提出无额外开销的轮次级GRPO框架优化响应质量降低冗余
practical_value: '- 电商直播导购Agent、多轮客服Agent等多轮交互场景的RL优化，可复用轮次级信用分配思路，将全局轨迹奖励拆解到每一轮，避免前面决策的正负收益异常传导到后续轮次，减少重复回复提升交互效率

  - 采用GRPO做RLHF/RLAIF优化多轮生成任务时，可直接复用turn-mean loss聚合方法，给每轮决策同等权重，解决长回复梯度权重天然大于短回复/沉默决策的偏差问题

  - 该方法无需额外引入critic模型或增加采样量，仅通过复用已有轨迹的评分结果即可实现轮次级信用分配，工程落地成本极低，适合线上多轮交互场景快速迭代'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有流视频交互RL方案普遍采用GRPO的轨迹级全局优势分配，同一轨迹所有轮次共享同一个优势信号，导致前期成功回复后的冗余重复内容也能获得正梯度，而前期失败后的有效后续回复反而获得负梯度；同时token级损失聚合会让长回复的权重天然远大于短回复/沉默决策，严重影响多轮交互的质量和时效性。

### 方法关键点
- 沉默补全前缀打分：对每个轨迹前缀，将后续所有轮次设为沉默后重新打分，得到当前轮之前的累计奖励，用总奖励减去累计奖励得到当前轮剩余回报，进而计算轮次级组相对优势，完全复用已有轨迹评分，无需额外采样或critic模型
- 轮均损失聚合：先在每轮内平均所有token的损失，再跨轮平均整条轨迹的损失，让每轮回复/等待决策的权重完全相同，不受输出长度影响
- 信用分配暖启动：训练前10%步长内线性将累计奖励扣除比例α从0升至1，避免训练初期梯度波动过大

### 关键实验
在ProactiveVQA、OVO-Timing、StreamingBench三个流视频基准测试，对比SFT、MMDuet2、ThinkStream、StreamPro等基线：采用Qwen2.5-VL-3B backbone时，三个基准综合得分分别比最优基线高3.96、3.87、0.69，冗余回复率比仅用轮次信用的方案低61.5%；采用Qwen3-VL-4B时三个基准得分分别提升6.26、1.92、2.38。

### 核心结论
多轮交互场景的RL优化，将决策轮次作为信用分配和损失聚合的基本单元，无额外开销即可显著提升交互质量、减少冗余。
